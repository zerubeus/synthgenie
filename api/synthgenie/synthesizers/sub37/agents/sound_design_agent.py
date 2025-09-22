"""Main entry point for Sub 37 sound design - uses intelligent two-agent system."""

from psycopg2.extensions import connection as Connection

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse
from synthgenie.synthesizers.sub37.agents.agent_orchestrator import run_two_agent_sound_design


async def run_sub37_sound_design_agent(
    user_prompt: str, conn: Connection, api_key: str
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    """Run the Sub 37 sound design agent using the intelligent two-agent system.

    This is the main entry point for Sub 37 sound design. It uses an intelligent
    two-agent architecture:

    1. Agent 1 analyzes the user prompt and selects appropriate toolsets
    2. Agent 2 executes sound design with only the selected tools

    This provides better tool selection and 70-80% context reduction compared
    to the original single-agent approach.

    Args:
        user_prompt: The user's sound design request
        conn: Database connection for API tracking
        api_key: API key for usage tracking

    Returns:
        List of SynthGenieResponse or SynthGenieAmbiguousResponse objects
    """
    return await run_two_agent_sound_design(user_prompt, conn, api_key)
