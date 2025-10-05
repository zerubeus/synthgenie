from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


def set_trig_note(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the note value for a trig.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI note value ranging from 0 to 127.
            - 0 = C-2
            - 60 = Middle C (C3)
            - 127 = G8
            Display range: 0-127 (MIDI note numbers).
            Default varies by trig.
        midi_channel (int): The MIDI channel (track) to set the note for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_trig_note',
        midi_cc=3,
        midi_channel=midi_channel,
        value=value,
    )


def set_trig_velocity(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the velocity for a trig.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Velocity value ranging from 0 to 127.
            - 0 = Minimum velocity
            - 127 = Maximum velocity
            Display range: 0-127.
            Default is 100.
        midi_channel (int): The MIDI channel (track) to set the velocity for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_trig_velocity',
        midi_cc=4,
        midi_channel=midi_channel,
        value=value,
    )


def set_trig_length(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the note length for a trig.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Length value ranging from 0 to 127.
            Controls the duration of the triggered note.
            Display range: 0-127.
            Default varies by trig.
        midi_channel (int): The MIDI channel (track) to set the note length for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_trig_length',
        midi_cc=5,
        midi_channel=midi_channel,
        value=value,
    )


def set_filter_trig(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the filter trigger parameter.

    Controls whether the filter envelope is triggered for this trig.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Filter trig value (0 or 1).
            - 0 = Filter envelope not triggered
            - 1 = Filter envelope triggered
            Display range: Off/On.
            Default is On (1).
        midi_channel (int): The MIDI channel (track) to set the filter trig for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_filter_trig',
        midi_cc=13,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo_trig(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the LFO trigger parameter.

    Controls whether the LFOs are triggered for this trig.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): LFO trig value (0 or 1).
            - 0 = LFOs not triggered
            - 1 = LFOs triggered
            Display range: Off/On.
            Default is On (1).
        midi_channel (int): The MIDI channel (track) to set the LFO trig for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo_trig',
        midi_cc=14,
        midi_channel=midi_channel,
        value=value,
    )


def set_portamento_time(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the portamento time (glide time between notes).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Portamento time value ranging from 0 to 127.
            - 0 = Instant transition (no portamento)
            - 127 = Maximum glide time
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the portamento time for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_portamento_time',
        midi_cc=9,
        midi_channel=midi_channel,
        value=value,
    )


def set_portamento_on_off(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Enable or disable portamento (pitch glide between notes).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Portamento state value (0 or 1).
            - 0 = Portamento off
            - 1 = Portamento on
            Display range: Off/On.
            Default is Off (0).
        midi_channel (int): The MIDI channel (track) to enable/disable portamento for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_portamento_on_off',
        midi_cc=65,
        midi_channel=midi_channel,
        value=value,
    )
