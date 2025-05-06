import logging

from pydantic_ai import RunContext

from synthgenie.schemas.agent import SynthGenieResponse

logger = logging.getLogger(__name__)


# Oscillator 1 methods
def set_wavetone_osc1_pitch(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the pitch of oscillator one.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI pitch value ranging from 0 to 127.
            - 0 maps to -5
            - 64 maps to 0
            - 127 maps to +5
            Values in between are linearly mapped.
            Display range: -5 to +5.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the pitch for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc1_pitch',
        midi_cc=40,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc1_waveform(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the waveform of oscillator one for a specific track.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Waveform value to set, ranging from 0 to 127.
            - 0   = Sine
            - 40  = Triangle
            - 80  = Saw
            - 3   = Square
            Values between these points represent transitions between waveforms.
            (Display range: 0–120)

        midi_channel (int): MIDI channel (track) number to set the waveform for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc1_waveform',
        midi_cc=41,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc1_phase_distortion(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the phase distortion of oscillator one.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Phase distortion value ranging from 0 to 127.
            - 0 maps to 0%
            - 64 maps to 50%
            - 127 maps to 100%
            Values in between are linearly mapped.
            Display range: 0-100%.
            Default is 50%.
        midi_channel (int): The MIDI channel (track) to set the phase distortion for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc1_phase_distortion',
        midi_cc=42,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc1_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the level of oscillator one.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 100.
        midi_channel (int): The MIDI channel (track) to set the level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc1_level',
        midi_cc=43,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc1_offset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the offset of oscillator one.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Offset value ranging from 0 to 127.
            - 0 maps to -10
            - 64 maps to 0
            - 127 maps to +10
            Values in between are linearly mapped.
            Display range: -10 to +10.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the offset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc1_offset',
        midi_cc=48,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc1_table(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Selects the wavetable for oscillator 1's WAVE parameter. Options include PRIM (basic waves like Sin, Tri, Saw, Square) and HARM (a range of harmonic combinations)

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): wavetable value ranging from 0 to 1.
            - 0 = "prim"
            - 1 = "harm"
            Display range: discrete options.
            Default is "prim".
        midi_channel (int): The MIDI channel (track) to set the wavetable for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc1_table',
        midi_cc=49,
        midi_channel=midi_channel,
        value=value,
    )


# Oscillator 2 methods
def set_wavetone_osc2_pitch(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the pitch of oscillator two.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI pitch value ranging from 0 to 127.
            - 0 maps to -5
            - 64 maps to 0
            - 127 maps to +5
            Values in between are linearly mapped.
            Display range: -5 to +5.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the pitch for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc2_pitch',
        midi_cc=44,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc2_waveform(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the waveform of oscillator two.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Waveform value to set, ranging from 0 to 127.
            - 0   = Sine
            - 40  = Triangle
            - 80  = Saw
            - 3   = Square
            Values between these points represent transitions between waveforms.
            Display range: 0-120.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the waveform for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc2_waveform',
        midi_cc=45,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc2_phase_distortion(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the phase distortion of oscillator two.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Phase distortion value ranging from 0 to 127.
            - 0 maps to 0%
            - 64 maps to 50%
            - 127 maps to 100%
            Values in between are linearly mapped.
            Display range: 0-100%.
            Default is 50%.
        midi_channel (int): The MIDI channel (track) to set the phase distortion for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc2_phase_distortion',
        midi_cc=46,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc2_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the level of oscillator two.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 100.
        midi_channel (int): The MIDI channel (track) to set the level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc2_level',
        midi_cc=47,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc2_offset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the offset of oscillator two.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Offset value ranging from 0 to 127.
            - 0 maps to -10
            - 64 maps to 0
            - 127 maps to +10
            Values in between are linearly mapped.
            Display range: -10 to +10.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the offset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc2_offset',
        midi_cc=52,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_osc2_table(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Selects the wavetable for oscillator 2's WAVE parameter. Options include PRIM (basic waves like Sin, Tri, Saw, Square) and HARM (a range of harmonic combinations)

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Table value ranging from 0 to 1.
            - 0 = "prim"
            - 1 = "harm"
            Display range: discrete options.
            Default is "prim".
        midi_channel (int): The MIDI channel (track) to set the table for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_osc2_table',
        midi_cc=53,
        midi_channel=midi_channel,
        value=value,
    )


# Modulation methods
def set_wavetone_mod_type(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    MOD Oscillator Modulation selects how the two oscillators interact. The options are OFF, RING MOD (Oscillator 2 modulates Oscillator 1), RING MODE FIXED (Oscillator 2 modulates Oscillator 1, but its pitch doesn't track note values), and HARD SYNC (Oscillator 1's phase resets with each new cycle of Oscillator 2)

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Modulation type value ranging from 0 to 3.
            - 0 = "off"
            - 1 = "ring mod"
            - 2 = "ring mod fixed"
            - 3 = "hard sync"
            Display range: discrete options.
            Default is "off".
        midi_channel (int): The MIDI channel (track) to set the modulation type for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_mod_type',
        midi_cc=50,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_reset_mode(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    RSET Oscillator Phase Reset determines if and how the oscillators' wave phases reset when a note is played. Options are OFF (no reset), ON (reset to the start of the waveform), and RAND (reset to a random position)

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Reset mode value ranging from 0 to 2.
            - 0 = "off"
            - 1 = "on"
            - 2 = "random"
            Display range: discrete options.
            Default is "on".
        midi_channel (int): The MIDI channel (track) to set the reset mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_reset_mode',
        midi_cc=51,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_drift(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the drift amount.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Drift value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the drift for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_drift',
        midi_cc=55,
        midi_channel=midi_channel,
        value=value,
    )


# Envelope methods
def set_wavetone_attack(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the attack time.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Attack time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the attack for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_attack',
        midi_cc=56,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_hold(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the hold time.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Hold time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        midi_channel (int): The MIDI channel (track) to set the hold for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_hold',
        midi_cc=57,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_decay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Decay time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        midi_channel (int): The MIDI channel (track) to set the decay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_decay',
        midi_cc=58,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_noise_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the noise level.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Noise level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the noise level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_noise_level',
        midi_cc=59,
        midi_channel=midi_channel,
        value=value,
    )


# Noise methods
def set_wavetone_noise_base(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the noise base frequency.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Noise base frequency value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the noise base for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_noise_base',
        midi_cc=60,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_noise_width(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the noise width.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Noise width value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        midi_channel (int): The MIDI channel (track) to set the noise width for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_noise_width',
        midi_cc=61,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_noise_type(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the noise type.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Noise type value ranging from 0 to 2.
            - 0 = "grain noise"
            - 1 = "tuned noise"
            - 2 = "sample and hold noise"
            Display range: discrete options.
            Default is "grain noise" (0).
        midi_channel (int): The MIDI channel (track) to set the noise type for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_noise_type',
        midi_cc=62,
        midi_channel=midi_channel,
        value=value,
    )


def set_wavetone_noise_character(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the noise character.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Noise character value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the noise character for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_wavetone_noise_character',
        midi_cc=63,
        midi_channel=midi_channel,
        value=value,
    )
