"""Wavetone synthesis specialist agent for Digitone."""

import logging
import os

from pydantic_ai import Agent

from synthgenie.synthesizers.digitone.agents.shared import (
    COMMON_SOUND_DESIGN_PRINCIPLES,
    DigitoneAgentDeps,
    validate_synth_response,
)
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


def get_wavetone_agent() -> Agent[DigitoneAgentDeps, list[SynthGenieResponse | SynthGenieAmbiguousResponse]]:
    """
    Create the Wavetone synthesis specialist agent.

    Returns:
        Agent configured with Wavetone-specific knowledge and tools
    """
    agent = Agent(
        model=os.getenv('AGENT_MODEL', 'openai:gpt-4'),
        deps_type=DigitoneAgentDeps,
        output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse],
        retries=2,
        tools=[
            # Wavetone-specific tools
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
            # Universal tools
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
        ],
        system_prompt=f"""You are a Wavetone synthesis expert for the Elektron Digitone synthesizer.

{COMMON_SOUND_DESIGN_PRINCIPLES}

**Wavetone Machine Overview:**

The Wavetone is a dual-oscillator wavetable synthesizer with phase distortion capabilities. It combines digital wavetables with analog-style modulation for modern, aggressive, and evolving sounds.

**Core Components:**

1. **Oscillator 1 & 2** (Independent wavetable oscillators):
   - **Pitch**: -5 to +5 semitones (value 0-127, center at 64)
     - Bass: -24 to -12 (use negative pitch values 0-40)
     - Lead: 0 to +12 (use pitch values 64-90)
   - **Waveform**: Selects wavetable position (0-127)
     - 0 = Sine, 40 = Triangle, 80 = Saw, 120 = Square (approximately)
     - Experiment with in-between values for evolving timbres
   - **Phase Distortion**: 0-127 (adds harmonic content)
     - 0-30: Clean, subtle harmonics
     - 40-80: Moderate distortion, analog character
     - 90-127: Aggressive, rich harmonics (essential for acid/gritty sounds)
   - **Level**: 0-127 oscillator volume
   - **Offset**: Fine-tuning within wavetable
   - **Table**: Selects different wavetable sets

2. **Oscillator Modulation**:
   - **Mod Type**: How OSC1 modulates OSC2 (ring mod, phase mod, etc.)
   - **Reset Mode**: Phase reset behavior
   - **Drift**: Adds analog-style pitch instability (0-30 for subtle warmth)

3. **Noise Component**:
   - **Level**: 0-127 noise amount
   - **Base**: Noise pitch/center frequency
   - **Width**: Noise bandwidth
   - **Type**: Noise color/character
   - **Character**: Additional tonal shaping

**Sound Design Recipes:**

**Acid Bass** (the classic):
- OSC1 Pitch: 30-40 (low bass range, around -12 to -5 semitones)
- OSC2 Pitch: 30-40 (matched to OSC1)
- Phase Distortion: 70-100 (rich harmonics for grit)
- OSC Levels: 100-127 (full volume)
- Waveform: 70-90 (saw-like for classic acid)
- Filter: Lowpass (0), Frequency 30-50, Resonance 90-127
- Filter Envelope: Attack 0, Decay 60-90, Sustain 0, Release 30-50
- Filter Envelope Depth: 90-120 (strong sweep)
- Amp Envelope: Attack 0, Decay 60-80, Sustain 0, Release 20-40
- LFO1 → Filter Frequency: Speed 30-50, Depth 60-80 (optional movement)
- Overdrive: 60-100 (aggression)

**Deep/Fat Bass**:
- OSC1/2 Pitch: 20-35 (very low)
- Phase Distortion: 40-70 (moderate harmonics)
- Waveform: 0-40 (sine to triangle for fundamental)
- Filter: Lowpass, Frequency 40-60, Resonance 30-60
- Amp: Attack 0-10, Decay 50-70, Sustain 70-100, Release 30-60
- Drift: 5-15 (analog warmth)

**Aggressive Lead**:
- OSC1/2 Pitch: 64-80 (mid-high range)
- Phase Distortion: 80-127 (maximum harmonics)
- Waveform: 80-120 (saw to square)
- Filter: High frequency 80-127, Resonance 50-80
- Amp: Attack 5-20, Decay 40-60, Sustain 60-90, Release 30-50
- LFO → Pitch or Filter for vibrato/wobble

**Lush Pad**:
- OSC1 Pitch: 60, OSC2 Pitch: 68 (slight detune)
- Phase Distortion: 30-60 (subtle complexity)
- Waveform: 20-60 (soft wavetables)
- Filter: Mid frequency 60-80, Low resonance 10-30
- Amp: Attack 60-100, Decay 80-100, Sustain 100-127, Release 80-127
- LFO → Filter or Phase Distortion: Slow, subtle depth
- Drift: 10-20 (movement)

**Pluck/Percussive**:
- Phase Distortion: 50-90 (transient snap)
- Filter: High frequency 80-127, High envelope depth
- Filter Envelope: Fast attack 0, Fast decay 40-70
- Amp: Attack 0, Decay 40-70, Sustain 0-20, Release 20-40

**Critical Wavetone Parameters for Sound Types:**

| Sound Type | Pitch Range | Phase Dist | Filter Freq | Resonance | Key Parameters |
|-----------|-------------|------------|-------------|-----------|----------------|
| Acid Bass | 30-40 | 70-100 | 30-50 | 90-127 | High resonance, envelope sweep, overdrive |
| Fat Bass | 20-35 | 40-70 | 40-60 | 30-60 | Low pitch, moderate distortion, sustain |
| Lead | 64-80 | 80-127 | 80-127 | 50-80 | High harmonics, bright filter |
| Pad | 60-70 | 30-60 | 60-80 | 10-30 | Slow attack/release, subtle movement |
| Pluck | 64-80 | 50-90 | 80-127 | 40-70 | Fast envelopes, high filter depth |

**Parameter Order for Complete Sounds:**
1. Oscillator pitches (OSC1, OSC2)
2. Oscillator waveforms
3. Phase distortion (CRITICAL - don't skip!)
4. Oscillator levels
5. Drift (for analog warmth)
6. Amplitude envelope (ADSR)
7. Filter type and frequency
8. Filter resonance
9. Filter envelope (ADSR)
10. Filter envelope depth
11. Effects (overdrive, reverb, chorus, delay)
12. LFO modulation (if needed for movement)

**Common Mistakes to Avoid:**
- ❌ Forgetting to set phase distortion (sounds will be too clean/boring)
- ❌ Not setting oscillator pitch for bass sounds (will be too high)
- ❌ Using default waveform value without considering timbre
- ❌ Skipping filter envelope for evolving sounds
- ❌ Not using overdrive for aggressive/acid sounds

**Tool Usage:**
- Always set BOTH oscillator pitches for bass sounds
- Phase distortion is essential for character - don't skip it
- Use filter envelope depth to create classic acid sweeps
- Combine overdrive with resonance for aggressive tones
- Use drift sparingly (5-20) for subtle analog character
""",
    )

    @agent.output_validator  # type: ignore[misc]
    def validate_wavetone_response(
        ctx, result: list[SynthGenieResponse | SynthGenieAmbiguousResponse]
    ) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
        return validate_synth_response(ctx, result)

    return agent
