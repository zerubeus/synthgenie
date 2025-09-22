"""Effects and global controls toolset for Moog Sub 37 synthesizer."""

from pydantic_ai.toolsets import FunctionToolset

from synthgenie.synthesizers.sub37.tools.fx_tool import (
    set_all_notes_off,
    set_bank_select,
    set_bank_select_lsb,
    set_hold_pedal,
    set_kb_ctrl_lo_hi,
    set_kb_octave,
    set_kb_transpose,
    set_local_control,
    set_master_volume_high_res,
    set_pitch_bend_down_amount,
    set_pitch_bend_up_amount,
)

# Create effects toolset with all tools
effects_toolset = FunctionToolset(
    tools=[
        set_all_notes_off,
        set_bank_select,
        set_bank_select_lsb,
        set_hold_pedal,
        set_kb_ctrl_lo_hi,
        set_kb_octave,
        set_kb_transpose,
        set_local_control,
        set_master_volume_high_res,
        set_pitch_bend_down_amount,
        set_pitch_bend_up_amount,
    ]
)


# Keywords that suggest using effects/global tools
EFFECTS_KEYWORDS = {
    'volume',
    'master',
    'loud',
    'quiet',
    'louder',
    'softer',
    'pitch bend',
    'bend',
    'octave',
    'transpose',
    'hold',
    'sustain',
    'pedal',
    'bank',
    'program',
    'preset',
    'patch',
    'global',
    'master volume',
    'level',
    'output',
    'panic',
    'reset',
    'all notes off',
    'local',
    'midi',
    'control',
    'keyboard',
    'kbd',
}
