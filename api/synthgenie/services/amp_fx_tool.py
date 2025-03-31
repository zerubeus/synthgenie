from pydantic_ai import RunContext
from services.synth_controller import SynthControllerDeps


# Amp Functions
def set_amp_attack(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the attack time of the amplitude envelope."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "ATK", value, midi_channel
    )


def set_amp_hold(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the hold time of the amplitude envelope."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "HOLD", value, midi_channel
    )


def set_amp_decay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the decay time of the amplitude envelope."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "DEC", value, midi_channel
    )


def set_amp_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the sustain level of the amplitude envelope."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel
    )


def set_amp_release(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the release time of the amplitude envelope."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "REL", value, midi_channel
    )


def set_amp_envelope_reset(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set envelope reset mode (0=off, 1=on)."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "Env. RSET", value, midi_channel
    )


def set_amp_envelope_mode(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set envelope mode (0=AHD, 1=ADSR)."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "MODE", value, midi_channel
    )


def set_amp_pan(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the stereo panning position (-64 to +64)."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "PAN", value, midi_channel
    )


def set_amp_volume(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the overall volume level (0-127)."""
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "VOL", value, midi_channel
    )


# FX Functions
def set_fx_bit_reduction(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the bit reduction amount (0-127)."""
    return ctx.deps.fx_synth_controller.get_direct_parameter("BR", value, midi_channel)


def set_fx_overdrive(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the overdrive amount (0-127)."""
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "OVER", value, midi_channel
    )


def set_fx_sample_rate_reduction(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the sample rate reduction amount (0-127)."""
    return ctx.deps.fx_synth_controller.get_direct_parameter("SRR", value, midi_channel)


def set_fx_sample_rate_routing(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set sample rate reduction routing (0=pre, 1=post)."""
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "SR.RT(pre/post)", value, midi_channel
    )


def set_fx_overdrive_routing(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set overdrive routing (0=pre, 1=post)."""
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "OD.RT(pre/post)", value, midi_channel
    )


def set_fx_delay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the delay send amount (0-127)."""
    return ctx.deps.fx_synth_controller.get_direct_parameter("DEL", value, midi_channel)


def set_fx_reverb(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the reverb send amount (0-127)."""
    return ctx.deps.fx_synth_controller.get_direct_parameter("REV", value, midi_channel)


def set_fx_chorus(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> bool:
    """Set the chorus send amount (0-127)."""
    return ctx.deps.fx_synth_controller.get_direct_parameter("CHR", value, midi_channel)
