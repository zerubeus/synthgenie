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


def set_osc2_offset(self, value: int) -> bool:
    """Set the offset of oscillator two."""
    return self.set_parameter("page_2", "OFS2", value)


def set_osc2_table(self, value: int) -> bool:
    """Set the table of oscillator two."""
    return self.set_parameter("page_2", "TBL2", value)


# Modulation methods
def set_mod_type(self, value: int) -> bool:
    """Set the modulation type."""
    return self.set_parameter("page_2", "MOD", value)


def set_reset_mode(self, value: int) -> bool:
    """Set the reset mode."""
    return self.set_parameter("page_2", "RSET", value)


def set_drift(self, value: int) -> bool:
    """Set the drift amount."""
    return self.set_parameter("page_2", "DRIF", value)


# Envelope methods
def set_attack(self, value: int) -> bool:
    """Set the attack time."""
    return self.set_parameter("page_3", "ATK", value)


def set_hold(self, value: int) -> bool:
    """Set the hold time."""
    return self.set_parameter("page_3", "HOLD", value)


def set_decay(self, value: int) -> bool:
    """Set the decay time."""
    return self.set_parameter("page_3", "DEC", value)


def set_noise_level(self, value: int) -> bool:
    """Set the noise level."""
    return self.set_parameter("page_3", "NLEV", value)


# Noise methods
def set_noise_base(self, value: int) -> bool:
    """Set the noise base frequency."""
    return self.set_parameter("page_3", "BASE", value)


def set_noise_width(self, value: int) -> bool:
    """Set the noise width."""
    return self.set_parameter("page_3", "WDTH", value)


def set_noise_type(self, value: int) -> bool:
    """Set the noise type."""
    return self.set_parameter("page_3", "TYPE", value)


def set_noise_character(self, value: int) -> bool:
    """Set the noise character."""
    return self.set_parameter("page_3", "CHAR", value)
