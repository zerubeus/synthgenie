# Diagnosing and Fixing Agent Infinite Loops

This document outlines the steps taken to address an issue where the Pydantic AI agent (`SynthGenie`) could enter an infinite loop, particularly when handling open-ended, creative sound design prompts.

## Problem Description

The agent would repeatedly call the same or similar tools in a cycle without reaching a final state or returning a result. This was observed through logs showing repeated tool calls until the server process was manually stopped or timed out. The issue was more prominent with prompts like "design a dark bass sound" compared to specific instructions like "set filter frequency to 80".

## Root Cause Analysis

Infinite loops in LLM-based agents often stem from the agent's reasoning process:

1.  **Ambiguity:** Open-ended prompts require the agent to make creative choices. It might continuously try to "improve" the result based on its internal criteria or system prompt, leading to repeated adjustments.
2.  **Lack of Explicit Stop Condition:** If the agent isn't clearly instructed when a task is considered "complete" (especially for subjective tasks), it might continue executing steps.
3.  **Tool Feedback:** If tool execution doesn't provide feedback that satisfies the agent's internal checks, it might retry the same tool or try alternative tools indefinitely.

## Iterative Solutions and Findings

Several approaches were attempted:

1.  **System Prompt Refinement (Attempt 1):**

    - **Action:** Added explicit `STOP` commands, parameter limits (e.g., 5-8 for general requests), and loop prevention rules to the system prompt in `synthgenie/services/agent.py`.
    - **Result:** Reduced looping for some cases but didn't fully solve it for generative prompts. The agent still sometimes attempted further refinement beyond the initial execution.

2.  **Step Limit (`MAX_STEPS`):**

    - **Action:** Implemented a `MAX_STEPS` limit within the agent execution loop in `synthgenie/routes/agent.py` using `agent.iter()`.
    - **Result:** Acted as a crucial safety net, preventing the server from hanging indefinitely by raising an error after too many steps. However, it didn't guarantee that the _intended first result_ was captured, as the error occurred _after_ the loop had already progressed.

3.  **Forced Single-Turn Execution (Attempt 1 - `agent_run.result`):**

    - **Action:** Modified the loop in `routes/agent.py` to manually iterate using `agent.iter()` and `agent_run.next()`, breaking the loop immediately after the first `CallToolsNode` was processed and before the subsequent `ModelRequestNode`.
    - **Result:** This successfully stopped the loop after one cycle but often failed with `HTTPException: 500: Agent failed to produce a valid result after the first execution cycle.`. This indicated that interrupting the flow this way prevented Pydantic AI from properly populating the final `agent_run.result.data` object.

4.  **Tool Return Value Fix:**
    - **Action:** Investigated tool implementation (`synthgenie/services/synth_controller.py`) and found that `get_direct_parameter` could return `False` instead of raising an error or returning the expected `SynthGenieResponse` if a parameter lacked configuration. This was fixed to raise a `ValueError`.
    - **Result:** Corrected potential tool-level errors but didn't resolve the core issue of capturing results during the forced single-turn execution.

## Final Solution: Manual Iteration with Event Streaming

The successful approach combined manual iteration with event streaming:

1.  **Manual Iteration:** Continued using `agent.iter()` with manual `agent_run.next()` calls in `routes/agent.py`.
2.  **Event Streaming:** When processing the first `CallToolsNode` (identified via `Agent.is_call_tools_node(processed_node)`), used `async with processed_node.stream(agent_run.ctx) as handle_stream:` to listen for execution events within that node.
3.  **Result Collection:** Inside the stream loop, specifically captured `FunctionToolResultEvent` instances. The actual `SynthGenieResponse` object was extracted from `event.result.content` and appended to an external list (`collected_responses`).
4.  **Forced Stop:** Kept the logic to `break` the main iteration loop immediately after the `CallToolsNode` stream completed and before the next `ModelRequestNode`.
5.  **Return Collected Results:** Returned the `collected_responses` list directly, bypassing the potentially incomplete `agent_run.result.data`.
6.  **Import Correction:** Ensured `FunctionToolResultEvent` was correctly imported from `pydantic_ai.messages`.

## Outcome

This event-streaming approach reliably captures the results of the tools executed during the _first_ reasoning cycle planned by the LLM. By stopping the agent immediately after this cycle and collecting results via events, we prevent infinite loops while ensuring the initial, intended output is returned to the user.

With this robust loop prevention mechanism in place at the route level, the system prompt (`services/agent.py`) could be relaxed again, removing the strict STOP commands and parameter limits to allow the LLM more freedom in its initial sound design planning, leading to potentially more comprehensive and creative results within the enforced single execution turn.
