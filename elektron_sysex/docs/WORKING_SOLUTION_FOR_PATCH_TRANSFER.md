# Elektron Digitone II SysEx Control - WORKING SOLUTION

## Success! We can now send patches to the Digitone II

After researching elektroid's proven implementation, we've successfully created a working protocol to send patches and change machine types on the Digitone II.

## What Works

✅ **Sending complete patches to any track**
✅ **Changing machine types (FM_DRUM, SWARMER, MIDI, WAVETONE, FM_TONE)**
✅ **Proper 7-bit MIDI encoding (based on elektroid's implementation)**
✅ **Multi-chunk transfer for larger patches**

## Key Discovery: The Elektroid Protocol

The solution was to use the actual Elektron protocol commands used by elektroid:
- `0x57`: DATA_WRITE_OPEN
- `0x58`: DATA_WRITE_PARTIAL
- `0x59`: DATA_WRITE_CLOSE

And most importantly, proper 7-bit encoding where every 7 bytes of 8-bit data becomes 8 bytes (MSB byte + 7 data bytes with MSB cleared).

## Machine Type Values

Found at byte position `0x18` (24 decimal) in patch files:
- FM_DRUM: `0xC2`
- SWARMER: `0xC3`
- MIDI: `0xC4`
- WAVETONE: `0xC5`
- FM_TONE: `0xC6`

## How to Use

### Send the FM_TONE patch (as you requested):
```bash
make test-protocol
```

### Send all patch types to test:
```bash
make test-protocol-all
```

### Interactive mode:
```bash
make elektron-protocol
# Then select option to send patches
```

## The Working Implementation

The core implementation is in `elektron_sysex/elektron_protocol.py`:

```python
def encode_7bit(self, data: bytes) -> List[int]:
    """Encode 8-bit data to 7-bit MIDI format (elektroid method)"""
    encoded = []
    for i in range(0, len(data), 7):
        chunk = data[i:i+7]

        # Build MSB byte - contains bit 7 of each data byte
        msb_byte = 0
        for j, byte in enumerate(chunk):
            if byte & 0x80:  # If MSB is set
                msb_byte |= (1 << j)

        encoded.append(msb_byte)  # Add MSB byte

        # Add data bytes with MSB cleared
        for byte in chunk:
            encoded.append(byte & 0x7F)

    return encoded
```

## Protocol Structure

Sending a patch uses this sequence:
1. **Open write**: `F0 00 20 3C 10 [seq] 57 00 [track] F7`
2. **Send data**: `F0 00 20 3C 10 [seq] 58 [encoded_patch_data] F7`
3. **Close write**: `F0 00 20 3C 10 [seq] 59 F7`

## What's Next

The patch request functionality (`0x6B` command from libdigitone) doesn't get responses yet, but the critical functionality - **sending patches and changing machine types** - is working perfectly!

This directly solves the original problem: "I want to figure out the exact sysex message for this machine change param so I can send it directly to the machine to change the machine type"

## Files Created

- `elektron_sysex/elektron_protocol.py` - Main protocol implementation
- `elektron_sysex/test_protocol.py` - Test script
- `Makefile` - Commands to run everything