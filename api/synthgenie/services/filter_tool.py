from pydantic_ai import RunContext
from synthgenie.services.synth_controller import SynthControllerDeps
from synthgenie.schemas.agent import SynthGenieResponse

import logging

logger = logging.getLogger(__name__)


# Multi-Mode Filter functions
def set_multi_mode_filter_attack(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the attack time of the multi-mode filter envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Attack time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the filter attack for. 1-16
    """
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "ATK", value, track, "set_multi_mode_filter_attack"
    )


def set_multi_mode_filter_decay(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the decay time of the multi-mode filter envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Decay time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 64.
        track (int): The track number to set the filter decay for. 1-16
    """
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "DEC", value, track, "set_multi_mode_filter_decay"
    )


def set_multi_mode_filter_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the sustain level of the multi-mode filter envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Sustain level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the filter sustain for. 1-16
    """
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "SUS", value, track, "set_multi_mode_filter_sustain"
    )


def set_multi_mode_filter_release(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the release time of the multi-mode filter envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Release time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 64.
        track (int): The track number to set the filter release for. 1-16
    """
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "REL", value, track, "set_multi_mode_filter_release"
    )


def set_multi_mode_filter_frequency(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the cutoff frequency of the multi-mode filter.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Cutoff frequency value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        track (int): The track number to set the filter frequency for. 1-16
    """
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "FREQ", value, track, "set_multi_mode_filter_frequency"
    )


def set_multi_mode_filter_resonance(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the resonance of the multi-mode filter.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Resonance value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the filter resonance for. 1-16
    """
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "RESO", value, track, "set_multi_mode_filter_resonance"
    )


def set_multi_mode_filter_type(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the type of the multi-mode filter.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Filter type value ranging from 0 to 127.
            - 0   = Lowpass
            - 64  = EQ
            - 127 = Highpass
            Values between these points represent transitions between filter types.
            Display range: continuous.
            Default is 0 (Lowpass).
        track (int): The track number to set the filter type for. 1-16
    """
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "TYPE", value, track, "set_multi_mode_filter_type"
    )


def set_multi_mode_filter_envelope_depth(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the envelope depth of the multi-mode filter.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Envelope depth value ranging from 0 to 127.
            - 0 maps to -64
            - 64 maps to 0
            - 127 maps to +64
            Values in between are linearly mapped.
            Display range: -64 to +64.
            Default is 0.
        track (int): The track number to set the filter envelope depth for. 1-16
    """
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "ENV.Depth", value, track, "set_multi_mode_filter_envelope_depth"
    )
