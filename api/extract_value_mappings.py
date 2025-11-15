#!/usr/bin/env python3
"""Extract ALL MIDI parameters from Digitone tool files."""

import json
import re
from pathlib import Path

tools_dir = Path('/Users/zerbasta/synthgenie/api/synthgenie/synthesizers/digitone/tools')

all_params = {}

for tool_file in tools_dir.glob('*.py'):
    if tool_file.name == '__init__.py':
        continue

    content = tool_file.read_text()

    # Find all function definitions with their docstrings and return statements
    # Updated pattern to capture both midi_cc and nrpn parameters
    pattern = r'def (set_\w+)\([^)]*\)\s*->\s*SynthGenieResponse:\s*"""(.*?)""".*?(?:midi_cc=(\d+)|nrpn_msb=(\d+),\s*nrpn_lsb=(\d+))'
    functions = re.finditer(pattern, content, re.DOTALL)

    for match in functions:
        func_name = match.group(1)
        docstring = match.group(2)
        cc_number = match.group(3)  # Will be None for NRPN
        nrpn_msb = match.group(4)  # Will be None for CC
        nrpn_lsb = match.group(5)  # Will be None for CC

        # Determine the MIDI control type
        if cc_number:
            midi_identifier = int(cc_number)
        elif nrpn_msb and nrpn_lsb:
            # For NRPN, we'll use the MSB as the identifier (not perfect but works for grouping)
            midi_identifier = int(nrpn_msb) * 128 + int(nrpn_lsb)
        else:
            continue

        # Extract parameter name from function docstring
        param_name_match = re.search(r'Set the (.+?)\.', docstring)
        param_name = param_name_match.group(1) if param_name_match else func_name.replace('set_', '')

        # Extract value range info
        range_match = re.search(r'value \(int\):\s*(.+?)(?:Args:|midi_channel)', docstring, re.DOTALL)
        if not range_match:
            continue

        value_desc = range_match.group(1)

        # Look for explicit mappings (- 0 = something)
        mapping_pattern = r'^\s+- (\d+) = (.+?)$'
        mappings = re.findall(mapping_pattern, value_desc, re.MULTILINE)

        # Look for range info
        range_pattern = r'ranging from (\d+) to (\d+)'
        range_info = re.search(range_pattern, value_desc)

        param_key = f'{tool_file.stem}.{func_name}'

        # Prioritize range_info over mappings for generating full value lists
        if range_info:
            # Has continuous range
            min_val = int(range_info.group(1))
            max_val = int(range_info.group(2))

            # For large ranges (>1000 values), create sparse mappings with decimal display
            if max_val - min_val > 1000:
                # Check if this looks like a decimal parameter (DTUN: 0-12700 = 0.00-127.00)
                values = []
                for i in range(min_val, max_val + 1):
                    display_val = i / 100.0  # Divide by 100 for decimal display
                    values.append({'midi': i, 'display': f'{display_val:.2f}'})
            else:
                values = [{'midi': i, 'display': str(i)} for i in range(min_val, max_val + 1)]

            all_params[param_key] = {
                'cc': midi_identifier,
                'function': func_name,
                'name': param_name,
                'type': 'continuous',
                'min': min_val,
                'max': max_val,
                'values': values,
            }
        elif mappings:
            # Has explicit mappings (only use if no range info found)
            all_params[param_key] = {
                'cc': midi_identifier,
                'function': func_name,
                'name': param_name,
                'type': 'discrete',
                'values': [
                    {'midi': int(m[0]), 'display': m[1].strip()}
                    for m in mappings
                ],
            }

# Output as JSON
print(json.dumps(all_params, indent=2))
