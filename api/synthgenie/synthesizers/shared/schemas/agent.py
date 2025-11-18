from pydantic import BaseModel


class SynthGenieResponse(BaseModel):
    used_tool: str
    midi_channel: int
    value: int
    midi_cc: int | None = None
    midi_cc_lsb: int | None = None
    nrpn_msb: int | None = None
    nrpn_lsb: int | None = None

    model_config = {
        'json_schema_extra': {
            # These examples illustrate different ways the MIDI control fields can be used.
            # In the generated JSON responses, fields with a value of `None`
            # (e.g., `midi_cc_lsb` in a standard CC message) are omitted via
            # FastAPI's `response_model_exclude_none=True` configuration.
            # The full list of all possible fields (including optional ones) can always be
            # found in the schema definition in the OpenAPI documentation.
            'examples': [
                {
                    'used_tool': 'set_filter_cutoff',  # Example of a standard MIDI CC message
                    'midi_channel': 1,
                    'value': 100,
                    'midi_cc': 74,
                    # For this standard CC example:
                    # 'midi_cc_lsb': None,  (Not a high-resolution CC, so LSB is not used)
                    # 'nrpn_msb': None,     (Not an NRPN message)
                    # 'nrpn_lsb': None,     (Not an NRPN message)
                },
                {
                    'used_tool': 'set_amp_eg_attack_time',  # Example of a High-Resolution MIDI CC message
                    'midi_channel': 3,
                    'value': 8192,  # High-resolution value (0-16383)
                    'midi_cc': 28,  # MSB CC for the parameter
                    'midi_cc_lsb': 60,  # LSB CC for finer control
                    # For this High-Res CC example:
                    # 'nrpn_msb': None,     (Not an NRPN message)
                    # 'nrpn_lsb': None,     (Not an NRPN message)
                },
                {
                    'used_tool': 'set_arp_rate',  # Example of an NRPN message
                    'midi_channel': 3,
                    'value': 10000,  # Value for the NRPN parameter
                    # For this NRPN example:
                    'midi_cc': None,  # NRPN uses specific CCs (98/99) for addressing, not for the data itself directly here.
                    'midi_cc_lsb': None,  # Not a standard CC LSB
                    'nrpn_msb': 3,  # NRPN MSB
                    'nrpn_lsb': 19,  # NRPN LSB
                },
            ]
        }
    }


class SynthGenieAmbiguousResponse(BaseModel):
    message: str
