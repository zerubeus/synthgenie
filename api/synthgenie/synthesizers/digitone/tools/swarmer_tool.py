import logging

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse

logger = logging.getLogger(__name__)


def set_swarmer_tune(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the master tuning of the Swarmer synthesizer.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI tuning value ranging from 0 to 127.
            - 0 maps to -60
            - 64 maps to 0
            - 127 maps to +60
            Values in between are linearly mapped.
            Display range: -60 to +60.
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the tuning for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_swarmer_tune',
        midi_cc=40,
        midi_channel=midi_channel,
        value=value,
    )


def set_swarmer_swarm(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the swarm amount parameter which controls the density and behavior of the swarming voices.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Swarm amount value ranging from 0 to 127.
            - 0 maps to 0
            - 127 maps to 120
            Display range: 0-120.
            Default is 80.
        midi_channel (int): The MIDI channel (track) to set the swarm amount for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_swarmer_swarm',
        midi_cc=41,
        midi_channel=midi_channel,
        value=value,
    )


def set_swarmer_detune(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the detune amount between the swarming voices.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Detune value ranging from 0 to 127.
            Display range: 0-127.
            Default is 70.
        midi_channel (int): The MIDI channel (track) to set the detune for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_swarmer_detune',
        midi_cc=42,
        midi_channel=midi_channel,
        value=value,
    )


def set_swarmer_mix(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the mix balance between the dry signal and the swarmer effect.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Mix value ranging from 0 to 127.
            Display range: 0-127.
            Default is 127.
        midi_channel (int): The MIDI channel (track) to set the mix for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_swarmer_mix',
        midi_cc=43,
        midi_channel=midi_channel,
        value=value,
    )


def set_swarmer_main_octave(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the main octave offset for the swarmer voices.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Main octave value ranging from 0 to 2.
            - 0 = No octave shift
            - 1 = +1 octave
            - 2 = +2 octaves
            Display range: discrete options (0, 1, 2).
            Default is 0.
        midi_channel (int): The MIDI channel (track) to set the main octave for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_swarmer_main_octave',
        midi_cc=44,
        midi_channel=midi_channel,
        value=value,
    )


def set_swarmer_main(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the main parameter that controls the character of the swarm algorithm.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Main parameter value ranging from 0 to 120.
            Display range: 0-120.
            Default is 80.
        midi_channel (int): The MIDI channel (track) to set the main parameter for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_swarmer_main',
        midi_cc=45,
        midi_channel=midi_channel,
        value=value,
    )


def set_swarmer_animation(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the animation amount which controls the movement and liveliness of the swarm.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Animation value ranging from 0 to 127.
            Display range: 0-127.
            Default is 15.
        midi_channel (int): The MIDI channel (track) to set the animation for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_swarmer_animation',
        midi_cc=46,
        midi_channel=midi_channel,
        value=value,
    )


def set_swarmer_noise_mod(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the noise modulation amount which adds random variation to the swarm.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Noise modulation value ranging from 0 to 127.
            Display range: 0-127.
            Default is 20.
        midi_channel (int): The MIDI channel (track) to set the noise modulation for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_swarmer_noise_mod',
        midi_cc=47,
        midi_channel=midi_channel,
        value=value,
    )
