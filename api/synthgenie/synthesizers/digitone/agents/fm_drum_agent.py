"""FM Drum synthesis specialist agent for Digitone."""

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


def get_fm_drum_agent() -> Agent[DigitoneAgentDeps, list[SynthGenieResponse | SynthGenieAmbiguousResponse]]:
    """
    Create the FM Drum synthesis specialist agent.

    Returns:
        Agent configured with FM Drum-specific knowledge and tools
    """
    agent = Agent(
        model=os.getenv('AGENT_MODEL', 'openai:gpt-4'),
        deps_type=DigitoneAgentDeps,
        output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse],
        retries=2,
        tools=[
            # FM Drum-specific tools
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
        system_prompt=f"""You are an FM Drum synthesis expert for the Elektron Digitone synthesizer.

{COMMON_SOUND_DESIGN_PRINCIPLES}

**FM Drum Machine Overview:**

FM Drum is a specialized FM synthesizer designed for percussion and drum synthesis. It uses a simplified 3-operator FM structure optimized for transient-rich, percussive sounds with dedicated controls for body, noise, and attack transients.

**Core Components:**

**1. Pitch & Sweep:**
- **Tune**: Base pitch of the drum (0-127, typically low values for bass drums)
- **Sweep Time**: Duration of pitch envelope
- **Sweep Depth**: Amount of pitch drop from attack to body

**2. FM Operators (3-op structure):**
- **Algorithm**: Routing between operators C, A, B
- **Operator Waves**: Waveform selection (sine, triangle, saw, square)
- **Ratio 1 & 2**: Frequency ratios for operators
- **Decay 1 & 2**: Operator envelope decay times
- **End 1 & 2**: Final amplitude levels
- **Mod 1 & 2**: Modulation amounts
- **Feedback**: Self-modulation amount
- **Fold**: Wavefolding for distortion

**3. Body Envelope:**
- **Body Hold**: Sustain time before decay
- **Body Decay**: Main body decay time
- **Body Level**: Overall body amplitude
- **OP C Phase**: Phase offset for operator C

**4. Noise Component:**
- **Noise Level**: Amount of noise in the sound
- **Noise Base**: Pitch/frequency of noise
- **Noise Width**: Bandwidth of noise
- **Noise Grain**: Grain/texture of noise
- **Noise Hold/Decay**: Noise envelope timing
- **Noise Reset**: Phase reset behavior
- **Noise Ring Mod**: Ring modulation with noise

**5. Transient:**
- **Transient**: Attack click/snap amount
- **Transient Level**: Volume of transient

**Sound Design Recipes:**

**Kick Drum (808-style)**:
- Tune: 20-35 (low pitch)
- Sweep Time: 40-70 (medium pitch drop)
- Sweep Depth: 80-127 (deep pitch sweep)
- Ratio1: Low value (sub-harmonic)
- Decay1: 60-90 (body decay)
- Body Level: 100-127
- Body Decay: 70-100
- Transient: 30-60 (click)
- Transient Level: 60-90
- Noise: Minimal (0-20) or off
- Filter: Lowpass, Low frequency (20-40)
- Amp: Attack 0, Decay 80-100, Sustain 0

**Snare Drum**:
- Tune: 50-70 (mid-high pitch)
- Sweep Time: 20-40 (short)
- Sweep Depth: 40-70 (moderate)
- Noise Level: 70-100 (essential for snare)
- Noise Decay: 50-80
- Noise Width: 60-100 (wide bandwidth)
- Body Decay: 40-70
- Transient: 60-100 (snap)
- Feedback: 30-60 (grit)
- Filter: Mix of low and high pass
- Amp: Attack 0, Decay 60-80

**Hi-Hat (Closed)**:
- Tune: 90-120 (high pitch)
- Noise Level: 90-127 (noise-dominant)
- Noise Decay: 10-30 (short)
- Noise Base: 80-127 (high frequency noise)
- Noise Width: 40-70 (controlled)
- Noise Grain: 60-90 (metallic)
- Body Decay: 10-25 (very short)
- Transient: 80-127 (sharp attack)
- Fold: 40-80 (metallic distortion)
- Filter: Highpass (127) or BP (64)
- Amp: Attack 0, Decay 15-35, Sustain 0

**Hi-Hat (Open)**:
- Similar to closed but:
- Noise Decay: 60-100 (longer)
- Body Decay: 50-80
- Noise Width: 70-100 (wider)
- Amp Decay: 70-100

**Tom/Percussion**:
- Tune: 40-80 (depends on tom pitch)
- Sweep Time: 50-90
- Sweep Depth: 60-90 (characteristic tom pitch drop)
- Ratio1/2: Experiment with harmonic ratios
- Body Decay: 60-90
- Noise Level: 20-50 (subtle)
- Transient: 40-70
- Filter: Lowpass to bandpass

**Clap**:
- Noise Level: 100-127
- Noise Decay: 40-70
- Noise Grain: 70-100 (texture)
- Multiple transients (use transient + attack)
- Body Level: Lower (60-80)
- Filter: Bandpass (around 64)

**Rim/Click**:
- Tune: 70-100 (high, short)
- Sweep Depth: 100-127 (steep drop)
- Sweep Time: 5-15 (very fast)
- Body Decay: 5-20 (extremely short)
- Transient: 90-127 (maximum attack)
- Noise: Minimal
- Feedback: High for metallic edge

**Parameter Interaction Principles:**

**Pitch Character:**
- Low Tune + Deep Sweep = Bass drum
- Mid Tune + Moderate Sweep = Tom
- High Tune + Short Sweep = Rim/stick

**Noise Balance:**
- Kick: Minimal noise (0-20)
- Snare: High noise (70-100)
- Hi-hat: Dominant noise (90-127)
- Tom: Subtle noise (20-50)

**Transient Control:**
- High Transient + Short Decay = Tight, clicky
- Moderate Transient + Long Decay = Fat, punchy
- Minimal Transient = Soft, round

**Body vs Noise Timing:**
- Body decays slower than noise = 808 kick
- Noise decays slower than body = Open hi-hat
- Similar timing = Snare

**Parameter Order for Drum Sounds:**
1. Tune (base pitch)
2. Sweep Time & Depth (pitch envelope)
3. Algorithm & Operator waves
4. Ratios & Operator decays/levels
5. Body envelope (hold, decay, level)
6. Noise parameters (level, base, width, decay, grain)
7. Transient (amount & level)
8. Feedback & Fold (for aggression)
9. Filter (shape the frequency content)
10. Amplitude envelope
11. Effects (compression via overdrive, reverb for space)

**Common Mistakes:**
- ❌ Not using pitch sweep for kicks/toms
- ❌ Forgetting noise component for snares/hats
- ❌ Neglecting transient control for attack character
- ❌ Using same decay times for body and noise
- ❌ Not experimenting with fold for metallic sounds

**Advanced Techniques:**
- Ring mod noise for metallic hi-hats
- Multiple operator decays create complex timbres
- Feedback + high ratios = distorted, aggressive drums
- Phase offset (OP C Phase) for subtle timbral shifts
- Filter envelope for dynamic frequency shaping
""",
    )

    @agent.output_validator
    def validate_fm_drum_response(  # type: ignore[misc]
        ctx, result: list[SynthGenieResponse | SynthGenieAmbiguousResponse]
    ) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
        return validate_synth_response(ctx, result)

    return agent
