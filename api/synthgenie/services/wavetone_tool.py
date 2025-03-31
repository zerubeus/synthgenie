from synthgenie.schemas.digitone import DigitoneConfig
from synthgenie.services.synth_controller import BaseSynthController


wavetone_pages = DigitoneConfig.wavetone.pages

wavetone_synth_controller = BaseSynthController(wavetone_pages)


# Oscillator 1 methods
def set_osc1_pitch(value: int, midi_channel: int) -> bool:
    """Set the pitch of oscillator one."""
    return wavetone_synth_controller.set_parameter(
        "page_1", "TUN1", value, midi_channel
    )


def set_osc1_waveform(value: int, midi_channel: int) -> bool:
    """Set the waveform of oscillator one."""
    return wavetone_synth_controller.set_parameter(
        "page_1", "WAV1", value, midi_channel
    )


def set_osc1_phase_distortion(value: int, midi_channel: int) -> bool:
    """Set the phase distortion of oscillator one."""
    return wavetone_synth_controller.set_parameter("page_1", "PD1", value, midi_channel)


def set_osc1_level(value: int, midi_channel: int) -> bool:
    """Set the level of oscillator one."""
    return wavetone_synth_controller.set_parameter(
        "page_1", "LEV1", value, midi_channel
    )


def set_osc1_offset(value: int, midi_channel: int) -> bool:
    """Set the offset of oscillator one."""
    return wavetone_synth_controller.set_parameter(
        "page_2", "OFS1", value, midi_channel
    )


def set_osc1_table(value: int, midi_channel: int) -> bool:
    """Set the table of oscillator one."""
    return wavetone_synth_controller.set_parameter(
        "page_2", "TBL1", value, midi_channel
    )


# Oscillator 2 methods
def set_osc2_pitch(value: int, midi_channel: int) -> bool:
    """Set the pitch of oscillator two."""
    return wavetone_synth_controller.set_parameter(
        "page_1", "TUN2", value, midi_channel
    )


def set_osc2_waveform(value: int, midi_channel: int) -> bool:
    """Set the waveform of oscillator two."""
    return wavetone_synth_controller.set_parameter(
        "page_1", "WAV2", value, midi_channel
    )


def set_osc2_phase_distortion(value: int, midi_channel: int) -> bool:
    """Set the phase distortion of oscillator two."""
    return wavetone_synth_controller.set_parameter("page_1", "PD2", value, midi_channel)


def set_osc2_level(value: int, midi_channel: int) -> bool:
    """Set the level of oscillator two."""
    return wavetone_synth_controller.set_parameter(
        "page_1", "LEV2", value, midi_channel
    )


def set_osc2_offset(value: int, midi_channel: int) -> bool:
    """Set the offset of oscillator two."""
    return wavetone_synth_controller.set_parameter(
        "page_2", "OFS2", value, midi_channel
    )


def set_osc2_table(value: int, midi_channel: int) -> bool:
    """Set the table of oscillator two."""
    return wavetone_synth_controller.set_parameter(
        "page_2", "TBL2", value, midi_channel
    )


# Modulation methods
def set_mod_type(value: int, midi_channel: int) -> bool:
    """Set the modulation type."""
    return wavetone_synth_controller.set_parameter("page_2", "MOD", value, midi_channel)


def set_reset_mode(value: int, midi_channel: int) -> bool:
    """Set the reset mode."""
    return wavetone_synth_controller.set_parameter(
        "page_2", "RSET", value, midi_channel
    )


def set_drift(value: int, midi_channel: int) -> bool:
    """Set the drift amount."""
    return wavetone_synth_controller.set_parameter(
        "page_2", "DRIF", value, midi_channel
    )


# Envelope methods
def set_attack(value: int, midi_channel: int) -> bool:
    """Set the attack time."""
    return wavetone_synth_controller.set_parameter("page_3", "ATK", value, midi_channel)


def set_hold(value: int, midi_channel: int) -> bool:
    """Set the hold time."""
    return wavetone_synth_controller.set_parameter(
        "page_3", "HOLD", value, midi_channel
    )


def set_decay(value: int, midi_channel: int) -> bool:
    """Set the decay time."""
    return wavetone_synth_controller.set_parameter("page_3", "DEC", value, midi_channel)


def set_noise_level(value: int, midi_channel: int) -> bool:
    """Set the noise level."""
    return wavetone_synth_controller.set_parameter(
        "page_3", "NLEV", value, midi_channel
    )


# Noise methods
def set_noise_base(value: int, midi_channel: int) -> bool:
    """Set the noise base frequency."""
    return wavetone_synth_controller.set_parameter(
        "page_3", "BASE", value, midi_channel
    )


def set_noise_width(value: int, midi_channel: int) -> bool:
    """Set the noise width."""
    return wavetone_synth_controller.set_parameter(
        "page_3", "WDTH", value, midi_channel
    )


def set_noise_type(value: int, midi_channel: int) -> bool:
    """Set the noise type."""
    return wavetone_synth_controller.set_parameter(
        "page_3", "TYPE", value, midi_channel
    )


def set_noise_character(value: int, midi_channel: int) -> bool:
    """Set the noise character."""
    return wavetone_synth_controller.set_parameter(
        "page_3", "CHAR", value, midi_channel
    )
