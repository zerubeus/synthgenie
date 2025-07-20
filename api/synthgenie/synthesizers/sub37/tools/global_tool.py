"""
Global and utility tools for controlling global parameters on the Moog Sub 37.
Parameters controlled via standard and high-resolution CC messages.
"""

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


def set_bank_select_msb(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Bank Select MSB (CC 0).
    Note: According to Sub 37 spec, this should always be 0.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Bank Select MSB (should be 0).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_bank_select_msb',
        midi_channel=midi_channel,
        value=value,  # Should ideally validate this is 0
        midi_cc=0,
    )


def set_bank_select_lsb(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Bank Select LSB (CC 32).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Bank Select LSB (0 = Banks 1–8, 1 = Banks 9–16).
                     Values 0-1 specify the bank group.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_bank_select_lsb',
        midi_channel=midi_channel,
        value=value,
        midi_cc=32,
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


def set_kb_octave(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Keyboard Octave (CC 89).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Keyboard Octave (0 = -2 Oct, 26 = -1 Oct, 51 = +0 Oct, 77 = +1 Oct, 102 = +2 Oct).
                     Use values 0, 26, 51, 77, 102 for standard octaves.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_kb_octave',
        midi_channel=midi_channel,
        value=value,
        midi_cc=89,
    )


def set_kb_transpose(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Keyboard Transpose (CC 119).
    Note: This is receive-only on the Sub 37.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Keyboard Transpose (-12 to +13 semitones).
                     Map this range to 0-127 if necessary, or handle in processing.
                     Example mapping: -12=0, 0=64, +13=127
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_kb_transpose',
        midi_channel=midi_channel,
        value=value,  # Requires mapping/interpretation
        midi_cc=119,
    )


def set_local_control(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set Local Control On/Off (CC 122).

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
    )


def all_notes_off(ctx: RunContext, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Send All Notes Off message (CC 123, value 0).

    Args:
        ctx (RunContext): The run context containing dependencies.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='all_notes_off',
        midi_channel=midi_channel,
        value=0,  # CC 123 always uses value 0 for All Notes Off
        midi_cc=123,
    )
