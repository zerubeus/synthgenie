from fastapi import APIRouter
from typing import List

from pydantic_ai.usage import UsageLimits

from synthgenie.schemas.user import UserPrompt
from synthgenie.services.agent import synthgenie_agent
from synthgenie.schemas.agent import SynthGenieResponse
from synthgenie.services.synth_controller import SynthControllerDeps


router = APIRouter(prefix="/agent", tags=["synthgenie"])


@router.post("/prompt", response_model=List[SynthGenieResponse])
async def process_prompt(user_prompt: UserPrompt):
    """
    Process a user prompt with the SynthGenie AI agent.

    The agent will interpret the prompt and return a list of synthesizer parameter changes.
    """
    deps = SynthControllerDeps()
    result = await synthgenie_agent.run(user_prompt.prompt, deps=deps, usage_limits=UsageLimits(response_tokens_limit=500000, request_limit=100, request_tokens_limit=500000))
    return result.data


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    status = "ok"
    return {"status": status}
