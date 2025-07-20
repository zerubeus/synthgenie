import logging

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse

logger = logging.getLogger(__name__)


# LFO1 Functions
def set_lfo1_speed(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the speed of LFO1.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Speed value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 48.
        midi_channel (int): The MIDI channel (track) to set the LFO speed for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_speed',
        midi_cc=102,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo1_multiplier(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the multiplier of LFO1.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Multiplier value ranging from 0 to 11.
            - 0 maps to 1
            - 11 maps to 2000
            Display range: 1-2000.
            Default is 2.
        midi_channel (int): The MIDI channel (track) to set the LFO multiplier for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_multiplier',
        midi_cc=103,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo1_fade(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the fade in/out of LFO1.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Fade value ranging from 0 to 127.
            - 0 maps to -64
            - 64 maps to 0
            - 127 maps to 63
            Display range: -64 to 63.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the LFO fade for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_fade',
        midi_cc=104,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo1_destination(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the destination of LFO1.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Destination value ranging from 0 to 99.
            - 0 = none (default)
            - 25 = wavetone_osc1_pitch
            - 26 = wavetone_osc1_waveform
            - 27 = wavetone_osc1_wavetable
            - 28 = wavetone_osc1_offset
            - 29 = wavetone_osc1_phase_distortion
            - 30 = wavetone_osc1_level
            - 31 = wavetone_osc2_pitch
            - 32 = wavetone_osc2_waveform
            - 33 = wavetone_osc2_wavetable
            - 34 = wavetone_osc2_offset
            - 35 = wavetone_osc2_phase_distortion
            - 36 = wavetone_osc2_level
            - 37 = wavetone_mode
            - 38 = wavetone_drift
            - 39 = wavetone_phase_reset
            - 40 = wavetone_noise_attack
            - 41 = wavetone_noise_hold
            - 42 = wavetone_noise_decay
            - 43 = wavetone_noise_level
            - 44 = wavetone_noise_base
            - 45 = wavetone_noise_width
            - 46 = wavetone_noise_type
            - 47 = wavetone_noise_character
            - 66 = filter_type
            - 67 = filter_freq
            - 69 = filter_envelope_depth
            - 70 = filter_envelope_delay
            - 71 = filter_envelope_attack
            - 72 = filter_envelope_decay
            - 73 = filter_envelope_sustain
            - 74 = filter_envelope_release
            - 75 = filter_reset
            - 76 = filter_base
            - 77 = filter_width
            - 78 = filter_bw_rt
            - 79 = filter_key_track
            - 81 = amp_attack
            - 82 = amp_hold
            - 83 = amp_decay
            - 84 = amp_sustain
            - 85 = amp_release
            - 86 = fx_delay_send
            - 87 = fx_reverb_send
            - 88 = fx_chorus_send
            - 89 = amp_pan
            - 90 = amp_volume
            - 95 = fx_bit_reduction
            - 96 = fx_srr
            - 97 = fx_srr_routing
            - 98 = fx_overdrive
            - 99 = fx_overdrive_routing
        midi_channel (int): The MIDI channel (track) to set the LFO destination for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_destination',
        midi_cc=105,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo1_waveform(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the waveform of LFO1.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Waveform value ranging from 0 to 6.
            - 0 = "tri"
            - 1 = "sine"
            - 2 = "sqr"
            - 3 = "saw"
            - 4 = "expo"
            - 5 = "ramp"
            - 6 = "rand"
            Default is "sine" (1).
        midi_channel (int): The MIDI channel (track) to set the LFO waveform for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_waveform',
        midi_cc=106,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo1_start_phase(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the start phase of LFO1.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Start phase value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
        midi_channel (int): The MIDI channel (track) to set the LFO start phase for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_start_phase',
        midi_cc=107,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo1_trigger_mode(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the trigger mode of LFO1.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Trigger mode value ranging from 0 to 4.
            - 0 = "free"
            - 1 = "trig"
            - 2 = "hold"
            - 3 = "one"
            - 4 = "half"
            Default is "free" (0).
        midi_channel (int): The MIDI channel (track) to set the LFO trigger mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_trigger_mode',
        midi_cc=108,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo1_depth(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the depth of LFO1.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Depth value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
        midi_channel (int): The MIDI channel (track) to set the LFO depth for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo1_depth',
        midi_cc=109,
        midi_channel=midi_channel,
        value=value,
    )


# LFO2 Functions
def set_lfo2_speed(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the speed of LFO2.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Speed value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 48.
        midi_channel (int): The MIDI channel (track) to set the LFO speed for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_speed',
        midi_cc=111,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo2_multiplier(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the multiplier of LFO2.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Multiplier value ranging from 0 to 11.
            - 0 maps to 1
            - 11 maps to 2000
            Display range: 1-2000.
            Default is 2.
        midi_channel (int): The MIDI channel (track) to set the LFO multiplier for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_multiplier',
        midi_cc=112,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo2_fade(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the fade in/out of LFO2.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Fade value ranging from 0 to 127.
            - 0 maps to -64
            - 64 maps to 0
            - 127 maps to 63
            Display range: -64 to 63.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the LFO fade for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_fade',
        midi_cc=113,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo2_destination(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the destination of LFO2.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Destination value ranging from 0 to 99.
            - 0 = none (default)
            - 1 = lfo1_speed
            - 2 = lfo1_multiplier
            - 3 = lfo1_fade
            - 5 = lfo1_wave
            - 6 = lfo1_start_phase
            - 7 = lfo1_mode
            - 8 = lfo1_depth
            - 25 = wavetone_osc1_pitch
            - 26 = wavetone_osc1_waveform
            - 27 = wavetone_osc1_wavetable
            - 28 = wavetone_osc1_offset
            - 29 = wavetone_osc1_phase_distortion
            - 30 = wavetone_osc1_level
            - 31 = wavetone_osc2_pitch
            - 32 = wavetone_osc2_waveform
            - 33 = wavetone_osc2_wavetable
            - 34 = wavetone_osc2_offset
            - 35 = wavetone_osc2_phase_distortion
            - 36 = wavetone_osc2_level
            - 37 = wavetone_mode
            - 38 = wavetone_drift
            - 39 = wavetone_phase_reset
            - 40 = wavetone_noise_attack
            - 41 = wavetone_noise_hold
            - 42 = wavetone_noise_decay
            - 43 = wavetone_noise_level
            - 44 = wavetone_noise_base
            - 45 = wavetone_noise_width
            - 46 = wavetone_noise_type
            - 47 = wavetone_noise_character
            - 66 = filter_type
            - 67 = filter_freq
            - 69 = filter_envelope_depth
            - 70 = filter_envelope_delay
            - 71 = filter_envelope_attack
            - 72 = filter_envelope_decay
            - 73 = filter_envelope_sustain
            - 74 = filter_envelope_release
            - 75 = filter_reset
            - 76 = filter_base
            - 77 = filter_width
            - 78 = filter_bw_rt
            - 79 = filter_key_track
            - 81 = amp_attack
            - 82 = amp_hold
            - 83 = amp_decay
            - 84 = amp_sustain
            - 85 = amp_release
            - 86 = fx_delay_send
            - 87 = fx_reverb_send
            - 88 = fx_chorus_send
            - 89 = amp_pan
            - 90 = amp_volume
            - 95 = fx_bit_reduction
            - 96 = fx_srr
            - 97 = fx_srr_routing
            - 98 = fx_overdrive
            - 99 = fx_overdrive_routing
        midi_channel (int): The MIDI channel (track) to set the LFO destination for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_destination',
        midi_cc=114,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo2_waveform(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the waveform of LFO2.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Waveform value ranging from 0 to 6.
            - 0 = "tri"
            - 1 = "sine"
            - 2 = "sqr"
            - 3 = "saw"
            - 4 = "expo"
            - 5 = "ramp"
            - 6 = "rand"
            Default is "sine" (1).
        midi_channel (int): The MIDI channel (track) to set the LFO waveform for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_waveform',
        midi_cc=115,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo2_start_phase(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the start phase of LFO2.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Start phase value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
        midi_channel (int): The MIDI channel (track) to set the LFO start phase for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_start_phase',
        midi_cc=116,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo2_trigger_mode(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the trigger mode of LFO2.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Trigger mode value ranging from 0 to 4.
            - 0 = "free"
            - 1 = "trig"
            - 2 = "hold"
            - 3 = "one"
            - 4 = "half"
            Default is "free" (0).
        midi_channel (int): The MIDI channel (track) to set the LFO trigger mode for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_trigger_mode',
        midi_cc=117,
        midi_channel=midi_channel,
        value=value,
    )


def set_lfo2_depth(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the depth of LFO2.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Depth value ranging from 0 to 127.
            - 0 maps to -128
            - 127 maps to 128
            Display range: from -128 to +128.
        midi_channel (int): The MIDI channel (track) to set the LFO depth for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_lfo2_depth',
        midi_cc=118,
        midi_channel=midi_channel,
        value=value,
    )
