"""Service layer for Digitone sound design agent orchestration."""

import logging

import psycopg2
from fastapi import HTTPException
from pydantic import ValidationError

from synthgenie.auth.models import track_api_key_usage
from synthgenie.synthesizers.digitone.agents.fm_drum_agent import get_fm_drum_agent
from synthgenie.synthesizers.digitone.agents.fm_tone_agent import get_fm_tone_agent
from synthgenie.synthesizers.digitone.agents.router_agent import route_to_machine
from synthgenie.synthesizers.digitone.agents.shared import DigitoneAgentDeps
from synthgenie.synthesizers.digitone.agents.swarmer_agent import get_swarmer_agent
from synthgenie.synthesizers.digitone.agents.wavetone_agent import get_wavetone_agent
from synthgenie.synthesizers.shared.agents.validation_agent import prompt_validation_agent
from synthgenie.synthesizers.shared.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse

logger = logging.getLogger(__name__)


async def run_digitone_agent_workflow(
    user_prompt: str, api_key: str, conn: psycopg2.extensions.connection
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    """
    Orchestrate the multi-agent Digitone sound design workflow.

    Workflow:
    1. Validate prompt is about sound design
    2. Route to appropriate machine-specific agent
    3. Execute machine agent with context
    4. Track API usage
    5. Return results

    Args:
        user_prompt: The user's sound design request
        api_key: API key for authentication and usage tracking
        conn: Database connection for usage tracking

    Returns:
        List of SynthGenieResponse or SynthGenieAmbiguousResponse objects

    Raises:
        HTTPException: For validation errors, routing errors, or agent failures
    """
    # Step 1: Validate the prompt
    logger.info(f'Validating prompt: {user_prompt[:100]}...')
    is_valid = await prompt_validation_agent(user_prompt)
    if not is_valid:
        raise HTTPException(status_code=422, detail='This prompt is not about sound design.')

    # Step 2: Route to appropriate machine agent
    try:
        deps = DigitoneAgentDeps(api_key=api_key, conn=conn)
        routing_decision = await route_to_machine(user_prompt, deps)

        logger.info(
            f'Routed to {routing_decision.machine} on track {routing_decision.track}: {routing_decision.reasoning}'
        )

    except HTTPException:
        # Re-raise HTTPExceptions from route_to_machine (e.g., input validation)
        raise
    except ValidationError:
        raise HTTPException(status_code=422, detail='Invalid routing decision')
    except TimeoutError:
        raise HTTPException(status_code=503, detail='Agent timeout - please try again')
    except Exception:
        logger.exception('Unexpected routing error')
        raise HTTPException(status_code=500, detail='Internal routing error')

    # Step 3: Get the appropriate machine agent
    machine_agents = {
        'fm_tone': get_fm_tone_agent,
        'fm_drum': get_fm_drum_agent,
        'wavetone': get_wavetone_agent,
        'swarmer': get_swarmer_agent,
    }

    agent_factory = machine_agents.get(routing_decision.machine)
    if not agent_factory:
        raise HTTPException(status_code=500, detail=f'Unknown machine type: {routing_decision.machine}')

    agent = agent_factory()

    # Step 4: Update dependencies with routed track
    deps.default_midi_channel = routing_decision.track

    # Step 5: Run the machine-specific agent
    try:
        logger.info(f'Running {routing_decision.machine} agent on track {routing_decision.track}')

        result = await agent.run(
            routing_decision.original_prompt,
            deps=deps,
            model_settings={'temperature': 0.3},  # Lower temperature for more consistent tool usage
        )

        responses = result.output
        logger.info(f'{routing_decision.machine} agent returned {len(responses)} responses')

        # Step 6: Track API usage
        track_api_key_usage(conn, api_key)

        return responses

    except ValidationError as e:
        logger.error(f'Validation error in {routing_decision.machine} agent: {e}')
        raise HTTPException(status_code=422, detail='Agent produced invalid response')

    except TimeoutError:
        raise HTTPException(status_code=503, detail='Agent timeout - please try again')

    except Exception:
        logger.exception(f'Error in {routing_decision.machine} agent')
        raise HTTPException(status_code=500, detail='Sound design agent failed')
