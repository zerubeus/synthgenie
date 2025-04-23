import logging
from fastapi import APIRouter, HTTPException, Depends

import psycopg2
from pydantic_ai import UsageLimitExceeded, Agent
from pydantic_ai.usage import UsageLimits
from pydantic_ai.messages import FunctionToolResultEvent

from synthgenie.schemas.user import UserPrompt
from synthgenie.synthesizers.digitone.agents.sound_design_agent import get_synthgenie_agent
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
    of tool execution and collects results via events to prevent loops.

    Requires a valid API key.
    """
    deps = SynthControllerDeps()
    agent = get_synthgenie_agent()
    step_count = 0
    first_tool_call_node_processed = False
    collected_responses: list[SynthGenieResponse] = (
        []
    )  # Explicit list to collect results

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

                # --- Event Collection Logic ---
                # If processing the node where tools are called, stream events to capture results
                if Agent.is_call_tools_node(processed_node):
                    logger.info(
                        "Streaming events from CallToolsNode to collect results..."
                    )
                    try:
                        async with processed_node.stream(
                            agent_run.ctx
                        ) as handle_stream:
                            async for event in handle_stream:
                                if isinstance(event, FunctionToolResultEvent):
                                    # Ensure the result content is the expected type
                                    if isinstance(
                                        event.result.content, SynthGenieResponse
                                    ):
                                        logger.debug(
                                            f"Collected tool result: {event.result.content}"
                                        )
                                        collected_responses.append(event.result.content)
                                    else:
                                        logger.warning(
                                            f"Tool {event.part.tool_name} result content was not SynthGenieResponse: {type(event.result.content)}"
                                        )
                        first_tool_call_node_processed = True
                        logger.info(
                            f"Finished streaming CallToolsNode. Collected {len(collected_responses)} responses."
                        )
                    except Exception as stream_exc:
                        # Catch errors specifically during the event streaming/tool execution phase
                        logger.exception(
                            f"Error during CallToolsNode event streaming: {stream_exc}"
                        )
                        # Depending on desired behavior, we might raise here or just log and continue
                        # Let's break the loop to be safe and report based on potentially partial results
                        break
                # --- End Event Collection ---

                # Advance to the next node *after* potentially streaming the current one
                node = await agent_run.next(processed_node)

                # **Core Stop Logic:** If we just processed the tools node, and the *next* step
                # is the agent wanting to think again, stop now.
                if first_tool_call_node_processed and Agent.is_model_request_node(node):
                    logger.info(
                        "First tool call cycle completed. Stopping agent before second reasoning step."
                    )
                    break

            # --- Loop finished (End node, MAX_STEPS, stream error, or early break) ---

            # Return the explicitly collected responses
            if collected_responses:
                logger.info(
                    f"Agent finished or was stopped. Returning {len(collected_responses)} collected responses after {step_count} steps."
                )
                track_api_key_usage(conn, api_key)
                return collected_responses
            else:
                # Handle cases where loop finished but no responses were collected
                log_message = (
                    "Agent run finished, but no tool responses were collected."
                )
                if first_tool_call_node_processed:
                    log_message = "Agent processed tool calls, but failed to collect any valid SynthGenieResponse results (check tool implementations and logs)."
                elif step_count >= MAX_STEPS:
                    log_message = (
                        f"Agent hit MAX_STEPS ({MAX_STEPS}) without collecting results."
                    )
                logger.error(f"{log_message} Step count: {step_count}")
                # Use a more specific detail message
                raise HTTPException(status_code=500, detail=log_message)

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
