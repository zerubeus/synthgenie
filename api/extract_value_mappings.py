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
    pattern = r'def (set_\w+)\([^)]*\)\s*->\s*SynthGenieResponse:\s*"""(.*?)""".*?midi_cc=(\d+)'
    functions = re.finditer(pattern, content, re.DOTALL)

    for match in functions:
        func_name = match.group(1)
        docstring = match.group(2)
        cc_number = match.group(3)

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

        if mappings:
            # Has explicit mappings
            all_params[param_key] = {
                'cc': int(cc_number),
                'function': func_name,
                'name': param_name,
                'type': 'discrete',
                'values': [
                    {'midi': int(m[0]), 'display': m[1].strip()}
                    for m in mappings
                ],
            }
        elif range_info:
            # Has continuous range
            min_val = int(range_info.group(1))
            max_val = int(range_info.group(2))
            all_params[param_key] = {
                'cc': int(cc_number),
                'function': func_name,
                'name': param_name,
                'type': 'continuous',
                'min': min_val,
                'max': max_val,
                'values': [{'midi': i, 'display': str(i)} for i in range(min_val, max_val + 1)],
            }

# Output as JSON
print(json.dumps(all_params, indent=2))
