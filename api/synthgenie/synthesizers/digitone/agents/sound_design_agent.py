import logging
import os

import psycopg2
from fastapi import HTTPException
from pydantic_ai import Agent, UsageLimitExceeded
from pydantic_ai.messages import FunctionToolResultEvent
from pydantic_ai.usage import UsageLimits
from pydantic_graph import End

from synthgenie.auth.models import track_api_key_usage
from synthgenie.synthesizers.digitone.tools.amp_fx_tool import (
    set_amp_attack,
    set_amp_decay,
    set_amp_envelope_mode,
    set_amp_envelope_reset,
    set_amp_hold,
    set_amp_pan,
    set_amp_release,
    set_amp_sustain,
    set_amp_volume,
    set_fx_bit_reduction,
    set_fx_chorus,
    set_fx_delay,
    set_fx_overdrive,
    set_fx_overdrive_routing,
    set_fx_reverb,
    set_fx_sample_rate_reduction,
    set_fx_sample_rate_routing,
)
from synthgenie.synthesizers.digitone.tools.filter_tool import (
    set_multi_mode_filter_attack,
    set_multi_mode_filter_decay,
    set_multi_mode_filter_envelope_depth,
    set_multi_mode_filter_frequency,
    set_multi_mode_filter_release,
    set_multi_mode_filter_resonance,
    set_multi_mode_filter_sustain,
    set_multi_mode_filter_type,
)
from synthgenie.synthesizers.digitone.tools.lfo_tool import (
    set_lfo1_depth,
    set_lfo1_destination,
    set_lfo1_fade,
    set_lfo1_multiplier,
    set_lfo1_speed,
    set_lfo1_start_phase,
    set_lfo1_trigger_mode,
    set_lfo1_waveform,
    set_lfo2_depth,
    set_lfo2_destination,
    set_lfo2_fade,
    set_lfo2_multiplier,
    set_lfo2_speed,
    set_lfo2_start_phase,
    set_lfo2_trigger_mode,
    set_lfo2_waveform,
)
from synthgenie.synthesizers.digitone.tools.swarmer_tool import (
    set_swarmer_animation,
    set_swarmer_detune,
    set_swarmer_main,
    set_swarmer_main_octave,
    set_swarmer_mix,
    set_swarmer_noise_mod,
    set_swarmer_swarm,
    set_swarmer_tune,
)
from synthgenie.synthesizers.digitone.tools.wavetone_tool import (
    set_wavetone_attack,
    set_wavetone_decay,
    set_wavetone_drift,
    set_wavetone_hold,
    set_wavetone_mod_type,
    set_wavetone_noise_base,
    set_wavetone_noise_character,
    set_wavetone_noise_level,
    set_wavetone_noise_type,
    set_wavetone_noise_width,
    set_wavetone_osc1_level,
    set_wavetone_osc1_offset,
    set_wavetone_osc1_phase_distortion,
    set_wavetone_osc1_pitch,
    set_wavetone_osc1_table,
    set_wavetone_osc1_waveform,
    set_wavetone_osc2_level,
    set_wavetone_osc2_offset,
    set_wavetone_osc2_phase_distortion,
    set_wavetone_osc2_pitch,
    set_wavetone_osc2_table,
    set_wavetone_osc2_waveform,
    set_wavetone_reset_mode,
)
from synthgenie.synthesizers.shared.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse

MAX_STEPS = 70  # Slightly more than REQUEST_LIMIT

REQUEST_LIMIT = 64  # Keep existing request limit

logger = logging.getLogger(__name__)


def get_digitone_agent():
    return Agent(
        model=os.getenv('AGENT_MODEL'),
        tools=[
            set_multi_mode_filter_attack,
            set_multi_mode_filter_decay,
            set_multi_mode_filter_sustain,
            set_multi_mode_filter_release,
            set_multi_mode_filter_frequency,
            set_multi_mode_filter_resonance,
            set_multi_mode_filter_type,
            set_multi_mode_filter_envelope_depth,
            set_amp_attack,
            set_amp_hold,
            set_amp_decay,
            set_amp_sustain,
            set_amp_release,
            set_amp_envelope_reset,
            set_amp_envelope_mode,
            set_amp_pan,
            set_amp_volume,
            set_fx_bit_reduction,
            set_fx_overdrive,
            set_fx_sample_rate_reduction,
            set_fx_sample_rate_routing,
            set_fx_overdrive_routing,
            set_fx_delay,
            set_fx_reverb,
            set_fx_chorus,
            set_lfo1_speed,
            set_lfo1_multiplier,
            set_lfo1_fade,
            set_lfo1_destination,
            set_lfo1_waveform,
            set_lfo1_start_phase,
            set_lfo1_trigger_mode,
            set_lfo1_depth,
            set_lfo2_speed,
            set_lfo2_multiplier,
            set_lfo2_fade,
            set_lfo2_destination,
            set_lfo2_waveform,
            set_lfo2_start_phase,
            set_lfo2_trigger_mode,
            set_lfo2_depth,
            set_wavetone_osc1_pitch,
            set_wavetone_osc1_waveform,
            set_wavetone_osc1_phase_distortion,
            set_wavetone_osc1_level,
            set_wavetone_osc1_offset,
            set_wavetone_osc1_table,
            set_wavetone_osc2_pitch,
            set_wavetone_osc2_waveform,
            set_wavetone_osc2_phase_distortion,
            set_wavetone_osc2_level,
            set_wavetone_osc2_offset,
            set_wavetone_osc2_table,
            set_wavetone_mod_type,
            set_wavetone_reset_mode,
            set_wavetone_drift,
            set_wavetone_attack,
            set_wavetone_hold,
            set_wavetone_decay,
            set_wavetone_noise_level,
            set_wavetone_noise_base,
            set_wavetone_noise_width,
            set_wavetone_noise_type,
            set_wavetone_noise_character,
            set_swarmer_tune,
            set_swarmer_swarm,
            set_swarmer_detune,
            set_swarmer_mix,
            set_swarmer_main_octave,
            set_swarmer_main,
            set_swarmer_animation,
            set_swarmer_noise_mod,
        ],
        output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse],
        instrument=True,
        system_prompt=(
            """
            **Role:** You are an expert sound design assistant for the Elektron Digitone synthesizer.
            **Goal:** Accurately interpret user requests for sound design and execute the appropriate parameter changes using the available tools.

            **Sound Design Principles:**
            *   Analyze the user's request (e.g., "dark fat bass", "shimmering pad", "percussive pluck") to understand the core sonic characteristics.
            *   For general requests, identify *all relevant* parameters across oscillators, filters, envelopes, LFOs, and effects that contribute to the desired sound.
            *   Select appropriate values for these parameters based on standard sound design techniques to achieve the target sound effectively.
            *   Prioritize parameters most impactful for the requested sound type (e.g., low filter frequency for dark sounds, oscillator waveforms/levels/pitch for timbre, envelopes for shape).

            **Parameter Handling Guidelines:**
            *   **Explicit Values:** If the user provides a specific parameter and value (e.g., "set filter resonance to 90"), use that exact value after mapping it to the tool's range.
            *   **General Requests:** If the user makes a general request (e.g., "make it brighter"), determine the most relevant parameters and select appropriate values based on your sound design expertise.
            *   **Default Track:** Always use track 1 by default unless the user explicitly specifies a different track (1-16).

            **Execution:**
            *   Plan and execute the necessary tool calls in a single, logical sequence to achieve the requested sound modification based on your analysis.
            *   Use the tool descriptions to understand parameter ranges and mappings.

            **Available Tool Categories:**
            *   **Amplitude Envelope & Volume:** Control attack, hold, decay, sustain, release, volume, panning, and envelope modes.
            *   **Effects:** Manage delay, reverb, chorus sends and adjust bit reduction, sample rate reduction, overdrive settings.
            *   **LFOs:** Control speed, multiplier, waveform, depth, fade, destination, phase, and trigger modes for both LFO1 and LFO2.
            *   **Filters:** Modify cutoff frequency, resonance, filter type, and envelope parameters (attack, decay, sustain, release, depth).
            *   **Wavetone Synthesis:** Adjust oscillator pitch, waveform, phase distortion, levels, offsets, modulation, phase reset, drift, and noise parameters.

            **Response Handling:**
            *   **Ambiguous Responses:** If the user's request is too vague to determine appropriate parameter(s), return a SynthGenieAmbiguousResponse.
            """
        ),
    )


async def run_digitone_sound_design_agent(user_prompt: str, api_key: str, conn: psycopg2.extensions.connection):
    """
    Process a user prompt with the Digitone AI agent.

    This implementation forces the agent to stop after the first cycle
    of tool execution and collects results via events to prevent loops.

    Requires a valid API key.
    """
    agent = get_digitone_agent()
    step_count = 0
    first_tool_call_node_processed = False
    collected_responses: list[SynthGenieResponse | SynthGenieAmbiguousResponse] = []

    try:
        async with agent.iter(
            user_prompt,
            usage_limits=UsageLimits(request_limit=REQUEST_LIMIT),
        ) as agent_run:
            node = agent_run.next_node

            while not isinstance(node, End):
                step_count += 1
                logger.debug(f'Agent step {step_count}: {type(node).__name__}')

                if step_count > MAX_STEPS:
                    logger.error(f'Agent exceeded maximum step limit ({MAX_STEPS}). Forcing stop.')
                    break

                processed_node = node

                # --- Event Collection Logic ---
                # If processing the node where tools are called, stream events to capture results
                if Agent.is_call_tools_node(processed_node):
                    logger.info('Streaming events from CallToolsNode to collect results...')
                    try:
                        async with processed_node.stream(agent_run.ctx) as handle_stream:
                            async for event in handle_stream:
                                if isinstance(event, FunctionToolResultEvent):
                                    # Ensure the result content is the expected type
                                    if isinstance(event.result.content, SynthGenieResponse):
                                        logger.debug(f'Collected tool result: {event.result.content}')
                                        collected_responses.append(event.result.content)
                                    else:
                                        logger.warning(
                                            f'Tool call {event.tool_call_id} result content was not SynthGenieResponse: {type(event.result.content)}'
                                        )
                        first_tool_call_node_processed = True
                        logger.info(
                            f'Finished streaming CallToolsNode. Collected {len(collected_responses)} responses.'
                        )
                    except Exception as stream_exc:
                        # Catch errors specifically during the event streaming/tool execution phase
                        logger.exception(f'Error during CallToolsNode event streaming: {stream_exc}')
                        # Depending on desired behavior, we might raise here or just log and continue
                        # Let's break the loop to be safe and report based on potentially partial results
                        break
                # --- End Event Collection ---

                # Advance to the next node *after* potentially streaming the current one
                if isinstance(processed_node, End):
                    break

                node = await agent_run.next(processed_node)

                # **Core Stop Logic:** If we just processed the tools node, and the *next* step
                # is the agent wanting to think again, stop now.
                if first_tool_call_node_processed and Agent.is_model_request_node(node):
                    logger.info('First tool call cycle completed. Stopping agent before second reasoning step.')
                    break

            # --- Loop finished (End node, MAX_STEPS, stream error, or early break) ---

            # Return the explicitly collected responses
            if collected_responses:
                logger.info(
                    f'Agent finished or was stopped. Returning {len(collected_responses)} collected responses after {step_count} steps.'
                )
                track_api_key_usage(conn, api_key)
                return collected_responses
            else:
                # Handle cases where loop finished but no responses were collected
                log_message = 'Agent run finished, but no tool responses were collected.'
                if first_tool_call_node_processed:
                    log_message = 'Agent processed tool calls, but failed to collect any valid SynthGenieResponse results (check tool implementations and logs).'
                elif step_count >= MAX_STEPS:
                    log_message = f'Agent hit MAX_STEPS ({MAX_STEPS}) without collecting results.'
                logger.error(f'{log_message} Step count: {step_count}')
                # Use a more specific detail message
                raise HTTPException(status_code=500, detail=log_message)

    except UsageLimitExceeded as e:
        logger.error(f'Usage limit exceeded: {e}')
        raise HTTPException(status_code=429, detail=str(e))
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.exception(f'An unexpected error occurred during agent processing: {e}')
        raise HTTPException(
            status_code=500,
            detail='An internal error occurred during agent processing.',
        )
