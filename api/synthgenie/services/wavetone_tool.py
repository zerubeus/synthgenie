from pydantic_ai import RunContext
from services.synth_controller import SynthControllerDeps
from typing import Tuple

import logging

logger = logging.getLogger(__name__)


# Oscillator 1 methods
def set_wavetone_osc1_pitch(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the pitch of oscillator one.

    Args:
        value (int): MIDI pitch value ranging from 0 to 127.
            - 0 maps to -5
            - 64 maps to 0
            - 127 maps to +5
            Values in between are linearly mapped.
            Display range: -5 to +5.
            Default is 0.
        track (int): The track number to set the pitch for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "TUN1", value, track, "set_wavetone_osc1_pitch"
    )


def set_wavetone_osc1_waveform(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the waveform of oscillator one for a specific track.

    Args:
        value (int): Waveform value to set, ranging from 0 to 127.
            - 0   = Sine
            - 40  = Triangle
            - 80  = Saw
            - 3   = Square
            Values between these points represent transitions between waveforms.
            (Display range: 0–120)

        track (int): Track number to set the waveform for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "WAV1", value, track, "set_wavetone_osc1_waveform"
    )


def set_wavetone_osc1_phase_distortion(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the phase distortion of oscillator one.

    Args:
        value (int): Phase distortion value ranging from 0 to 127.
            - 0 maps to 0%
            - 64 maps to 50%
            - 127 maps to 100%
            Values in between are linearly mapped.
            Display range: 0-100%.
            Default is 50%.
        track (int): The track number to set the phase distortion for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "PD1", value, track, "set_wavetone_osc1_phase_distortion"
    )


def set_wavetone_osc1_level(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the level of oscillator one.

    Args:
        value (int): Level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 100.
        track (int): The track number to set the level for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "LEV1", value, track, "set_wavetone_osc1_level"
    )


def set_wavetone_osc1_offset(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the offset of oscillator one.

    Args:
        value (int): Offset value ranging from 0 to 127.
            - 0 maps to -10
            - 64 maps to 0
            - 127 maps to +10
            Values in between are linearly mapped.
            Display range: -10 to +10.
            Default is 0.
        track (int): The track number to set the offset for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "OFS1", value, track, "set_wavetone_osc1_offset"
    )


def set_wavetone_osc1_table(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Selects the wavetable for oscillator 1's WAVE parameter. Options include PRIM (basic waves like Sin, Tri, Saw, Square) and HARM (a range of harmonic combinations)

    Args:
        value (int): wavetable value ranging from 0 to 1.
            - 0 = "prim"
            - 1 = "harm"
            Display range: discrete options.
            Default is "prim".
        track (int): The track number to set the wavetable for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "TBL1", value, track, "set_wavetone_osc1_table"
    )


# Oscillator 2 methods
def set_wavetone_osc2_pitch(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the pitch of oscillator two.

    Args:
        value (int): MIDI pitch value ranging from 0 to 127.
            - 0 maps to -5
            - 64 maps to 0
            - 127 maps to +5
            Values in between are linearly mapped.
            Display range: -5 to +5.
            Default is 0.
        track (int): The track number to set the pitch for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "TUN2", value, track, "set_wavetone_osc2_pitch"
    )


def set_wavetone_osc2_waveform(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the waveform of oscillator two.

    Args:
        value (int): Waveform value to set, ranging from 0 to 127.
            - 0   = Sine
            - 40  = Triangle
            - 80  = Saw
            - 3   = Square
            Values between these points represent transitions between waveforms.
            Display range: 0-120.
            Default is 0.
        track (int): The track number to set the waveform for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "WAV2", value, track, "set_wavetone_osc2_waveform"
    )


def set_wavetone_osc2_phase_distortion(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the phase distortion of oscillator two.

    Args:
        value (int): Phase distortion value ranging from 0 to 127.
            - 0 maps to 0%
            - 64 maps to 50%
            - 127 maps to 100%
            Values in between are linearly mapped.
            Display range: 0-100%.
            Default is 50%.
        track (int): The track number to set the phase distortion for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "PD2", value, track, "set_wavetone_osc2_phase_distortion"
    )


def set_wavetone_osc2_level(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the level of oscillator two.

    Args:
        value (int): Level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 100.
        track (int): The track number to set the level for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_1", "LEV2", value, track, "set_wavetone_osc2_level"
    )


def set_wavetone_osc2_offset(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the offset of oscillator two.

    Args:
        value (int): Offset value ranging from 0 to 127.
            - 0 maps to -10
            - 64 maps to 0
            - 127 maps to +10
            Values in between are linearly mapped.
            Display range: -10 to +10.
            Default is 0.
        track (int): The track number to set the offset for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "OFS2", value, track, "set_wavetone_osc2_offset"
    )


def set_wavetone_osc2_table(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Selects the wavetable for oscillator 2's WAVE parameter. Options include PRIM (basic waves like Sin, Tri, Saw, Square) and HARM (a range of harmonic combinations)

    Args:
        value (int): Table value ranging from 0 to 1.
            - 0 = "prim"
            - 1 = "harm"
            Display range: discrete options.
            Default is "prim".
        track (int): The track number to set the table for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "TBL2", value, track, "set_wavetone_osc2_table"
    )


# Modulation methods
def set_wavetone_mod_type(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    MOD Oscillator Modulation selects how the two oscillators interact. The options are OFF, RING MOD (Oscillator 2 modulates Oscillator 1), RING MODE FIXED (Oscillator 2 modulates Oscillator 1, but its pitch doesn't track note values), and HARD SYNC (Oscillator 1's phase resets with each new cycle of Oscillator 2)

    Args:
        value (int): Modulation type value ranging from 0 to 3.
            - 0 = "off"
            - 1 = "ring mod"
            - 2 = "ring mod fixed"
            - 3 = "hard sync"
            Display range: discrete options.
            Default is "off".
        track (int): The track number to set the modulation type for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "MOD", value, track, "set_wavetone_mod_type"
    )


def set_wavetone_reset_mode(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    RSET Oscillator Phase Reset determines if and how the oscillators' wave phases reset when a note is played. Options are OFF (no reset), ON (reset to the start of the waveform), and RAND (reset to a random position)

    Args:
        value (int): Reset mode value ranging from 0 to 2.
            - 0 = "off"
            - 1 = "on"
            - 2 = "random"
            Display range: discrete options.
            Default is "on".
        track (int): The track number to set the reset mode for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "RSET", value, track, "set_wavetone_reset_mode"
    )


def set_wavetone_drift(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the drift amount.

    Args:
        value (int): Drift value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the drift for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_2", "DRIF", value, track, "set_wavetone_drift"
    )


# Envelope methods
def set_wavetone_attack(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the attack time.

    Args:
        value (int): Attack time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the attack for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "ATK", value, track, "set_wavetone_attack"
    )


def set_wavetone_hold(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the hold time.

    Args:
        value (int): Hold time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        track (int): The track number to set the hold for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "HOLD", value, track, "set_wavetone_hold"
    )


def set_wavetone_decay(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the decay time.

    Args:
        value (int): Decay time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        track (int): The track number to set the decay for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "DEC", value, track, "set_wavetone_decay"
    )


def set_wavetone_noise_level(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the noise level.

    Args:
        value (int): Noise level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the noise level for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "NLEV", value, track, "set_wavetone_noise_level"
    )


# Noise methods
def set_wavetone_noise_base(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the noise base frequency.

    Args:
        value (int): Noise base frequency value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the noise base for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "BASE", value, track, "set_wavetone_noise_base"
    )


def set_wavetone_noise_width(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the noise width.

    Args:
        value (int): Noise width value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        track (int): The track number to set the noise width for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "WDTH", value, track, "set_wavetone_noise_width"
    )


def set_wavetone_noise_type(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the noise type.

    Args:
        value (int): Noise type value ranging from 0 to 2.
            - 0 = "grain noise"
            - 1 = "tuned noise"
            - 2 = "sample and hold noise"
            Display range: discrete options.
            Default is "grain noise" (0).
        track (int): The track number to set the noise type for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "TYPE", value, track, "set_wavetone_noise_type"
    )


def set_wavetone_noise_character(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> Tuple[int, int, int]:
    """
    Set the noise character.

    Args:
        value (int): Noise character value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the noise character for. 1-16
    """
    return ctx.deps.wavetone_synth_controller.set_parameter(
        "page_3", "CHAR", value, track, "set_wavetone_noise_character"
    )
