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
    set_base_width_filter_base,
    set_base_width_filter_envelope_delay,
    set_base_width_filter_envelope_reset,
    set_base_width_filter_key_tracking,
    set_base_width_filter_width,
    set_comb_minus_filter_attack,
    set_comb_minus_filter_decay,
    set_comb_minus_filter_envelope_depth,
    set_comb_minus_filter_feedback,
    set_comb_minus_filter_frequency,
    set_comb_minus_filter_lowpass,
    set_comb_minus_filter_release,
    set_comb_minus_filter_sustain,
    set_comb_plus_filter_attack,
    set_comb_plus_filter_decay,
    set_comb_plus_filter_envelope_depth,
    set_comb_plus_filter_feedback,
    set_comb_plus_filter_frequency,
    set_comb_plus_filter_lowpass,
    set_comb_plus_filter_release,
    set_comb_plus_filter_sustain,
    set_equalizer_filter_attack,
    set_equalizer_filter_decay,
    set_equalizer_filter_envelope_depth,
    set_equalizer_filter_frequency,
    set_equalizer_filter_gain,
    set_equalizer_filter_q,
    set_equalizer_filter_release,
    set_equalizer_filter_sustain,
    set_legacy_lp_hp_filter_attack,
    set_legacy_lp_hp_filter_decay,
    set_legacy_lp_hp_filter_envelope_depth,
    set_legacy_lp_hp_filter_frequency,
    set_legacy_lp_hp_filter_release,
    set_legacy_lp_hp_filter_resonance,
    set_legacy_lp_hp_filter_sustain,
    set_legacy_lp_hp_filter_type,
    set_lowpass4_filter_attack,
    set_lowpass4_filter_decay,
    set_lowpass4_filter_envelope_depth,
    set_lowpass4_filter_frequency,
    set_lowpass4_filter_release,
    set_lowpass4_filter_resonance,
    set_lowpass4_filter_sustain,
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


synthgenie_agent = Agent(
    "anthropic:claude-3-7-sonnet-latest",
    tools=[
        set_multi_mode_filter_attack,
        set_multi_mode_filter_decay,
        set_multi_mode_filter_sustain,
        set_multi_mode_filter_release,
        set_multi_mode_filter_frequency,
        set_multi_mode_filter_resonance,
        set_multi_mode_filter_type,
        set_multi_mode_filter_envelope_depth,
        set_lowpass4_filter_attack,
        set_lowpass4_filter_decay,
        set_lowpass4_filter_sustain,
        set_lowpass4_filter_release,
        set_lowpass4_filter_frequency,
        set_lowpass4_filter_resonance,
        set_lowpass4_filter_envelope_depth,
        set_equalizer_filter_attack,
        set_equalizer_filter_decay,
        set_equalizer_filter_sustain,
        set_equalizer_filter_release,
        set_equalizer_filter_frequency,
        set_equalizer_filter_gain,
        set_equalizer_filter_q,
        set_equalizer_filter_envelope_depth,
        set_base_width_filter_envelope_delay,
        set_base_width_filter_key_tracking,
        set_base_width_filter_base,
        set_base_width_filter_width,
        set_base_width_filter_envelope_reset,
        set_legacy_lp_hp_filter_attack,
        set_legacy_lp_hp_filter_decay,
        set_legacy_lp_hp_filter_sustain,
        set_legacy_lp_hp_filter_release,
        set_legacy_lp_hp_filter_frequency,
        set_legacy_lp_hp_filter_resonance,
        set_legacy_lp_hp_filter_type,
        set_legacy_lp_hp_filter_envelope_depth,
        set_comb_minus_filter_attack,
        set_comb_minus_filter_decay,
        set_comb_minus_filter_sustain,
        set_comb_minus_filter_release,
        set_comb_minus_filter_frequency,
        set_comb_minus_filter_feedback,
        set_comb_minus_filter_lowpass,
        set_comb_minus_filter_envelope_depth,
        set_comb_plus_filter_attack,
        set_comb_plus_filter_decay,
        set_comb_plus_filter_sustain,
        set_comb_plus_filter_release,
        set_comb_plus_filter_frequency,
        set_comb_plus_filter_feedback,
        set_comb_plus_filter_lowpass,
        set_comb_plus_filter_envelope_depth,
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
          **Role:** You are an expert sound design assistant specifically for the Elektron Digitone synthesizer.
          **Goal:** Accurately interpret user requests describing desired sound characteristics or specific parameter changes, and use the available tools to modify the synthesizer's settings accordingly.

          **Available Tool Categories:** You have a wide range of tools to control various aspects of the Digitone sound engine:
          *   **Amplitude Envelope & Volume:** Tools to set attack, hold, decay, sustain, release, overall volume, panning, and envelope modes.
          *   **Effects (FX):** Tools to manage send levels for delay, reverb, chorus, and adjust parameters for bit reduction, sample rate reduction, and overdrive, including their routing.
          *   **Low-Frequency Oscillators (LFOs):** Tools to control speed, multiplier, waveform, depth, fade, destination, start phase, and trigger mode for LFO1, LFO2, and LFO3.
          *   **Filters:** Tools to modify parameters across multiple filter types (Multi-Mode, Lowpass4, EQ, Base/Width, Legacy LP/HP, Comb+/Comb-), including cutoff frequency, resonance, filter type, envelope controls (attack, decay, sustain, release, depth), key tracking, and specific filter parameters like Q, Gain, Base, Width, Feedback, LPF.
          *   **Wavetone Synthesis Engine:** Tools to control oscillator pitch, waveform selection, levels, phase distortion, offsets, wavetables, modulation modes, phase reset, drift, noise parameters (level, base, width, type, character), and the wavetone envelope (attack, hold, decay).

          **Instructions:**
          1.  Carefully analyze the user's prompt to understand the desired sound change or specific instruction.
          2.  Identify the relevant Digitone parameter(s) that need modification.
          3.  Select the most appropriate tool(s) from your extensive list to adjust these parameters.
          4.  Extract all necessary arguments for the tool(s), including the target value and the MIDI channel (if not specified by the user, you might need to ask or use a default like channel 1).
          5.  Execute the necessary tool calls to satisfy the user's request. You may need to call multiple distinct tools for a single user prompt (e.g., changing filter cutoff and LFO speed).
        """
    ),
)
