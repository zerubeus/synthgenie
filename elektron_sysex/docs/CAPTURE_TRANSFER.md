# How to Capture What Transfer Sends

Since our implementation isn't working but Transfer works instantly, we need to see exactly what Transfer sends.

## Option 1: Use MIDI Monitor (Recommended)

1. **Download MIDI Monitor** from https://www.snoize.com/MIDIMonitor/
2. **Open MIDI Monitor**
3. In MIDI Monitor:
   - Go to Preferences
   - Under "Sources", check "Elektron Digitone II"
   - Make sure "Act as a destination for other programs" is checked
4. **Clear the MIDI Monitor window**
5. **Open Transfer** and send the FM_TONE patch
6. **Copy all the SysEx messages** that appear (they start with F0 and end with F7)

## Option 2: Use SysEx Librarian

1. **Download SysEx Librarian** from https://www.snoize.com/SysExLibrarian/
2. Set it to record from "Elektron Digitone II"
3. Click "Record Many"
4. Send the patch from Transfer
5. Stop recording and save the SysEx

## What to Look For

When Transfer successfully changes the machine type, look for:
- Messages starting with `F0 00 20 3C` (Elektron manufacturer ID)
- The device ID byte (4th byte after F0 00 20 3C)
- The command byte (5th byte)
- How many messages are sent
- The order and structure of messages

## Current Problem

Our code sends:
```
F0 00 20 3C 0D 00 57 00 00 F7  (Open write)
F0 00 20 3C 0D 01 58 [data] F7  (Send data)
F0 00 20 3C 0D 03 59 F7  (Close write)
```

But the machine type doesn't change. We need to see what Transfer sends differently.

Please share the SysEx messages you capture!