import logging
from dataclasses import dataclass, field

from synthgenie.data.digitone_params import digitone_config
from synthgenie.schemas.digitone import ParameterGroup
from synthgenie.schemas.agent import SynthGenieResponse

logger = logging.getLogger(__name__)


class BaseSynthController:
    """Base controller for Digitone parameters."""

    def __init__(
        self,
        config: dict[str, ParameterGroup],
    ):
        """
        Initialize the controller.

        Args:
            config: A dictionary mapping parameter names/pages to ParameterGroup objects.
        """
        self.config = config

    def get_parameter(
        self, page: str, param_name: str, value: int, midi_channel: int, used_tool: str
    ) -> SynthGenieResponse:
        """
        Set a page-based parameter via CC (original method for backward compatibility).

        Args:
            page: Parameter page key in config (e.g. 'page_1', 'page_2').
            param_name: The name of the parameter to set.
            value: The CC value to send (0-127).

        Returns:
            SynthGenieResponse: A response object containing the MIDI CC and channel.
        """
        if page not in self.config:
            raise ValueError(f"Invalid page: {page}")
        if param_name not in self.config[page].parameters:
            raise ValueError(f"Invalid parameter: {param_name} on {page}")

        param = self.config[page].parameters[param_name]
        cc_msb = param.midi.cc_msb

        return SynthGenieResponse(
            used_tool=used_tool,
            midi_cc=cc_msb,
            midi_channel=midi_channel,
            value=value,
        )

    def get_direct_parameter(
        self, param_name: str, value: int, midi_channel: int, used_tool: str
    ) -> SynthGenieResponse:
        """
        Args:
            param_name: Parameter name in config.
            value: The value to send (0-127).

        Returns:
            SynthGenieResponse: A response object containing the MIDI CC and channel.
        """
        if param_name not in self.config:
            raise ValueError(f"Invalid parameter: {param_name}")

        param = self.config[param_name]

        try:
            if not param.midi.cc_msb:
                logger.error(f"No CC MSB defined for {param_name}")
                return False

            cc_msb = param.midi.cc_msb

            return SynthGenieResponse(
                used_tool=used_tool,
                midi_cc=cc_msb,
                midi_channel=midi_channel,
                value=value,
            )

        except Exception as e:
            logger.error(f"Failed to set {param_name}: {e}")
            raise Exception(f"Failed to set {param_name}") from e


@dataclass
class SynthControllerDeps:
    """Dependencies for all synthesizer controllers"""

    # Amp and FX controllers
    amp_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(digitone_config.amp_page.parameters)
    )
    fx_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(digitone_config.fx_page.parameters)
    )

    # LFO controllers
    lfo1_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.lfo.lfo_groups["lfo_1"]
        )
    )
    lfo2_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.lfo.lfo_groups["lfo_2"]
        )
    )
    lfo3_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.lfo.lfo_groups["lfo_3"]
        )
    )

    # Filter controllers
    filter_multi_mode_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.multi_mode_filter.parameters
        )
    )
    filter_lowpass4_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.lowpass_4_filter.parameters
        )
    )
    filter_equalizer_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.equalizer_filter.parameters
        )
    )
    filter_base_width_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.base_width_filter.parameters
        )
    )
    filter_legacy_lp_hp_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.legacy_lp_hp_filter.parameters
        )
    )
    filter_comb_minus_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.comb_minus_filter.parameters
        )
    )
    filter_comb_plus_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(
            digitone_config.comb_plus_filter.parameters
        )
    )

    wavetone_synth_controller: BaseSynthController = field(
        default_factory=lambda: BaseSynthController(digitone_config.wavetone.pages)
    )
