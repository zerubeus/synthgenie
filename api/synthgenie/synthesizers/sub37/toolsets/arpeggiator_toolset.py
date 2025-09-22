"""Arpeggiator toolset for Moog Sub 37 synthesizer."""

from pydantic_ai.toolsets import FunctionToolset

from synthgenie.synthesizers.sub37.tools.arp_tool import (
    set_arp_back_forth,
    set_arp_bf_mode,
    set_arp_clk_div,
    set_arp_gate_len,
    set_arp_invert,
    set_arp_latch,
    set_arp_on_off_cc,
    set_arp_pattern,
    set_arp_range,
    set_arp_rate,
    set_arp_run,
    set_arp_step1_reset,
    set_arp_sync,
    set_arpeggiator_latch_cc,
)

# Create arpeggiator toolset with all tools
arpeggiator_toolset = FunctionToolset(
    tools=[
        set_arp_back_forth,
        set_arp_bf_mode,
        set_arp_clk_div,
        set_arp_gate_len,
        set_arp_invert,
        set_arp_latch,
        set_arp_on_off_cc,
        set_arp_pattern,
        set_arp_range,
        set_arp_rate,
        set_arp_run,
        set_arp_step1_reset,
        set_arp_sync,
        set_arpeggiator_latch_cc,
    ]
)


# Keywords that suggest using arpeggiator tools
ARPEGGIATOR_KEYWORDS = {
    'arp',
    'arpeggiator',
    'arpeggiate',
    'sequence',
    'sequencer',
    'pattern',
    'step',
    'gate',
    'latch',
    'run',
    'sync',
    'clock',
    'division',
    'rate',
    'speed',
    'range',
    'octave',
    'back',
    'forth',
    'ping pong',
    'up',
    'down',
    'invert',
    'reverse',
    'rhythmic',
    'repeating',
    'broken chord',
    'sequence pattern',
    'timing',
}
