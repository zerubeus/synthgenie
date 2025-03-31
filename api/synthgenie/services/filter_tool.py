from services.synth_controller import BaseSynthController
from schemas.digitone import digitone_config

import logging

logger = logging.getLogger(__name__)


def set_multi_mode_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return BaseSynthController(
        digitone_config.multi_mode_filter.parameters, midi_channel
    ).get_direct_parameter("ATK", value)


def set_multi_mode_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return BaseSynthController(
        digitone_config.multi_mode_filter.parameters, midi_channel
    ).get_direct_parameter("DEC", value)


def set_multi_mode_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return BaseSynthController(
        digitone_config.multi_mode_filter.parameters, midi_channel
    ).get_direct_parameter("SUS", value)


def set_multi_mode_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return BaseSynthController(
        digitone_config.multi_mode_filter.parameters, midi_channel
    ).get_direct_parameter("REL", value)


def set_multi_mode_filter_frequency(value, midi_channel: int) -> bool:
    """Set the cutoff frequency of the filter."""
    return BaseSynthController(
        digitone_config.multi_mode_filter.parameters, midi_channel
    ).get_direct_parameter("FREQ", value)


def set_multi_mode_filter_resonance(value, midi_channel: int) -> bool:
    """Set the resonance of the filter."""
    return BaseSynthController(
        digitone_config.multi_mode_filter.parameters, midi_channel
    ).get_direct_parameter("RESO", value)


def set_multi_mode_filter_type(value, midi_channel: int) -> bool:
    """Set the filter type."""
    return BaseSynthController(
        digitone_config.multi_mode_filter.parameters, midi_channel
    ).get_direct_parameter("TYPE", value)


def set_multi_mode_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return BaseSynthController(
        digitone_config.multi_mode_filter.parameters, midi_channel
    ).get_direct_parameter("ENV.Depth", value)


# Lowpass 4 Filter functions
def set_lowpass4_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return BaseSynthController(
        digitone_config.lowpass_4_filter.parameters, midi_channel
    ).get_direct_parameter("ATK", value)


def set_lowpass4_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return BaseSynthController(
        digitone_config.lowpass_4_filter.parameters, midi_channel
    ).get_direct_parameter("DEC", value)


def set_lowpass4_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return BaseSynthController(
        digitone_config.lowpass_4_filter.parameters, midi_channel
    ).get_direct_parameter("SUS", value)


def set_lowpass4_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return BaseSynthController(
        digitone_config.lowpass_4_filter.parameters, midi_channel
    ).get_direct_parameter("REL", value)


def set_lowpass4_filter_frequency(value, midi_channel: int) -> bool:
    """Set the cutoff frequency of the filter."""
    return BaseSynthController(
        digitone_config.lowpass_4_filter.parameters, midi_channel
    ).get_direct_parameter("FREQ", value)


def set_lowpass4_filter_resonance(value, midi_channel: int) -> bool:
    """Set the resonance of the filter."""
    return BaseSynthController(
        digitone_config.lowpass_4_filter.parameters, midi_channel
    ).get_direct_parameter("RESO", value)


def set_lowpass4_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return BaseSynthController(
        digitone_config.lowpass_4_filter.parameters, midi_channel
    ).get_direct_parameter("ENV.Depth", value)


# Equalizer Filter functions
def set_equalizer_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return BaseSynthController(
        digitone_config.equalizer_filter.parameters, midi_channel
    ).get_direct_parameter("ATK", value)


def set_equalizer_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return BaseSynthController(
        digitone_config.equalizer_filter.parameters, midi_channel
    ).get_direct_parameter("DEC", value)


def set_equalizer_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return BaseSynthController(
        digitone_config.equalizer_filter.parameters, midi_channel
    ).get_direct_parameter("SUS", value)


def set_equalizer_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return BaseSynthController(
        digitone_config.equalizer_filter.parameters, midi_channel
    ).get_direct_parameter("REL", value)


def set_equalizer_filter_frequency(value, midi_channel: int) -> bool:
    """Set the center frequency of the equalizer."""
    return BaseSynthController(
        digitone_config.equalizer_filter.parameters, midi_channel
    ).get_direct_parameter("FREQ", value)


def set_equalizer_filter_gain(value, midi_channel: int) -> bool:
    """Set the gain of the equalizer."""
    return BaseSynthController(
        digitone_config.equalizer_filter.parameters, midi_channel
    ).get_direct_parameter("GAIN", value)


def set_equalizer_filter_q(value, midi_channel: int) -> bool:
    """Set the Q factor (bandwidth) of the equalizer."""
    return BaseSynthController(
        digitone_config.equalizer_filter.parameters, midi_channel
    ).get_direct_parameter("Q", value)


def set_equalizer_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the center frequency)."""
    return BaseSynthController(
        digitone_config.equalizer_filter.parameters, midi_channel
    ).get_direct_parameter("ENV.Depth", value)


# Base-Width Filter functions
def set_base_width_filter_envelope_delay(value, midi_channel: int) -> bool:
    """Set the envelope delay."""
    return BaseSynthController(
        digitone_config.base_width_filter.parameters, midi_channel
    ).get_direct_parameter("ENV.Delay", value)


def set_base_width_filter_key_tracking(value, midi_channel: int) -> bool:
    """Set the key tracking amount."""
    return BaseSynthController(
        digitone_config.base_width_filter.parameters, midi_channel
    ).get_direct_parameter("KEY.Tracking", value)


def set_base_width_filter_base(value, midi_channel: int) -> bool:
    """Set the base frequency."""
    return BaseSynthController(
        digitone_config.base_width_filter.parameters, midi_channel
    ).get_direct_parameter("BASE", value)


def set_base_width_filter_width(value, midi_channel: int) -> bool:
    """Set the width."""
    return BaseSynthController(
        digitone_config.base_width_filter.parameters, midi_channel
    ).get_direct_parameter("WDTH", value)


def set_base_width_filter_envelope_reset(value, midi_channel: int) -> bool:
    """Set the envelope reset mode (0=off, 1=on)."""
    return BaseSynthController(
        digitone_config.base_width_filter.parameters, midi_channel
    ).get_direct_parameter("Env Reset", value)


# Legacy LP/HP Filter functions
def set_legacy_lp_hp_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return BaseSynthController(
        digitone_config.legacy_lp_hp_filter.parameters, midi_channel
    ).get_direct_parameter("ATK", value)


def set_legacy_lp_hp_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return BaseSynthController(
        digitone_config.legacy_lp_hp_filter.parameters, midi_channel
    ).get_direct_parameter("DEC", value)


def set_legacy_lp_hp_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return BaseSynthController(
        digitone_config.legacy_lp_hp_filter.parameters, midi_channel
    ).get_direct_parameter("SUS", value)


def set_legacy_lp_hp_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return BaseSynthController(
        digitone_config.legacy_lp_hp_filter.parameters, midi_channel
    ).get_direct_parameter("REL", value)


def set_legacy_lp_hp_filter_frequency(value, midi_channel: int) -> bool:
    """Set the cutoff frequency of the filter."""
    return BaseSynthController(
        digitone_config.legacy_lp_hp_filter.parameters, midi_channel
    ).get_direct_parameter("FREQ", value)


def set_legacy_lp_hp_filter_resonance(value, midi_channel: int) -> bool:
    """Set the resonance of the filter."""
    return BaseSynthController(
        digitone_config.legacy_lp_hp_filter.parameters, midi_channel
    ).get_direct_parameter("RESO", value)


def set_legacy_lp_hp_filter_type(value, midi_channel: int) -> bool:
    """Set the filter type (0=lowpass, 1=highpass, 2=off)."""
    return BaseSynthController(
        digitone_config.legacy_lp_hp_filter.parameters, midi_channel
    ).get_direct_parameter("TYPE(lowpass/highpass)", value)


def set_legacy_lp_hp_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
    return BaseSynthController(
        digitone_config.legacy_lp_hp_filter.parameters, midi_channel
    ).get_direct_parameter("ENV.Depth", value)


# Comb- Filter functions
def set_comb_minus_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return BaseSynthController(
        digitone_config.comb_minus_filter.parameters, midi_channel
    ).get_direct_parameter("ATK", value)


def set_comb_minus_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return BaseSynthController(
        digitone_config.comb_minus_filter.parameters, midi_channel
    ).get_direct_parameter("DEC", value)


def set_comb_minus_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return BaseSynthController(
        digitone_config.comb_minus_filter.parameters, midi_channel
    ).get_direct_parameter("SUS", value)


def set_comb_minus_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return BaseSynthController(
        digitone_config.comb_minus_filter.parameters, midi_channel
    ).get_direct_parameter("REL", value)


def set_comb_minus_filter_frequency(value, midi_channel: int) -> bool:
    """Set the frequency of the comb filter."""
    return BaseSynthController(
        digitone_config.comb_minus_filter.parameters, midi_channel
    ).get_direct_parameter("FREQ", value)


def set_comb_minus_filter_feedback(value, midi_channel: int) -> bool:
    """Set the feedback amount of the comb filter."""
    return BaseSynthController(
        digitone_config.comb_minus_filter.parameters, midi_channel
    ).get_direct_parameter("FDBK", value)


def set_comb_minus_filter_lowpass(value, midi_channel: int) -> bool:
    """Set the lowpass filter amount in the feedback path."""
    return BaseSynthController(
        digitone_config.comb_minus_filter.parameters, midi_channel
    ).get_direct_parameter("LPF", value)


def set_comb_minus_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the frequency)."""
    return BaseSynthController(
        digitone_config.comb_minus_filter.parameters, midi_channel
    ).get_direct_parameter("ENV.Depth", value)


# Comb+ Filter functions
def set_comb_plus_filter_attack(value, midi_channel: int) -> bool:
    """Set the attack time of the filter envelope."""
    return BaseSynthController(
        digitone_config.comb_plus_filter.parameters, midi_channel
    ).get_direct_parameter("ATK", value)


def set_comb_plus_filter_decay(value, midi_channel: int) -> bool:
    """Set the decay time of the filter envelope."""
    return BaseSynthController(
        digitone_config.comb_plus_filter.parameters, midi_channel
    ).get_direct_parameter("DEC", value)


def set_comb_plus_filter_sustain(value, midi_channel: int) -> bool:
    """Set the sustain level of the filter envelope."""
    return BaseSynthController(
        digitone_config.comb_plus_filter.parameters, midi_channel
    ).get_direct_parameter("SUS", value)


def set_comb_plus_filter_release(value, midi_channel: int) -> bool:
    """Set the release time of the filter envelope."""
    return BaseSynthController(
        digitone_config.comb_plus_filter.parameters, midi_channel
    ).get_direct_parameter("REL", value)


def set_comb_plus_filter_frequency(value, midi_channel: int) -> bool:
    """Set the frequency of the comb filter."""
    return BaseSynthController(
        digitone_config.comb_plus_filter.parameters, midi_channel
    ).get_direct_parameter("FREQ", value)


def set_comb_plus_filter_feedback(value, midi_channel: int) -> bool:
    """Set the feedback amount of the comb filter."""
    return BaseSynthController(
        digitone_config.comb_plus_filter.parameters, midi_channel
    ).get_direct_parameter("FDBK", value)


def set_comb_plus_filter_lowpass(value, midi_channel: int) -> bool:
    """Set the lowpass filter amount in the feedback path."""
    return BaseSynthController(
        digitone_config.comb_plus_filter.parameters, midi_channel
    ).get_direct_parameter("LPF", value)


def set_comb_plus_filter_envelope_depth(value, midi_channel: int) -> bool:
    """Set the envelope depth (how much the envelope affects the frequency)."""
    return BaseSynthController(
        digitone_config.comb_plus_filter.parameters, midi_channel
    ).get_direct_parameter("ENV.Depth", value)
