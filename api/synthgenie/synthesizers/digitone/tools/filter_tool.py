import logging

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse

logger = logging.getLogger(__name__)


# Multi-Mode Filter functions
def set_multi_mode_filter_attack(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the attack time of the multi-mode filter envelope.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Attack time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the filter attack for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_attack',
        midi_cc=20,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_decay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the decay time of the multi-mode filter envelope.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Decay time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 64.
        midi_channel (int): The MIDI channel (track) to set the filter decay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_decay',
        midi_cc=21,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_sustain(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the sustain level of the multi-mode filter envelope.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Sustain level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the filter sustain for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_sustain',
        midi_cc=22,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_release(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the release time of the multi-mode filter envelope.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Release time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 64.
        midi_channel (int): The MIDI channel (track) to set the filter release for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_release',
        midi_cc=23,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_frequency(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the cutoff frequency of the multi-mode filter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Cutoff frequency value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        midi_channel (int): The MIDI channel (track) to set the filter frequency for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_frequency',
        midi_cc=16,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_resonance(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the resonance of the multi-mode filter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Resonance value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the filter resonance for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_resonance',
        midi_cc=17,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_type(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the type of the multi-mode filter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Filter type value ranging from 0 to 127.
            - 0   = Lowpass
            - 64  = EQ
            - 127 = Highpass
            Values between these points represent transitions between filter types.
            Display range: continuous.
            Default is 0 (Lowpass).
        midi_channel (int): The MIDI channel (track) to set the filter type for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_type',
        midi_cc=18,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_envelope_depth(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the envelope depth of the multi-mode filter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Envelope depth value ranging from 0 to 127.
            - 0 maps to -64
            - 64 maps to 0
            - 127 maps to +64
            Values in between are linearly mapped.
            Display range: -64 to +64.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the filter envelope depth for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_envelope_depth',
        midi_cc=24,
        midi_channel=midi_channel,
        value=value,
    )
