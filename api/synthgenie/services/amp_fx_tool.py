from pydantic_ai import RunContext
from synthgenie.services.synth_controller import SynthControllerDeps
from synthgenie.schemas.agent import SynthGenieResponse


# Amp Functions
def set_amp_attack(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the attack time of the amplitude envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Attack time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 8.
        track (int): The track number to set the amp attack for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "ATK", value, track, "set_amp_attack"
    )


def set_amp_hold(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the hold time of the amplitude envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Hold time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 127.
        track (int): The track number to set the amp hold for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "HOLD", value, track, "set_amp_hold"
    )


def set_amp_decay(
    ctx: RunContext[SynthControllerDeps], value: int, track: int
) -> SynthGenieResponse:
    """
    Set the decay time of the amplitude envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Decay time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 32.
        track (int): The track number to set the amp decay for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "DEC", value, track, "set_amp_decay"
    )


def set_amp_sustain(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the sustain level of the amplitude envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Sustain level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 96.
        track (int): The track number to set the amp sustain for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "SUS", value, midi_channel, "set_amp_sustain"
    )


def set_amp_release(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the release time of the amplitude envelope.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Release time value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 24.
        track (int): The track number to set the amp release for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "REL", value, midi_channel, "set_amp_release"
    )


def set_amp_envelope_reset(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the envelope reset mode.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Envelope reset mode value ranging from 0 to 1.
            - 0 = "off"
            - 1 = "on"
            Display range: discrete options.
            Default is "on" (1).
        track (int): The track number to set the amp envelope reset for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "Env. RSET", value, midi_channel, "set_amp_envelope_reset"
    )


def set_amp_envelope_mode(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the envelope mode.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Envelope mode value ranging from 0 to 1.
            - 0 = "AHD"
            - 1 = "ADSR"
            Display range: discrete options.
            Default is "ADSR" (1).
        track (int): The track number to set the amp envelope mode for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "MODE", value, midi_channel, "set_amp_envelope_mode"
    )


def set_amp_pan(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the stereo panning position.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Pan position value ranging from 0 to 127.
            - 0 maps to -64
            - 64 maps to 0
            - 127 maps to +64
            Values in between are linearly mapped.
            Display range: -64 to +64.
            Default is 0 (center).
        track (int): The track number to set the amp pan for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "PAN", value, midi_channel, "set_amp_pan"
    )


def set_amp_volume(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the overall volume level.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Volume level value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 110.
        track (int): The track number to set the amp volume for. 1-16
    """
    return ctx.deps.amp_synth_controller.get_direct_parameter(
        "VOL", value, midi_channel, "set_amp_volume"
    )


# FX Functions
def set_fx_bit_reduction(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the bit reduction amount.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Bit reduction value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the FX bit reduction for. 1-16
    """
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "BR", value, midi_channel, "set_fx_bit_reduction"
    )


def set_fx_overdrive(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the overdrive amount.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Overdrive value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the FX overdrive for. 1-16
    """
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "OVER", value, midi_channel, "set_fx_overdrive"
    )


def set_fx_sample_rate_reduction(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the sample rate reduction amount.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Sample rate reduction value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the FX sample rate reduction for. 1-16
    """
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "SRR", value, midi_channel, "set_fx_sample_rate_reduction"
    )


def set_fx_sample_rate_routing(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the sample rate reduction routing.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Sample rate routing value ranging from 0 to 1.
            - 0 = "pre"
            - 1 = "post"
            Display range: discrete options.
            Default is "pre" (0).
        track (int): The track number to set the FX sample rate routing for. 1-16
    """
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "SR.RT(pre/post)", value, midi_channel, "set_fx_sample_rate_routing"
    )


def set_fx_overdrive_routing(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the overdrive routing.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Overdrive routing value ranging from 0 to 1.
            - 0 = "pre"
            - 1 = "post"
            Display range: discrete options.
            Default is "pre" (0).
        track (int): The track number to set the FX overdrive routing for. 1-16
    """
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "OD.RT(pre/post)", value, midi_channel, "set_fx_overdrive_routing"
    )


def set_fx_delay(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the delay send amount.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Delay send value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the FX delay for. 1-16
    """
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "DEL", value, midi_channel, "set_fx_delay"
    )


def set_fx_reverb(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the reverb send amount.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Reverb send value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the FX reverb for. 1-16
    """
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "REV", value, midi_channel, "set_fx_reverb"
    )


def set_fx_chorus(
    ctx: RunContext[SynthControllerDeps], value: int, midi_channel: int
) -> SynthGenieResponse:
    """
    Set the chorus send amount.

    Args:
        ctx (RunContext[SynthControllerDeps]): The run context containing dependencies.
        value (int): Chorus send value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 127
            Display range: 0-127.
            Default is 0.
        track (int): The track number to set the FX chorus for. 1-16
    """
    return ctx.deps.fx_synth_controller.get_direct_parameter(
        "CHR", value, midi_channel, "set_fx_chorus"
    )
