#!/usr/bin/env python3
"""Extract value mappings from data files that have complete parameter definitions."""

import json
import sys
from pathlib import Path

# Add the project to path so we can import the data modules
sys.path.insert(0, str(Path(__file__).parent))

from synthgenie.data.fm_tone import FM_TONE_PARAMS

all_params = {}


def generate_values_for_param(param_name, param_config):
    """Generate value mappings based on parameter configuration."""
    min_midi = param_config.get('min_midi', 0)
    max_midi = param_config.get('max_midi', 127)
    min_val = param_config.get('min_val', min_midi)
    max_val = param_config.get('max_val', max_midi)

    # Skip parameters with list values (like B which controls two operators)
    if isinstance(min_val, list) or isinstance(max_val, list):
        return None

    # Generate all values in the MIDI range
    values = []

    # Check if this is a decimal parameter (large MIDI range with smaller display range)
    if max_midi > 1000:
        # Decimal parameter like HARM or DTUN
        # Calculate the ratio between MIDI range and display range
        midi_range = max_midi - min_midi
        display_range = max_val - min_val

        for midi_val in range(min_midi, max_midi + 1):
            # Map MIDI value to display value
            display_val = min_val + (midi_val - min_midi) * display_range / midi_range
            values.append({'midi': midi_val, 'display': f'{display_val:.2f}'})
    else:
        # Standard parameter or discrete parameter
        for midi_val in range(min_midi, max_midi + 1):
            if max_midi <= 127 and min_midi == 0:
                # Standard 0-127 parameter
                values.append({'midi': midi_val, 'display': str(midi_val)})
            else:
                # Map MIDI to display range
                display_val = min_val + (midi_val - min_midi) * (max_val - min_val) / (max_midi - min_midi)
                if isinstance(min_val, float) or isinstance(max_val, float):
                    values.append({'midi': midi_val, 'display': f'{display_val:.2f}'})
                else:
                    values.append({'midi': midi_val, 'display': str(int(display_val))})

    return values


# Process FM_TONE_PARAMS
for page_name, page_params in FM_TONE_PARAMS.items():
    for param_name, param_config in page_params.items():
        # Skip nested structures for now (like page_2.A.atk)
        if isinstance(param_config, dict) and 'cc_msb' in param_config:
            cc_msb = param_config['cc_msb']

            # Create a unique key
            param_key = f'fm_tone_tool.set_fm_tone_{param_name.lower()}'

            # Generate value mappings
            values = generate_values_for_param(param_name, param_config)

            # Skip if values couldn't be generated
            if values is None:
                continue

            all_params[param_key] = {
                'cc': cc_msb,
                'function': f'set_fm_tone_{param_name.lower()}',
                'name': param_name,
                'type': 'continuous',
                'min': param_config.get('min_midi', 0),
                'max': param_config.get('max_midi', 127),
                'values': values
            }

# Output as JSON
print(json.dumps(all_params, indent=2))
