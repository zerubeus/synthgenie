"""
ARP tools for controlling arpeggiator parameters on the Moog Sub 37.
These parameters are controlled via NRPN messages.
"""

from pydantic_ai import RunContext

from synthgenie.schemas.agent import SynthGenieResponse


def set_arp_rate(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Rate (NRPN MSB 3, LSB 19).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Rate (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_rate',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=19,
    )


def set_arp_sync(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Sync (NRPN MSB 3, LSB 20).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Sync (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_sync',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=20,
    )


def set_arp_range(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Range (NRPN MSB 3, LSB 21).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Range (0 = -2 oct, 1 = -1 oct, 2 = 0 oct, 3 = +1 oct, 4 = +2 oct, 5 = +3 oct, 6 = +4 oct).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_range',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=21,
    )


def set_arp_back_forth(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Back/Forth (NRPN MSB 3, LSB 22).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Back/Forth (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_back_forth',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=22,
    )


def set_arp_bf_mode(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Back/Forth Mode (NRPN MSB 3, LSB 23).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP BF Mode (0 = End Repeat, 1 = No Repeat).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_bf_mode',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=23,
    )


def set_arp_invert(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Invert (NRPN MSB 3, LSB 24).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Invert (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_invert',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=24,
    )


def set_arp_pattern(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Pattern (NRPN MSB 3, LSB 25).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Pattern (0=Up, 1=Down, 2=Order, 3=Random, 4=Up KB Oct, 5=Down KB Oct).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_pattern',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=25,
    )


def set_arp_run(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Run (NRPN MSB 3, LSB 26).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Run (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_run',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=26,
    )


def set_arp_latch(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Latch (NRPN MSB 3, LSB 27).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Latch (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_latch',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=27,
    )


def set_arp_gate_len(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Gate Length (NRPN MSB 3, LSB 28).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Gate Length (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_gate_len',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=28,
    )


def set_arp_clk_div(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Clock Divider (NRPN MSB 3, LSB 29).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Clock Divider (0-20).
            See Sub 37 manual for exact note division mapping.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_clk_div',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=29,
    )


def set_arp_step1_reset(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the ARP Step 1 Reset (NRPN MSB 3, LSB 32).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for ARP Step 1 Reset (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_arp_step1_reset',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=32,
    )
