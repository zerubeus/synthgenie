from services.synth_controller import BaseSynthController
from data.digitone_params import digitone_config

import logging

logger = logging.getLogger(__name__)

filter_multi_mode_synth_controller = BaseSynthController(
    digitone_config.multi_mode_filter.parameters
)

filter_lowpass4_synth_controller = BaseSynthController(
    digitone_config.lowpass_4_filter.parameters
)

equalizer_synth_controller = BaseSynthController(
    digitone_config.equalizer_filter.parameters
)

base_width_synth_controller = BaseSynthController(
    digitone_config.base_width_filter.parameters
)

legacy_lp_hp_synth_controller = BaseSynthController(
    digitone_config.legacy_lp_hp_filter.parameters
)

comb_minus_synth_controller = BaseSynthController(
    digitone_config.comb_minus_filter.parameters
)

comb_plus_synth_controller = BaseSynthController(
    digitone_config.comb_plus_filter.parameters
)


def set_multi_mode_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return filter_multi_mode_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_multi_mode_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return filter_multi_mode_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_multi_mode_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return filter_multi_mode_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_multi_mode_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return filter_multi_mode_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_multi_mode_filter_frequency(value, midi_channel: int) -> bool:
    """Set the cutoff frequency of the filter."""
    return filter_multi_mode_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_multi_mode_filter_resonance(value, midi_channel: int) -> bool:
    """Set the resonance of the filter."""
    return filter_multi_mode_synth_controller.get_direct_parameter(
        "RESO", value, midi_channel
    )


def set_multi_mode_filter_type(value, midi_channel: int) -> bool:
    """Set the filter type."""
    return filter_multi_mode_synth_controller.get_direct_parameter(
        "TYPE", value, midi_channel
    )


def set_multi_mode_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return filter_multi_mode_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Lowpass 4 Filter functions
def set_lowpass4_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return filter_lowpass4_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_lowpass4_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return filter_lowpass4_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_lowpass4_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return filter_lowpass4_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_lowpass4_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return filter_lowpass4_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_lowpass4_filter_frequency(value, midi_channel: int) -> bool:
    """Set the cutoff frequency of the filter."""
    return filter_lowpass4_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_lowpass4_filter_resonance(value, midi_channel: int) -> bool:
    """Set the resonance of the filter."""
    return filter_lowpass4_synth_controller.get_direct_parameter(
        "RESO", value, midi_channel
    )


def set_lowpass4_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return filter_lowpass4_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Equalizer Filter functions
def set_equalizer_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return equalizer_synth_controller.get_direct_parameter("ATK", value, midi_channel)


def set_equalizer_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return equalizer_synth_controller.get_direct_parameter("DEC", value, midi_channel)


def set_equalizer_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return equalizer_synth_controller.get_direct_parameter("SUS", value, midi_channel)


def set_equalizer_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return equalizer_synth_controller.get_direct_parameter("REL", value, midi_channel)


def set_equalizer_filter_frequency(value, midi_channel: int) -> bool:
    """Set the center frequency of the equalizer."""
    return equalizer_synth_controller.get_direct_parameter("FREQ", value, midi_channel)


def set_equalizer_filter_gain(value, midi_channel: int) -> bool:
    """Set the gain of the equalizer."""
    return equalizer_synth_controller.get_direct_parameter("GAIN", value, midi_channel)


def set_equalizer_filter_q(value, midi_channel: int) -> bool:
    """Set the Q factor (bandwidth) of the equalizer."""
    return equalizer_synth_controller.get_direct_parameter("Q", value, midi_channel)


def set_equalizer_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the center frequency)."""
    return equalizer_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Base-Width Filter functions
def set_base_width_filter_envelope_delay(value, midi_channel: int) -> bool:
    """Set the envelope delay."""
    return base_width_synth_controller.get_direct_parameter(
        "ENV.Delay", value, midi_channel
    )


def set_base_width_filter_key_tracking(value, midi_channel: int) -> bool:
    """Set the key tracking amount."""
    return base_width_synth_controller.get_direct_parameter(
        "KEY.Tracking", value, midi_channel
    )


def set_base_width_filter_base(value, midi_channel: int) -> bool:
    """Set the base frequency."""
    return base_width_synth_controller.get_direct_parameter("BASE", value, midi_channel)


def set_base_width_filter_width(value, midi_channel: int) -> bool:
    """Set the width."""
    return base_width_synth_controller.get_direct_parameter("WDTH", value, midi_channel)


def set_base_width_filter_envelope_reset(value, midi_channel: int) -> bool:
    """Set the envelope reset mode (0=off, 1=on)."""
    return base_width_synth_controller.get_direct_parameter(
        "Env Reset", value, midi_channel
    )


# Legacy LP/HP Filter functions
def set_legacy_lp_hp_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return legacy_lp_hp_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_legacy_lp_hp_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return legacy_lp_hp_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_legacy_lp_hp_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return legacy_lp_hp_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_legacy_lp_hp_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return legacy_lp_hp_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_legacy_lp_hp_filter_frequency(value, midi_channel: int) -> bool:
    """Set the cutoff frequency of the filter."""
    return legacy_lp_hp_synth_controller.get_direct_parameter(
        "FREQ", value, midi_channel
    )


def set_legacy_lp_hp_filter_resonance(value, midi_channel: int) -> bool:
    """Set the resonance of the filter."""
    return legacy_lp_hp_synth_controller.get_direct_parameter(
        "RESO", value, midi_channel
    )


def set_legacy_lp_hp_filter_type(value, midi_channel: int) -> bool:
    """Set the filter type (0=lowpass, 1=highpass, 2=off)."""
    return legacy_lp_hp_synth_controller.get_direct_parameter(
        "TYPE(lowpass/highpass)", value, midi_channel
    )


def set_legacy_lp_hp_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return legacy_lp_hp_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Comb- Filter functions
def set_comb_minus_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return comb_minus_synth_controller.get_direct_parameter("ATK", value, midi_channel)


def set_comb_minus_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return comb_minus_synth_controller.get_direct_parameter("DEC", value, midi_channel)


def set_comb_minus_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return comb_minus_synth_controller.get_direct_parameter("SUS", value, midi_channel)


def set_comb_minus_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return comb_minus_synth_controller.get_direct_parameter("REL", value, midi_channel)


def set_comb_minus_filter_frequency(value, midi_channel: int) -> bool:
    """Set the frequency of the comb filter."""
    return comb_minus_synth_controller.get_direct_parameter("FREQ", value, midi_channel)


def set_comb_minus_filter_feedback(value, midi_channel: int) -> bool:
    """Set the feedback amount of the comb filter."""
    return comb_minus_synth_controller.get_direct_parameter("FDBK", value, midi_channel)


def set_comb_minus_filter_lowpass(value, midi_channel: int) -> bool:
    """Set the lowpass filter amount in the feedback path."""
    return comb_minus_synth_controller.get_direct_parameter("LPF", value, midi_channel)


def set_comb_minus_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the frequency)."""
    return comb_minus_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )


# Comb+ Filter functions
def set_comb_plus_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return comb_plus_synth_controller.get_direct_parameter("ATK", value, midi_channel)


def set_comb_plus_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return comb_plus_synth_controller.get_direct_parameter("DEC", value, midi_channel)


def set_comb_plus_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return comb_plus_synth_controller.get_direct_parameter("SUS", value, midi_channel)


def set_comb_plus_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return comb_plus_synth_controller.get_direct_parameter("REL", value, midi_channel)


def set_comb_plus_filter_frequency(value, midi_channel: int) -> bool:
    """Set the frequency of the comb filter."""
    return comb_plus_synth_controller.get_direct_parameter("FREQ", value, midi_channel)


def set_comb_plus_filter_feedback(value, midi_channel: int) -> bool:
    """Set the feedback amount of the comb filter."""
    return comb_plus_synth_controller.get_direct_parameter("FDBK", value, midi_channel)


def set_comb_plus_filter_lowpass(value, midi_channel: int) -> bool:
    """Set the lowpass filter amount in the feedback path."""
    return comb_plus_synth_controller.get_direct_parameter("LPF", value, midi_channel)


def set_comb_plus_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the frequency)."""
    return comb_plus_synth_controller.get_direct_parameter(
        "ENV.Depth", value, midi_channel
    )
