from pydantic_ai import RunContext
from services.synth_controller import SynthControllerDeps

import logging

logger = logging.getLogger(__name__)


# Multi-Mode Filter functions
def set_multi_mode_filter_attack(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the attack time of the filter envelope."""
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_multi_mode_filter_decay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the decay time of the filter envelope."""
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_multi_mode_filter_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the sustain level of the filter envelope."""
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_multi_mode_filter_release(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the release time of the filter envelope."""
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_multi_mode_filter_frequency(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the cutoff frequency of the filter."""
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_multi_mode_filter_resonance(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the resonance of the filter."""
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "RESO", value, midi_channel
    )


def set_multi_mode_filter_type(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the filter type."""
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "TYPE", value, midi_channel
    )


def set_multi_mode_filter_envelope_depth(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return ctx.deps.filter_multi_mode_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Lowpass 4 Filter functions
def set_lowpass4_filter_attack(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the attack time of the filter envelope."""
    return ctx.deps.filter_lowpass4_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_lowpass4_filter_decay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the decay time of the filter envelope."""
    return ctx.deps.filter_lowpass4_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_lowpass4_filter_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the sustain level of the filter envelope."""
    return ctx.deps.filter_lowpass4_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_lowpass4_filter_release(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the release time of the filter envelope."""
    return ctx.deps.filter_lowpass4_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_lowpass4_filter_frequency(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the cutoff frequency of the filter."""
    return ctx.deps.filter_lowpass4_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_lowpass4_filter_resonance(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the resonance of the filter."""
    return ctx.deps.filter_lowpass4_synth_controller.get_direct_parameter(
        "RESO", value, midi_channel
    )


def set_lowpass4_filter_envelope_depth(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return ctx.deps.filter_lowpass4_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Equalizer Filter functions
def set_equalizer_filter_attack(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the attack time of the filter envelope."""
    return ctx.deps.filter_equalizer_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_equalizer_filter_decay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the decay time of the filter envelope."""
    return ctx.deps.filter_equalizer_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_equalizer_filter_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the sustain level of the filter envelope."""
    return ctx.deps.filter_equalizer_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_equalizer_filter_release(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the release time of the filter envelope."""
    return ctx.deps.filter_equalizer_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_equalizer_filter_frequency(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the center frequency of the equalizer."""
    return ctx.deps.filter_equalizer_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_equalizer_filter_gain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the gain of the equalizer."""
    return ctx.deps.filter_equalizer_synth_controller.get_direct_parameter(
        "GAIN", value, midi_channel
    )


def set_equalizer_filter_q(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the Q factor (bandwidth) of the equalizer."""
    return ctx.deps.filter_equalizer_synth_controller.get_direct_parameter(
        "Q", value, midi_channel
    )


def set_equalizer_filter_envelope_depth(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the envelope depth (how much the envelope affects the center frequency)."""
    return ctx.deps.filter_equalizer_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Base-Width Filter functions
def set_base_width_filter_envelope_delay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the envelope delay."""
    return ctx.deps.filter_base_width_synth_controller.get_direct_parameter(
        "ENV.Delay", value, midi_channel
    )


def set_base_width_filter_key_tracking(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the key tracking amount."""
    return ctx.deps.filter_base_width_synth_controller.get_direct_parameter(
        "KEY.Tracking", value, midi_channel
    )


def set_base_width_filter_base(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the base frequency."""
    return ctx.deps.filter_base_width_synth_controller.get_direct_parameter(
        "BASE", value, midi_channel
    )


def set_base_width_filter_width(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the width."""
    return ctx.deps.filter_base_width_synth_controller.get_direct_parameter(
        "WDTH", value, midi_channel
    )


def set_base_width_filter_envelope_reset(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the envelope reset mode (0=off, 1=on)."""
    return ctx.deps.filter_base_width_synth_controller.get_direct_parameter(
        "Env Reset", value, midi_channel
    )


# Legacy LP/HP Filter functions
def set_legacy_lp_hp_filter_attack(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the attack time of the filter envelope."""
    return ctx.deps.filter_legacy_lp_hp_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_legacy_lp_hp_filter_decay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the decay time of the filter envelope."""
    return ctx.deps.filter_legacy_lp_hp_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_legacy_lp_hp_filter_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the sustain level of the filter envelope."""
    return ctx.deps.filter_legacy_lp_hp_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_legacy_lp_hp_filter_release(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the release time of the filter envelope."""
    return ctx.deps.filter_legacy_lp_hp_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_legacy_lp_hp_filter_frequency(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the cutoff frequency of the filter."""
    return ctx.deps.filter_legacy_lp_hp_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_legacy_lp_hp_filter_resonance(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the resonance of the filter."""
    return ctx.deps.filter_legacy_lp_hp_synth_controller.get_direct_parameter(
        "RESO", value, midi_channel
    )


def set_legacy_lp_hp_filter_type(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the filter type (0=lowpass, 1=highpass, 2=off)."""
    return ctx.deps.filter_legacy_lp_hp_synth_controller.get_direct_parameter(
        "TYPE(lowpass/highpass)", value, midi_channel
    )


def set_legacy_lp_hp_filter_envelope_depth(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return ctx.deps.filter_legacy_lp_hp_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Comb- Filter functions
def set_comb_minus_filter_attack(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the attack time of the filter envelope."""
    return ctx.deps.filter_comb_minus_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_comb_minus_filter_decay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the decay time of the filter envelope."""
    return ctx.deps.filter_comb_minus_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_comb_minus_filter_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the sustain level of the filter envelope."""
    return ctx.deps.filter_comb_minus_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_comb_minus_filter_release(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the release time of the filter envelope."""
    return ctx.deps.filter_comb_minus_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_comb_minus_filter_frequency(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the frequency of the comb filter."""
    return ctx.deps.filter_comb_minus_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_comb_minus_filter_feedback(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the feedback amount of the comb filter."""
    return ctx.deps.filter_comb_minus_synth_controller.get_direct_parameter(
        "FDBK", value, midi_channel
    )


def set_comb_minus_filter_lowpass(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the lowpass filter amount in the feedback path."""
    return ctx.deps.filter_comb_minus_synth_controller.get_direct_parameter(
        "LPF", value, midi_channel
    )


def set_comb_minus_filter_envelope_depth(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the envelope depth (how much the envelope affects the frequency)."""
    return ctx.deps.filter_comb_minus_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Comb+ Filter functions
def set_comb_plus_filter_attack(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the attack time of the filter envelope."""
    return ctx.deps.filter_comb_plus_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_comb_plus_filter_decay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the decay time of the filter envelope."""
    return ctx.deps.filter_comb_plus_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_comb_plus_filter_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the sustain level of the filter envelope."""
    return ctx.deps.filter_comb_plus_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_comb_plus_filter_release(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the release time of the filter envelope."""
    return ctx.deps.filter_comb_plus_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_comb_plus_filter_frequency(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the frequency of the comb filter."""
    return ctx.deps.filter_comb_plus_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_comb_plus_filter_feedback(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the feedback amount of the comb filter."""
    return ctx.deps.filter_comb_plus_synth_controller.get_direct_parameter(
        "FDBK", value, midi_channel
    )


def set_comb_plus_filter_lowpass(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the lowpass filter amount in the feedback path."""
    return ctx.deps.filter_comb_plus_synth_controller.get_direct_parameter(
        "LPF", value, midi_channel
    )


def set_comb_plus_filter_envelope_depth(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the envelope depth (how much the envelope affects the frequency)."""
    return ctx.deps.filter_comb_plus_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )
