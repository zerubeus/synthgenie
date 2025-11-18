import logging

import psycopg2
from fastapi import APIRouter, Depends

from synthgenie.auth.services import get_api_key
from synthgenie.db.connection import get_db
from synthgenie.synthesizers.shared.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse
from synthgenie.synthesizers.shared.schemas.user import UserPrompt
from synthgenie.synthesizers.sub37.services import run_sub37_agent_workflow

logger = logging.getLogger(__name__)

router = APIRouter(prefix='/agent/sub37', tags=['synthgenie'])


@router.post(
    '/prompt',
    response_model=list[SynthGenieResponse | SynthGenieAmbiguousResponse],
    response_model_exclude_none=True,
)
async def process_sub37_prompt(
    user_prompt: UserPrompt,
    api_key: str = Depends(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    return await run_sub37_agent_workflow(user_prompt.prompt, api_key, conn)
