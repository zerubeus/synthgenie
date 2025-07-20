import psycopg2
from fastapi import HTTPException

from synthgenie.synthesizers.shared.agents.validation_agent import prompt_validation_agent
from synthgenie.synthesizers.sub37.agents.sound_design_agent import run_sub37_sound_design_agent


async def run_sub37_agent_workflow(user_prompt: str, api_key: str, conn: psycopg2.extensions.connection):
    """
    Process a user prompt with the Sub37 AI agent.

    This implementation forces the agent to stop after the first cycle
    of tool execution and collects results via events to prevent loops.

    Requires a valid API key.
    """

    # Validate the user prompt
    # if not valid, return http 422 Unprocessable Entity error
    is_user_prompt_valid = await prompt_validation_agent(user_prompt)
    if not is_user_prompt_valid:
        raise HTTPException(status_code=422, detail='This prompt is not about sound design.')

    # Run the sound design agent
    return await run_sub37_sound_design_agent(user_prompt, api_key, conn)
