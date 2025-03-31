from pydantic_ai import RunContext
from services.synth_controller import SynthControllerDeps

import logging

logger = logging.getLogger(__name__)


# LFO1 Functions
def set_lfo1_speed(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the speed of LFO1.

    Args:
        value (int): Speed value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 48.
        track (int): The track number to set the LFO speed for. 1-16
    """
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "SPD", value, track, "set_lfo1_speed"
    )


def set_lfo1_multiplier(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the multiplier of LFO1.

    Args:
        value (int): Multiplier value ranging from 0 to 11.
            - 0 maps to 1
            - 11 maps to 2000
            Display range: 1-2000.
            Default is 2.
        track (int): The track number to set the LFO multiplier for. 1-16
    """
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "MULT", value, track, "set_lfo1_multiplier"
    )


def set_lfo1_fade(ctx: RunContext[SynthControllerDeps], value: int, track: int) -> bool:
    """
    Set the fade in/out of LFO1.

    Args:
        value (int): Fade value ranging from 0 to 127.
            - 0 maps to -64
            - 64 maps to 0
            - 127 maps to 63
            Display range: -64 to 63.
            Default is 0.
        track (int): The track number to set the LFO fade for. 1-16
    """
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "FADE", value, track, "set_lfo1_fade"
    )


def set_lfo1_destination(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the destination of LFO1.

    Args:
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
        track (int): The track number to set the LFO destination for. 1-16
    """
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "DEST", value, track, "set_lfo1_destination"
    )


def set_lfo1_waveform(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the waveform of LFO1.

    Args:
        value (int): Waveform value ranging from 0 to 6.
            - 0 = "tri"
            - 1 = "sine"
            - 2 = "sqr"
            - 3 = "saw"
            - 4 = "expo"
            - 5 = "ramp"
            - 6 = "rand"
            Default is "sine" (1).
        track (int): The track number to set the LFO waveform for. 1-16
    """
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "WAVE", value, track, "set_lfo1_waveform"
    )


def set_lfo1_start_phase(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the start phase of LFO1.

    Args:
        value (int): Start phase value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
        track (int): The track number to set the LFO start phase for. 1-16
    """
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "SPH", value, track, "set_lfo1_start_phase"
    )


def set_lfo1_trigger_mode(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the trigger mode of LFO1.

    Args:
        value (int): Trigger mode value ranging from 0 to 4.
            - 0 = "free"
            - 1 = "trig"
            - 2 = "hold"
            - 3 = "one"
            - 4 = "half"
            Default is "free" (0).
        track (int): The track number to set the LFO trigger mode for. 1-16
    """
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "MODE", value, track, "set_lfo1_trigger_mode"
    )


def set_lfo1_depth(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the depth of LFO1.

    Args:
        value (int): Depth value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
        track (int): The track number to set the LFO depth for. 1-16
    """
    return ctx.deps.lfo1_synth_controller.get_direct_parameter(
        "DEP", value, track, "set_lfo1_depth"
    )


# LFO2 Functions
def set_lfo2_speed(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the speed of LFO2.

    Args:
        value (int): Speed value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 48.
        track (int): The track number to set the LFO speed for. 1-16
    """
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "SPD", value, track, "set_lfo2_speed"
    )


def set_lfo2_multiplier(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the multiplier of LFO2.

    Args:
        value (int): Multiplier value ranging from 0 to 11.
            - 0 maps to 1
            - 11 maps to 2000
            Display range: 1-2000.
            Default is 2.
        track (int): The track number to set the LFO multiplier for. 1-16
    """
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "MULT", value, track, "set_lfo2_multiplier"
    )


def set_lfo2_fade(ctx: RunContext[SynthControllerDeps], value: int, track: int) -> bool:
    """
    Set the fade in/out of LFO2.

    Args:
        value (int): Fade value ranging from 0 to 127.
            - 0 maps to -64
            - 64 maps to 0
            - 127 maps to 63
            Display range: -64 to 63.
            Default is 0.
        track (int): The track number to set the LFO fade for. 1-16
    """
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "FADE", value, track, "set_lfo2_fade"
    )


def set_lfo2_destination(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the destination of LFO2.

    Args:
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
        track (int): The track number to set the LFO destination for. 1-16
    """
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "DEST", value, track, "set_lfo2_destination"
    )


def set_lfo2_waveform(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the waveform of LFO2.

    Args:
        value (int): Waveform value ranging from 0 to 6.
            - 0 = "tri"
            - 1 = "sine"
            - 2 = "sqr"
            - 3 = "saw"
            - 4 = "expo"
            - 5 = "ramp"
            - 6 = "rand"
            Default is "sine" (1).
        track (int): The track number to set the LFO waveform for. 1-16
    """
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "WAVE", value, track, "set_lfo2_waveform"
    )


def set_lfo2_start_phase(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the start phase of LFO2.

    Args:
        value (int): Start phase value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
        track (int): The track number to set the LFO start phase for. 1-16
    """
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "SPH", value, track, "set_lfo2_start_phase"
    )


def set_lfo2_trigger_mode(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the trigger mode of LFO2.

    Args:
        value (int): Trigger mode value ranging from 0 to 4.
            - 0 = "free"
            - 1 = "trig"
            - 2 = "hold"
            - 3 = "one"
            - 4 = "half"
            Default is "free" (0).
        track (int): The track number to set the LFO trigger mode for. 1-16
    """
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "MODE", value, track, "set_lfo2_trigger_mode"
    )


def set_lfo2_depth(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> bool:
    """
    Set the depth of LFO2.

    Args:
        value (int): Depth value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
        track (int): The track number to set the LFO depth for. 1-16
    """
    return ctx.deps.lfo2_synth_controller.get_direct_parameter(
        "DEP", value, track, "set_lfo2_depth"
    )
