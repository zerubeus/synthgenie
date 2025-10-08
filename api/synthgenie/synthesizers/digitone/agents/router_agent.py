"""Router agent for Digitone sound design - determines which machine-specific agent to use."""

import logging
import os

from fastapi import HTTPException
from pydantic_ai import Agent

from synthgenie.synthesizers.digitone.agents.shared import DigitoneAgentDeps, MachineRoutingDecision

logger = logging.getLogger(__name__)

# Input validation constants
VALID_MACHINES = {'fm_tone', 'fm_drum', 'wavetone', 'swarmer'}
MAX_PROMPT_LENGTH = 2000


def get_router_agent() -> Agent[DigitoneAgentDeps, MachineRoutingDecision]:
    """
    Create the router agent that analyzes user prompts and routes to the correct machine agent.

    Returns:
        Agent configured to return routing decisions
    """
    return Agent(
        model=os.getenv('AGENT_MODEL', 'openai:gpt-4'),
        deps_type=DigitoneAgentDeps,
        output_type=MachineRoutingDecision,
        retries=1,
        system_prompt="""You are a routing specialist for the Elektron Digitone synthesizer.

**Your Role:**
Extract the synthesis machine and track number from the user's prompt. The user MUST specify which machine to use.

**Valid Machines:**
- **fm_tone** (or "FM Tone", "FM TONE", "fmtone")
- **fm_drum** (or "FM Drum", "FM DRUM", "fmdrum")
- **wavetone** (or "Wavetone", "WAVETONE", "wave tone")
- **swarmer** (or "Swarmer", "SWARMER")

**Track Detection:**
- Parse explicit track numbers: "track 2", "on track 5", "channel 3", "track: 2"
- Default to track 1 if not specified
- Track range is 1-16

**Machine Detection (STRICT - User MUST Specify):**
Look for these patterns in the prompt:
- "using [machine]"
- "with [machine]"
- "[machine] machine"
- "on [machine]"
- Machine name anywhere in the prompt

**Examples:**

User: "Design a crashing acid bassline on track 2 using wavetone"
→ machine: wavetone, track: 2, reasoning: "User explicitly specified wavetone machine on track 2"

User: "Create a warm piano sound with FM Tone"
→ machine: fm_tone, track: 1, reasoning: "User specified FM Tone machine, defaulting to track 1"

User: "Make a fat kick drum on track 5 using FM Drum machine"
→ machine: fm_drum, track: 5, reasoning: "User specified FM Drum machine on track 5"

User: "Lush detuned pad with swarmer on track 3"
→ machine: swarmer, track: 3, reasoning: "User specified swarmer machine on track 3"

**CRITICAL:**
The user MUST specify a machine name. If you cannot find a machine name in the prompt, default to "wavetone" but explain in the reasoning that the machine was not specified.

**Output Format:**
Always return a MachineRoutingDecision with:
- `machine`: One of ['fm_tone', 'fm_drum', 'wavetone', 'swarmer']
- `track`: Integer 1-16
- `reasoning`: Brief explanation (mention if machine was not specified by user)
- `original_prompt`: Exact user prompt
""",
    )


async def route_to_machine(user_prompt: str, deps: DigitoneAgentDeps) -> MachineRoutingDecision:
    """
    Route a user prompt to the appropriate machine agent.

    Args:
        user_prompt: The user's sound design request
        deps: Agent dependencies

    Returns:
        MachineRoutingDecision with machine, track, and reasoning

    Raises:
        HTTPException: If prompt exceeds maximum length
    """
    # Input validation
    if len(user_prompt) > MAX_PROMPT_LENGTH:
        raise HTTPException(status_code=400, detail=f'Prompt too long (max {MAX_PROMPT_LENGTH} characters)')

    agent = get_router_agent()
    logger.info(f'Routing prompt: {user_prompt[:100]}...')

    result = await agent.run(user_prompt, deps=deps)
    decision = result.output

    logger.info(f'Routed to {decision.machine} on track {decision.track}. Reasoning: {decision.reasoning}')

    return decision
