import os

import psycopg2
from pydantic_ai import Agent

from synthgenie.models.api_key import track_api_key_usage
from synthgenie.schemas.agent import SynthGenieAmbiguousResponse, SynthGenieResponse
from synthgenie.synthesizers.sub37.tools.amp_tool import (
    set_amp_eg_attack_time,
    set_amp_eg_decay_time,
    set_amp_eg_hold,
    set_amp_eg_multi_trig,
    set_amp_eg_release_time,
    set_amp_eg_sustain_time,
)
from synthgenie.synthesizers.sub37.tools.arp_tool import (
    set_arp_back_forth,
    set_arp_bf_mode,
    set_arp_clk_div,
    set_arp_gate_len,
    set_arp_invert,
    set_arp_latch,
    set_arp_pattern,
    set_arp_range,
    set_arp_rate,
    set_arp_run,
    set_arp_step1_reset,
    set_arp_sync,
)
from synthgenie.synthesizers.sub37.tools.filter_tool import (
    set_amp_eg_delay,
    set_amp_eg_kb_amt,
    set_amp_eg_reset,
    set_amp_eg_vel_amt,
    set_filter_cutoff,
    set_filter_cutoff_nrpn,
    set_filter_drive_nrpn,
    set_filter_eg_amt,
    set_filter_eg_amt_nrpn,
    set_filter_eg_attack_exp_nrpn,
    set_filter_eg_attack_nrpn,
    set_filter_eg_attack_time,
    set_filter_eg_clk_div_nrpn,
    set_filter_eg_decay_nrpn,
    set_filter_eg_decay_time,
    set_filter_eg_delay,
    set_filter_eg_delay_nrpn,
    set_filter_eg_hold_nrpn,
    set_filter_eg_kb_amt,
    set_filter_eg_kb_track_nrpn,
    set_filter_eg_latch_nrpn,
    set_filter_eg_loop_nrpn,
    set_filter_eg_multi_trig_nrpn,
    set_filter_eg_release_nrpn,
    set_filter_eg_release_time,
    set_filter_eg_reset,
    set_filter_eg_reset_nrpn,
    set_filter_eg_sustain_level,
    set_filter_eg_sustain_nrpn,
    set_filter_eg_sync_nrpn,
    set_filter_eg_vel_amt,
    set_filter_eg_vel_amt_nrpn,
    set_filter_kb_amt,
    set_filter_kb_amt_nrpn,
    set_filter_multidrive,
    set_filter_resonance,
    set_filter_resonance_nrpn,
    set_filter_slope_nrpn,
)
from synthgenie.synthesizers.sub37.tools.fx_tool import (
    set_arp_on_off,
    set_arpeggiator_latch,
    set_filter_eg_multi_trig,
    set_glide,
    set_glide_dest_osc,
    set_hold_pedal,
)
from synthgenie.synthesizers.sub37.tools.glide_tool import (
    set_glide_gate_nrpn,
    set_glide_legato_nrpn,
    set_glide_on_nrpn,
    set_glide_osc_nrpn,
    set_glide_time,
    set_glide_type_nrpn,
)
from synthgenie.synthesizers.sub37.tools.lfo_tool import (
    set_lfo1_clk_div_nrpn,
    set_lfo1_clk_src_nrpn,
    set_lfo1_kb_reset_nrpn,
    set_lfo1_kb_track_nrpn,
    set_lfo1_range_nrpn,
    set_lfo1_rate_high_res,
    set_lfo1_sync_nrpn,
    set_lfo2_clk_div_nrpn,
    set_lfo2_clk_src_nrpn,
    set_lfo2_kb_reset_cc,
    set_lfo2_kb_reset_nrpn,
    set_lfo2_kb_track_nrpn,
    set_lfo2_range_cc,
    set_lfo2_range_nrpn,
    set_lfo2_rate_cc,
    set_lfo2_rate_nrpn,
    set_lfo2_sync_nrpn,
    set_mod1_dest_nrpn,
    set_mod1_filter_amt_cc,
    set_mod1_filter_amt_nrpn,
    set_mod1_pgm_amt_nrpn,
    set_mod1_pgm_dest_amt_cc,
    set_mod1_pgm_dest_nrpn,
    set_mod1_pgm_src_nrpn,
    set_mod1_pitch_amt_cc,
    set_mod1_pitch_amt_nrpn,
    set_mod1_pitch_dest_nrpn,
)


def get_sub37_sound_design_agent():
    return Agent(
        model=os.getenv('AGENT_MODEL'),
        tools=[
            set_amp_eg_attack_time,
            set_amp_eg_decay_time,
            set_amp_eg_sustain_time,
            set_amp_eg_release_time,
            set_amp_eg_hold,
            set_amp_eg_multi_trig,
            set_arp_rate,
            set_arp_sync,
            set_arp_range,
            set_arp_back_forth,
            set_arp_bf_mode,
            set_arp_invert,
            set_arp_pattern,
            set_arp_run,
            set_arp_latch,
            set_arp_gate_len,
            set_arp_clk_div,
            set_arp_step1_reset,
            set_filter_multidrive,
            set_filter_cutoff,
            set_filter_resonance,
            set_filter_kb_amt,
            set_filter_eg_attack_time,
            set_filter_eg_decay_time,
            set_filter_eg_sustain_level,
            set_filter_eg_release_time,
            set_filter_eg_amt,
            set_filter_eg_kb_amt,
            set_filter_eg_reset,
            set_filter_eg_vel_amt,
            set_filter_eg_delay,
            set_filter_cutoff_nrpn,
            set_filter_resonance_nrpn,
            set_filter_drive_nrpn,
            set_filter_slope_nrpn,
            set_filter_eg_amt_nrpn,
            set_filter_kb_amt_nrpn,
            set_filter_eg_attack_nrpn,
            set_filter_eg_decay_nrpn,
            set_filter_eg_sustain_nrpn,
            set_filter_eg_release_nrpn,
            set_filter_eg_delay_nrpn,
            set_filter_eg_hold_nrpn,
            set_filter_eg_vel_amt_nrpn,
            set_filter_eg_kb_track_nrpn,
            set_filter_eg_multi_trig_nrpn,
            set_filter_eg_reset_nrpn,
            set_filter_eg_sync_nrpn,
            set_filter_eg_loop_nrpn,
            set_filter_eg_latch_nrpn,
            set_filter_eg_clk_div_nrpn,
            set_filter_eg_attack_exp_nrpn,
            set_amp_eg_kb_amt,
            set_amp_eg_reset,
            set_amp_eg_vel_amt,
            set_amp_eg_delay,
            set_hold_pedal,
            set_glide,
            set_arpeggiator_latch,
            set_arp_on_off,
            set_glide_dest_osc,
            set_filter_eg_multi_trig,
            set_glide_time,
            set_glide_osc_nrpn,
            set_glide_type_nrpn,
            set_glide_gate_nrpn,
            set_glide_legato_nrpn,
            set_glide_on_nrpn,
            set_lfo1_rate_high_res,
            set_lfo1_range_nrpn,
            set_lfo1_sync_nrpn,
            set_lfo1_kb_reset_nrpn,
            set_lfo1_clk_div_nrpn,
            set_lfo1_clk_src_nrpn,
            set_lfo1_kb_track_nrpn,
            set_lfo2_rate_nrpn,
            set_lfo2_range_nrpn,
            set_lfo2_sync_nrpn,
            set_lfo2_kb_reset_nrpn,
            set_lfo2_clk_div_nrpn,
            set_lfo2_clk_src_nrpn,
            set_lfo2_kb_track_nrpn,
            set_lfo2_rate_cc,
            set_lfo2_range_cc,
            set_lfo2_kb_reset_cc,
            set_mod1_pitch_amt_nrpn,
            set_mod1_filter_amt_nrpn,
            set_mod1_pgm_amt_nrpn,
            set_mod1_pgm_src_nrpn,
            set_mod1_dest_nrpn,
            set_mod1_pgm_dest_nrpn,
            set_mod1_pitch_dest_nrpn,
            set_mod1_pitch_amt_cc,
            set_mod1_filter_amt_cc,
            set_mod1_pgm_dest_amt_cc,
        ],
        output_type=list[SynthGenieResponse | SynthGenieAmbiguousResponse],
        instrument=True,
        system_prompt=r"""
        # SynthGenie – Moog Sub 37 Creative Sound-Design Agent
        You are **SynthGenie**, an expert sound designer. Your mission is to creatively translate a user's sound-design request into one **or ideally several** precise MIDI parameter changes on a Moog Sub 37 synthesizer. Aim for a rich, nuanced sound that fully captures the user's intent, even if it requires multiple adjustments across various synth sections.

        ──────────────────────────────────────────────────────────────────────────────
        ## CONTRACT
        1. **If the request can be met with concrete parameter changes**, reply **only** with a JSON **array** whose elements are valid **SynthGenieResponse** objects.
        *If only one change is needed, the array contains one object. If multiple changes are needed for a comprehensive sound, include all necessary objects.*

        ```json
        [
            {
                "used_tool": "<tool_name>",
                "midi_channel": <int>,          // default 1
                "value": <int>,                 // 0-127 (standard CC) or 0-16383 (high-res CC/NRPN)
                "midi_cc": <int|null>,
                "midi_cc_lsb": <int|null>,      // Used for high-resolution CCs
                "nrpn_msb": <int|null>,
                "nrpn_lsb": <int|null>
            }
            // ... potentially more objects for other parameter changes ...
        ]
        ````

        2. **If the request is ambiguous or requires clarification**, reply **only** with a JSON object matching **SynthGenieAmbiguousResponse**:

        ```json
        { "message": "<single, concise clarifying question>" }
        ```

        3. **Produce nothing else**—either the array of parameter changes or the single ambiguity object.

        ──────────────────────────────────────────────────────────────────────────────

        ## PARAMETER-SELECTION GUIDE (Creative Starting Points)

        This guide offers suggestions. Feel free to combine these and other tools creatively. The best sound often comes from adjusting multiple parameters across envelopes, filters, LFOs, and other modules. Don't hesitate to experiment!

        | Desired Sound Quality | Potential Tools & Concepts (explore combinations)                                  |
        | --------------------- | ---------------------------------------------------------------------------------- |
        | Dark / Mellow         | `set_filter_cutoff` (lower), `set_filter_resonance` (adjust to taste)              |
        | Bright / Sharp        | `set_filter_cutoff` (higher), `set_filter_resonance` (adjust), consider EG sharpness |
        | Fat / Warm            | `set_filter_resonance`, `set_filter_multidrive`, oscillator detuning/mix (if tools added) |
        | Punchy / Percussive   | Fast `set_amp_eg_attack_time`, `set_amp_eg_decay_time`. Sharp `set_filter_eg_attack_time`, `set_filter_eg_decay_time` with `set_filter_eg_amt`. |
        | Plucky / Short Decay  | Fast `set_amp_eg_decay_time`, low `set_amp_eg_sustain_time` (level). Similar for filter EG. |
        | Sweeping / Evolving   | `set_filter_eg_attack_time` / `set_filter_eg_decay_time` with `set_filter_eg_amt`, LFO modulation (`set_lfo1_rate_high_res`, `set_mod1_filter_amt_nrpn`, etc.) |
        | Shimmer / Motion      | `set_lfo1_rate_high_res`, `set_lfo1_sync_nrpn`, modulate pitch/filter/amp subtly.      |
        | Rhythmic / Pulsing    | Arpeggiator tools (`set_arp_run`, `set_arp_rate`), LFO sync (`set_lfo1_sync_nrpn`), EG looping (`set_filter_eg_loop_nrpn`). |

        **Tip**: Think holistically. How do the amp envelope, filter envelope, LFOs, and filter settings interact? Use multiple tools to shape the sound intricately.

        ──────────────────────────────────────────────────────────────────────────────

        ## RULES & BEST PRACTICES

        *   **Embrace Creativity**: Strive for the most fitting and creative sound. This often involves multiple parameter changes. Don't limit yourself to only one or two adjustments if more are needed to fully realize the user's request.
        *   **Tool Usage**: You can call multiple different tools in a single response. Call each specific tool function at most once per turn.
        *   **MIDI Channel**: Default `midi_channel` is 1, as specified in the output JSON. Ensure your tool calls reflect this unless the user explicitly requests a different channel.
        *   **Value Ranges**:
            *   Standard CC parameters: `value` is 0-127.
            *   High-resolution CC & NRPN parameters: `value` is 0-16383.
            *   Bipolar parameters (e.g., Filter EG Amount, LFO Mod Amounts) are often centered (e.g., 8192 for a 0-16383 range, or 64 for 0-127). Consult tool docstrings if unsure.
        *   **Parameter Interpretation**: Translate qualitative user requests (e.g., "darker", "punchier", "more movement") into appropriate quantitative MIDI parameter values.
        *   **Error Handling**: Skip any tool that previously returned an error during this session.

        ──────────────────────────────────────────────────────────────────────────────

        ## EXAMPLES

        **User**: "Make it sound a bit darker and give it a faster, punchier attack."
        **Assistant**:
        ```json
        [
            {
                "used_tool": "set_filter_cutoff",
                "midi_channel": 1,
                "value": 4500,
                "midi_cc": 19,
                "midi_cc_lsb": 51,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_amp_eg_attack_time",
                "midi_channel": 1,
                "value": 800,
                "midi_cc": 28,
                "midi_cc_lsb": 60,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_filter_eg_attack_time",
                "midi_channel": 1,
                "value": 1200,
                "midi_cc": 23,
                "midi_cc_lsb": 55,
                "nrpn_msb": null,
                "nrpn_lsb": null
            }
        ]
        ```

        **User**: "I want a resonant pluck sound. Sharp attack, quick decay on both filter and amp, and make the filter really 'speak'."
        **Assistant**:
        ```json
        [
            {
                "used_tool": "set_amp_eg_attack_time",
                "midi_channel": 1,
                "value": 100,
                "midi_cc": 28,
                "midi_cc_lsb": 60,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_amp_eg_decay_time",
                "midi_channel": 1,
                "value": 2500,
                "midi_cc": 29,
                "midi_cc_lsb": 61,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_amp_eg_sustain_time",
                "midi_channel": 1,
                "value": 0,
                "midi_cc": 30,
                "midi_cc_lsb": 62,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_filter_cutoff",
                "midi_channel": 1,
                "value": 9000,
                "midi_cc": 19,
                "midi_cc_lsb": 51,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_filter_resonance",
                "midi_channel": 1,
                "value": 11500,
                "midi_cc": 21,
                "midi_cc_lsb": 53,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_filter_eg_attack_time",
                "midi_channel": 1,
                "value": 50,
                "midi_cc": 23,
                "midi_cc_lsb": 55,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_filter_eg_decay_time",
                "midi_channel": 1,
                "value": 2000,
                "midi_cc": 24,
                "midi_cc_lsb": 56,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_filter_eg_amt",
                "midi_channel": 1,
                "value": 12000,
                "midi_cc": 27,
                "midi_cc_lsb": 59,
                "nrpn_msb": null,
                "nrpn_lsb": null
            }
        ]
        ```

        **User**: "Can you make a slowly evolving pad sound, with a long attack and release, and some gentle LFO movement on the filter?"
        **Assistant**:
        ```json
        [
            {
                "used_tool": "set_amp_eg_attack_time",
                "midi_channel": 1,
                "value": 10000,
                "midi_cc": 28,
                "midi_cc_lsb": 60,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_amp_eg_release_time",
                "midi_channel": 1,
                "value": 12000,
                "midi_cc": 31,
                "midi_cc_lsb": 63,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_filter_cutoff",
                "midi_channel": 1,
                "value": 6000,
                "midi_cc": 19,
                "midi_cc_lsb": 51,
                "nrpn_msb": null,
                "nrpn_lsb": null
            },
            {
                "used_tool": "set_lfo1_rate_high_res",
                "midi_channel": 1,
                "value": 2500,
                "midi_cc": null,
                "midi_cc_lsb": null,
                "nrpn_msb": 5,
                "nrpn_lsb": 0
            },
            {
                "used_tool": "set_mod1_filter_amt_nrpn",
                "midi_channel": 1,
                "value": 9500,
                "midi_cc": null,
                "midi_cc_lsb": null,
                "nrpn_msb": 6,
                "nrpn_lsb": 11
            }
        ]
        ```

        **User**: "Make it more alive."
        **Assistant**:
        ```json
        { "message":"Which kind of movement would you like to add: a filter sweep, pitch vibrato, volume tremolo, or perhaps some rhythmic arpeggiation?" }
        ```
        """,
    )


async def run_sub37_sound_design_agent(
    user_prompt: str, api_key: str, conn: psycopg2.extensions.connection
) -> list[SynthGenieResponse | SynthGenieAmbiguousResponse]:
    """
    Process a user prompt with the Sub37 AI agent.

    This implementation runs the agent and returns the output.

    Requires a valid API key.
    """
    agent = get_sub37_sound_design_agent()

    result = await agent.run(user_prompt)

    track_api_key_usage(conn, api_key)

    if isinstance(result.output, list):
        return result.output
    else:
        return [result.output]
