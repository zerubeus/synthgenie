import logging
from fastapi import APIRouter, HTTPException, Depends

import psycopg2
from pydantic_ai import UsageLimitExceeded
from pydantic_ai.usage import UsageLimits

from synthgenie.schemas.user import UserPrompt
from synthgenie.services.agent import get_synthgenie_agent
from synthgenie.schemas.agent import SynthGenieResponse
from synthgenie.services.synth_controller import SynthControllerDeps
from synthgenie.services.auth import get_api_key
from synthgenie.db.connection import get_db
from synthgenie.models.api_key import track_api_key_usage

# Define a maximum number of steps to prevent infinite loops
MAX_STEPS = 70  # Slightly more than REQUEST_LIMIT

REQUEST_LIMIT = 64  # Keep existing request limit

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/agent", tags=["synthgenie"])


@router.post("/prompt", response_model=list[SynthGenieResponse])
async def process_prompt(
    user_prompt: UserPrompt,
    api_key: str = Depends(get_api_key),
    conn: psycopg2.connect = Depends(get_db),
):
    """
    Process a user prompt with the SynthGenie AI agent.

    The agent will interpret the prompt and return a list of synthesizer parameter changes.

    Requires a valid API key.
    """
    deps = SynthControllerDeps()
    agent = get_synthgenie_agent()
    step_count = 0

    try:
        # Use agent.iter() for fine-grained control and loop prevention
        async with agent.iter(
            user_prompt.prompt,
            deps=deps,
            usage_limits=UsageLimits(
                request_limit=REQUEST_LIMIT,
            ),
        ) as agent_run:
            async for node in agent_run:
                step_count += 1
                logger.debug(
                    f"Agent step {step_count}: {type(node).__name__}"
                )  # Optional: log each step

                if step_count > MAX_STEPS:
                    logger.error(
                        f"Agent exceeded maximum step limit ({MAX_STEPS}). Potential loop detected."
                    )
                    raise HTTPException(
                        status_code=500,
                        detail=f"Agent processing exceeded maximum steps ({MAX_STEPS}). Please refine your prompt or contact support.",
                    )

                # The loop finishes when an End node is reached or an exception occurs
                # The final result is available in agent_run.result after the loop

            # Check if the run completed successfully and has a result
            if agent_run.result:
                # Track API key usage after successful response
                track_api_key_usage(conn, api_key)
                return agent_run.result.data
            else:
                # This case might occur if the loop finished unexpectedly without an End node
                # or if an error occurred that wasn't caught (though agent.iter should handle most)
                logger.error("Agent run finished without a final result.")
                raise HTTPException(
                    status_code=500, detail="Agent failed to produce a result."
                )

    except UsageLimitExceeded as e:
        logger.error(f"Usage limit exceeded: {e}")
        raise HTTPException(
            status_code=429, detail=str(e)
        )  # Use 429 for rate/usage limits
    except HTTPException as http_exc:
        # Re-raise HTTPExceptions (like the one for MAX_STEPS)
        raise http_exc
    except Exception as e:
        # Catch any other unexpected errors during agent execution
        logger.exception(f"An unexpected error occurred during agent processing: {e}")
        raise HTTPException(
            status_code=500,
            detail="An internal error occurred during agent processing.",
        )
