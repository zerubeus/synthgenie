import logging

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse

logger = logging.getLogger(__name__)


# Page 1: FM Algorithm and Operator Parameters
def set_fm_tone_algorithm(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the FM algorithm that determines how the four operators (C, A, B1, B2) are routed and interact.
    
    The algorithm defines the modulation routing between operators, controlling the FM synthesis structure.
    Each algorithm has two carrier outputs (X and Y) that can be mixed using the MIX parameter.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Algorithm number ranging from 0 to 7 (displayed as 1-8).
            - 0 = Algorithm 1: Classic 4-op stack (B2->B1->A->C). Most complex modulation.
                  Output X: C (carrier), Output Y: A (carrier)
            - 1 = Algorithm 2: Dual 2-op stacks (B2->B1, A->C). Two independent FM pairs.
                  Output X: C (carrier), Output Y: B1 (carrier)
            - 2 = Algorithm 3: Three modulators to one carrier (B2, B1, A all modulate C).
                  Output X: C (carrier), Output Y: A (carrier)
            - 3 = Algorithm 4: Y-shaped routing (B2->B1->C, A->C). Branched modulation.
                  Output X: C (carrier), Output Y: A (carrier)
            - 4 = Algorithm 5: Diamond configuration with complex cross-modulation.
                  Output X: C (carrier), Output Y: B1 (carrier)
            - 5 = Algorithm 6: Two carriers with shared modulators.
                  Output X: C (carrier), Output Y: A (carrier)
            - 6 = Algorithm 7: Parallel configuration with B2 modulating both B1 and A.
                  Output X: C (carrier), Output Y: A (carrier)
            - 7 = Algorithm 8: Four parallel carriers (additive synthesis, no FM).
                  Output X: C+A (mixed carriers), Output Y: B1+B2 (mixed carriers)
            Display range: 1-8.
            Default is 1.
        midi_channel (int): The MIDI channel (track) to set the algorithm for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_algorithm',
        midi_cc=40,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_c_ratio(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the frequency ratio for operator C (carrier).
    
    This controls the frequency relationship between operator C and the played note.
    Operator C is limited mostly to integers since it is generally used for carrying the
    base note of the sound.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ratio value ranging from 0 to 18.
            - 0 = 0.25
            - 1 = 0.5
            - 2 = 1
            - 3 = 2
            - 4 = 3
            - 5 = 4
            - 6 = 5
            - 7 = 6
            - 8 = 7
            - 9 = 8
            - 10 = 9
            - 11 = 10
            - 12 = 11
            - 13 = 12
            - 14 = 13
            - 15 = 14
            - 16 = 15
            - 17 = 16
            - 18 = 16 (maximum)
            Display range: 0.25-16.
            Default is 1.00 (value = 2).
        midi_channel (int): The MIDI channel (track) to set the C ratio for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_c_ratio',
        midi_cc=41,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_a_ratio(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the frequency ratio for operator A.
    
    This controls the frequency relationship between operator A and the played note.
    Operator A can act as either a carrier or modulator depending on the selected algorithm.
    A has a more extensive number of ratio values to allow for more inharmonic relationships.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ratio value ranging from 0 to 35.
            - 0 = 0.25
            - 1 = 0.5
            - 2 = 0.75
            - 3 = 1
            - 4 = 1.25
            - 5 = 1.5
            - 6 = 1.75
            - 7 = 2
            - 8 = 2.5
            - 9 = 3
            - 10 = 3.5
            - 11 = 4
            - 12 = 4.5
            - 13 = 5
            - 14 = 5.5
            - 15 = 6
            - 16 = 6.5
            - 17 = 7
            - 18 = 7.5
            - 19 = 8
            - 20 = 8.5
            - 21 = 9
            - 22 = 9.5
            - 23 = 10
            - 24 = 10.5
            - 25 = 11
            - 26 = 11.5
            - 27 = 12
            - 28 = 12.5
            - 29 = 13
            - 30 = 13.5
            - 31 = 14
            - 32 = 14.5
            - 33 = 15
            - 34 = 15.5
            - 35 = 16
            Display range: 0.25-16.
            Default is 1.00 (value = 3).
        midi_channel (int): The MIDI channel (track) to set the A ratio for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_ratio',
        midi_cc=42,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b_ratio(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the frequency ratio for operators B1 and B2.
    
    This parameter controls both B1 and B2 operators' frequency ratios simultaneously.
    B operators typically act as modulators in most algorithms.
    
    The B ratio control works like watch hands: as you turn the encoder, B2 increases 
    until it reaches the max (16), then it starts over from 0.25 and B1 increases to 
    the next value. This revolving behavior continues until both operators reach maximum.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ratio value ranging from 0 to 3.
            Due to the limited MIDI range, this parameter uses coarse stepping.
            The actual B1/B2 combinations are much more extensive on the device.
            - 0 = B1: 0.25, B2: 0.25 (minimum)
            - 1 = B1: ~5.33, B2: ~5.33 (intermediate)
            - 2 = B1: ~10.67, B2: ~10.67 (intermediate)  
            - 3 = B1: 16, B2: 16 (maximum)
            Note: On the actual device, B2 cycles through all values (0.25-16) 
            before B1 increments, creating many more combinations.
            Display range: [0.25-16, 0.25-16].
            Default is [1.00, 1.00].
        midi_channel (int): The MIDI channel (track) to set the B ratio for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b_ratio',
        midi_cc=43,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_harmonics(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the harmonics parameter that adds additional harmonic content to the FM synthesis.
    
    This parameter enhances the harmonic complexity of the sound by introducing
    additional frequency components.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Harmonics value ranging from 37 to 90.
            Maps to display values from -26 to +26.
            - 37 = -26
            - 64 = 0
            - 90 = +26
            Display range: -26 to +26.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the harmonics for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_harmonics',
        midi_cc=44,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_detune(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the detune amount for the FM operators.
    
    This creates slight pitch variations between operators, adding richness and
    movement to the sound.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Detune value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the detune for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_detune',
        midi_cc=45,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_feedback(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the feedback amount for the FM synthesis.
    
    Feedback routes an operator's output back to its own input, creating more
    complex and often noisier timbres. Higher values produce more aggressive sounds.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Feedback value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the feedback for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_feedback',
        midi_cc=46,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_mix(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the mix balance between operators in the FM synthesis.
    
    This controls the relative levels of different operators in the final output,
    affecting the timbral balance of the sound.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Mix value ranging from 0 to 127.
            Maps to display values from -63 to +63.
            - 0 = -63
            - 64 = 0
            - 127 = +63
            Display range: -63 to +63.
            Default is -63.
        midi_channel (int): The MIDI channel (track) to set the mix for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_mix',
        midi_cc=47,
        midi_channel=midi_channel,
        value=value,
    )


# Page 2: Envelope Parameters for Operators A and B
def set_fm_tone_a_attack(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the attack time for operator A's envelope.
    
    Controls how quickly operator A reaches its maximum level after a note is triggered.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Attack time value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the attack for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_attack',
        midi_cc=48,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_a_decay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time for operator A's envelope.
    
    Controls how quickly operator A falls from its maximum level to the end level.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Decay time value ranging from 0 to 127.
            Display range: 0-127.
            Default is 32.
        midi_channel (int): The MIDI channel (track) to set the decay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_decay',
        midi_cc=49,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_a_end(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the end level for operator A's envelope.
    
    Determines the level that operator A sustains at after the decay phase.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): End level value ranging from 0 to 127.
            Display range: 0-127.
            Default is 127.
        midi_channel (int): The MIDI channel (track) to set the end level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_end',
        midi_cc=50,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_a_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the overall level for operator A.
    
    Controls the output amplitude of operator A, affecting its contribution to the
    overall sound whether as carrier or modulator.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_level',
        midi_cc=51,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b_attack(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the attack time for operator B's envelope.
    
    Controls how quickly operator B (both B1 and B2) reaches maximum level after a note is triggered.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Attack time value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the attack for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b_attack',
        midi_cc=52,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b_decay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time for operator B's envelope.
    
    Controls how quickly operator B (both B1 and B2) falls from maximum level to the end level.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Decay time value ranging from 0 to 127.
            Display range: 0-127.
            Default is 32.
        midi_channel (int): The MIDI channel (track) to set the decay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b_decay',
        midi_cc=53,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b_end(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the end level for operator B's envelope.
    
    Determines the level that operator B (both B1 and B2) sustains at after the decay phase.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): End level value ranging from 0 to 127.
            Display range: 0-127.
            Default is 127.
        midi_channel (int): The MIDI channel (track) to set the end level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b_end',
        midi_cc=54,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the overall level for operator B.
    
    Controls the output amplitude of operator B (both B1 and B2), affecting their
    modulation depth when acting as modulators.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b_level',
        midi_cc=55,
        midi_channel=midi_channel,
        value=value,
    )


# Page 3: Envelope Control Parameters
def set_fm_tone_a_delay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the delay time before operator A's envelope starts.
    
    Introduces a time delay between note trigger and when operator A's envelope begins.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Delay time value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the delay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_delay',
        midi_cc=56,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_a_trigger(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the trigger mode for operator A's envelope.
    
    Determines whether operator A's envelope is triggered by note events.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Trigger mode value (0 or 1).
            - 0 = Off
            - 1 = On
            Display range: Off/On.
            Default is 1 (On).
        midi_channel (int): The MIDI channel (track) to set the trigger mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_trigger',
        midi_cc=57,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_a_reset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the reset mode for operator A's envelope.
    
    Determines whether operator A's envelope resets to the beginning when retriggered.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Reset mode value (0 or 1).
            - 0 = Off
            - 1 = On
            Display range: Off/On.
            Default is 1 (On).
        midi_channel (int): The MIDI channel (track) to set the reset mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_reset',
        midi_cc=58,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_phase_reset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the phase reset mode for the FM operators.
    
    Controls which operators have their phase reset when a note is triggered.
    This affects the consistency of the attack transient.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Phase reset mode ranging from 0 to 4.
            - 0 = off (no phase reset)
            - 1 = all (all operators reset)
            - 2 = c (only operator C resets)
            - 3 = a+b (operators A and B reset)
            - 4 = a+b2 (operators A and B2 reset)
            Display range: discrete options.
            Default is 'all'.
        midi_channel (int): The MIDI channel (track) to set the phase reset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_phase_reset',
        midi_cc=59,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b_delay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the delay time before operator B's envelope starts.
    
    Introduces a time delay between note trigger and when operator B's envelope begins.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Delay time value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the delay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b_delay',
        midi_cc=60,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b_trigger(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the trigger mode for operator B's envelope.
    
    Determines whether operator B's envelope is triggered by note events.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Trigger mode value (0 or 1).
            - 0 = Off
            - 1 = On
            Display range: Off/On.
            Default is 1 (On).
        midi_channel (int): The MIDI channel (track) to set the trigger mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b_trigger',
        midi_cc=61,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b_reset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the reset mode for operator B's envelope.
    
    Determines whether operator B's envelope resets to the beginning when retriggered.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Reset mode value (0 or 1).
            - 0 = Off
            - 1 = On
            Display range: Off/On.
            Default is 1 (On).
        midi_channel (int): The MIDI channel (track) to set the reset mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b_reset',
        midi_cc=62,
        midi_channel=midi_channel,
        value=value,
    )


# Page 4: Ratio Offset and Key Tracking Parameters
def set_fm_tone_c_ratio_offset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the ratio offset for operator C.
    
    Fine-tunes the frequency ratio of operator C, allowing for subtle detuning
    and inharmonic effects.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ratio offset value ranging from 0 to 127.
            Maps to offset values from -1.00 to +0.999.
            - 0 = -1.00
            - 64 = 0.00
            - 127 = +0.999
            Display range: -1.00 to +0.999.
            Default is 0.00.
        midi_channel (int): The MIDI channel (track) to set the ratio offset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_c_ratio_offset',
        midi_cc=70,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_a_ratio_offset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the ratio offset for operator A.
    
    Fine-tunes the frequency ratio of operator A, allowing for subtle detuning
    and inharmonic effects.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ratio offset value ranging from 0 to 127.
            Maps to offset values from -1.00 to +0.999.
            - 0 = -1.00
            - 64 = 0.00
            - 127 = +0.999
            Display range: -1.00 to +0.999.
            Default is 0.00.
        midi_channel (int): The MIDI channel (track) to set the ratio offset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_ratio_offset',
        midi_cc=71,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b1_ratio_offset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the ratio offset for operator B1.
    
    Fine-tunes the frequency ratio of operator B1, allowing for subtle detuning
    and inharmonic effects.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ratio offset value ranging from 0 to 127.
            Maps to offset values from -1.00 to +0.999.
            - 0 = -1.00
            - 64 = 0.00
            - 127 = +0.999
            Display range: -1.00 to +0.999.
            Default is 0.00.
        midi_channel (int): The MIDI channel (track) to set the ratio offset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b1_ratio_offset',
        midi_cc=72,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b2_ratio_offset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the ratio offset for operator B2.
    
    Fine-tunes the frequency ratio of operator B2, allowing for subtle detuning
    and inharmonic effects.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ratio offset value ranging from 0 to 127.
            Maps to offset values from -1.00 to +0.999.
            - 0 = -1.00
            - 64 = 0.00
            - 127 = +0.999
            Display range: -1.00 to +0.999.
            Default is 0.00.
        midi_channel (int): The MIDI channel (track) to set the ratio offset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b2_ratio_offset',
        midi_cc=73,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_a_key_track(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the key tracking amount for operator A.
    
    Controls how much operator A's envelope speed changes with the played note pitch.
    Higher values make envelopes faster for higher notes.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Key tracking value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the key tracking for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_a_key_track',
        midi_cc=75,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b1_key_track(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the key tracking amount for operator B1.
    
    Controls how much operator B1's envelope speed changes with the played note pitch.
    Higher values make envelopes faster for higher notes.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Key tracking value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the key tracking for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b1_key_track',
        midi_cc=76,
        midi_channel=midi_channel,
        value=value,
    )


def set_fm_tone_b2_key_track(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the key tracking amount for operator B2.
    
    Controls how much operator B2's envelope speed changes with the played note pitch.
    Higher values make envelopes faster for higher notes.
    
    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Key tracking value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the key tracking for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_fm_tone_b2_key_track',
        midi_cc=77,
        midi_channel=midi_channel,
        value=value,
    )