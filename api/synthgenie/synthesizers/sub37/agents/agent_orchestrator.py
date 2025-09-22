"""Agent Orchestrator for Moog Sub 37 Two-Agent System.

Coordinates the Tool Selector Agent (Agent 1) and Sound Design Agent (Agent 2)
to provide intelligent tool selection and efficient sound design execution.
"""

import os

from psycopg2.extensions import connection as Connection
from pydantic_ai import Agent

from synthgenie.auth.models import track_api_key_usage
from synthgenie.synthesizers.shared.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse
from synthgenie.synthesizers.sub37.agents.tool_selector_agent import analyze_sound_design_request
from synthgenie.synthesizers.sub37.schemas.toolset_selection import validate_toolset_selection
from synthgenie.synthesizers.sub37.toolsets.tool_selector import create_dynamic_toolset


def get_sub37_sound_design_agent():
    """Create the Sub 37 sound design agent (Agent 2)."""
    return Agent(
        model=os.getenv('AGENT_MODEL'),
        # Start with no tools - they'll be added dynamically at runtime
        tools=[],
        output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse],
        instrument=True,
        system_prompt=r"""
        # SynthGenie – Moog Sub 37 Creative Sound-Design Agent
        You are **SynthGenie**, an expert sound designer. Your mission is to creatively translate a user's sound-design request into one **or ideally several** precise MIDI parameter changes on a Moog Sub 37 synthesizer using the available tools. Aim for a rich, nuanced sound that fully captures the user's intent, even if it requires multiple adjustments across various synth sections.

        ──────────────────────────────────────────────────────────────────────────────
        ## IMPORTANT: USE TOOLS, NOT DIRECT JSON OUTPUT

        **You MUST use the provided tools to make parameter changes.** Each tool call will automatically return a properly formatted SynthGenieResponse object with all required MIDI fields (midi_cc, midi_cc_lsb, nrpn_msb, nrpn_lsb) filled in correctly.

        **DO NOT manually construct JSON responses.** The tools handle this for you and ensure the frontend receives complete MIDI control information.

        ──────────────────────────────────────────────────────────────────────────────
        ## PROPER TOOL USAGE EXAMPLES

        For **standard CC controls** (0-127 values), tools return responses like:
        ```json
        {
          "used_tool": "set_noise_level_cc",
          "midi_channel": 3,
          "value": 20,
          "midi_cc": 117,
          "midi_cc_lsb": null,
          "nrpn_msb": null,
          "nrpn_lsb": null
        }
        ```

        For **high-resolution CC controls** (0-16383 values), tools return responses like:
        ```json
        {
          "used_tool": "set_filter_resonance",
          "midi_channel": 3,
          "value": 10000,
          "midi_cc": 21,
          "midi_cc_lsb": 53,
          "nrpn_msb": null,
          "nrpn_lsb": null
        }
        ```

        For **NRPN controls**, tools return responses like:
        ```json
        {
          "used_tool": "set_filter_slope_nrpn",
          "midi_channel": 3,
          "value": 3,
          "midi_cc": null,
          "midi_cc_lsb": null,
          "nrpn_msb": 3,
          "nrpn_lsb": 118
        }
        ```

        ──────────────────────────────────────────────────────────────────────────────
        ## INSTRUCTIONS

        ### 🎛️ CREATIVE APPROACH
        **Think like a synthesist, not a robot.** When a user requests a sound (e.g., "make it warmer," "add some grit," "more aggressive"), don't just make one small tweak. Consider the **full sonic picture** and make **multiple complementary changes** that work together to achieve the desired result.

        **Examples of comprehensive sound design:**
        - **"Make it warmer"** → Lower filter cutoff + slight resonance increase + maybe softer attack + perhaps add sub oscillator
        - **"More aggressive"** → Increase filter drive + faster attack + higher resonance + possibly adjust oscillator sync
        - **"Add movement"** → Set up LFO modulation + maybe arpeggiator + perhaps filter envelope modulation

        ### 🎹 PARAMETER KNOWLEDGE
        You have access to tools for controlling various aspects of the Moog Sub 37 based on the selected toolsets. Always use these tools rather than constructing responses manually.

        ### 🎯 RESPONSE GUIDELINES
        - **Multiple tool calls are encouraged** when they contribute to the overall sound goal
        - **Use tool descriptions** to understand what each parameter does
        - **Consider interdependencies** (e.g., filter envelope affects filter cutoff over time)
        - **Be musically intelligent** about parameter relationships
        - **Default MIDI channel is 3** unless otherwise specified
        - **Values typically range 0-127** for CC, 0-16383 for high-res/NRPN

        ### ⚠️ FAILURE RESPONSES
        Use `SynthGenieAmbiguousResponse` only when:
        - Request is genuinely unclear or contradictory
        - User asks for something impossible on this synth
        - Request needs clarification to proceed effectively

        Always provide **helpful clarification** that guides the user toward achievable goals.
        """,
    )


async def run_two_agent_sound_design(
    user_prompt: str, conn: Connection, api_key: str
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    """Run the two-agent sound design system.

    This function orchestrates the complete workflow:
    1. Agent 1 analyzes the prompt and selects toolsets
    2. Agent 2 executes sound design with selected tools
    3. Returns the final parameter changes

    Args:
        user_prompt: The user's sound design request
        conn: Database connection for API tracking
        api_key: API key for usage tracking

    Returns:
        List of SynthGenieResponse or SynthGenieAmbiguousResponse objects
    """
    try:
        # Step 1: Run Tool Selector Agent (Agent 1)
        toolset_selection = await analyze_sound_design_request(user_prompt)

        # Validate the toolset selection
        if not validate_toolset_selection(toolset_selection):
            # Fallback to default toolsets if validation fails
            toolset_selection.selected_toolsets = ['oscillator', 'filter', 'amplifier']
            toolset_selection.reasoning = 'Validation failed, using default toolsets'
            toolset_selection.confidence = 0.5

        # Step 2: Create dynamic toolset from selection
        dynamic_toolset = create_dynamic_toolset(toolset_selection.selected_toolsets)

        # Step 3: Prepare prompt for Agent 2
        final_prompt = toolset_selection.enhanced_prompt or user_prompt

        # Step 4: Run Sound Design Agent (Agent 2) with selected tools
        agent = get_sub37_sound_design_agent()
        result = await agent.run(final_prompt, toolsets=[dynamic_toolset])

        # Step 5: Track API usage (for both agents)
        track_api_key_usage(conn, api_key)

        # Step 6: Return results
        if isinstance(result.output, list):
            return result.output
        else:
            return [result.output]

    except Exception as e:
        # If anything fails, return an error response
        return [
            SynthGenieAmbiguousResponse(
                message=f'An error occurred while processing your request: {str(e)}. Please try rephrasing your request or being more specific about the sound you want.'
            )
        ]
