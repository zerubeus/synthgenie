# Elektron SysEx Control

Control Digitone II machine types via MIDI SysEx messages.

## Project Structure

```
elektron_sysex/
    elektron_sysex/          # Main package directory
    __init__.py          # Package initialization
    main.py              # Main entry point
    models/              # Data models
        __init__.py
    services/            # Service layer
        __init__.py
    utils/               # Utility functions
        __init__.py
    dn_patches/              # Digitone patch files
    docs/                    # Documentation
    pyproject.toml           # Project configuration
```

## Installation

```bash
# Install uv if not already installed
# brew install uv  # macOS
# or check https://docs.astral.sh/uv/

# Install dependencies (uv handles virtual environment automatically)
uv sync
```

## Usage

### Interactive Mode (Default)

```bash

```

## Machine Types

| Internal Value | Machine Type | Patch Value |
| -------------- | ------------ | ----------- |
| 0              | FM_TONE      | 0xC6        |
| 1              | FM_DRUM      | 0xC2        |
| 2              | WAVETONE     | 0xC5        |
| 3              | SWARMER      | 0xC3        |
| 4              | MIDI         | 0xC4        |
