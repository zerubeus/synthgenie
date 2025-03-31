from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from synthgenie.schemas.agent import SynthGenieResponse
from synthgenie.services.agent import synthgenie_agent
from synthgenie.services.synth_controller import SynthControllerDeps


class UserPrompt(BaseModel):
    prompt: str


router = APIRouter(prefix="/agent", tags=["synthgenie"])


@router.post("/prompt", response_model=List[SynthGenieResponse])
async def process_prompt(user_prompt: UserPrompt):
    """
    Process a user prompt with the SynthGenie AI agent.

    The agent will interpret the prompt and return a list of synthesizer parameter changes.
    """
    # Create dependencies for the agent
    deps = SynthControllerDeps()

    # Run the agent with the user's prompt
    result = await synthgenie_agent.run(user_prompt.prompt, deps=deps)

    return result.data


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}
