"""Amplifier toolset for Moog Sub 37 synthesizer."""

from pydantic_ai.toolsets import FunctionToolset

from synthgenie.synthesizers.sub37.tools.amp_tool import (
    set_amp_eg_attack_time,
    set_amp_eg_decay_time,
    set_amp_eg_delay,
    set_amp_eg_hold,
    set_amp_eg_kb_amt,
    set_amp_eg_multi_trig,
    set_amp_eg_release_time,
    set_amp_eg_reset,
    set_amp_eg_sustain_level,
    set_amp_eg_vel_amt,
)

# Create amplifier toolset with all tools
amplifier_toolset = FunctionToolset(
    tools=[
        set_amp_eg_attack_time,
        set_amp_eg_decay_time,
        set_amp_eg_delay,
        set_amp_eg_hold,
        set_amp_eg_kb_amt,
        set_amp_eg_multi_trig,
        set_amp_eg_release_time,
        set_amp_eg_reset,
        set_amp_eg_sustain_level,
        set_amp_eg_vel_amt,
    ]
)


# Keywords that suggest using amplifier tools
AMPLIFIER_KEYWORDS = {
    'amp',
    'amplifier',
    'amplitude',
    'volume',
    'loudness',
    'envelope',
    'adsr',
    'attack',
    'decay',
    'sustain',
    'release',
    'punch',
    'snap',
    'pluck',
    'fade',
    'quick',
    'slow',
    'sharp',
    'soft',
    'velocity',
    'dynamics',
    'trigger',
    'gate',
    'hold',
    'delay',
    'timing',
    'response',
    'level',
    'gain',
}
