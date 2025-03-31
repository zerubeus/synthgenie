from pydantic_ai import RunContext
from services.synth_controller import SynthControllerDeps
from typing import Tuple

import logging

logger = logging.getLogger(__name__)


# Oscillator 1 methods
def set_osc1_pitch(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the pitch of oscillator one."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "TUN1", value, midi_channel
    )


def set_osc1_waveform(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the waveform of oscillator one."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "WAV1", value, midi_channel
    )


def set_osc1_phase_distortion(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the phase distortion of oscillator one."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "PD1", value, midi_channel
    )


def set_osc1_level(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the level of oscillator one."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "LEV1", value, midi_channel
    )


def set_osc1_offset(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the offset of oscillator one."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "OFS1", value, midi_channel
    )


def set_osc1_table(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the table of oscillator one."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "TBL1", value, midi_channel
    )


# Oscillator 2 methods
def set_osc2_pitch(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the pitch of oscillator two."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "TUN2", value, midi_channel
    )


def set_osc2_waveform(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the waveform of oscillator two."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "WAV2", value, midi_channel
    )


def set_osc2_phase_distortion(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the phase distortion of oscillator two."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "PD2", value, midi_channel
    )


def set_osc2_level(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the level of oscillator two."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "LEV2", value, midi_channel
    )


def set_osc2_offset(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the offset of oscillator two."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "OFS2", value, midi_channel
    )


def set_osc2_table(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the table of oscillator two."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "TBL2", value, midi_channel
    )


# Modulation methods
def set_mod_type(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the modulation type."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "MOD", value, midi_channel
    )


def set_reset_mode(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the reset mode."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "RSET", value, midi_channel
    )


def set_drift(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the drift amount."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "DRIF", value, midi_channel
    )


# Envelope methods
def set_attack(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the attack time."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "ATK", value, midi_channel
    )


def set_hold(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the hold time."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "HOLD", value, midi_channel
    )


def set_decay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the decay time."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "DEC", value, midi_channel
    )


def set_noise_level(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the noise level."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "NLEV", value, midi_channel
    )


# Noise methods
def set_noise_base(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the noise base frequency."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "BASE", value, midi_channel
    )


def set_noise_width(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the noise width."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "WDTH", value, midi_channel
    )


def set_noise_type(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the noise type."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "TYPE", value, midi_channel
    )


def set_noise_character(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> Tuple[int, int, int]:
    """Set the noise character."""
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "CHAR", value, midi_channel
    )
