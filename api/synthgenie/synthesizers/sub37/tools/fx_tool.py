"""
FX and Misc tools for controlling miscellaneous parameters on the Moog Sub 37.
These are typically controlled via standard MIDI CC messages.
"""

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


def set_hold_pedal(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Hold Pedal/Sustain (CC 64).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Hold Pedal (0 = OFF, 64 = ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_hold_pedal',
        midi_channel=midi_channel,
        value=value,
        midi_cc=64,
        midi_cc_lsb=None,
    )


def set_bank_select(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Bank Select (CC 0).
    Always transmits 0, should always send 0 when sending this CC.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Bank Select (always 0).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_bank_select',
        midi_channel=midi_channel,
        value=value,
        midi_cc=0,
        midi_cc_lsb=None,
    )


def set_bank_select_lsb(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Bank Select LSB (CC 32).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Bank Select LSB (0 = Preset Banks 1-8, 1 = Preset Banks 9-16).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_bank_select_lsb',
        midi_channel=midi_channel,
        value=value,
        midi_cc=32,
        midi_cc_lsb=None,
    )


def set_kb_octave(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Keyboard Octave (CC 89).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for KB Octave (0 = -2 Oct, 26 = -1 Oct, 51 = +0 Oct, 77 = +1 Oct, 102 = +2 Oct).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_kb_octave',
        midi_channel=midi_channel,
        value=value,
        midi_cc=89,
        midi_cc_lsb=None,
    )


def set_pitch_bend_up_amount(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Pitch Bend Up Amount (CC 107).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Pitch Bend Up Amount (0-24 Semitones).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_pitch_bend_up_amount',
        midi_channel=midi_channel,
        value=value,
        midi_cc=107,
        midi_cc_lsb=None,
    )


def set_pitch_bend_down_amount(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Pitch Bend Down Amount (CC 108).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Pitch Bend Down Amount (0-24 Semitones).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_pitch_bend_down_amount',
        midi_channel=midi_channel,
        value=value,
        midi_cc=108,
        midi_cc_lsb=None,
    )


def set_kb_ctrl_lo_hi(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Keyboard Control Lo/Hi (CC 111).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for KB Ctrl Lo/Hi (0 = Neither, 32 = Lo, 64 = Hi).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_kb_ctrl_lo_hi',
        midi_channel=midi_channel,
        value=value,
        midi_cc=111,
        midi_cc_lsb=None,
    )


def set_kb_transpose(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Keyboard Transpose (CC 119).
    Receive Only: -12 to +13 Semitones.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for KB Transpose (-12 to +13 Semitones).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_kb_transpose',
        midi_channel=midi_channel,
        value=value,
        midi_cc=119,
        midi_cc_lsb=None,
    )


def set_local_control(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Local Control On/Off (CC 122).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Local Control (0 = OFF, 127 = ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_local_control',
        midi_channel=midi_channel,
        value=value,
        midi_cc=122,
        midi_cc_lsb=None,
    )


def set_all_notes_off(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set All Notes Off (CC 123).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for All Notes Off.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_all_notes_off',
        midi_channel=midi_channel,
        value=value,
        midi_cc=123,
        midi_cc_lsb=None,
    )


def set_master_volume_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Master Volume (High-Resolution CC 7/39).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Master Volume (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_master_volume_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=7,
        midi_cc_lsb=39,
    )
