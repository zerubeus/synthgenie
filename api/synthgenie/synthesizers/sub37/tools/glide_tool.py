"""
Glide tools for controlling glide parameters on the Moog Sub 37.
Parameters are controlled via High-Resolution CC and NRPN.
"""

from pydantic_ai import RunContext

from synthgenie.schemas.agent import SynthGenieResponse


def set_glide_time(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Glide Time (High-Resolution CC 5/37).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Glide Time (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_glide_time',
        midi_channel=midi_channel,
        value=value,
        midi_cc=5,
        midi_cc_lsb=37,
    )


def set_glide_osc_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Glide OSC Destination (NRPN MSB 3, LSB 34).
    Note: Glide destination is also controllable via CC 102.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Glide OSC Destination (0=OSC1, 1=OSC2, 2=BOTH).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_glide_osc_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=34,
    )


def set_glide_type_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Glide Type (NRPN MSB 3, LSB 35).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Glide Type (0=Linear Constant Rate, 1=Linear Constant Time, 2=Exponential).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_glide_type_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=35,
    )


def set_glide_gate_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Glide Gated setting (NRPN MSB 3, LSB 36).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Glide Gate (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_glide_gate_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=36,
    )


def set_glide_legato_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Glide Legato setting (NRPN MSB 3, LSB 37).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Glide Legato (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_glide_legato_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=37,
    )


def set_glide_on_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Glide On/Off state via NRPN (NRPN MSB 3, LSB 38).
    Note: Glide On/Off is also controllable via CC 65.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Glide On (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_glide_on_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=38,
    )
