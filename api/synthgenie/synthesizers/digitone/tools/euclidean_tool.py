from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


def set_euclidean_pulse_gen1(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set Pulse Generator 1 for the Euclidean sequencer.

    Defines the number of pulses in the first Euclidean pattern.

    Note: Uses NRPN messages only (no MIDI CC support).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Number of pulses ranging from 0 to 16.
            Display range: 0-16.
            Default varies by pattern.
        midi_channel (int): The MIDI channel (track) to set pulse generator 1 for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_euclidean_pulse_gen1',
        nrpn_msb=3,
        nrpn_lsb=8,
        midi_channel=midi_channel,
        value=value,
    )


def set_euclidean_pulse_gen2(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set Pulse Generator 2 for the Euclidean sequencer.

    Defines the number of pulses in the second Euclidean pattern.

    Note: Uses NRPN messages only (no MIDI CC support).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Number of pulses ranging from 0 to 16.
            Display range: 0-16.
            Default varies by pattern.
        midi_channel (int): The MIDI channel (track) to set pulse generator 2 for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_euclidean_pulse_gen2',
        nrpn_msb=3,
        nrpn_lsb=9,
        midi_channel=midi_channel,
        value=value,
    )


def set_euclidean_mode(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Enable or disable Euclidean mode for the sequencer.

    Note: Uses NRPN messages only (no MIDI CC support).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Mode value (0 or 1).
            - 0 = Euclidean mode off
            - 1 = Euclidean mode on
            Display range: Off/On.
            Default is Off (0).
        midi_channel (int): The MIDI channel (track) to set Euclidean mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_euclidean_mode',
        nrpn_msb=3,
        nrpn_lsb=14,
        midi_channel=midi_channel,
        value=value,
    )


def set_euclidean_rotation_gen1(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set Rotation Generator 1 for the Euclidean sequencer.

    Rotates the first Euclidean pattern by the specified number of steps.

    Note: Uses NRPN messages only (no MIDI CC support).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Rotation amount ranging from 0 to 15.
            Display range: 0-15.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set rotation generator 1 for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_euclidean_rotation_gen1',
        nrpn_msb=3,
        nrpn_lsb=11,
        midi_channel=midi_channel,
        value=value,
    )


def set_euclidean_rotation_gen2(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set Rotation Generator 2 for the Euclidean sequencer.

    Rotates the second Euclidean pattern by the specified number of steps.

    Note: Uses NRPN messages only (no MIDI CC support).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Rotation amount ranging from 0 to 15.
            Display range: 0-15.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set rotation generator 2 for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_euclidean_rotation_gen2',
        nrpn_msb=3,
        nrpn_lsb=12,
        midi_channel=midi_channel,
        value=value,
    )


def set_euclidean_track_rotation(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set track rotation for the Euclidean sequencer.

    Rotates the entire pattern on the track by the specified number of steps.

    Note: Uses NRPN messages only (no MIDI CC support).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Rotation amount ranging from 0 to 15.
            Display range: 0-15.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set track rotation for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_euclidean_track_rotation',
        nrpn_msb=3,
        nrpn_lsb=13,
        midi_channel=midi_channel,
        value=value,
    )


def set_euclidean_boolean_operator(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the Boolean operator for combining the two Euclidean generators.

    The Boolean operator determines how Generator 1 and Generator 2 interact.

    Note: Uses NRPN messages only (no MIDI CC support).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Boolean operator value ranging from 0 to 7.
            - 0 = OR (either generator triggers)
            - 1 = AND (both generators must trigger)
            - 2 = XOR (only one generator triggers, not both)
            - 3 = NOR (neither generator triggers)
            - 4-7 = Other boolean combinations
            Display range: discrete options (0-7).
            Default is OR (0).
        midi_channel (int): The MIDI channel (track) to set the Boolean operator for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_euclidean_boolean_operator',
        nrpn_msb=3,
        nrpn_lsb=10,
        midi_channel=midi_channel,
        value=value,
    )
