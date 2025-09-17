# Fix: Agent Final Result Tool Execution Issue

## Problem
The Digitone sound design agent was failing with the error:
```
Agent processed tool calls, but failed to collect any valid SynthGenieResponse results (check tool implementations and logs).
```

## Root Cause
The agent was configured with `output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse]` in the Agent constructor. This caused Pydantic AI to automatically add a `final_result` tool to the agent's toolset.

The agent was incorrectly calling this `final_result` tool first with an empty response array, which prevented all other synthesizer tools from executing (they would show "Tool not executed - a final result was already processed").

## Solution
Removed the `output_type` parameter from the agent configuration in `api/synthgenie/synthesizers/digitone/agents/sound_design_agent.py`.

The existing event streaming mechanism already properly:
1. Captures `FunctionToolResultEvent` instances during tool execution
2. Extracts `SynthGenieResponse` objects from individual synthesizer tools  
3. Collects responses in the `collected_responses` list
4. Returns the final collection

## Files Changed
- `api/synthgenie/synthesizers/digitone/agents/sound_design_agent.py`: Removed conflicting `output_type` parameter

## Expected Result
The agent should now properly execute multiple synthesizer tools (like `set_fm_tone_algorithm`, `set_multi_mode_filter_frequency`, etc.) and collect their responses without the tool execution order issue.