import logging
from fastapi import APIRouter, HTTPException, Depends

import psycopg2
from pydantic_ai import UsageLimitExceeded, Agent
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

    This implementation forces the agent to stop after the first cycle
    of tool execution to prevent potential loops in generative tasks,
    returning only the initial set of parameter changes.

    Requires a valid API key.
    """
    deps = SynthControllerDeps()
    agent = get_synthgenie_agent()
    step_count = 0
    first_tool_call_processed = False

    try:
        async with agent.iter(
            user_prompt.prompt,
            deps=deps,
            usage_limits=UsageLimits(request_limit=REQUEST_LIMIT),
        ) as agent_run:
            node = agent_run.next_node

            while node is not None and not Agent.is_end_node(node):
                step_count += 1
                logger.debug(f"Agent step {step_count}: {type(node).__name__}")

                if step_count > MAX_STEPS:
                    logger.error(
                        f"Agent exceeded maximum step limit ({MAX_STEPS}). Forcing stop."
                    )
                    break

                processed_node = node
                node = await agent_run.next(processed_node)

                if Agent.is_call_tools_node(processed_node):
                    logger.info("Processed first CallToolsNode.")
                    first_tool_call_processed = True

                if first_tool_call_processed and Agent.is_model_request_node(node):
                    logger.info(
                        "First tool call cycle completed. Stopping agent before second reasoning step."
                    )
                    break

            if agent_run.result and agent_run.result.data:
                logger.info(
                    f"Agent finished or was stopped. Returning result after {step_count} steps."
                )
                track_api_key_usage(conn, api_key)
                return agent_run.result.data
            else:
                log_message = "Agent run finished without a final result."
                if first_tool_call_processed:
                    log_message = "Agent stopped after first tool cycle, but no result data found (tools might have failed or returned nothing)."
                logger.error(f"{log_message} Step count: {step_count}")
                raise HTTPException(
                    status_code=500,
                    detail="Agent failed to produce a valid result after the first execution cycle.",
                )

    except UsageLimitExceeded as e:
        logger.error(f"Usage limit exceeded: {e}")
        raise HTTPException(status_code=429, detail=str(e))
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.exception(f"An unexpected error occurred during agent processing: {e}")
        raise HTTPException(
            status_code=500,
            detail="An internal error occurred during agent processing.",
        )
