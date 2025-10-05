from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


# DELAY Parameters
def set_delay_time(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the delay time for the global delay effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Delay time value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set the delay time for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_delay_time',
        midi_cc=21,
        nrpn_msb=2,
        nrpn_lsb=0,
        midi_channel=midi_channel,
        value=value,
    )


def set_delay_pingpong(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the pingpong mode for the delay effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Pingpong value (0 or 1).
            - 0 = Pingpong off
            - 1 = Pingpong on
            Display range: Off/On.
            Default is Off (0).
        midi_channel (int): The MIDI channel (track) to set delay pingpong for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_delay_pingpong',
        midi_cc=22,
        nrpn_msb=2,
        nrpn_lsb=1,
        midi_channel=midi_channel,
        value=value,
    )


def set_delay_stereo_width(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the stereo width of the delay effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Stereo width value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set delay stereo width for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_delay_stereo_width',
        midi_cc=23,
        nrpn_msb=2,
        nrpn_lsb=2,
        midi_channel=midi_channel,
        value=value,
    )


def set_delay_feedback(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the feedback amount for the delay effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Feedback value ranging from 0 to 127.
            - 0 = No feedback (single repeat)
            - 127 = Maximum feedback (infinite repeats)
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set delay feedback for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_delay_feedback',
        midi_cc=24,
        nrpn_msb=2,
        nrpn_lsb=3,
        midi_channel=midi_channel,
        value=value,
    )


def set_delay_highpass_filter(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the highpass filter frequency for the delay effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Highpass filter value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set delay highpass filter for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_delay_highpass_filter',
        midi_cc=25,
        nrpn_msb=2,
        nrpn_lsb=4,
        midi_channel=midi_channel,
        value=value,
    )


def set_delay_lowpass_filter(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the lowpass filter frequency for the delay effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Lowpass filter value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set delay lowpass filter for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_delay_lowpass_filter',
        midi_cc=26,
        nrpn_msb=2,
        nrpn_lsb=5,
        midi_channel=midi_channel,
        value=value,
    )


def set_delay_reverb_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the reverb send amount from the delay effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Reverb send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set delay reverb send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_delay_reverb_send',
        midi_cc=27,
        nrpn_msb=2,
        nrpn_lsb=6,
        midi_channel=midi_channel,
        value=value,
    )


def set_delay_mix_volume(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the mix volume for the delay effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Mix volume value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set delay mix volume for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_delay_mix_volume',
        midi_cc=28,
        nrpn_msb=2,
        nrpn_lsb=7,
        midi_channel=midi_channel,
        value=value,
    )


# REVERB Parameters
def set_reverb_predelay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the predelay time for the reverb effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Predelay time value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set reverb predelay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_reverb_predelay',
        midi_cc=29,
        nrpn_msb=2,
        nrpn_lsb=8,
        midi_channel=midi_channel,
        value=value,
    )


def set_reverb_decay_time(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time for the reverb effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Decay time value ranging from 0 to 127.
            - 0 = Short decay
            - 127 = Long decay
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set reverb decay time for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_reverb_decay_time',
        midi_cc=30,
        nrpn_msb=2,
        nrpn_lsb=9,
        midi_channel=midi_channel,
        value=value,
    )


def set_reverb_shelving_freq(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the shelving filter frequency for the reverb effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Shelving frequency value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set reverb shelving freq for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_reverb_shelving_freq',
        midi_cc=31,
        nrpn_msb=2,
        nrpn_lsb=10,
        midi_channel=midi_channel,
        value=value,
    )


def set_reverb_shelving_gain(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the shelving filter gain for the reverb effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Shelving gain value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set reverb shelving gain for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_reverb_shelving_gain',
        midi_cc=89,
        nrpn_msb=2,
        nrpn_lsb=11,
        midi_channel=midi_channel,
        value=value,
    )


def set_reverb_highpass_filter(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the highpass filter frequency for the reverb effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Highpass filter value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set reverb highpass filter for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_reverb_highpass_filter',
        midi_cc=90,
        nrpn_msb=2,
        nrpn_lsb=12,
        midi_channel=midi_channel,
        value=value,
    )


def set_reverb_lowpass_filter(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the lowpass filter frequency for the reverb effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Lowpass filter value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set reverb lowpass filter for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_reverb_lowpass_filter',
        midi_cc=91,
        nrpn_msb=2,
        nrpn_lsb=13,
        midi_channel=midi_channel,
        value=value,
    )


def set_reverb_mix_volume(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the mix volume for the reverb effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Mix volume value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set reverb mix volume for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_reverb_mix_volume',
        midi_cc=92,
        nrpn_msb=2,
        nrpn_lsb=15,
        midi_channel=midi_channel,
        value=value,
    )


# CHORUS Parameters
def set_chorus_depth(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the depth of the chorus effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Depth value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set chorus depth for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_chorus_depth',
        midi_cc=16,
        nrpn_msb=2,
        nrpn_lsb=41,
        midi_channel=midi_channel,
        value=value,
    )


def set_chorus_speed(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the speed (rate) of the chorus LFO.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Speed value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set chorus speed for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_chorus_speed',
        midi_cc=9,
        nrpn_msb=2,
        nrpn_lsb=42,
        midi_channel=midi_channel,
        value=value,
    )


def set_chorus_highpass_filter(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the highpass filter frequency for the chorus effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Highpass filter value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set chorus highpass filter for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_chorus_highpass_filter',
        midi_cc=70,
        nrpn_msb=2,
        nrpn_lsb=43,
        midi_channel=midi_channel,
        value=value,
    )


def set_chorus_width(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the stereo width of the chorus effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Width value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set chorus width for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_chorus_width',
        midi_cc=71,
        nrpn_msb=2,
        nrpn_lsb=44,
        midi_channel=midi_channel,
        value=value,
    )


def set_chorus_delay_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the delay send amount from the chorus effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Delay send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set chorus delay send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_chorus_delay_send',
        midi_cc=12,
        nrpn_msb=2,
        nrpn_lsb=45,
        midi_channel=midi_channel,
        value=value,
    )


def set_chorus_reverb_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the reverb send amount from the chorus effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Reverb send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set chorus reverb send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_chorus_reverb_send',
        midi_cc=13,
        nrpn_msb=2,
        nrpn_lsb=46,
        midi_channel=midi_channel,
        value=value,
    )


def set_chorus_mix_volume(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the mix volume for the chorus effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Mix volume value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set chorus mix volume for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_chorus_mix_volume',
        midi_cc=14,
        nrpn_msb=2,
        nrpn_lsb=47,
        midi_channel=midi_channel,
        value=value,
    )
