"""
AMP Envelope tools for controlling AMP EG parameters on the Moog Sub 37.
"""

from pydantic_ai import RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieResponse


def set_amp_eg_attack_time(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the AMP EG Attack Time. This is a high-resolution parameter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for AMP EG Attack Time (0-16383).
                     The value will be mapped appropriately for MIDI transmission.
        midi_channel (int): MIDI channel (default is 3 if not specified).
    """
    return SynthGenieResponse(
        used_tool='set_amp_eg_attack_time',
        midi_cc=28,
        midi_channel=midi_channel,
        value=value,
        midi_cc_lsb=60,  # LSB for Attack Time
    )


def set_amp_eg_decay_time(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the AMP EG Decay Time. This is a high-resolution parameter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for AMP EG Decay Time (0-16383).
                     The value will be mapped appropriately for MIDI transmission.
        midi_channel (int): MIDI channel (default is 3 if not specified).
    """
    return SynthGenieResponse(
        used_tool='set_amp_eg_decay_time',
        midi_cc=29,
        midi_channel=midi_channel,
        value=value,
        midi_cc_lsb=61,  # LSB for Decay Time
    )


def set_amp_eg_sustain_time(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the AMP EG Sustain Level. This is a high-resolution parameter.
    Note: Despite the name 'Sustain Time', MIDI CC 30/62 controls Sustain Level on the Sub37.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for AMP EG Sustain Level (0-16383).
                     The value will be mapped appropriately for MIDI transmission.
        midi_channel (int): MIDI channel (default is 3 if not specified).
    """
    return SynthGenieResponse(
        used_tool='set_amp_eg_sustain_level',  # Renamed tool for clarity
        midi_cc=30,
        midi_channel=midi_channel,
        value=value,
        midi_cc_lsb=62,  # LSB for Sustain Level
    )


def set_amp_eg_release_time(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the AMP EG Release Time. This is a high-resolution parameter.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): High-resolution value for AMP EG Release Time (0-16383).
                     The value will be mapped appropriately for MIDI transmission.
        midi_channel (int): MIDI channel (default is 3 if not specified).
    """
    return SynthGenieResponse(
        used_tool='set_amp_eg_release_time',
        midi_cc=31,
        midi_channel=midi_channel,
        value=value,
        midi_cc_lsb=63,  # LSB for Release Time
    )


def set_amp_eg_hold(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the AMP EG Hold.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for AMP EG Hold (0-127).
        midi_channel (int): MIDI channel (default is 3 if not specified).
    """
    return SynthGenieResponse(
        used_tool='set_amp_eg_hold',
        midi_cc=106,
        midi_channel=midi_channel,
        value=value,
        midi_cc_lsb=None,  # Standard CC
    )


def set_amp_eg_multi_trig(ctx: RunContext, value: int, midi_channel: int = 3) -> SynthGenieResponse:
    """
    Set the AMP EG Multi Trigger.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): Value for AMP EG Multi Trigger (0 = OFF, 64 = ON).
                     Ensure the value is either 0 or 64.
        midi_channel (int): MIDI channel (default is 3 if not specified).
    """
    return SynthGenieResponse(
        used_tool='set_amp_eg_multi_trig',
        midi_cc=113,
        midi_channel=midi_channel,
        value=value,
        midi_cc_lsb=None,  # Standard CC
    )
