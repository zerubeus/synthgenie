from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from synthgenie.schemas.agent import SynthGenieResponse


class UserPrompt(BaseModel):
    prompt: str


router = APIRouter(prefix="/agent", tags=["synthgenie"])


@router.post("/prompt", response_model=List[SynthGenieResponse])
async def process_prompt(user_prompt: UserPrompt):
    """
    Process a user prompt with the SynthGenie AI agent.

    The agent will interpret the prompt and return a list of synthesizer parameter changes.
    """
    # This is a mock implementation for testing
    # In the real implementation, we would use the Pydantic AI agent to process the prompt
    # and return the appropriate responses

    # Mock response for testing
    mock_responses = [
        SynthGenieResponse(
            used_tool="set_wavetone_osc1_pitch",
            midi_cc=12,  # Example MIDI CC number
            midi_channel=1,  # Track 1
            value=80,  # Example value for +2 pitch
        )
    ]

    return mock_responses


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}
