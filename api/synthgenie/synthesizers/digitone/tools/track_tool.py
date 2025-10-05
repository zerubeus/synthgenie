from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


def set_track_mute(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the mute state for a track.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Mute state value (0 or 1).
            - 0 = Unmuted
            - 1 = Muted
            Display range: Off/On.
            Default is Off (0).
        midi_channel (int): The MIDI channel (track) to mute/unmute. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_track_mute',
        midi_cc=94,
        midi_channel=midi_channel,
        value=value,
    )


def set_track_level(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the level (volume) for a track.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Track level value ranging from 0 to 127.
            - 0 = Silent
            - 127 = Maximum level
            Display range: 0-127.
            Default varies by track.
        midi_channel (int): The MIDI channel (track) to set the level for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_track_level',
        midi_cc=95,
        midi_channel=midi_channel,
        value=value,
    )
