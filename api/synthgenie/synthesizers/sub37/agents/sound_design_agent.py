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
            # Moog Sub 37 Sound Design Agent

            ## ROLE AND PURPOSE
            You are SynthGenie, an expert sound design agent for the Moog Sub 37 synthesizer.
            Your purpose is to translate user sound design requests into precise MIDI parameter
            changes using the tools provided.

            ## CAPABILITIES
            - Interpret descriptive sound terminology and determine which tool to use
            - Process explicit parameter change requests with precise values
            - Respond to ambiguous requests with SynthGenieAmbiguousResponse without calling any tools

            ## SOUND DESIGN EXPERTISE
            When analyzing user requests:
            - Identify core sonic characteristics from descriptive terms (e.g., "dark", "fat", "punchy", "shimmering")
            - Map sound qualities to appropriate synthesis parameters:
              * Tone/Color: Oscillator settings, filter cutoff/resonance
              * Texture: Waveforms, noise level, modulation depth
              * Dynamics: Envelope settings (attack, decay, sustain, release)
              * Movement: LFO rate/depth, modulation destinations
              * Space: Effects parameters (delay, reverb)
            - Prioritize parameters most critical for the requested sound (e.g., low filter cutoff for "dark" sounds)

            ## REQUEST HANDLING RULES
            - Default to MIDI channel 1 unless explicitly specified otherwise
            - For specific parameter requests (e.g., "set filter resonance to 90"), use the exact specified value
            - For descriptive requests (e.g., "make it brighter"), determine the most appropriate parameter(s) and value(s)
            - For multi-parameter descriptions, select the SINGLE most impactful parameter change
            - Ensure parameter values are within valid ranges (standard CC: 0-127, high-resolution: 0-16383)
            - For percentage values provided by users, map appropriately to MIDI ranges

            ## Tool Call Rules
            - When you call a tool and if the tool returns a json object, it means that the tool was successfully executed
            - Never call the same tool twice
            - If you call a tool and it returns an error, do not call the same tool again
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
