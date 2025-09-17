# Fix for "Agent processed tool calls, but failed to collect any valid SynthGenieResponse results"

## Problem

The Digitone sound design agent was failing with the error:
```
HTTPException: 500: Agent processed tool calls, but failed to collect any valid SynthGenieResponse results (check tool implementations and logs).
```

## Root Cause

When a Pydantic AI agent is configured with `output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse]`, the framework automatically adds a `final_result` tool that the agent can call to return structured output.

However, the agent was calling this `final_result` tool FIRST with an empty response array (`{'response': []}`), which caused Pydantic AI to prevent all subsequent tool calls from executing with the message "Tool not executed - a final result was already processed."

## Solution

Removed the `output_type` parameter from the agent configuration in `/api/synthgenie/synthesizers/digitone/agents/sound_design_agent.py`.

The agent now relies on the existing event streaming mechanism that:
1. Captures `FunctionToolResultEvent` instances during tool execution
2. Extracts `SynthGenieResponse` objects from individual tool calls  
3. Collects them in the `collected_responses` list
4. Returns the collected responses

## Files Changed

- `/api/synthgenie/synthesizers/digitone/agents/sound_design_agent.py`:
  - Removed `output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse]` from agent configuration
  - This prevents the automatic `final_result` tool from being added

## Testing

The fix should allow the agent to properly execute multiple synthesizer tools (like `set_fm_tone_algorithm`, `set_multi_mode_filter_frequency`, etc.) and collect their `SynthGenieResponse` objects without interference from the `final_result` tool.

## Context

The Sub37 agent uses a different approach (JSON-based output with `agent.run()`) while the Digitone agent uses tool calls with event streaming (`agent.iter()`). This fix maintains the Digitone's event streaming approach while removing the conflicting `output_type` configuration.