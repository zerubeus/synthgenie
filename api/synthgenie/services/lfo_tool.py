from services.synth_controller import BaseSynthController
from data.digitone_params import digitone_config

import logging

logger = logging.getLogger(__name__)

lfo1_synth_controller = BaseSynthController(digitone_config.lfo.lfo_groups["lfo_1"])

lfo2_synth_controller = BaseSynthController(digitone_config.lfo.lfo_groups["lfo_2"])


# LFO1 Functions
def set_lfo1_speed(value, midi_channel: int) -> bool:
    """Set the speed of LFO1."""
    return lfo1_synth_controller.get_direct_parameter("SPD", value, midi_channel)


def set_lfo1_multiplier(value, midi_channel: int) -> bool:
    """Set the multiplier of LFO1."""
    return lfo1_synth_controller.get_direct_parameter("MULT", value, midi_channel)


def set_lfo1_fade(value, midi_channel: int) -> bool:
    """Set the fade in/out of LFO1."""
    return lfo1_synth_controller.get_direct_parameter("FADE", value, midi_channel)


def set_lfo1_destination(value, midi_channel: int) -> bool:
    """Set the destination of LFO1."""
    return lfo1_synth_controller.get_direct_parameter("DEST", value, midi_channel)


def set_lfo1_waveform(value, midi_channel: int) -> bool:
    """Set the waveform of LFO1."""
    return lfo1_synth_controller.get_direct_parameter("WAVE", value, midi_channel)


def set_lfo1_start_phase(value, midi_channel: int) -> bool:
    """Set the start phase of LFO1."""
    return lfo1_synth_controller.get_direct_parameter("SPH", value, midi_channel)


def set_lfo1_trigger_mode(value, midi_channel: int) -> bool:
    """Set the trigger mode of LFO1."""
    return lfo1_synth_controller.get_direct_parameter("MODE", value, midi_channel)


def set_lfo1_depth(value, midi_channel: int) -> bool:
    """Set the depth of LFO1."""
    return lfo1_synth_controller.get_direct_parameter("DEP", value, midi_channel)


# LFO2 Functions
def set_lfo2_speed(value, midi_channel: int) -> bool:
    """Set the speed of LFO2."""
    return lfo2_synth_controller.get_direct_parameter("SPD", value, midi_channel)


def set_lfo2_multiplier(value, midi_channel: int) -> bool:
    """Set the multiplier of LFO2."""
    return lfo2_synth_controller.get_direct_parameter("MULT", value, midi_channel)


def set_lfo2_fade(value, midi_channel: int) -> bool:
    """Set the fade in/out of LFO2."""
    return lfo2_synth_controller.get_direct_parameter("FADE", value, midi_channel)


def set_lfo2_destination(value, midi_channel: int) -> bool:
    """Set the destination of LFO2."""
    return lfo2_synth_controller.get_direct_parameter("DEST", value, midi_channel)


def set_lfo2_waveform(value, midi_channel: int) -> bool:
    """Set the waveform of LFO2."""
    return lfo2_synth_controller.get_direct_parameter("WAVE", value, midi_channel)


def set_lfo2_start_phase(value, midi_channel: int) -> bool:
    """Set the start phase of LFO2."""
    return lfo2_synth_controller.get_direct_parameter("SPH", value, midi_channel)


def set_lfo2_trigger_mode(value, midi_channel: int) -> bool:
    """Set the trigger mode of LFO2."""
    return lfo2_synth_controller.get_direct_parameter("MODE", value, midi_channel)


def set_lfo2_depth(value, midi_channel: int) -> bool:
    """Set the depth of LFO2."""
    return lfo2_synth_controller.get_direct_parameter("DEP", value, midi_channel)
