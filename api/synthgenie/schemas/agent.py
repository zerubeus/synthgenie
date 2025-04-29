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
            'examples': [
                {
                    'used_tool': 'set_filter_cutoff',
                    'midi_channel': 1,
                    'value': 100,
                    'midi_cc': 74,
                    'midi_cc_lsb': None,
                    'nrpn_msb': None,
                    'nrpn_lsb': None,
                },
                {
                    'used_tool': 'set_amp_eg_attack_time',
                    'midi_channel': 3,
                    'value': 8192,  # High-resolution value (0-16383)
                    'midi_cc': 28,  # High-Res CC example (MSB CC)
                    'midi_cc_lsb': 60,  # LSB CC
                    'nrpn_msb': None,
                    'nrpn_lsb': None,
                },
                {
                    'used_tool': 'set_arp_rate',
                    'midi_channel': 3,
                    'value': 10000,  # NRPN value
                    'midi_cc': None,
                    'midi_cc_lsb': None,
                    'nrpn_msb': 3,  # NRPN example
                    'nrpn_lsb': 19,
                },
            ]
        }
    }
