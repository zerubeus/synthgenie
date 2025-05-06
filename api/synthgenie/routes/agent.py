import logging

import psycopg2
from fastapi import APIRouter, Depends

from synthgenie.db.connection import get_db
from synthgenie.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse
from synthgenie.schemas.user import UserPrompt
from synthgenie.services.auth import get_api_key
from synthgenie.synthesizers.digitone.agents.agent_workflow import run_digitone_agent_workflow
from synthgenie.synthesizers.sub37.agents.agent_workflow import run_sub37_agent_workflow

logger = logging.getLogger(__name__)

router = APIRouter(prefix='/agent', tags=['synthgenie'])


@router.post('/digitone/prompt', response_model=list[SynthGenieResponse | SynthGenieAmbiguousResponse])
async def process_digitone_prompt(
    user_prompt: UserPrompt,
    api_key: str = Depends(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    """
    Process a user prompt with the SynthGenie AI agent.

    This implementation forces the agent to stop after the first cycle
    of tool execution and collects results via events to prevent loops.

    Requires a valid API key.
    """
    return await run_digitone_agent_workflow(user_prompt.prompt, api_key, conn)


@router.post('/sub37/prompt', response_model=list[SynthGenieResponse | SynthGenieAmbiguousResponse])
async def process_sub37_prompt(
    user_prompt: UserPrompt,
    api_key: str = Depends(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    return await run_sub37_agent_workflow(user_prompt.prompt, api_key, conn)
