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
from synthgenie.synthesizers.digitone.tools.fm_drum_tool import (
    set_fm_drum_algorithm,
    set_fm_drum_body_decay,
    set_fm_drum_body_hold,
    set_fm_drum_body_level,
    set_fm_drum_decay1,
    set_fm_drum_decay2,
    set_fm_drum_end1,
    set_fm_drum_end2,
    set_fm_drum_feedback,
    set_fm_drum_fold,
    set_fm_drum_mod1,
    set_fm_drum_mod2,
    set_fm_drum_noise_base,
    set_fm_drum_noise_decay,
    set_fm_drum_noise_grain,
    set_fm_drum_noise_hold,
    set_fm_drum_noise_level,
    set_fm_drum_noise_reset,
    set_fm_drum_noise_ring_mod,
    set_fm_drum_noise_width,
    set_fm_drum_op_ab_wave,
    set_fm_drum_op_c_phase,
    set_fm_drum_op_c_wave,
    set_fm_drum_ratio1,
    set_fm_drum_ratio2,
    set_fm_drum_sweep_depth,
    set_fm_drum_sweep_time,
    set_fm_drum_transient,
    set_fm_drum_transient_level,
    set_fm_drum_tune,
)
from synthgenie.synthesizers.digitone.tools.fm_tone_tool import (
    set_fm_tone_a_attack,
    set_fm_tone_a_decay,
    set_fm_tone_a_delay,
    set_fm_tone_a_end,
    set_fm_tone_a_key_track,
    set_fm_tone_a_level,
    set_fm_tone_a_ratio,
    set_fm_tone_a_ratio_offset,
    set_fm_tone_a_reset,
    set_fm_tone_a_trigger,
    set_fm_tone_algorithm,
    set_fm_tone_b1_key_track,
    set_fm_tone_b1_ratio_offset,
    set_fm_tone_b2_key_track,
    set_fm_tone_b2_ratio_offset,
    set_fm_tone_b_attack,
    set_fm_tone_b_decay,
    set_fm_tone_b_delay,
    set_fm_tone_b_end,
    set_fm_tone_b_level,
    set_fm_tone_b_ratio,
    set_fm_tone_b_reset,
    set_fm_tone_b_trigger,
    set_fm_tone_c_ratio,
    set_fm_tone_c_ratio_offset,
    set_fm_tone_detune,
    set_fm_tone_feedback,
    set_fm_tone_harmonics,
    set_fm_tone_mix,
    set_fm_tone_phase_reset,
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
            set_fm_tone_algorithm,
            set_fm_tone_c_ratio,
            set_fm_tone_a_ratio,
            set_fm_tone_b_ratio,
            set_fm_tone_harmonics,
            set_fm_tone_detune,
            set_fm_tone_feedback,
            set_fm_tone_mix,
            set_fm_tone_a_attack,
            set_fm_tone_a_decay,
            set_fm_tone_a_end,
            set_fm_tone_a_level,
            set_fm_tone_b_attack,
            set_fm_tone_b_decay,
            set_fm_tone_b_end,
            set_fm_tone_b_level,
            set_fm_tone_a_delay,
            set_fm_tone_a_trigger,
            set_fm_tone_a_reset,
            set_fm_tone_phase_reset,
            set_fm_tone_b_delay,
            set_fm_tone_b_trigger,
            set_fm_tone_b_reset,
            set_fm_tone_c_ratio_offset,
            set_fm_tone_a_ratio_offset,
            set_fm_tone_b1_ratio_offset,
            set_fm_tone_b2_ratio_offset,
            set_fm_tone_a_key_track,
            set_fm_tone_b1_key_track,
            set_fm_tone_b2_key_track,
            set_fm_drum_tune,
            set_fm_drum_sweep_time,
            set_fm_drum_sweep_depth,
            set_fm_drum_algorithm,
            set_fm_drum_op_c_wave,
            set_fm_drum_op_ab_wave,
            set_fm_drum_feedback,
            set_fm_drum_fold,
            set_fm_drum_ratio1,
            set_fm_drum_decay1,
            set_fm_drum_end1,
            set_fm_drum_mod1,
            set_fm_drum_ratio2,
            set_fm_drum_decay2,
            set_fm_drum_end2,
            set_fm_drum_mod2,
            set_fm_drum_body_hold,
            set_fm_drum_body_decay,
            set_fm_drum_op_c_phase,
            set_fm_drum_body_level,
            set_fm_drum_noise_reset,
            set_fm_drum_noise_ring_mod,
            set_fm_drum_noise_hold,
            set_fm_drum_noise_decay,
            set_fm_drum_transient,
            set_fm_drum_transient_level,
            set_fm_drum_noise_base,
            set_fm_drum_noise_width,
            set_fm_drum_noise_grain,
            set_fm_drum_noise_level,
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

            **IMPORTANT - Machine Selection:**
            *   The Digitone II has 4 synthesis machines: FM TONE, FM DRUM, WAVETONE, and SWARMER
            *   You can ONLY use the tools that match the currently selected machine on the track
            *   If the user asks for a sound that requires a specific machine, inform them they need to select that machine first
            *   Machine-to-tool mapping:
                - **FM TONE machine:** Use set_fm_tone_* tools (algorithms, ratios, harmonics, operator envelopes, etc.)
                - **FM DRUM machine:** Use set_fm_drum_* tools (drum-specific parameters)
                - **WAVETONE machine:** Use set_wavetone_* tools (oscillators, phase distortion, noise)
                - **SWARMER machine:** Use set_swarmer_* tools (swarm, detune, animation)
            *   Filter, amplitude, effects, and LFO tools work with ALL machines

            **Instrument-Specific Sound Design Guidelines:**
            
            **Piano Sounds (Acoustic/Electric) - Requires FM TONE machine:**
            *   **FM Algorithm:** Use algorithm 1 (value=0) or 2 (value=1) for piano-like tones. Algorithm 1 gives classic 4-op stack for complex harmonics, Algorithm 2 provides dual 2-op stacks for cleaner tone.
            *   **Operator Ratios:** 
                - C ratio: value=2 (ratio 1.0 - fundamental frequency)
                - A ratio: value=7 (ratio 2.0) or value=10 (ratio 3.0) for harmonic overtones
                - B ratio: value=3 (highest available, approximates ratio 16) for metallic string resonance
            *   **Harmonics:** value=64 (neutral/0) to value=74 (slight positive +10) for clean piano tones
            *   **Feedback:** value=20-30 for subtle warmth without harshness
            *   **Detune:** value=10-15 for slight beating between strings
            *   **Operator Envelopes:**
                - A Attack: value=0-5, A Decay: value=50-70, A End: value=0-15, A Level: value=80-100
                - B Attack: value=0-5, B Decay: value=35-50, B End: value=0, B Level: value=60-80
            *   **Amplitude Envelope:** Attack=0, Hold=0, Decay=85-100, Sustain=0, Release=60-80
            *   **Filter:** Frequency=120-127 (fully open), Resonance=0-10 for natural tone
            *   **Effects:** Reverb=35-45, Chorus=20-30 for richness
            *   **Mix:** value=10-25 (slightly towards Y output for brightness)

            **Bass Sounds - Best with FM TONE or WAVETONE machine:**
            *   **FM TONE:** Use algorithms 4 (value=3), 5 (value=4), or 8 (value=7) for deep fundamental with controlled harmonics
            *   **WAVETONE:** Use low-pitched oscillators with phase distortion for analog-style bass
            *   **Filter:** Low frequency (20-60), moderate resonance (20-50)
            *   **Amplitude:** Punchy attack (0-10), medium decay (40-60), high sustain (80-100)

            **Lead Sounds - Works with FM TONE, WAVETONE, or SWARMER:**
            *   **FM TONE:** Algorithms 3 (value=2), 6 (value=5) for bright, cutting tones
            *   **WAVETONE:** High oscillator levels with phase distortion for aggressive leads
            *   **SWARMER:** Use for detuned unison leads with animation
            *   **Filter:** High frequency (80-127), moderate resonance (30-60)
            *   **Harmonics:** Higher values for richer timbres

            **Pad Sounds - Works with all machines:**
            *   **FM TONE:** Algorithms with multiple carriers for complex, evolving textures
            *   **WAVETONE:** Soft waveforms with slow modulation
            *   **SWARMER:** Perfect for lush, animated pads with swarm parameter
            *   **Amplitude:** Slow attack (50-100), high sustain (90-127), slow release (80-127)
            *   **LFO:** Subtle pitch or filter modulation for movement

            **Drum/Percussion Sounds - Requires FM DRUM machine:**
            *   Use FM DRUM machine exclusively for kick, snare, hi-hat, and percussion sounds
            *   FM DRUM has specialized parameters for transients, body, and noise components

            **Parameter Handling Guidelines:**
            *   **Explicit Values:** If the user provides a specific parameter and value (e.g., "set filter resonance to 90"), use that exact value after mapping it to the tool's range.
            *   **General Requests:** If the user makes a general request (e.g., "make it brighter"), determine the most relevant parameters and select appropriate values based on your sound design expertise.
            *   **Default Track:** Always use track 1 by default unless the user explicitly specifies a different track (1-16).

            **Execution:**
            *   Plan and execute the necessary tool calls in a single, logical sequence to achieve the requested sound modification based on your analysis.
            *   Use the tool descriptions to understand parameter ranges and mappings.
            *   For complex sounds like pianos, ensure you set ALL relevant parameters for a complete sound design.
            *   **Parameter Order:** When designing sounds from scratch, follow this order:
                1. FM Algorithm selection
                2. Operator ratios (C, A, B)
                3. Operator envelopes (attack, decay, end, level for both A and B)
                4. Harmonics and feedback
                5. Detune and mix
                6. Amplitude envelope (ADSR)
                7. Filter settings
                8. Effects (reverb, chorus, delay)
                9. LFO settings if needed
            *   **Always initialize unused LFOs:** Set LFO destinations to 0 (OFF) if not using modulation

            **Available Tool Categories:**
            *   **Amplitude Envelope & Volume:** Control attack, hold, decay, sustain, release, volume, panning, and envelope modes.
            *   **Effects:** Manage delay, reverb, chorus sends and adjust bit reduction, sample rate reduction, overdrive settings.
            *   **LFOs:** Control speed, multiplier, waveform, depth, fade, destination, phase, and trigger modes for both LFO1 and LFO2.
            *   **Filters:** Modify cutoff frequency, resonance, filter type, and envelope parameters (attack, decay, sustain, release, depth).
            *   **Wavetone Synthesis:** Adjust oscillator pitch, waveform, phase distortion, levels, offsets, modulation, phase reset, drift, and noise parameters.
            *   **FM Tone Synthesis:** Control FM algorithm, operator ratios (C, A, B1/B2), harmonics, detune, feedback, mix, operator envelopes (attack, decay, end level, level), envelope delays, triggers, resets, phase reset modes, ratio offsets, and key tracking.
            *   **FM Drum Synthesis:** Specialized FM engine for drums with tune, sweep time/depth, algorithm, operator waves, feedback, wavefolding, operator ratios/envelopes, body/noise envelopes, phase control, transients, and noise shaping (base, width, grain, ring mod).
            *   **Swarmer Synthesis:** Adjust tuning, swarm amount, detune, mix, main oscillator octave and settings, animation, and noise modulation.

            **Response Handling:**
            *   **Ambiguous Responses:** If the user's request is too vague to determine appropriate parameter(s), return a SynthGenieAmbiguousResponse.
            *   **Informational Responses:** If the user asks questions about parameters or their current state (e.g., "where is the distortion?", "what is the current filter cutoff?"), return a SynthGenieAmbiguousResponse with helpful information.
            *   **Machine Mismatch:** If the user requests a sound that requires a different machine than what's currently selected:
                - Return a SynthGenieAmbiguousResponse explaining which machine is needed
                - Example: "To create a piano sound, please select the FM TONE machine on track 1 first."
                - Do NOT attempt to use tools from a different machine than what's selected
            *   **Important:** Only use tool calls that return SynthGenieResponse objects when you need to actually change MIDI parameters. For all other responses (questions, clarifications, information), use SynthGenieAmbiguousResponse.
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
                                    # Log the actual type and content for debugging
                                    logger.info(
                                        f'FunctionToolResultEvent received - type: {type(event.result.content)}, content: {event.result.content}'
                                    )

                                    # The result.content can be a ToolReturnPart or RetryPromptPart
                                    # We need to check if it has a 'content' attribute and handle it appropriately
                                    result_content = event.result.content

                                    # Handle both direct SynthGenieResponse objects and dictionaries
                                    if isinstance(result_content, SynthGenieResponse):
                                        logger.debug(f'Collected tool result: {result_content}')
                                        collected_responses.append(result_content)
                                    elif isinstance(result_content, dict):
                                        try:
                                            # Try to parse the dictionary as a SynthGenieResponse
                                            response = SynthGenieResponse.model_validate(result_content)
                                            logger.debug(f'Parsed tool result from dict: {response}')
                                            collected_responses.append(response)
                                        except Exception as e:
                                            logger.warning(
                                                f'Tool call {event.tool_call_id} failed to parse dict as SynthGenieResponse: {e} - {result_content}'
                                            )
                                    else:
                                        logger.warning(
                                            f'Tool call {event.tool_call_id} result content was not SynthGenieResponse or dict: {type(result_content).__name__} - {result_content}'
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
