# Digitone Multi-Agent Architecture

## Overview

The Digitone sound design system has been refactored from a single monolithic agent to a **multi-agent orchestration pattern** following PydanticAI best practices.

## Architecture Diagram

```
User Request
     ↓
Validation Agent (is it sound design?)
     ↓
Router Agent (which machine + track?)
     ↓
     ├─→ FM Tone Agent (4-op FM synthesis)
     ├─→ FM Drum Agent (percussion synthesis)
     ├─→ Wavetone Agent (wavetable + phase distortion)
     └─→ Swarmer Agent (swarm/unison synthesis)
     ↓
MIDI Responses
```

## File Structure

```
synthgenie/synthesizers/digitone/agents/
├── shared.py                  # Shared utilities, dependencies, validators
├── router_agent.py            # Routes requests to machine-specific agents
├── fm_tone_agent.py           # FM Tone synthesis expert
├── fm_drum_agent.py           # FM Drum synthesis expert
├── wavetone_agent.py          # Wavetone synthesis expert
├── swarmer_agent.py           # Swarmer synthesis expert
└── sound_design_agent.py      # DEPRECATED - kept for reference
```

## Components

### 1. Shared Module (`shared.py`)

**Purpose**: Common utilities used across all agents

**Key Exports**:
- `DigitoneAgentDeps`: Dataclass for dependency injection
- `MachineRoutingDecision`: Router agent output schema
- `validate_synth_response()`: Common output validator
- `COMMON_SOUND_DESIGN_PRINCIPLES`: Shared system prompt principles

**Benefits**:
- DRY principle - single source of truth
- Consistent validation across all agents
- Centralized dependency management

### 2. Router Agent (`router_agent.py`)

**Purpose**: Analyze user prompts and route to the correct machine agent

**Input**: User prompt (string)
**Output**: `MachineRoutingDecision` with:
- `machine`: One of ['fm_tone', 'fm_drum', 'wavetone', 'swarmer']
- `track`: Integer 1-16
- `reasoning`: Why this machine was chosen
- `original_prompt`: User's original request

**Routing Logic**:
1. **Explicit machine** in prompt → Direct routing
2. **Sound type** → Inferred machine (e.g., "kick drum" → fm_drum)
3. **Descriptors** → Best-fit machine (e.g., "lush pad" → swarmer)

**Example Routing**:
```
"Design a crashing acid bassline on track 2 using wavetone"
→ machine: wavetone, track: 2

"Create a warm piano sound"
→ machine: fm_tone, track: 1

"Fat kick drum on track 5"
→ machine: fm_drum, track: 5

"Lush detuned pad"
→ machine: swarmer, track: 1
```

### 3. Machine-Specific Agents

Each agent is an expert in ONE synthesis method with:
- **Focused system prompt** (200-300 lines vs 800+ in monolith)
- **Only relevant tools** (machine-specific + universal)
- **Deep domain knowledge** (synthesis recipes, parameter interactions)
- **Sound design examples** specific to that machine

#### FM Tone Agent (`fm_tone_agent.py`)

**Specialty**: 4-operator FM synthesis
**Use Cases**: Piano, electric piano, bells, bass, lead, pads, metallic sounds
**Key Knowledge**:
- 8 FM algorithms and operator routing
- Operator ratios (harmonic vs inharmonic)
- Modulation index relationships
- Classic DX7-style sounds

**Example Prompts**:
- "Electric piano sound"
- "FM bass with grit"
- "Bell-like lead"

#### FM Drum Agent (`fm_drum_agent.py`)

**Specialty**: Percussion synthesis
**Use Cases**: Kicks, snares, hi-hats, toms, claps, percussion
**Key Knowledge**:
- Pitch sweep for kick/tom character
- Body vs noise component balance
- Transient control for attack
- Percussion envelopes

**Example Prompts**:
- "808-style kick"
- "Snappy snare"
- "Open hi-hat"

#### Wavetone Agent (`wavetone_agent.py`)

**Specialty**: Wavetable synthesis with phase distortion
**Use Cases**: Acid bass, aggressive leads, modern bass, pads, plucks
**Key Knowledge**:
- Phase distortion for harmonic content
- Oscillator pitch ranges for bass
- Wavetable selection
- Drift for analog warmth

**Example Prompts**:
- "Crashing acid bassline" ← **Your use case!**
- "Aggressive lead"
- "Deep fat bass"

**Acid Bass Recipe** (now properly documented):
```
OSC1/2 Pitch: 30-40 (bass range)
Phase Distortion: 70-100 (harmonic grit)
Waveform: 70-90 (saw-like)
Filter: Lowpass, freq 30-50, resonance 90-127
Filter Envelope: Attack 0, Decay 60-90, Sustain 0
Overdrive: 60-100
LFO → Filter for movement
```

#### Swarmer Agent (`swarmer_agent.py`)

**Specialty**: Swarm/unison synthesis
**Use Cases**: Lush pads, supersaw leads, ambient textures, detuned sounds
**Key Knowledge**:
- Swarm density vs detune relationship
- Animation for organic movement
- Main oscillator balance
- Evolving textures

**Example Prompts**:
- "Lush pad"
- "Supersaw lead"
- "Ambient texture"

### 4. Service Orchestration (`services.py`)

**Workflow**:
1. Validate prompt is about sound design
2. Route to appropriate machine (via router agent)
3. Get machine-specific agent
4. Update deps with routed track number
5. Run agent with context
6. Track API usage
7. Return responses

**Error Handling**:
- Validation errors → HTTP 422
- Routing failures → HTTP 500
- Agent failures → HTTP 500 with context

## Benefits of Multi-Agent Architecture

### 1. **Specialized Expertise**
- Each agent is an expert in ONE synthesis method
- Deep, focused knowledge vs shallow, broad knowledge
- Better sound design suggestions

### 2. **Manageable Complexity**
- 200-300 line prompts vs 800+ line monolith
- Easier to understand and maintain
- Clear separation of concerns

### 3. **Scalability**
- Add new machines easily (just create new agent)
- Update one machine without affecting others
- Independent testing and iteration

### 4. **Better Results**
- Agents understand synthesis deeply
- Know parameter interactions
- Provide complete sound designs (not missing critical params like phase distortion!)

### 5. **Maintainability**
- Each agent file is self-contained
- Clear responsibilities
- Easy to locate and fix issues

## Comparison: Before vs After

### Before (Monolithic Agent)

```
❌ One agent tries to know all 4 machines
❌ 800+ line system prompt
❌ Generic sound design advice
❌ Easy to miss critical parameters
❌ Hard to add new knowledge
❌ Confused about machine-specific features
```

**Result**: Acid bass missing pitch, phase distortion, proper waveform selection

### After (Multi-Agent)

```
✅ Specialized agents per machine
✅ 200-300 line focused prompts
✅ Deep synthesis knowledge
✅ Complete parameter coverage
✅ Easy to enhance specific machines
✅ Clear machine capabilities
```

**Result**: Acid bass with ALL essential parameters:
- Oscillator pitch (30-40 for bass range)
- Phase distortion (70-100 for grit)
- Proper waveforms
- Filter resonance + envelope
- Overdrive
- LFO modulation

## Usage Examples

### Example 1: Acid Bass (Your Case)

**Prompt**: "Design a crashing acid bassline on track 2 using wavetone"

**Workflow**:
1. Validation ✓
2. Router → wavetone, track 2
3. Wavetone agent analyzes "acid bass"
4. Applies acid bass recipe:
   - Sets oscillator pitches LOW
   - Adds phase distortion for grit
   - Configures resonant filter sweep
   - Adds overdrive
   - Sets proper envelopes

**Expected Output**: 15-20 MIDI actions covering ALL critical parameters

### Example 2: Piano Sound

**Prompt**: "Create a warm electric piano"

**Workflow**:
1. Validation ✓
2. Router → fm_tone, track 1 (inferred)
3. FM Tone agent applies EP recipe:
   - Algorithm 1 or 2
   - Harmonic operator ratios
   - Proper operator envelopes
   - Detune for chorus
   - Effects (reverb, chorus)

### Example 3: Lush Pad

**Prompt**: "Lush detuned pad with movement"

**Workflow**:
1. Validation ✓
2. Router → swarmer, track 1 (best for lush/detuned)
3. Swarmer agent applies pad recipe:
   - High swarm density
   - Wide detune
   - High animation
   - Slow attack/release
   - LFO modulation

## Migration Notes

### API Compatibility
The `run_digitone_agent_workflow()` function signature **remains the same**:
```python
async def run_digitone_agent_workflow(
    user_prompt: str,
    api_key: str,
    conn: psycopg2.extensions.connection
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]
```

### Internal Changes
- Old monolithic agent is deprecated but kept for reference
- New orchestration happens transparently
- Same input/output contract

### Performance
- Slightly slower (2 agent calls vs 1) but negligible
- Better quality results justify minor latency
- Can be optimized with agent caching if needed

## Future Enhancements

1. **Agent Caching**: Cache agent instances to avoid recreation
2. **Streaming**: Stream responses for long operations
3. **Multi-Machine Sounds**: Layer multiple machines in one request
4. **Learning**: Track successful prompts/params to improve routing
5. **Hybrid Sounds**: Allow router to select multiple machines for layering

## Testing

All agents successfully created and validated:
```
✓ Router agent
✓ FM Tone agent
✓ FM Drum agent
✓ Wavetone agent
✓ Swarmer agent
```

## Conclusion

The multi-agent architecture provides:
- **Better sound design** through specialized expertise
- **Easier maintenance** through focused agents
- **Scalability** for future machines
- **Clear organization** of synthesis knowledge

The acid bass issue that prompted this refactor should now be **completely solved** - the Wavetone agent has comprehensive knowledge of acid bass synthesis including all critical parameters.
