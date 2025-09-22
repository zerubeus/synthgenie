"""Tool selector utilities for Moog Sub 37 sound design agent.

NOTE: Keyword-based analysis has been replaced by the intelligent two-agent system.
This file now only contains utility functions for toolset creation.
"""

from pydantic_ai.toolsets import CombinedToolset

from synthgenie.synthesizers.sub37.toolsets import (
    amplifier_toolset,
    arpeggiator_toolset,
    effects_toolset,
    filter_toolset,
    glide_toolset,
    modulation_toolset,
    oscillator_toolset,
)


def create_dynamic_toolset(selected_toolsets: list[str]) -> CombinedToolset:
    """Create a combined toolset from selected toolset names.

    Args:
        selected_toolsets: List of toolset names to include

    Returns:
        Combined toolset containing only the selected tools
    """
    toolset_map = {
        'oscillator': oscillator_toolset,
        'filter': filter_toolset,
        'amplifier': amplifier_toolset,
        'modulation': modulation_toolset,
        'arpeggiator': arpeggiator_toolset,
        'effects': effects_toolset,
        'glide': glide_toolset,
    }

    # Get the toolsets that were selected
    toolsets_to_combine = [toolset_map[name] for name in selected_toolsets if name in toolset_map]

    # Create combined toolset
    return CombinedToolset(toolsets_to_combine)
