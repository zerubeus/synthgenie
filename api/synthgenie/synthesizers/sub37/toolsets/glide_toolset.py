"""Glide/portamento toolset for Moog Sub 37 synthesizer."""

from pydantic_ai.toolsets import FunctionToolset

from synthgenie.synthesizers.sub37.tools.glide_tool import (
    set_glide_cc,
    set_glide_dest_osc_cc,
    set_glide_gate_nrpn,
    set_glide_legato_cc,
    set_glide_legato_nrpn,
    set_glide_on_nrpn,
    set_glide_osc_nrpn,
    set_glide_time,
    set_glide_type_cc,
    set_glide_type_nrpn,
)

# Create glide toolset with all tools
glide_toolset = FunctionToolset(
    tools=[
        set_glide_cc,
        set_glide_dest_osc_cc,
        set_glide_gate_nrpn,
        set_glide_legato_cc,
        set_glide_legato_nrpn,
        set_glide_on_nrpn,
        set_glide_osc_nrpn,
        set_glide_time,
        set_glide_type_cc,
        set_glide_type_nrpn,
    ]
)


# Keywords that suggest using glide tools
GLIDE_KEYWORDS = {
    'glide',
    'portamento',
    'slide',
    'smooth',
    'transition',
    'legato',
    'connected',
    'flowing',
    'seamless',
    'bend',
    'pitch slide',
    'note transition',
    'slur',
    'sweep',
    'continuous',
    'time',
    'rate',
    'speed',
    'fast',
    'slow',
    'gate',
}
