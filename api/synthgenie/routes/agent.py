import logging

import psycopg2
from fastapi import APIRouter, Depends

from synthgenie.db.connection import get_db
from synthgenie.schemas.agent import SynthGenieResponse
from synthgenie.schemas.user import UserPrompt
from synthgenie.services.auth import get_api_key
from synthgenie.synthesizers.digitone.agents.sound_design_agent import run_synthgenie_agent

logger = logging.getLogger(__name__)

router = APIRouter(prefix='/agent', tags=['synthgenie'])


@router.post('/digitone/prompt', response_model=list[SynthGenieResponse])
async def process_digitone_prompt(
    user_prompt: UserPrompt,
    api_key: str = Depends(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
):
    """
    Process a user prompt with the SynthGenie AI agent.

    This implementation forces the agent to stop after the first cycle
    of tool execution and collects results via events to prevent loops.

    Requires a valid API key.
    """
    return await run_synthgenie_agent(user_prompt.prompt, api_key, conn)
