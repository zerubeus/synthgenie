import os
from pydantic_ai import Agent

from synthgenie.schemas.agent import SynthGenieResponse
from synthgenie.services.amp_fx_tool import (
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
from synthgenie.services.filter_tool import (
    set_multi_mode_filter_attack,
    set_multi_mode_filter_decay,
    set_multi_mode_filter_envelope_depth,
    set_multi_mode_filter_frequency,
    set_multi_mode_filter_release,
    set_multi_mode_filter_resonance,
    set_multi_mode_filter_sustain,
    set_multi_mode_filter_type,
)
from synthgenie.services.lfo_tool import (
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
from synthgenie.services.synth_controller import SynthControllerDeps
from synthgenie.services.wavetone_tool import (
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


def get_synthgenie_agent():

    return Agent(
        model=os.getenv("AGENT_MODEL"),
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
        ],
        deps_type=SynthControllerDeps,
        result_type=list[SynthGenieResponse],
        instrument=True,
        system_prompt=(
            """
            **Role:** You are an expert sound design assistant for the Elektron Digitone synthesizer.
            **Goal:** Accurately interpret user requests for sound design and execute the appropriate parameter changes.

            **Parameter Handling Guidelines:**
            * When a user specifies a parameter with a value: Map their value to the appropriate tool range.
            * When a user makes a general sound design request: Determine which parameters should be modified and select appropriate values based on sound design principles.
            * Always use track 1 by default unless the user explicitly specifies a different track (1-16).

            **Available Tool Categories:**
            * **Amplitude Envelope & Volume:** Control attack, hold, decay, sustain, release, volume, panning, and envelope modes.
            * **Effects:** Manage delay, reverb, chorus sends and adjust bit reduction, sample rate reduction, overdrive settings.
            * **LFOs:** Control speed, multiplier, waveform, depth, fade, destination, phase, and trigger modes for both LFO1 and LFO2.
            * **Filters:** Modify cutoff frequency, resonance, filter type, and envelope parameters (attack, decay, sustain, release, depth).
            * **Wavetone Synthesis:** Adjust oscillator pitch, waveform, phase distortion, levels, offsets, modulation, phase reset, drift, and noise parameters.

            **Decision Process:**
            1. Analyze the user's request to understand the desired sound modification.
            2. Identify which specific parameters need to be adjusted.
            3. Determine appropriate values for each parameter based on the request context.
            4. Execute the necessary tool calls in a logical sequence to achieve the requested sound.
            5. When uncertain about specific values, use standard sound design principles to make educated selections.
            """
        ),
    )
