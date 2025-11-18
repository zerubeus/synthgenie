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

    This parameter uses NRPN (1:20) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI cutoff frequency value ranging from 0 to 16383.
            This parameter uses NRPN (1:20) for full 14-bit resolution.
            Maps to display values from 0 to 127.
            Formula: display = (value / 16383) * 127.0
            - 0 = lowest cutoff frequency (0)
            - 8191 = ~63 (approximately)
            - 16383 = highest cutoff frequency (127)
            Display range: 0-127 with fine precision.
            Default is 127 (MIDI 16383).
        midi_channel (int): The MIDI channel (track) to set the filter frequency for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_frequency',
        nrpn_msb=1,
        nrpn_lsb=20,
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


def set_multi_mode_filter_envelope_delay(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the envelope delay time before the filter envelope starts.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Delay time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the envelope delay for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_envelope_delay',
        midi_cc=19,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_envelope_reset(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the filter envelope reset mode.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Envelope reset mode value (0 or 1).
            - 0 = Off
            - 1 = On
            Display range: Off/On.
            Default is On (1).
        midi_channel (int): The MIDI channel (track) to set the envelope reset for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_envelope_reset',
        midi_cc=25,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_key_tracking(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the key tracking amount for the filter.

    Controls how much the filter frequency follows the played note pitch.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Key tracking value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the key tracking for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_key_tracking',
        midi_cc=26,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_base(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the base frequency for the filter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Base frequency value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the base frequency for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_base',
        midi_cc=27,
        midi_channel=midi_channel,
        value=value,
    )


def set_multi_mode_filter_width(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the filter width parameter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Width value ranging from 0 to 127.
            Display range: 0-127.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the width for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_multi_mode_filter_width',
        midi_cc=28,
        midi_channel=midi_channel,
        value=value,
    )
