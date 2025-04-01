import logging
from fastapi import APIRouter, HTTPException, Depends
from typing import List

from pydantic_ai import UsageLimitExceeded
from pydantic_ai.usage import UsageLimits

from synthgenie.schemas.user import UserPrompt
from synthgenie.services.agent import synthgenie_agent
from synthgenie.schemas.agent import SynthGenieResponse
from synthgenie.services.synth_controller import SynthControllerDeps
from synthgenie.auth.api_key import get_api_key

# RESPONSE_TOKENS_LIMIT = 500000
# REQUEST_TOKENS_LIMIT = 500000
REQUEST_LIMIT = 64


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/agent", tags=["synthgenie"])


@router.post("/prompt", response_model=List[SynthGenieResponse])
async def process_prompt(user_prompt: UserPrompt, api_key: str = Depends(get_api_key)):
    """
    Process a user prompt with the SynthGenie AI agent.

    The agent will interpret the prompt and return a list of synthesizer parameter changes.

    Requires a valid API key.
    """
    deps = SynthControllerDeps()

    try:
        result = await synthgenie_agent.run(
            user_prompt.prompt,
            deps=deps,
            usage_limits=UsageLimits(
                request_limit=REQUEST_LIMIT,
            ),
        )
        return result.data
    except UsageLimitExceeded as e:
        logger.error(f"Usage limit exceeded: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    status = "ok"
    return {"status": status}
