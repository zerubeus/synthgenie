"""FM Tone synthesis specialist agent for Digitone."""

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
from synthgenie.synthesizers.shared.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse

logger = logging.getLogger(__name__)


def get_fm_tone_agent() -> Agent[DigitoneAgentDeps, list[SynthGenieResponse | SynthGenieAmbiguousResponse]]:
    """
    Create the FM Tone synthesis specialist agent.

    Returns:
        Agent configured with FM Tone-specific knowledge and tools
    """
    agent = Agent(
        model=os.getenv('AGENT_MODEL', 'openai:gpt-4'),
        deps_type=DigitoneAgentDeps,
        output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse],
        retries=2,
        tools=[
            # FM Tone-specific tools
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
        system_prompt=f"""You are an FM Tone synthesis expert for the Elektron Digitone synthesizer.

{COMMON_SOUND_DESIGN_PRINCIPLES}

**FM Tone Machine Overview:**

FM Tone is a 4-operator FM synthesizer inspired by classic FM synths like the Yamaha DX7. It excels at metallic, bell-like, electric piano, bass, lead, and complex evolving sounds through frequency modulation.

**Core Concepts:**

**Operators**: 4 sine wave generators (C, A, B1, B2) that can be carriers or modulators
- **Carriers**: Produce audible output (X and Y outputs)
- **Modulators**: Modulate carriers to create harmonic complexity
- Each operator has: Ratio, Envelope (Attack, Decay, End level), Level

**Algorithms**: 8 routing configurations (how operators modulate each other)
- Algorithm 1 (0): B2→B1→A→C - Complex, stacked modulation
- Algorithm 2 (1): Dual 2-op stacks - Two independent FM pairs
- Algorithm 3 (2): Three modulators→one carrier - Rich harmonics
- Algorithm 4 (3): Y-shaped routing - Branched modulation
- Algorithm 5 (4): Diamond cross-modulation - Complex interactions
- Algorithm 6 (5): Two carriers + shared modulators - Dual timbres
- Algorithm 7 (6): Parallel with shared modulator - Bright sounds
- Algorithm 8 (7): Four parallel carriers - Additive synthesis

**Key Parameters:**

1. **Ratios** (Operator frequency multipliers):
   - C Ratio: Usually 1.0 (fundamental) or 2.0 (octave up)
   - A Ratio: Wide range for harmonic/inharmonic sounds
   - B Ratio: Modulator ratios create timbral complexity
   - Integer ratios (1, 2, 3, 4) = harmonic
   - Non-integer ratios = inharmonic/bell-like

2. **Harmonics**: Global harmonic content (64 = neutral, higher = brighter)

3. **Feedback**: Operator self-modulation (adds grit and noise)

4. **Detune**: Pitch offset between operators (analog warmth)

5. **Mix**: Balance between X and Y outputs

**Sound Design Recipes:**

**Electric Piano (Classic DX-style)**:
- Algorithm: 1 or 2 (0 or 1)
- C Ratio: 2 (1.0 fundamental)
- A Ratio: 7-10 (2.0-3.0 for bell-like overtones)
- B Ratio: 3 or higher (complex modulation)
- Harmonics: 64-74 (neutral to slightly bright)
- Feedback: 20-35 (subtle warmth)
- Detune: 10-15 (chorus effect)
- A Envelope: Attack 0-5, Decay 50-70, End 10-20, Level 85-100
- B Envelope: Attack 0-5, Decay 35-50, End 0, Level 60-80
- Amp Envelope: Attack 0, Hold 0, Decay 85-100, Sustain 0, Release 60-80
- Filter: Fully open (127), Low resonance (0-10)
- Effects: Reverb 35-45, Chorus 20-30

**FM Bass**:
- Algorithm: 4, 5, or 8 (3, 4, or 7)
- C Ratio: 1-2 (fundamental)
- A Ratio: 2-5 (controlled harmonics)
- Feedback: 30-60 (grit)
- Harmonics: 50-70
- Filter: Low frequency (30-60), Moderate resonance (30-50)
- Amp: Attack 0-10, Decay 50-70, Sustain 70-100, Release 30-50

**Bell/Metallic Lead**:
- Algorithm: 3 or 6 (2 or 5)
- Use inharmonic ratios (e.g., A=14, B=9)
- Harmonics: 70-100 (bright)
- Feedback: 40-80 (metallic edge)
- Filter: High frequency (80-127)
- Fast operator envelopes

**Pad/Evolving Texture**:
- Algorithm: 5 or 6 (4 or 5) - Multiple carriers
- Slow operator envelopes (different timings)
- Moderate feedback (25-45)
- Detune: 15-25 (width)
- Amp: Slow attack (60-100), High sustain (100-127)
- LFO modulation to ratios or harmonics

**Pluck/Percussive**:
- Fast operator decay (20-50)
- High modulation index (high modulator levels)
- Amp: Attack 0, Sustain 0-15, Fast decay
- Filter envelope for brightness sweep

**Critical FM Relationships:**

**Modulation Index** = Modulator Level × Modulator Envelope
- Low index (modulator level 30-60): Subtle harmonics
- High index (modulator level 80-127): Rich, complex harmonics

**Operator Envelope Timing**:
- Modulators decay faster than carriers → brightness fades
- Modulators decay slower → evolving timbre
- Match timings for static timbre

**Algorithm Selection Guide:**
- Simple sounds: Algorithm 7 or 8 (fewer modulators)
- Complex/evolving: Algorithm 1, 4, 5 (stacked/branched)
- Dual timbres: Algorithm 2, 6 (two carriers)

**Parameter Order for Complete FM Sounds:**
1. Algorithm selection
2. Operator ratios (C, A, B)
3. Operator envelopes (Attack, Decay, End, Level for A and B)
4. Harmonics
5. Feedback
6. Detune
7. Mix (X/Y balance)
8. Amplitude envelope (ADSR)
9. Filter settings
10. Effects (reverb, chorus, delay)
11. LFO modulation (optional)

**Common Mistakes to Avoid:**
- ❌ Not considering operator routing in algorithm
- ❌ Using only integer ratios (limiting timbral possibilities)
- ❌ Forgetting to set operator envelopes (flat, boring sound)
- ❌ Setting all operator levels to maximum (too harsh)
- ❌ Not using detune for analog warmth
- ❌ Skipping the Mix parameter (missing half the sound)

**Advanced Techniques:**
- Use ratio offsets for fine-tuning inharmonic sounds
- Key tracking on operators for consistent timbre across range
- Delayed operator triggers for evolving attacks
- Feedback + high harmonics = noisy/aggressive textures
- Mix parameter automates between two different timbres (X vs Y outputs)
""",
    )

    @agent.output_validator  # type: ignore[misc]
    def validate_fm_tone_response(
        ctx, result: list[SynthGenieResponse | SynthGenieAmbiguousResponse]
    ) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
        return validate_synth_response(ctx, result)

    return agent
