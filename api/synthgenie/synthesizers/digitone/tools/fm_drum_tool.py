import logging

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse

logger = logging.getLogger(__name__)


# Page 1: FM Drum Core Parameters
def set_fm_drum_tune(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the pitch tuning of the FM drum oscillator.

    This parameter controls the fundamental pitch of the drum sound.
    Uses NRPN (1:73) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI pitch value ranging from 0 to 16383.
            This parameter uses NRPN (1:73) for full 14-bit resolution.
            Maps to display values from -60 to +60 semitones.
            Formula: display = ((value / 16383) * 120.0) - 60.0
            - 0 = -60 semitones
            - 8191 = 0 semitones (approximately)
            - 16383 = +60 semitones
            Display range: -60 to +60 semitones with fine precision.
            Default is 0 (MIDI ~8191).
        midi_channel (int): The MIDI channel (track) to set the tuning for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_tune',
        nrpn_msb=1,
        nrpn_lsb=73,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_sweep_time(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the pitch sweep time for the FM drum.

    Controls how quickly the pitch sweep occurs. Lower values result in shorter,
    snappier sweeps ideal for kick drums, while higher values create longer pitch bends.
    Uses NRPN (1:74) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI sweep time value ranging from 0 to 16383.
            This parameter uses NRPN (1:74) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = 0 (shortest sweep time)
            - 8191 = ~63 (approximately)
            - 16383 = 127 (longest sweep time)
            Display range: 0 to 127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the sweep time for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_sweep_time',
        nrpn_msb=1,
        nrpn_lsb=74,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_sweep_depth(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the depth of the pitch sweep for the FM drum.

    Determines how much the pitch changes during the sweep. Essential for creating
    punch and impact in drum sounds, especially kicks and toms.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Sweep depth value ranging from 0 to 127.
            0 = no pitch sweep
            127 = maximum pitch sweep
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the sweep depth for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_sweep_depth',
        midi_cc=42,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_algorithm(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the FM algorithm that determines how the three operators are routed in the FM drum engine.

    The FM drum uses a simplified 3-operator FM architecture optimized for percussive sounds.
    Different algorithms create different timbral characteristics suitable for various drum types.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Algorithm number ranging from 0 to 6 (displayed as 1-7).
            - 0 = Algorithm 1: Simple stack (B->A->C). Good for punchy kicks.
            - 1 = Algorithm 2: Parallel modulation (B->C, A->C). Versatile, good for snares.
            - 2 = Algorithm 3: Y-configuration. Complex modulation for metallic sounds.
            - 3 = Algorithm 4: Triangle configuration. Rich harmonics for toms.
            - 4 = Algorithm 5: Mixed routing. Balanced for general percussion.
            - 5 = Algorithm 6: Complex branching. Good for hi-hats and cymbals.
            - 6 = Algorithm 7: Maximum complexity. Experimental/noise percussion.
            Display range: 1-7.
            Default is 1.
        midi_channel (int): The MIDI channel (track) to set the algorithm for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_algorithm',
        midi_cc=43,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_op_c_wave(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the waveform for operator C in the FM drum engine.

    Operator C typically acts as the carrier, defining the fundamental character of the drum sound.
    This parameter uses NRPN (1:77) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI waveform value ranging from 0 to 16383.
            This parameter uses NRPN (1:77) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = waveform 0
            - 8191 = ~63 (approximately)
            - 16383 = waveform 127
            Different ranges select different waveforms optimized for drum synthesis.
            Common selections include sine, triangle, square, and various harmonic combinations.
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the operator C waveform for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_op_c_wave',
        nrpn_msb=1,
        nrpn_lsb=77,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_op_ab_wave(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the waveform for operators A and B in the FM drum engine.

    Operators A and B typically act as modulators, shaping the harmonic content and texture
    of the drum sound. This parameter controls both operators simultaneously.
    This parameter uses NRPN (1:78) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI waveform value ranging from 0 to 16383.
            This parameter uses NRPN (1:78) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = waveform 0
            - 8191 = ~63 (approximately)
            - 16383 = waveform 127
            Different ranges select different waveforms optimized for modulation.
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the operator A/B waveform for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_op_ab_wave',
        nrpn_msb=1,
        nrpn_lsb=78,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_feedback(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the feedback amount for the FM drum synthesis.

    Feedback routes an operator's output back to its own input, creating more complex
    and often noisier/grittier timbres. Essential for snare buzz, cymbal sizzle, and distorted kicks.
    The operator with feedback is shown with a feedback loop in the algorithm display.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Feedback amount ranging from 0 to 127.
            0 = no feedback (clean)
            127 = maximum feedback (noisy/distorted)
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the feedback for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_feedback',
        midi_cc=46,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_fold(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the wavefolding amount for the body part of the FM drum sound.

    Wavefolding increases the complexity of the wave and creates a more overtone-rich sound.
    This affects only the body (FM) part of the sound, not the noise or transient components.
    Great for adding harmonic richness and aggression to drums.
    This parameter uses NRPN (1:80) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI wavefolding value ranging from 0 to 16383.
            This parameter uses NRPN (1:80) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = no wavefolding (clean)
            - 8191 = ~63 (approximately)
            - 16383 = maximum wavefolding (complex harmonics)
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the wavefolding for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_fold',
        nrpn_msb=1,
        nrpn_lsb=80,
        midi_channel=midi_channel,
        value=value,
    )


# Page 2: Operator Parameters
def set_fm_drum_ratio1(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the frequency ratio for operator A.

    Controls the frequency relationship between operator A and the fundamental pitch.
    In drum synthesis, non-integer ratios create inharmonic content essential for
    metallic and noise-like drum sounds.
    This parameter uses NRPN (1:81) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI ratio value ranging from 0 to 16383.
            This parameter uses NRPN (1:81) for full 14-bit resolution.
            Maps to display values from 0.001 to 31.75.
            Formula: display = ((value / 16383) * 31.749) + 0.001
            - 0 = 0.001 (lowest ratio)
            - 8191 = ~15.875 (approximately)
            - 16383 = 31.75 (highest ratio)
            Low values create sub-harmonics, high values create bright overtones.
            Display range: 0.001-31.75 with fine precision.
            Default is 0.500 (MIDI ~257).
        midi_channel (int): The MIDI channel (track) to set the ratio for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_ratio1',
        nrpn_msb=1,
        nrpn_lsb=81,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_decay1(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time for operator A's envelope.

    Controls how quickly operator A's modulation fades out. Shorter decays create
    snappy, percussive modulation, while longer decays sustain the harmonic content.
    This parameter uses NRPN (1:82) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI decay time value ranging from 0 to 16383.
            This parameter uses NRPN (1:82) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = instant decay
            - 8191 = ~63 (approximately)
            - 16383 = longest decay (127)
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the decay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_decay1',
        nrpn_msb=1,
        nrpn_lsb=82,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_end1(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the end level for operator A's envelope.

    Determines the level that operator A sustains at after the decay phase.
    This allows for sustained harmonic content in the drum sound.
    This parameter uses NRPN (1:83) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI end level value ranging from 0 to 16383.
            This parameter uses NRPN (1:83) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = silent at end
            - 8191 = ~63 (approximately)
            - 16383 = full level at end (127)
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the end level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_end1',
        nrpn_msb=1,
        nrpn_lsb=83,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_mod1(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the modulation amount from operator A.

    Controls how much operator A modulates its target (determined by the algorithm).
    Higher values create more complex harmonic content and timbral change.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Modulation amount ranging from 0 to 127.
            0 = no modulation
            127 = maximum modulation
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the modulation amount for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_mod1',
        midi_cc=51,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_ratio2(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the frequency ratio for operator B.

    Controls the frequency relationship between operator B and the fundamental pitch.
    Works in conjunction with operator A to create complex modulation patterns.
    This parameter uses NRPN (1:85) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI ratio value ranging from 0 to 16383.
            This parameter uses NRPN (1:85) for full 14-bit resolution.
            Maps to display values from 0.001 to 31.75.
            Formula: display = ((value / 16383) * 31.749) + 0.001
            - 0 = 0.001 (lowest ratio)
            - 8191 = ~15.875 (approximately)
            - 16383 = 31.75 (highest ratio)
            Display range: 0.001-31.75 with fine precision.
            Default is 0.500 (MIDI ~257).
        midi_channel (int): The MIDI channel (track) to set the ratio for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_ratio2',
        nrpn_msb=1,
        nrpn_lsb=85,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_decay2(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time for operator B's envelope.

    Controls how quickly operator B's modulation fades out. Can be set differently
    from operator A to create evolving timbral changes.
    This parameter uses NRPN (1:86) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI decay time value ranging from 0 to 16383.
            This parameter uses NRPN (1:86) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = instant decay
            - 8191 = ~63 (approximately)
            - 16383 = longest decay (127)
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the decay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_decay2',
        nrpn_msb=1,
        nrpn_lsb=86,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_end2(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the end level for operator B's envelope.

    Determines the level that operator B sustains at after the decay phase.
    This parameter uses NRPN (1:87) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI end level value ranging from 0 to 16383.
            This parameter uses NRPN (1:87) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = silent at end
            - 8191 = ~63 (approximately)
            - 16383 = full level at end (127)
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the end level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_end2',
        nrpn_msb=1,
        nrpn_lsb=87,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_mod2(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the modulation amount from operator B.

    Controls how much operator B modulates its target (determined by the algorithm).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Modulation amount ranging from 0 to 127.
            0 = no modulation
            127 = maximum modulation
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the modulation amount for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_mod2',
        midi_cc=55,
        midi_channel=midi_channel,
        value=value,
    )


# Page 3: Body and Noise Control Parameters
def set_fm_drum_body_hold(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the hold time before the decay phase starts for the body part of the drum sound.

    Creates a sustained initial impact before the drum begins to decay. Useful for
    creating punchy attacks and controlling the drum's envelope shape.
    This parameter uses NRPN (1:89) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI hold time value ranging from 0 to 16383.
            This parameter uses NRPN (1:89) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = no hold (immediate decay)
            - 8191 = ~63 (approximately)
            - 16383 = longest hold (127)
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the body hold for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_body_hold',
        nrpn_msb=1,
        nrpn_lsb=89,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_body_decay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time for the body part of the drum sound.

    Controls how long the main FM-generated portion of the drum takes to fade out.
    The last value (127/16383) is infinite decay, creating a sustained drone.
    This parameter uses NRPN (1:90) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI decay time value ranging from 0 to 16383.
            This parameter uses NRPN (1:90) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = instant decay
            - 8191 = ~63 (approximately)
            - 16382 = very long decay (~126)
            - 16383 = infinite (no decay, ∞)
            Display range: 0-127 with fine precision (last value is ∞).
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the body decay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_body_decay',
        nrpn_msb=1,
        nrpn_lsb=90,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_op_c_phase(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the phase reset behavior for operator C.

    Controls whether and where operator C's waveform phase resets on each note trigger.
    Phase reset ensures consistent attack transients, while no reset creates variation.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Phase reset value ranging from 0 to 91.
            0-89 = phase reset ON, value represents start position in degrees
            90 = reset at waveform peak
            91 = phase reset OFF (free-running)
            Display range: 0-91 (91 = OFF).
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the phase reset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_op_c_phase',
        midi_cc=58,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_body_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the level of the body part of the drum sound.

    Controls the volume of the FM-generated portion relative to the noise and transient parts.
    Balancing body, noise, and transient levels is key to crafting realistic drum sounds.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            0 = silent
            127 = maximum level
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the body level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_body_level',
        midi_cc=59,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_noise_reset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set whether the noise generator resets to the same random seed on each note trigger.

    When ON, the noise component will sound identical each time, like a sampled noise.
    When OFF, the noise varies with each trigger for more natural variation.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Reset mode value (0 or 1).
            0 = OFF (varying noise)
            1 = ON (consistent noise)
            Display range: OFF/ON.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the noise reset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_noise_reset',
        midi_cc=62,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_noise_ring_mod(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set whether operator C is used as a ring modulator for the noise.

    When ON, operator C modulates the noise signal, creating metallic and bell-like
    textures. Essential for cymbals, hi-hats, and metallic percussion.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ring mod mode value (0 or 1).
            0 = OFF (pure noise)
            1 = ON (ring modulated noise)
            Display range: OFF/ON.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the noise ring mod for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_noise_ring_mod',
        midi_cc=63,
        midi_channel=midi_channel,
        value=value,
    )


# Page 4: Noise and Transient Parameters
def set_fm_drum_noise_hold(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the hold time before the decay phase starts for the noise part of the sound.

    Controls how long the noise component sustains at full level before decaying.
    Important for shaping the character of snares, hi-hats, and other noisy drums.
    This parameter uses NRPN (1:97) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI hold time value ranging from 0 to 16383.
            This parameter uses NRPN (1:97) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = no hold (immediate decay)
            - 8191 = ~63 (approximately)
            - 16383 = longest hold (127)
            Display range: 0-127 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the noise hold for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_noise_hold',
        nrpn_msb=1,
        nrpn_lsb=97,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_noise_decay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time for the noise part of the sound.

    Controls how long the noise component takes to fade out. The last value (127/16383)
    is infinite decay, creating a sustained noise layer.
    This parameter uses NRPN (1:98) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI decay time value ranging from 0 to 16383.
            This parameter uses NRPN (1:98) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = instant decay
            - 8191 = ~63 (approximately)
            - 16382 = very long decay (~126)
            - 16383 = infinite (no decay, ∞)
            Display range: 0-127 with fine precision (last value is ∞).
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the noise decay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_noise_decay',
        nrpn_msb=1,
        nrpn_lsb=98,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_transient(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Select the drum transient type.

    Transients are short attack samples that add punch and realism to drum sounds.
    Different transient types are optimized for different drum types (kick, snare, etc.).
    This parameter uses NRPN (1:99) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI transient selection value ranging from 0 to 16383.
            This parameter uses NRPN (1:99) for full 14-bit resolution.
            Maps to display values from 0 to 124.
            Formula: display = (value / 16383) * 124.0
            - 0 = transient 0 (typically kick-oriented)
            - 8191 = ~62 (approximately)
            - 16383 = transient 124 (typically snare/hat-like)
            Different values select different pre-recorded transient samples.
            Display range: 0-124 with fine precision.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the transient for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_transient',
        nrpn_msb=1,
        nrpn_lsb=99,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_transient_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the level of the transient part of the sound.

    Controls the volume of the initial attack transient relative to the body and noise.
    Higher levels create more punchy, aggressive drum sounds.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            0 = no transient
            127 = maximum transient level
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the transient level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_transient_level',
        midi_cc=73,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_noise_base(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the base frequency for the noise/transient filter.

    Determines the lower frequency boundary of the noise component. Higher values
    create brighter, more high-frequency noise content.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Base frequency value ranging from 0 to 127.
            0 = lowest frequency
            127 = highest frequency
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the noise base frequency for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_noise_base',
        midi_cc=74,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_noise_width(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the frequency width above the base frequency for the noise/transient filter.

    Controls the bandwidth of the noise component. Narrow widths create more focused,
    tonal noise, while wide settings create full-spectrum noise.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Width value ranging from 0 to 127.
            0 = narrow bandwidth (focused)
            127 = wide bandwidth (full spectrum)
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the noise width for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_noise_width',
        midi_cc=75,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_noise_grain(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Adjust the density of the grains for the noise part of the sound.

    Controls the texture of the noise from smooth white noise (high density) to
    granular, crackling textures (low density). Great for creating vintage drum machine
    sounds or lo-fi textures.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Grain density value ranging from 0 to 127.
            0 = sparse grains (crackling)
            127 = dense grains (smooth white noise)
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the noise grain for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_noise_grain',
        midi_cc=76,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_drum_noise_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the level of the noise part of the sound.

    Controls the volume of the noise component relative to the body and transient.
    Essential for balancing the tonal and noise elements in drum sounds.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            0 = no noise
            127 = maximum noise level
            Display range: 0-127.
            Default varies by preset.
        midi_channel (int): The MIDI channel (track) to set the noise level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_drum_noise_level',
        midi_cc=77,
        midi_channel=midi_channel,
        value=value,
    )
