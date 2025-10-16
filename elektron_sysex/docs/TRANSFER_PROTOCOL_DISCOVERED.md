# Transfer Protocol Discovery - SOLVED!

## The Problem
Our SysEx messages weren't changing the machine types, but Transfer worked instantly.

## The Solution - What Transfer ACTUALLY Sends

From the MIDI capture in `docs/MESSAGES_FROM_MIDI.md`, we discovered Transfer uses a completely different format than expected:

### Key Differences Found:

1. **Device ID**: Transfer uses `0x10`, NOT `0x0D`!
2. **Message Structure**: Commands are at byte position 11, not 5
3. **Sequence Numbers**: Two bytes (high/low) format

### Transfer's Actual Message Format:
```
F0 00 20 3C 10 00 00 [seq_high] [seq_low] 00 00 [command] [data...] F7
```

### The 4 Messages Transfer Sends for FM_TONE:

#### Message 1: Path/Location Setup (39 bytes)
```
F0 00 20 3C 10 00 00 07 6F 00 00 53 2F 73 00 6F 75 6E 64 62 61 6E 00 6B 73 2F 48 00 00 00 22 00 47 00 00 00 48 00 F7
```
- Sequence: `07 6F`
- Command: `53` (LIST/PATH) at byte 11
- Contains path: `/soundbanks/H`

#### Message 2: Write Open (38 bytes)
```
F0 00 20 3C 10 00 00 07 70 00 00 57 00 00 20 00 67 2F 73 6F 75 6E 00 64 62 61 6E 6B 73 2F 00 48 2F 31 39 39 00 F7
```
- Sequence: `07 70`
- Command: `57` (WRITE_OPEN) at byte 11
- Contains: `/soundbanks/H/199` (the FM_TONE patch number)

#### Message 3: Write Data (295 bytes)
```
F0 00 20 3C 10 00 00 07 71 00 00 58 [header bytes] [encoded patch data] F7
```
- Sequence: `07 71`
- Command: `58` (WRITE_PARTIAL) at byte 11
- Contains the actual 7-bit encoded patch data

#### Message 4: Write Close (22 bytes)
```
F0 00 20 3C 10 00 00 07 72 00 00 59 00 00 02 0A 0D 00 00 00 67 F7
```
- Sequence: `07 72`
- Command: `59` (WRITE_CLOSE) at byte 11

## Implementation

The working implementation is in `elektron_sysex/transfer_protocol.py`

To test it:
```bash
make test-transfer
```

This sends the FM_TONE patch using Transfer's EXACT format.

## Machine Type Values (at byte 0x18 in patch files)

- FM_DRUM: `0xC2`
- SWARMER: `0xC3`
- MIDI: `0xC4`
- WAVETONE: `0xC5`
- FM_TONE: `0xC6`

## Why Our Previous Attempts Failed

1. **Wrong Device ID**: We used `0x0D` (from libdigitone) instead of `0x10`
2. **Wrong Message Format**: We put commands at byte 5 instead of byte 11
3. **Missing Path Setup**: Transfer sends path/location messages before the data
4. **Different Header Structure**: Transfer includes additional header bytes

## Lessons Learned

- Always capture actual working traffic instead of guessing
- Device IDs and protocols can vary between software implementations
- The "standard" elektroid protocol might work for some devices but not Digitone II
- Transfer uses a more complex handshake with path setup before sending data