"""Shared utilities, dependencies, and validators for Digitone agents."""

import logging
from dataclasses import dataclass
from typing import Literal

import psycopg2
from pydantic import BaseModel
from pydantic_ai import ModelRetry, RunContext

from synthgenie.synthesizers.shared.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse

logger = logging.getLogger(__name__)

# MIDI Constants
MIDI_7BIT_MAX = 127
MIDI_14BIT_MAX = 16383
MIDI_CHANNEL_MIN = 1
MIDI_CHANNEL_MAX = 16


@dataclass
class DigitoneAgentDeps:
    """Dependencies for Digitone agents."""

    default_midi_channel: int = 1
    api_key: str | None = None
    conn: psycopg2.extensions.connection | None = None
    max_requests: int = 16
    request_timeout: int = 30


class MachineRoutingDecision(BaseModel):
    """Decision made by the router agent about which machine to use."""

    machine: Literal['fm_tone', 'fm_drum', 'wavetone', 'swarmer']
    track: int  # 1-16
    reasoning: str
    original_prompt: str


def validate_synth_response(
    ctx: RunContext[DigitoneAgentDeps], result: list[SynthGenieResponse | SynthGenieAmbiguousResponse]
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    """
    Validate agent output for all Digitone agents.

    Ensures:
    - At least one response is returned
    - All MIDI channel values are between 1-16
    - All parameter values are in valid range (0-127 or 0-16383)
    """
    if not result:
        raise ModelRetry('Agent must return at least one response')

    for response in result:
        if isinstance(response, SynthGenieResponse):
            # Validate MIDI channel
            if not MIDI_CHANNEL_MIN <= response.midi_channel <= MIDI_CHANNEL_MAX:
                raise ModelRetry(
                    f'MIDI channel must be between {MIDI_CHANNEL_MIN}-{MIDI_CHANNEL_MAX}, got {response.midi_channel}'
                )

            # Validate value based on message type
            if response.midi_cc_lsb is not None or response.nrpn_msb is not None:
                # High-resolution (14-bit) parameter
                if not 0 <= response.value <= MIDI_14BIT_MAX:
                    raise ModelRetry(
                        f'High-resolution value must be between 0-{MIDI_14BIT_MAX}, got {response.value}'
                    )
            else:
                # Standard 7-bit parameter
                if not 0 <= response.value <= MIDI_7BIT_MAX:
                    raise ModelRetry(f'Standard value must be between 0-{MIDI_7BIT_MAX}, got {response.value}')

    return result


# Common sound design principles used across all agents
COMMON_SOUND_DESIGN_PRINCIPLES = """
**Sound Design Thinking Framework:**

When analyzing user requests, consider these sonic dimensions:

1. **Pitch/Range**:
   - Bass: Low pitch (-24 to -12 semitones)
   - Lead: Mid-high range (0 to +12 semitones)
   - Pad: Wide range with detuning

2. **Brightness**:
   - Dark: Low filter cutoff (0-40), minimal high frequencies
   - Neutral: Mid filter cutoff (50-80)
   - Bright: High filter cutoff (90-127), rich harmonics

3. **Movement**:
   - Static: No LFO, short envelopes
   - Evolving: LFO modulation, long envelopes
   - Rhythmic: Fast LFO, synced modulation

4. **Transient**:
   - Punchy: Attack 0-5, medium decay
   - Soft: Attack 30-80, slow decay
   - Pluck: Attack 0-3, low sustain (0-20)

5. **Sustain Behavior**:
   - Percussive: Sustain 0-20
   - Sustained: Sustain 80-127
   - Pad: Sustain 100-127 + slow attack/release

6. **Texture**:
   - Clean: Low resonance, no distortion
   - Gritty: High resonance (80-127), overdrive, phase distortion
   - Aggressive: Maximum resonance, high distortion

**Parameter Execution Rules:**
- Use exact values when user specifies (e.g., "filter resonance to 90")
- Apply sound design expertise for general requests (e.g., "make it darker")
- Execute all tool calls in a single, logical sequence
- Set ALL relevant parameters for complete sound design

**MIDI Channel:**
ALL tools require a `midi_channel` parameter. You MUST provide the midi_channel value for every single tool call.
The midi_channel is available in the context as `ctx.deps.default_midi_channel`.
Example tool call pattern:
```
set_wavetone_osc1_pitch(ctx, value=35, midi_channel=ctx.deps.default_midi_channel)
```

**Response Rules:**

**CRITICAL - When to Use Tools:**
When the user requests ANY sound design action (e.g., "design a piano", "create a bass", "make it brighter"), you MUST:
1. Execute the appropriate tool calls to set MIDI parameters
2. Return a list of SynthGenieResponse objects from those tool calls
3. NEVER just describe what you would do - actually DO it by calling tools

**Return SynthGenieAmbiguousResponse ONLY for:**
- Questions about parameters (e.g., "what is the current filter cutoff?")
- Requests for information (e.g., "explain how FM synthesis works")
- Truly vague/impossible requests (e.g., "make it sound good" with no context)

**Example - CORRECT:**
User: "design a piano sound"
→ Agent calls: set_fm_tone_algorithm(...), set_fm_tone_c_ratio(...), set_amp_attack(...), [15-20 tool calls]
→ Returns: [SynthGenieResponse(...), SynthGenieResponse(...), ...]

**Example - WRONG:**
User: "design a piano sound"
→ Agent returns: [SynthGenieAmbiguousResponse("I have designed a piano sound")]
❌ This is WRONG - you must actually call the tools and return SynthGenieResponse objects!
"""
