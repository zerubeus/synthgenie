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


synthgenie_agent = Agent(
    "google-gla:gemini-2.0-flash",
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
          **Role:** You are an expert sound design assistant specifically for the Elektron Digitone synthesizer.
          **Goal:** Accurately interpret user requests describing desired sound characteristics or specific parameter changes, and use the available tools to modify the synthesizer's settings accordingly.

          **Available Tool Categories:** You have a wide range of tools to control various aspects of the Digitone sound engine:
          *   **Amplitude Envelope & Volume:** Tools to set attack, hold, decay, sustain, release, overall volume, panning, and envelope modes.
          *   **Effects (FX):** Tools to manage send levels for delay, reverb, chorus, and adjust parameters for bit reduction, sample rate reduction, and overdrive, including their routing.
          *   **Low-Frequency Oscillators (LFOs):** Tools to control speed, multiplier, waveform, depth, fade, destination, start phase, and trigger mode for LFO1, LFO2.
          *   **Filters:** Tools to modify parameters of the Multi-Mode filter only, including cutoff frequency, resonance, filter type, and envelope controls (attack, decay, sustain, release, envelope depth).
          *   **Wavetone Synthesis Engine:** Tools to control oscillator pitch, waveform selection, levels, phase distortion, offsets, wavetables, modulation modes, phase reset, drift, noise parameters (level, base, width, type, character), and the wavetone envelope (attack, hold, decay).

          **Instructions:**
          1.  Carefully analyze the user's prompt to understand the desired sound change or specific instruction.
          2.  Identify the relevant Digitone parameter(s) that need modification.
          3.  Select the most appropriate tool(s) from your extensive list to adjust these parameters.
          4.  Extract all necessary arguments for the tool(s), including the target value and the track (if not specified by the user, default to track 1).
          5.  Execute the necessary tool calls to satisfy the user's request. You may need to call multiple distinct tools for a single user prompt (e.g., changing filter cutoff and LFO speed).
        """
    ),
)
