"""
LFO and Modulation tools for controlling LFO and Mod Matrix parameters on the Moog Sub 37.
Parameters controlled via High-Resolution CC, standard CC, and NRPN.
"""

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse

# --- LFO 1 Tools ---


def set_lfo1_rate_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Rate (High-Resolution CC 3/35).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for LFO 1 Rate (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_rate_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=3,
        midi_cc_lsb=35,
    )


def set_lfo1_rate_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Rate (NRPN MSB 3, LSB 39).
    Note: LFO1 Rate is also controllable via High-Resolution CC 3/35.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 1 Rate (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_rate_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=39,
    )


def set_lfo1_range_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Range (NRPN MSB 3, LSB 40).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 1 Range (0=Low, 1=Mid, 2=High).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_range_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=40,
    )


def set_lfo1_sync_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Sync On/Off (NRPN MSB 3, LSB 41).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 1 Sync (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_sync_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=41,
    )


def set_lfo1_kb_reset_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Keyboard Reset On/Off (NRPN MSB 3, LSB 42).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 1 KB Reset (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_kb_reset_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=42,
    )


def set_lfo1_clk_div_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Clock Divider (NRPN MSB 3, LSB 43).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 1 Clock Divider (0-20). See manual for division mapping.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_clk_div_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=43,
    )


def set_lfo1_clk_src_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Clock Source (NRPN MSB 3, LSB 44).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 1 Clock Source (0=Internal, 1=MIDI Clock).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_clk_src_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=44,
    )


def set_lfo1_kb_track_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Keyboard Tracking Amount (NRPN MSB 3, LSB 46).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 1 KB Track Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_kb_track_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=46,
    )


# --- LFO 2 Tools ---


def set_lfo2_rate_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Rate (NRPN MSB 3, LSB 64).
    Note: LFO2 Rate is also controllable via High-Resolution CC 8/40.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 2 Rate (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_rate_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=64,
    )


def set_lfo2_range_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Range (NRPN MSB 3, LSB 65).
    Note: LFO2 Range is also controllable via standard CC 78.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 2 Range (0=Low, 1=Mid, 2=High).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_range_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=65,
    )


def set_lfo2_sync_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Sync On/Off (NRPN MSB 3, LSB 66).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 2 Sync (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_sync_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=66,
    )


def set_lfo2_kb_reset_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Keyboard Reset On/Off (NRPN MSB 3, LSB 67).
    Note: LFO2 KB Reset is also controllable via standard CC 95.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 2 KB Reset (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_kb_reset_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=67,
    )


def set_lfo2_clk_div_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Clock Divider (NRPN MSB 3, LSB 68).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 2 Clock Divider (0-20). See manual for division mapping.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_clk_div_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=68,
    )


def set_lfo2_clk_src_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Clock Source (NRPN MSB 3, LSB 69).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 2 Clock Source (0=Internal, 1=MIDI Clock).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_clk_src_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=69,
    )


def set_lfo2_kb_track_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Keyboard Tracking Amount (NRPN MSB 3, LSB 71).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 2 KB Track Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_kb_track_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=71,
    )


# --- LFO 2 CC Tools (Duplicates of NRPN) ---
# These are kept for potential alternative control methods if needed,
# but NRPN is generally preferred for these parameters.


def set_lfo2_rate_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Rate (High-Resolution CC 8/40).
    Alternative to NRPN (3, 64).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for LFO 2 Rate (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_rate_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=8,
        midi_cc_lsb=40,
    )


def set_lfo2_range_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Range selection (Standard CC 78).
    Alternative to NRPN (3, 65).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for range selection (0 = Low, 43 = Med, 85 = Hi).
                     Use values 0, 43, 85 for specific ranges.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_range_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=78,
        midi_cc_lsb=None,
    )


def set_lfo1_range_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Range selection (Standard CC 76).
    Alternative to NRPN (3, 40).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for range selection (0 = Low, 43 = Med, 85 = Hi).
                     Use values 0, 43, 85 for specific ranges.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_range_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=76,
        midi_cc_lsb=None,
    )


def set_lfo1_kb_reset_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 1 Keyboard Reset (Standard CC 93).
    Alternative to NRPN (3, 42).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for keyboard reset (0 = OFF, 64 = ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_kb_reset_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=93,
        midi_cc_lsb=None,
    )


def set_lfo2_kb_reset_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Keyboard Reset (Standard CC 95).
    Alternative to NRPN (3, 67).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for keyboard reset (0 = OFF, 64 = ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_kb_reset_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=95,
        midi_cc_lsb=None,
    )
