from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


# COMPRESSOR Parameters
def set_compressor_threshold(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the threshold for the master compressor.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Threshold value ranging from 0 to 127.
            Lower values mean more compression is applied.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set compressor threshold for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_compressor_threshold',
        midi_cc=111,
        nrpn_msb=2,
        nrpn_lsb=16,
        midi_channel=midi_channel,
        value=value,
    )


def set_compressor_attack_time(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the attack time for the master compressor.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Attack time value ranging from 0 to 127.
            - 0 = Fast attack
            - 127 = Slow attack
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set compressor attack time for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_compressor_attack_time',
        midi_cc=112,
        nrpn_msb=2,
        nrpn_lsb=17,
        midi_channel=midi_channel,
        value=value,
    )


def set_compressor_release_time(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the release time for the master compressor.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Release time value ranging from 0 to 127.
            - 0 = Fast release
            - 127 = Slow release
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set compressor release time for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_compressor_release_time',
        midi_cc=113,
        nrpn_msb=2,
        nrpn_lsb=18,
        midi_channel=midi_channel,
        value=value,
    )


def set_compressor_makeup_gain(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the makeup gain for the master compressor.

    Compensates for volume reduction caused by compression.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Makeup gain value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set compressor makeup gain for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_compressor_makeup_gain',
        midi_cc=114,
        nrpn_msb=2,
        nrpn_lsb=19,
        midi_channel=midi_channel,
        value=value,
    )


def set_compressor_ratio(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the compression ratio for the master compressor.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Ratio value ranging from 0 to 127.
            Higher values mean more aggressive compression.
            Display range: 0-127 (maps to ratios like 2:1, 4:1, 10:1, etc.).
            Default varies.
        midi_channel (int): The MIDI channel (track) to set compressor ratio for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_compressor_ratio',
        midi_cc=115,
        nrpn_msb=2,
        nrpn_lsb=20,
        midi_channel=midi_channel,
        value=value,
    )


def set_compressor_sidechain_source(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the sidechain source for the master compressor.

    Determines which signal triggers the compression.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Sidechain source value.
            Different values select different sidechain sources.
            Display range: discrete options.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set compressor sidechain source for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_compressor_sidechain_source',
        midi_cc=116,
        nrpn_msb=2,
        nrpn_lsb=21,
        midi_channel=midi_channel,
        value=value,
    )


def set_compressor_sidechain_filter(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the sidechain filter frequency for the master compressor.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Sidechain filter value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set compressor sidechain filter for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_compressor_sidechain_filter',
        midi_cc=117,
        nrpn_msb=2,
        nrpn_lsb=22,
        midi_channel=midi_channel,
        value=value,
    )


def set_compressor_dry_wet_mix(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the dry/wet mix for the master compressor.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Dry/wet mix value ranging from 0 to 127.
            - 0 = Fully dry (no compression)
            - 127 = Fully wet (full compression)
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set compressor dry/wet mix for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_compressor_dry_wet_mix',
        midi_cc=118,
        nrpn_msb=2,
        nrpn_lsb=23,
        midi_channel=midi_channel,
        value=value,
    )


def set_pattern_volume(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the overall pattern volume.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Pattern volume value ranging from 0 to 127.
            - 0 = Silent
            - 127 = Maximum volume
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set pattern volume for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_pattern_volume',
        midi_cc=119,
        nrpn_msb=2,
        nrpn_lsb=24,
        midi_channel=midi_channel,
        value=value,
    )


# EXTERNAL INPUT MIXER Parameters
def set_external_input_dual_mono(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Enable or disable dual mono mode for external inputs.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Dual mono mode value (0 or 1).
            - 0 = Stereo mode
            - 1 = Dual mono mode
            Display range: Off/On.
            Default is Off (0).
        midi_channel (int): The MIDI channel (track) to set dual mono mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_dual_mono',
        midi_cc=82,
        nrpn_msb=2,
        nrpn_lsb=40,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_l_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the level for the left external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set external input L level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_l_level',
        midi_cc=72,
        nrpn_msb=2,
        nrpn_lsb=30,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_l_pan(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the pan position for the left external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Pan value ranging from 0 to 127.
            - 0 = Full left
            - 64 = Center
            - 127 = Full right
            Display range: 0-127.
            Default is center (64).
        midi_channel (int): The MIDI channel (track) to set external input L pan for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_l_pan',
        midi_cc=74,
        nrpn_msb=2,
        nrpn_lsb=32,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_r_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the level for the right external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Level value ranging from 0 to 127.
            Display range: 0-127.
            Default varies.
        midi_channel (int): The MIDI channel (track) to set external input R level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_r_level',
        midi_cc=73,
        nrpn_msb=2,
        nrpn_lsb=31,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_r_pan(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the pan position for the right external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Pan value ranging from 0 to 127.
            - 0 = Full left
            - 64 = Center
            - 127 = Full right
            Display range: 0-127.
            Default is center (64).
        midi_channel (int): The MIDI channel (track) to set external input R pan for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_r_pan',
        midi_cc=75,
        nrpn_msb=2,
        nrpn_lsb=33,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_l_delay_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the delay send amount for the left external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Delay send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set external input L delay send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_l_delay_send',
        midi_cc=78,
        nrpn_msb=2,
        nrpn_lsb=36,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_r_delay_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the delay send amount for the right external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Delay send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set external input R delay send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_r_delay_send',
        midi_cc=79,
        nrpn_msb=2,
        nrpn_lsb=37,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_l_reverb_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the reverb send amount for the left external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Reverb send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set external input L reverb send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_l_reverb_send',
        midi_cc=80,
        nrpn_msb=2,
        nrpn_lsb=38,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_r_reverb_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the reverb send amount for the right external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Reverb send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set external input R reverb send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_r_reverb_send',
        midi_cc=81,
        nrpn_msb=2,
        nrpn_lsb=39,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_l_chorus_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the chorus send amount for the left external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Chorus send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set external input L chorus send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_l_chorus_send',
        midi_cc=76,
        nrpn_msb=2,
        nrpn_lsb=34,
        midi_channel=midi_channel,
        value=value,
    )


def set_external_input_r_chorus_send(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the chorus send amount for the right external input.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Chorus send value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set external input R chorus send for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_external_input_r_chorus_send',
        midi_cc=77,
        nrpn_msb=2,
        nrpn_lsb=35,
        midi_channel=midi_channel,
        value=value,
    )
