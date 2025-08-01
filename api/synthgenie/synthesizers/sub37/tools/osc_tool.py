"""
Oscillator tools for controlling oscillator parameters on the Moog Sub 37.
Parameters controlled via High-Resolution CC, standard CC, and NRPN.
"""

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse

# --- OSC 1 Tools ---


def set_osc1_wave_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 1 Waveform (High-Resolution CC 9/41).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for OSC 1 Wave (0-16383).
                     Maps continuously through wave shapes (Tri, Saw, Sq, Pulse).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc1_wave_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=9,
        midi_cc_lsb=41,
    )


def set_osc1_octave_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 1 Octave (NRPN MSB 3, LSB 95).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC 1 Octave (0=16', 1=8', 2=4', 3=2').
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc1_octave_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=95,
    )


def set_osc1_level_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 1 Level (NRPN MSB 3, LSB 105).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC 1 Level (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    # Note: Sub 37 Manual MIDI Spec lists OSC1 Level NRPN Value as 0-1. This seems wrong.
    # Assuming 0-16383 based on other level parameters.
    return SynthGenieResponse(
        used_tool='set_osc1_level_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=105,
    )


def set_osc1_on_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 1 On/Off state (NRPN MSB 3, LSB 106).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC 1 ON (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    # Note: Manual lists NRPN value as 0-20, which seems wrong for an On/Off switch.
    # Assuming 0=OFF, 1=ON like other switches.
    return SynthGenieResponse(
        used_tool='set_osc1_on_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=106,
    )


# --- OSC 2 Tools ---


def set_osc2_freq_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 2 Frequency (Coarse Tune) (High-Resolution CC 12/44).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for OSC 2 Frequency (0-16383).
                     Center=8192 (0 semitones).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc2_freq_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=12,
        midi_cc_lsb=44,
    )


def set_osc2_beat_freq_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 2 Beat Frequency (Fine Tune) (High-Resolution CC 13/45).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for OSC 2 Beat Frequency (0-16383).
                     Center=8192 (0 cents).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc2_beat_freq_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=13,
        midi_cc_lsb=45,
    )


def set_osc2_wave_high_res(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 2 Waveform (High-Resolution CC 14/46).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for OSC 2 Wave (0-16383).
                     Maps continuously through wave shapes (Tri, Saw, Sq, Pulse).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc2_wave_high_res',
        midi_channel=midi_channel,
        value=value,
        midi_cc=14,
        midi_cc_lsb=46,
    )


def set_osc2_octave_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 2 Octave (NRPN MSB 3, LSB 99).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC 2 Octave (0=16', 1=8', 2=4', 3=2').
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc2_octave_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=99,
    )


def set_osc2_hard_sync_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 2 Hard Sync On/Off (NRPN MSB 3, LSB 97).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC 2 Hard Sync (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc2_hard_sync_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=97,
    )


def set_osc2_level_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 2 Level (NRPN MSB 3, LSB 109).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC 2 Level (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc2_level_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=109,
    )


def set_osc2_kb_ctrl_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 2 Keyboard Control On/Off (NRPN MSB 3, LSB 101).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC 2 KB Control (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    # Note: Manual lists values 0-2, but likely 0/1 for On/Off.
    return SynthGenieResponse(
        used_tool='set_osc2_kb_ctrl_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=101,
    )


def set_osc2_on_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the OSC 2 On/Off state (NRPN MSB 3, LSB 110).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC 2 ON (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc2_on_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=110,
    )


# --- Sub Oscillator Tools ---


def set_sub_osc_level_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Sub Oscillator Level (NRPN MSB 3, LSB 108).
    Note: Also controllable via standard CC 115.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Sub Oscillator Level (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_sub_osc_level_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=108,
    )


def set_sub_osc_level_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Sub Oscillator Level (Standard CC 115).
    Alternative to NRPN (3, 108).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Sub Oscillator Level (0-127).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_sub_osc_level_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=115,
    )


def set_sub_osc_on_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Sub Oscillator On/Off state (NRPN MSB 3, LSB 107).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Sub Oscillator ON (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_sub_osc_on_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=107,
    )


# --- Noise/Feedback Tools ---


def set_noise_level_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Noise Level (NRPN MSB 3, LSB 112).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Noise Level (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_noise_level_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=112,
    )


def set_noise_on_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Noise On/Off state (NRPN MSB 3, LSB 111).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Noise ON (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_noise_on_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=111,
    )


def set_feedback_ext_level_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Feedback/External Input Level (NRPN MSB 3, LSB 113).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for Feedback/Ext Level (0-16383).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_feedback_ext_level_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=113,
    )


def set_fb_ext_on_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Feedback/External Input On/Off state (NRPN MSB 3, LSB 114).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for FB/Ext ON (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_fb_ext_on_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=114,
    )


# --- Misc Oscillator Tools ---


def set_osc_kb_reset_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Oscillator Keyboard Reset On/Off (NRPN MSB 3, LSB 98).
    Resets both OSC1 and OSC2 phase on key press.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC KB Reset (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc_kb_reset_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=98,
    )


def set_osc_duo_mode_nrpn(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Oscillator Duo Mode On/Off (NRPN MSB 3, LSB 102).
    Note: Also controllable via standard CC 110.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC Duo Mode (0=OFF, 1=ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    # Note: Manual lists value 0-16383, assuming 0/1 for On/Off.
    return SynthGenieResponse(
        used_tool='set_osc_duo_mode_nrpn',
        midi_channel=midi_channel,
        value=value,
        nrpn_msb=3,
        nrpn_lsb=102,
    )


def set_osc_duo_mode_cc(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the Oscillator Duo Mode On/Off (Standard CC 110).
    Alternative to NRPN (3, 102).

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for OSC Duo Mode (0 = OFF, 127 = ON).
        midi_channel (int): MIDI channel (default is 3).
    """
    return SynthGenieResponse(
        used_tool='set_osc_duo_mode_cc',
        midi_channel=midi_channel,
        value=value,
        midi_cc=110,
    )
