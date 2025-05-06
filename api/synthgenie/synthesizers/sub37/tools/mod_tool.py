"""
MOD tools for controlling Mod Matrix parameters (MOD1, MOD2) on the Moog Sub 37.
Parameters controlled via NRPN, standard CC, and High-Resolution CC.
"""

from pydantic_ai import RunContext

from synthgenie.schemas.agent import SynthGenieResponse

# --- MOD 1 Controller Amount Tools (NRPN) ---


def set_mod1_mwhl_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Mod Wheel Amount (NRPN MSB 3, LSB 51).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Mod Wheel Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_mwhl_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=51,
    )


def set_mod1_velocity_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Velocity Amount (NRPN MSB 3, LSB 52).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Velocity Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_velocity_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=52,
    )


def set_mod1_pressure_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Pressure Amount (NRPN MSB 3, LSB 53).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Pressure Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_pressure_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=53,
    )


def set_mod1_ctl4_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 CTL4 (Expression Pedal) Amount (NRPN MSB 3, LSB 54).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 CTL4 Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_ctl4_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=54,
    )


# --- MOD 1 Source/Destination Tools ---


def set_mod1_source_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Source (NRPN MSB 3, LSB 56).
    Note: Also controllable via standard CC 71.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Source (0-6):
            0 = LFO1 Triangle
            1 = LFO1 Square
            2 = LFO1 Saw
            3 = LFO1 Ramp
            4 = LFO1 S&H
            5 = F.EG/PGM
            6 = Reserved
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_source_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=56,
    )


def set_mod1_source_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 Source (Standard CC 71).
    Alternative to NRPN (3, 56).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 Source:
            0 = LFO1 Triangle
            21 = LFO1 Square
            43 = LFO1 Saw
            64 = LFO1 Ramp
            85 = LFO1 S&H
            107 = F.EG/PGM
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_source_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=71,
    )


def set_mod1_osc_1_2_sel_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 1 OSC 1/2 Select for Pitch Destination (CC 70).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 1 OSC 1/2 Select:
            0 = OSC1 + OSC2
            43 = OSC1
            85 = OSC2
            (Use values 0, 43, 85)
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod1_osc_1_2_sel_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=70,
    )


# --- MOD 2 Controller Amount Tools (NRPN) ---


def set_mod2_mwhl_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Mod Wheel Amount (NRPN MSB 3, LSB 76).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Mod Wheel Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_mwhl_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=76,
    )


def set_mod2_velocity_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Velocity Amount (NRPN MSB 3, LSB 77).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Velocity Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_velocity_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=77,
    )


def set_mod2_pressure_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Pressure Amount (NRPN MSB 3, LSB 78).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Pressure Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_pressure_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=78,
    )


def set_mod2_ctl4_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 CTL4 (Expression Pedal) Amount (NRPN MSB 3, LSB 79).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 CTL4 Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_ctl4_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=79,
    )


# --- MOD 2 Source/Destination Tools ---


def set_mod2_source_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Source (NRPN MSB 3, LSB 81).
    Note: Also controllable via standard CC 72.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Source (0-6):
            0 = LFO2 Triangle
            1 = LFO2 Square
            2 = LFO2 Saw
            3 = LFO2 Ramp
            4 = LFO2 S&H
            5 = F.EG/PGM
            6 = Reserved
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_source_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=81,
    )


def set_mod2_source_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Source (Standard CC 72).
    Alternative to NRPN (3, 81).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Source:
            0 = LFO2 Triangle
            21 = LFO2 Square
            43 = LFO2 Saw
            64 = LFO2 Ramp
            85 = LFO2 S&H
            107 = F.EG/PGM
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_source_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=72,
    )


def set_mod2_pgm_src_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Programmable Source (NRPN MSB 3, LSB 82).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 PGM Source (0-8). See manual for mapping.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_pgm_src_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=82,
    )


def set_mod2_dest_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Destination (excluding Pitch/Filter/PGM) (NRPN MSB 3, LSB 83).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Destination (0-7):
            0 = LFO1 Rate
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
        used_tool='set_mod2_dest_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=83,
    )


def set_mod2_pgm_dest_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Programmable Destination (NRPN MSB 3, LSB 84).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 PGM Destination (0-89). See manual for mapping.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_pgm_dest_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=84,
    )


def set_mod2_pgm_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Programmable Amount (NRPN MSB 3, LSB 85).
    Note: The amount for the PGM Dest is also controllable via High-Res CC 17/49.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 PGM Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_pgm_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=85,
    )


def set_mod2_pitch_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Pitch Amount (NRPN MSB 3, LSB 86).
    Note: Also controllable via standard CC 15.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Pitch Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_pitch_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=86,
    )


def set_mod2_filter_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Filter Amount (NRPN MSB 3, LSB 87).
    Note: Also controllable via standard CC 16.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Filter Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_filter_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=87,
    )


def set_mod2_pitch_dest_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Pitch Destination (NRPN MSB 3, LSB 88).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Pitch Destination (0=OSC1, 1=OSC2, 2=BOTH, 3=FREQ?).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_pitch_dest_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=88,
    )


def set_mod2_pgm_dest_amt_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 PGM Dest Amount (High-Resolution CC 17/49).
    Note: The amount for PGM Dest is also controllable via NRPN (3, 85).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for MOD 2 PGM Dest Amount (0-16383). Center=8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_pgm_dest_amt_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=17,
        midi_cc_lsb=49,
    )


# --- MOD 2 Amount CC Tools (Duplicates of NRPN) ---


def set_mod2_pitch_amt_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Pitch Amount (Standard CC 15).
    Alternative to NRPN (3, 86).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Pitch Amount (0-127). Center=64.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_pitch_amt_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=15,
    )


def set_mod2_filter_amt_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the MOD 2 Filter Amount (Standard CC 16).
    Alternative to NRPN (3, 87).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for MOD 2 Filter Amount (0-127). Center=64.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod2_filter_amt_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=16,
    )


def set_mod_wheel_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Mod Wheel (High-Resolution CC 1/33).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Mod Wheel (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_mod_wheel_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=1,
        midi_cc_lsb=33,
    )
