"""
Filter tools for controlling filter and filter envelope parameters on the Moog Sub 37.
Includes parameters controlled via standard CC, high-resolution CC, and NRPN.
"""

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse

# --- High-Resolution CC Filter Parameters ---


def set_filter_multidrive(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Multidrive (High-Resolution CC 18/50).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter Multidrive (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_multidrive',
        midi_channel=midi_channel,
        value=value,
        midi_cc=18,
        midi_cc_lsb=50,
    )


def set_filter_cutoff(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Cutoff (High-Resolution CC 19/51).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter Cutoff (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_cutoff',
        midi_channel=midi_channel,
        value=value,
        midi_cc=19,
        midi_cc_lsb=51,
    )


def set_filter_resonance(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Resonance (High-Resolution CC 21/53).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter Resonance (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_resonance',
        midi_channel=midi_channel,
        value=value,
        midi_cc=21,
        midi_cc_lsb=53,
    )


def set_filter_kb_amt(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Keyboard Amount (High-Resolution CC 22/54).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter Keyboard Amount (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_kb_amt',
        midi_channel=midi_channel,
        value=value,
        midi_cc=22,
        midi_cc_lsb=54,
    )


def set_filter_eg_attack_time(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Attack Time (High-Resolution CC 23/55).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter EG Attack Time (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_attack_time',
        midi_channel=midi_channel,
        value=value,
        midi_cc=23,
        midi_cc_lsb=55,
    )


def set_filter_eg_decay_time(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Decay Time (High-Resolution CC 24/56).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter EG Decay Time (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_decay_time',
        midi_channel=midi_channel,
        value=value,
        midi_cc=24,
        midi_cc_lsb=56,
    )


def set_filter_eg_sustain_level(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Sustain Level (High-Resolution CC 25/57).
    Note: Controls Sustain Level, not Time.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter EG Sustain Level (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_sustain_level',
        midi_channel=midi_channel,
        value=value,
        midi_cc=25,
        midi_cc_lsb=57,
    )


def set_filter_eg_release_time(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Release Time (High-Resolution CC 26/58).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter EG Release Time (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_release_time',
        midi_channel=midi_channel,
        value=value,
        midi_cc=26,
        midi_cc_lsb=58,
    )


def set_filter_eg_amt(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Amount (High-Resolution CC 27/59).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for Filter EG Amount (0-16383).
                     Center is 8192.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_amt',
        midi_channel=midi_channel,
        value=value,
        midi_cc=27,
        midi_cc_lsb=59,
    )


# --- Standard CC Filter/EG Parameters ---


def set_filter_eg_kb_amt(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Keyboard Amount (CC 79).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Keyboard Amount (0-127).
                     Center is 64.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_kb_amt',
        midi_channel=midi_channel,
        value=value,
        midi_cc=79,
    )


def set_filter_eg_reset(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Reset (CC 82).
    Note: Sub37 MIDI Spec says CC 82 is 'EG Reset', affecting both Filter and Amp Env.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Reset (0 = OFF, 64 = ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_reset',
        midi_channel=midi_channel,
        value=value,
        midi_cc=82,
    )


def set_filter_eg_vel_amt(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Velocity Amount (CC 86).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Velocity Amount (0-127).
                     Center is 64.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_vel_amt',
        midi_channel=midi_channel,
        value=value,
        midi_cc=86,
    )


def set_filter_eg_delay(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Delay (CC 103).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Delay (0-127).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_delay',
        midi_channel=midi_channel,
        value=value,
        midi_cc=103,
    )


def set_filter_eg_hold(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Hold (CC 105).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Hold (0-127).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_hold',
        midi_channel=midi_channel,
        value=value,
        midi_cc=105,
    )


# --- NRPN Filter/EG Parameters ---


def set_filter_cutoff_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Cutoff via NRPN (NRPN MSB 3, LSB 115).
    Alternative to High-Res CC 19/51.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter Cutoff (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_cutoff_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=115,
    )


def set_filter_resonance_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Resonance via NRPN (NRPN MSB 3, LSB 116).
    Alternative to High-Res CC 21/53.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter Resonance (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_resonance_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=116,
    )


def set_filter_drive_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Drive (NRPN MSB 3, LSB 117).
    Note: Filter *Multidrive* uses High-Res CC 18/50.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter Drive (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_drive_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=117,
    )


def set_filter_slope_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Slope (NRPN MSB 3, LSB 118).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter Slope (0=6dB, 1=12dB, 2=18dB, 3=24dB).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_slope_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=118,
    )


def set_filter_eg_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Amount via NRPN (NRPN MSB 3, LSB 119).
    Alternative to High-Res CC 27/59.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Amount (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=119,
    )


def set_filter_kb_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Keyboard Amount via NRPN (NRPN MSB 3, LSB 120).
    Alternative to High-Res CC 22/54.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter KB Amount (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_kb_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=120,
    )


def set_filter_eg_attack_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Attack Time via NRPN (NRPN MSB 3, LSB 121).
    Alternative to High-Res CC 23/55.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Attack Time (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_attack_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=121,
    )


def set_filter_eg_decay_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Decay Time via NRPN (NRPN MSB 3, LSB 122).
    Alternative to High-Res CC 24/56.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Decay Time (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_decay_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=122,
    )


def set_filter_eg_sustain_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Sustain Level via NRPN (NRPN MSB 3, LSB 123).
    Alternative to High-Res CC 25/57.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Sustain Level (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_sustain_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=123,
    )


def set_filter_eg_release_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Release Time via NRPN (NRPN MSB 3, LSB 124).
    Alternative to High-Res CC 26/58.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Release Time (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_release_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=124,
    )


def set_filter_eg_delay_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Delay via NRPN (NRPN MSB 3, LSB 125).
    Alternative to Standard CC 103.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Delay (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_delay_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=125,
    )


def set_filter_eg_hold_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Hold via NRPN (NRPN MSB 3, LSB 126).
    Alternative to Standard CC 105.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Hold (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_hold_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=126,
    )


def set_filter_eg_vel_amt_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Velocity Amount via NRPN (NRPN MSB 3, LSB 127).
    Alternative to Standard CC 86.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Velocity Amount (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_vel_amt_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=127,
    )


def set_filter_eg_kb_track_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Keyboard Track (NRPN MSB 4, LSB 0).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG KB Track (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_kb_track_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=4,
        nrpn_lsb=0,
    )


def set_filter_eg_multi_trig_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Multi Trigger (NRPN MSB 4, LSB 1).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Multi Trigger (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_multi_trig_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=4,
        nrpn_lsb=1,
    )


def set_filter_eg_reset_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Reset via NRPN (NRPN MSB 4, LSB 2).
    Alternative to standard CC 82 (which resets both EGs).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Reset (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_reset_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=4,
        nrpn_lsb=2,
    )


def set_filter_eg_sync_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Sync (NRPN MSB 4, LSB 3).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Sync (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_sync_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=4,
        nrpn_lsb=3,
    )


def set_filter_eg_loop_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Loop (NRPN MSB 4, LSB 4).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Loop (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_loop_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=4,
        nrpn_lsb=4,
    )


def set_filter_eg_latch_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Latch (NRPN MSB 4, LSB 5).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Latch (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_latch_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=4,
        nrpn_lsb=5,
    )


def set_filter_eg_clk_div_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Clock Divider (NRPN MSB 4, LSB 6).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Clock Divider (0-20).
                     See Sub 37 manual for mapping.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_clk_div_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=4,
        nrpn_lsb=6,
    )


def set_filter_eg_attack_exp_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Attack Exponential Curve (NRPN MSB 4, LSB 8).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Attack Exp (0=Linear, 1=Exponential).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_attack_exp_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=4,
        nrpn_lsb=8,
    )


def set_filter_slopes_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter Slopes/Poles (CC 109).
    Note: Also available as NRPN (3, 118) via set_filter_slope_nrpn.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter Slopes (0 = -6dB, 32 = -12dB, 64 = -18dB, 96 = -24dB).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_slopes_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=109,
        midi_cc_lsb=None,
    )


def set_filter_eg_multi_trig_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Filter EG Multi Trigger via CC (CC 112).
    Note: Also available as NRPN (4, 1) via set_filter_eg_multi_trig_nrpn.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Filter EG Multi Trigger (0 = OFF, 64 = ON).
                     Ensure the value is either 0 or 64.
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_filter_eg_multi_trig_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=112,
        midi_cc_lsb=None,
    )
