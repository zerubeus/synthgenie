from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


def set_pattern_mute(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Mute or unmute the entire pattern.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Pattern mute state value (0 or 1).
            - 0 = Pattern unmuted
            - 1 = Pattern muted
            Display range: Off/On.
            Default is Off (0).
        midi_channel (int): The MIDI channel (track) to set pattern mute for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_pattern_mute',
        midi_cc=110,
        nrpn_msb=1,
        nrpn_lsb=109,
        midi_channel=midi_channel,
        value=value,
    )


def set_master_overdrive(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the master overdrive amount for the global output.

    Adds harmonic saturation and warmth to the final output.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Master overdrive value ranging from 0 to 127.
            - 0 = No overdrive (clean)
            - 127 = Maximum overdrive
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set master overdrive for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_master_overdrive',
        midi_cc=17,
        nrpn_msb=2,
        nrpn_lsb=50,
        midi_channel=midi_channel,
        value=value,
    )
