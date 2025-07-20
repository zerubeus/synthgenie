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
    Note: LFO2 Rate is also controllable via standard CC 8.

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


def set_lfo2_rate_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Rate (Standard CC 8).
    Alternative to NRPN (3, 64).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for LFO 2 Rate (0-127).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_rate_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=8,
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
    )


def set_lfo2_kb_reset_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the LFO 2 Keyboard Reset (Standard CC 95).
    Alternative to NRPN (3, 67).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for keyboard reset (0 = OFF, 127 = ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_kb_reset_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=95,
    )


# --- Mod Matrix 1 Tools (Mostly NRPN) ---


def set_mod1_pitch_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Pitch Amount (NRPN MSB 3, LSB 61).
    Note: Also controllable via standard CC 4.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Pitch Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_pitch_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=61,
    )


def set_mod1_filter_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Filter Amount (NRPN MSB 3, LSB 62).
    Note: Also controllable via standard CC 11.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Filter Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_filter_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=62,
    )


def set_mod1_pgm_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Programmable Amount (NRPN MSB 3, LSB 60).
    Note: Also controllable via standard CC 20.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 PGM Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_pgm_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=60,
    )


def set_mod1_pgm_src_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Programmable Source (NRPN MSB 3, LSB 57).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 PGM Source (0-8). See manual for mapping.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_pgm_src_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=57,
    )


def set_mod1_dest_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Destination (excluding Pitch/Filter/PGM) (NRPN MSB 3, LSB 58).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Destination (0-7):
            0 = LFO2 Rate
            1 = VCA Level
            2 = OSC1 Wave
            3 = OSC1 + OSC2 Wave
            4 = OSC2 Wave
            5 = Noise Level
            6 = EG Time/PGM (?)
            7 = Reserved
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_dest_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=58,
    )


def set_mod1_pgm_dest_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Programmable Destination (NRPN MSB 3, LSB 59).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 PGM Destination (0-89). See manual for mapping.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_pgm_dest_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=59,
    )


def set_mod1_pitch_dest_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Pitch Destination (NRPN MSB 3, LSB 63).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Pitch Destination (0=OSC1, 1=OSC2, 2=BOTH, 3=FREQ?).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_pitch_dest_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=63,
    )


# --- Mod Matrix 1 CC Tools (Duplicates of NRPN) ---


def set_mod1_pitch_amt_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Pitch Amount (Standard CC 4).
    Alternative to NRPN (3, 61).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Pitch Amount (0-127). Center=64.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_pitch_amt_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=4,
    )


def set_mod1_filter_amt_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Filter Amount (Standard CC 11).
    Alternative to NRPN (3, 62).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Filter Amount (0-127). Center=64.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_filter_amt_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=11,
    )


def set_mod1_pgm_dest_amt_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 PGM Dest Amount (Standard CC 20).
    Alternative to NRPN (3, 60).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 PGM Dest Amount (0-127). Center=64.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_pgm_dest_amt_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=20,
    )
