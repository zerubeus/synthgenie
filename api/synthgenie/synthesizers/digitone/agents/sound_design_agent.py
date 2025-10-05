import logging
import os
from dataclasses import dataclass

import psycopg2
from fastapi import HTTPException
from pydantic import ValidationError
from pydantic_ai import Agent, ModelRetry, RunContext
from pydantic_ai.exceptions import UsageLimitExceeded

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

logger = logging.getLogger(__name__)


@dataclass
class DigitoneAgentDeps:
    """Dependencies for the Digitone sound design agent."""

    default_midi_channel: int = 1
    api_key: str | None = None
    conn: psycopg2.extensions.connection | None = None
    max_requests: int = 64


def get_digitone_agent() -> Agent[DigitoneAgentDeps, list[SynthGenieResponse | SynthGenieAmbiguousResponse]]:
    """
    Create and configure the Digitone sound design agent.

    Returns:
        Agent configured with tools, dependencies, and output validation
    """
    agent = Agent(
        model=os.getenv('AGENT_MODEL', 'openai:gpt-4'),
        deps_type=DigitoneAgentDeps,
        output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse],
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
        retries=2,
        system_prompt=(
            """You are an expert sound design assistant for the Elektron Digitone synthesizer.

**Core Objective:**
Interpret user sound design requests and execute appropriate parameter changes using available tools.

**Sound Design Approach:**
- Analyze requests to understand sonic characteristics (e.g., "dark fat bass" → low filter, high sustain)
- Identify ALL relevant parameters across oscillators, filters, envelopes, LFOs, and effects
- Prioritize most impactful parameters for the sound type
- Apply standard sound design techniques

**Synthesis Machines (Digitone II):**
The Digitone has 4 machines. Tools are machine-specific:
- **FM TONE:** set_fm_tone_* (algorithms, ratios, harmonics, operator envelopes)
- **FM DRUM:** set_fm_drum_* (drum synthesis parameters)
- **WAVETONE:** set_wavetone_* (oscillators, phase distortion, noise)
- **SWARMER:** set_swarmer_* (swarm, detune, animation)
- **UNIVERSAL:** Filter, amplitude, effects, LFO tools work with all machines

⚠️ If user requests a sound requiring a different machine, return SynthGenieAmbiguousResponse explaining which machine is needed.

**Sound Design Guidelines by Type:**

*Piano (FM TONE):* Algorithms 1-2, harmonic ratios, fast attack, moderate decay/release, open filter
*Bass (FM TONE/WAVETONE):* Low filter (20-60), high sustain, punchy attack
*Lead (FM TONE/WAVETONE/SWARMER):* High filter (80-127), bright harmonics, moderate sustain
*Pad (All machines):* Slow attack (50-100), high sustain/release, LFO modulation
*Drums (FM DRUM only):* Use specialized transient, body, and noise parameters

**Parameter Execution:**
- Use exact values when user specifies (e.g., "filter resonance to 90")
- Apply sound design expertise for general requests (e.g., "make it brighter")
- Default to track 1 unless specified
- Execute all tool calls in a single, logical sequence
- For complex sounds, set ALL relevant parameters (oscillators → envelopes → filter → effects → LFOs)

**Response Rules:**
- Return **SynthGenieResponse** ONLY when changing MIDI parameters via tools
- Return **SynthGenieAmbiguousResponse** for:
  - Vague requests needing clarification
  - Questions about parameters or state
  - Machine mismatch (e.g., "Select FM TONE machine for piano sounds")
  - Informational responses

**Critical:** Only use tools matching the currently selected machine. Never attempt cross-machine tool calls.
"""
        ),
    )

    @agent.output_validator
    def validate_response(  # type: ignore[misc]
        ctx: RunContext[DigitoneAgentDeps], result: list[SynthGenieResponse | SynthGenieAmbiguousResponse]
    ) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
        """
        Validate agent output.

        Ensures:
        - At least one response is returned
        - All MIDI channel values are between 1-16
        - All parameter values are in valid range (0-127 or 0-16383)
        """
        if not result:
            raise ModelRetry('Agent must return at least one response')

        for response in result:
            if isinstance(response, SynthGenieResponse):
                # Validate MIDI channel
                if not 1 <= response.midi_channel <= 16:
                    raise ModelRetry(f'MIDI channel must be between 1-16, got {response.midi_channel}')

                # Validate value based on message type
                if response.midi_cc_lsb is not None or response.nrpn_msb is not None:
                    # High-resolution (14-bit) parameter
                    if not 0 <= response.value <= 16383:
                        raise ModelRetry(f'High-resolution value must be between 0-16383, got {response.value}')
                else:
                    # Standard 7-bit parameter
                    if not 0 <= response.value <= 127:
                        raise ModelRetry(f'Standard value must be between 0-127, got {response.value}')

        return result

    return agent


async def run_digitone_sound_design_agent(
    user_prompt: str,
    api_key: str,
    conn: psycopg2.extensions.connection,
    midi_channel: int = 1,
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    """
    Process a user prompt with the Digitone AI agent.

    Args:
        user_prompt: The user's sound design request
        api_key: API key for authentication and usage tracking
        conn: Database connection for usage tracking
        midi_channel: Default MIDI channel (track) to use (1-16)

    Returns:
        List of responses (either parameter changes or ambiguous responses)

    Raises:
        HTTPException: For usage limits, validation errors, or internal errors
    """
    if not 1 <= midi_channel <= 16:
        raise HTTPException(status_code=400, detail=f'MIDI channel must be between 1-16, got {midi_channel}')

    agent = get_digitone_agent()
    deps = DigitoneAgentDeps(
        default_midi_channel=midi_channel,
        api_key=api_key,
        conn=conn,
        max_requests=64,
    )

    try:
        logger.info(f'Running Digitone agent with prompt: {user_prompt[:100]}...')

        # Run agent with dependencies
        result = await agent.run(
            user_prompt,
            deps=deps,
        )

        logger.info(f'Agent completed successfully with {len(result.output)} responses')

        # Track API usage
        if deps.conn and deps.api_key:
            track_api_key_usage(deps.conn, deps.api_key)

        return result.output

    except UsageLimitExceeded as e:
        logger.error(f'Usage limit exceeded: {e}')
        raise HTTPException(status_code=429, detail=f'Usage limit exceeded: {str(e)}')

    except ValidationError as e:
        logger.error(f'Validation error: {e}')
        raise HTTPException(status_code=422, detail=f'Invalid response from agent: {str(e)}')

    except ValueError as e:
        logger.error(f'Value error in agent processing: {e}')
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logger.exception(f'Unexpected error during agent processing: {e}')
        raise HTTPException(
            status_code=500,
            detail='An internal error occurred during sound design processing.',
        )
