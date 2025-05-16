Why the current prompt doesn’t trigger tool calls

Problem	Effect
1. No JSON/function schema is exposed to the model (the tools= list just holds Python callables).	The model can only “see” what you pass in the tools argument.  If that argument is a list of plain functions, the OpenAI function-calling interface never learns their name, description, or parameter schema, so it cannot select or populate them.
2. The system prompt never explains how to invoke a tool (required envelope, examples, argument names, ranges).	Even if schemas were present, the model has no instructions on the exact JSON shape it must emit (e.g. {"tool":"set_filter_cutoff","arguments":{"value":90}}).
3. Ambiguous-response format isn’t defined (SynthGenieAmbiguousResponse).	The model can’t fabricate a custom schema it’s never seen.
4. Mixed guidance about “single most impactful parameter” vs. dozens of tools	The model hesitates because it’s punished for calling the “wrong” tool yet isn’t given priorities or examples.
5. output_type=list[...] is irrelevant to the model	That hint is for your own validation layer; the model does not read it.

The model is fine—the prompt and tool spec aren’t.

⸻

Minimal fix list
	1.	Export every tool as an OpenAI-style function descriptor

from openai import OpenAI
from openai import tools  # or your own decorator that yields dicts

@tools.function(
    name="set_filter_cutoff",
    description="Set the low-pass filter cutoff (0-127).",
    parameters={
        "type": "object",
        "properties": { "value": { "type": "integer", "minimum": 0, "maximum": 127 } },
        "required": ["value"]
    }
)
def set_filter_cutoff(value: int): ...


	2.	Rewrite the system prompt so the model knows exactly when and how to call a tool, and what to do when it can’t.

system_prompt = r"""
# SynthGenie - Moog Sub 37 Sound-Design Agent

## Your contract
1. **If the user’s request can be satisfied by one of the tools below, reply ONLY with a JSON object of the form**  
   ```json
   {
     "tool": "<tool_name>",
     "arguments": { ... }
   }

No markdown, no prose.
2. If the request is ambiguous, reply with

{ "type": "ambiguous", "message": "<a clarifying question>" }

	3.	Default MIDI channel 1 unless instructed otherwise.
How to choose a parameter

Sound quality	Main parameter(s)
Dark / mellow	filter_cutoff ↓, resonance ↓
Bright / sharp	filter_cutoff ↑, resonance ↑
Punchy / percussive	amp_eg_attack_time ↓, decay ↓
Shimmer / motion	lfo1_rate ↑, lfo1_dest=filter

Call only ONE tool per user turn.
Tool reference (excerpt)

Tool name	Argument schema	Valid range
set_filter_cutoff	{“value”: int}	0-127
set_filter_resonance	{“value”: int}	0-127
set_amp_eg_attack_time	{“value”: int}	0-127
…		
“””		




	3.	Provide 1-2 concrete examples inside the prompt so the model sees the required JSON:

### Examples
**User**: “Make it darker”
**Assistant**: {"tool":"set_filter_cutoff","arguments":{"value":35}}

**User**: “That’s too dark, open the filter to 80”
**Assistant**: {"tool":"set_filter_cutoff","arguments":{"value":80}}


	4.	Remove output_type from the agent constructor. It doesn’t influence the LLM.

⸻

Result: patched agent factory

def get_sub37_sound_design_agent() -> Agent:
    return Agent(
        model=os.getenv("AGENT_MODEL"),
        tools=[
            set_filter_cutoff,
            set_filter_resonance,
            set_amp_eg_attack_time,
            # ⋯ include the rest, each decorated with @tools.function
        ],
        system_prompt=system_prompt,   # the rewritten prompt shown above
        instrument=True,
    )

With explicit schemas plus clear “when-to-call” and “how-to-format” rules, GPT-4 oℹ will confidently emit tool calls instead of prose.