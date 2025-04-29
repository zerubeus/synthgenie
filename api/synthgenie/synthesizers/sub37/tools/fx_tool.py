"""
FX and Misc tools for controlling miscellaneous parameters on the Moog Sub 37.
These are typically controlled via standard MIDI CC messages.
"""

from pydantic_ai import RunContext

from synthgenie.schemas.agent import SynthGenieResponse


def set_hold_pedal(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Hold Pedal/Sustain (CC 64).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Hold Pedal (0 = OFF, 127 = ON).
                     Note: Often 64 is used for ON, but 127 is standard.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_hold_pedal',
        midi_channel=midi_channel,
        value=value,
        midi_cc=64,
    )


def set_glide(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Glide On/Off (CC 65).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Glide (0 = OFF, 127 = ON).
                     Note: Often 64 is used for ON, but 127 is standard.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_glide',
        midi_channel=midi_channel,
        value=value,
        midi_cc=65,
    )


def set_arpeggiator_latch(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Arpeggiator Latch (CC 69).
    Note: Arpeggiator Latch is also controllable via NRPN (3, 27).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Arpeggiator Latch (0 = OFF, 127 = ON).
                     Note: Often 64 is used for ON, but 127 is standard.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arpeggiator_latch',
        midi_channel=midi_channel,
        value=value,
        midi_cc=69,
    )


def set_arp_on_off(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Arpeggiator On/Off (CC 73).
    Note: Arpeggiator Run/On/Off is also controllable via NRPN (3, 26).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Arpeggiator (0 = OFF, 127 = ON).
                     Note: Often 64 is used for ON, but 127 is standard.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_on_off',
        midi_channel=midi_channel,
        value=value,
        midi_cc=73,
    )


def set_glide_dest_osc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Glide Destination OSC 1/2/BOTH (CC 102).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Glide Destination (0 = OSC1 + OSC2, 43 = OSC1, 85 = OSC2).
                     Values 0-42 map to OSC1+OSC2, 43-84 map to OSC1, 85-127 map to OSC2.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_glide_dest_osc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=102,
    )


def set_filter_eg_multi_trig(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Multi Trig (CC 112).
    Note: Filter EG Multi Trig is also controllable via NRPN (4, 1).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Multi Trig (0 = OFF, 127 = ON).
                     Note: Often 64 is used for ON, but 127 is standard.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_multi_trig',
        midi_channel=midi_channel,
        value=value,
        midi_cc=112,
    )
