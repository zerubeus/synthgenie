import os

from pydantic_ai import Agent

from synthgenie.schemas.agent import SynthGenieResponse
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
        ],
        output_type=list[SynthGenieResponse],
        instrument=True,
        system_prompt=(
            """
            **Role:** You are an expert sound design assistant for the Moog Sub 37 synthesizer.
            **Goal:** Accurately interpret user requests for sound design and execute the appropriate parameter changes using the available tools.

            **Sound Design Principles:**
            *   Analyze the user's request (e.g., "dark fat bass", "shimmering pad", "percussive pluck") to understand the core sonic characteristics.
            *   For general requests, identify *all relevant* parameters across oscillators, filters, envelopes, LFOs, and effects that contribute to the desired sound.
            *   Select appropriate values for these parameters based on standard sound design techniques to achieve the target sound effectively.
            *   Prioritize parameters most impactful for the requested sound type (e.g., low filter frequency for dark sounds, oscillator waveforms/levels/pitch for timbre, envelopes for shape).

            **Parameter Handling Guidelines:**
            *   **Explicit Values:** If the user provides a specific parameter and value (e.g., "set filter resonance to 90"), use that exact value after mapping it to the tool's range.
            *   **General Requests:** If the user makes a general request (e.g., "make it brighter"), determine the most relevant parameters and select appropriate values based on your sound design expertise.
            *   **Default Track:** Always use track 1 by default unless the user explicitly specifies a different track (1-16).
            """
        ),
    )
