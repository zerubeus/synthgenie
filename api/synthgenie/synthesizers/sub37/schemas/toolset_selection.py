"""Schema for toolset selection by the tool selector agent."""

from pydantic import BaseModel, Field


class ToolsetSelection(BaseModel):
    """Response from the tool selector agent.

    This schema defines how Agent 1 communicates toolset choices to Agent 2.
    """

    selected_toolsets: list[str] = Field(
        description='List of toolset names that should be loaded for this sound design request',
        examples=[
            ['oscillator', 'filter', 'amplifier'],
            ['oscillator', 'filter', 'modulation'],
            ['arpeggiator', 'oscillator', 'filter'],
        ],
    )

    enhanced_prompt: str | None = Field(
        default=None,
        description="Optional enhanced or clarified version of the user's prompt to help the sound design agent",
    )

    reasoning: str = Field(description='Brief explanation of why these toolsets were selected')

    confidence: float = Field(
        ge=0.0, le=1.0, default=0.8, description='Confidence level in the toolset selection (0.0 to 1.0)'
    )


# Valid toolset names that can be selected
VALID_TOOLSETS = {
    'oscillator',  # 34 tools - waveforms, pitch, noise, sub-oscillator
    'filter',  # 36 tools - cutoff, resonance, envelope, drive
    'amplifier',  # 10 tools - volume envelope ADSR
    'modulation',  # 56 tools - LFOs, mod wheel, routing
    'arpeggiator',  # 14 tools - patterns, timing, sequences
    'effects',  # 11 tools - volume, pitch bend, global settings
    'glide',  # 10 tools - portamento and pitch transitions
}


def validate_toolset_selection(selection: ToolsetSelection) -> bool:
    """Validate that all selected toolsets are valid.

    Args:
        selection: The toolset selection to validate

    Returns:
        True if all toolsets are valid, False otherwise
    """
    return all(toolset in VALID_TOOLSETS for toolset in selection.selected_toolsets)
