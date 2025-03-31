from pydantic_ai import RunContext
from services.synth_controller import SynthControllerDeps

import logging

logger = logging.getLogger(__name__)


# LFO1 Functions
def set_lfo1_speed(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the speed of LFO1."""
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "SPD", value, midi_channel
    )


def set_lfo1_multiplier(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the multiplier of LFO1."""
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "MULT", value, midi_channel
    )


def set_lfo1_fade(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the fade in/out of LFO1."""
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "FADE", value, midi_channel
    )


def set_lfo1_destination(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the destination of LFO1."""
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "DEST", value, midi_channel
    )


def set_lfo1_waveform(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the waveform of LFO1."""
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "WAVE", value, midi_channel
    )


def set_lfo1_start_phase(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the start phase of LFO1."""
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "SPH", value, midi_channel
    )


def set_lfo1_trigger_mode(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the trigger mode of LFO1."""
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "MODE", value, midi_channel
    )


def set_lfo1_depth(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the depth of LFO1."""
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "DEP", value, midi_channel
    )


# LFO2 Functions
def set_lfo2_speed(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the speed of LFO2."""
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "SPD", value, midi_channel
    )


def set_lfo2_multiplier(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the multiplier of LFO2."""
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "MULT", value, midi_channel
    )


def set_lfo2_fade(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the fade in/out of LFO2."""
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "FADE", value, midi_channel
    )


def set_lfo2_destination(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the destination of LFO2."""
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "DEST", value, midi_channel
    )


def set_lfo2_waveform(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the waveform of LFO2."""
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "WAVE", value, midi_channel
    )


def set_lfo2_start_phase(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the start phase of LFO2."""
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "SPH", value, midi_channel
    )


def set_lfo2_trigger_mode(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the trigger mode of LFO2."""
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "MODE", value, midi_channel
    )


def set_lfo2_depth(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the depth of LFO2."""
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "DEP", value, midi_channel
    )
