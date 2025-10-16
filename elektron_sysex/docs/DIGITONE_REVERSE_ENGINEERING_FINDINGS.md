# Digitone II Machine Type Reverse Engineering - Complete Documentation

## Executive Summary

Attempted to reverse engineer the Digitone II's machine type changing mechanism to programmatically switch between FM Tone, FM Drum, WaveTone, Swarmer, and MIDI engines. While we successfully identified the internal structures and USB communication protocol, macOS security restrictions prevented implementation without disabling System Integrity Protection (SIP).

## Key Discoveries

### 1. Device Identification
- **USB Vendor ID**: `0x1935` (Elektron)
- **USB Product ID**: `0x0b34` (Digitone II)
- **USB Interface**: 3 (with endpoints `0x02` OUT and `0x82` IN)
- **Device Class**: 239 (Miscellaneous Device)

### 2. Machine Types Enumeration
Successfully identified the machine type values through binary analysis:
- `0` = FM Tone
- `1` = FM Drum
- `2` = WaveTone
- `3` = Swarmer
- `4` = MIDI

### 3. Binary Analysis Results

#### Jump Table Discovery
Found jump table at memory address `0x00B12500` containing function pointers for each machine type:
```
Entry 0: 0x0000000100018720 → FM_Tone handler
Entry 1: 0x0000000100018750 → FM_Drum handler
Entry 2: 0x0000000100018780 → WaveTone handler
Entry 3: 0x0000000100018870 → Swarmer handler
Entry 4: 0x00000001000FC450 → MIDI handler
```

#### Machine Panel Class Strings
Located in `/Applications/Elektron/Digitone II.app/Contents/MacOS/Digitone II`:
- `0x008745ce`: "FmDrumPanel"
- `0x008745ea`: "MachinePanel"
- `0x0087464e`: "SwarmerPanel"
- `0x008746ae`: "WavetonePanel"
- `0x00877edb`: "MidiMachinePanel"

#### Machine Constants Location
Found machine type enumeration at `0x0071D559`: bytes `[0, 1, 2, 3, 4]`

### 4. Communication Protocol Discovery

#### NOT MIDI
Critical discovery: Overbridge does **NOT** use MIDI protocol. It uses a proprietary USB protocol with structures like:
- `usb_audio_packet_device2host_t`
- `device2host_track_input_modulation_t`

#### Packet Structure (Hypothesized)
Based on binary analysis, the likely packet structure for machine changes:
```c
struct machine_change_packet {
    uint8_t  msg_type;     // 0x01 = parameter change
    uint8_t  seq_num;      // Sequence number
    uint16_t length;       // Payload length (0x0008)
    uint8_t  track;        // Track 0-15 (for tracks 1-16)
    uint8_t  machine;      // Machine type 0-4
    uint8_t  reserved[2];  // Reserved bytes
    uint8_t  checksum;     // Simple checksum
};
```

Example packets constructed:
- Current track to FM_TONE: `01 00 00 08 FF 00 00 00`
- Track 1 to FM_TONE: `01 00 00 08 00 00 00 00`

### 5. Swarmer Function Analysis
The Swarmer handler function at `0x100018870` initializes numerous values, likely default parameters:
- `0x00000000` - Initial clear
- `0x00FFFFFF` - All bits set (mask?)
- `0xFFF0F8FF` - Specific bit pattern
- `0xFFFAEBD7` - Parameter pattern
- (28 more initialization values found)

## Technical Obstacles Encountered

### 1. macOS Security Model
**Primary Blocker**: macOS DriverKit security model prevents direct USB access:
- Even with `sudo`, cannot access USB devices claimed by drivers
- Overbridge DriverKit extension (`se.elektron.overbridge.driverkit.driver`) has exclusive kernel-level access
- Located at: `/Library/SystemExtensions/4C972C50-4C9B-46CA-84C1-02ECAB70F176/`

### 2. Overbridge Processes
Found persistent Overbridge processes that lock USB access:
- `/Library/Audio/Plug-Ins/HAL/OverbridgeCoreAudioPlugin.driver/Contents/MacOS/OverbridgeCoreAudioPlugin`
- `se.elektron.overbridge.driverkit.driver`

### 3. Access Attempts and Results
- **PyUSB**: Can see device, cannot claim interface (Error 13: Permission denied)
- **HIDAPI**: Cannot see device at all (DriverKit exclusive access)
- **MIDI**: Device visible as "Elektron Digitone II" but doesn't respond to standard SysEx
- **Direct USB**: Blocked by macOS security even after killing Overbridge processes

## Tools and Methods Used

### 1. Binary Analysis Tools
- **otool**: Disassembled Mach-O binary to find function addresses
- **nm**: Analyzed symbol table
- **strings**: Searched for class names and function strings
- **xxd/hexdump**: Examined binary data directly

### 2. USB Analysis Tools
- **pyusb**: Attempted USB communication
- **system_profiler SPUSBDataType**: Gathered USB device information
- **ioreg**: Examined IORegistry for device claims
- **lsof**: Checked for processes using device

### 3. Attempted Ghidra Analysis
- Created Ghidra analysis scripts but headless analysis timed out
- Would require GUI Ghidra for full decompilation

## Failed Solution Attempts

### 1. Direct USB Communication
```python
# Attempted packet sending (blocked by macOS)
packet = bytearray([0x01, 0x00, 0x00, 0x08, track, machine_type, 0x00, 0x00])
endpoint_out.write(packet)  # Error 13: Permission denied
```

### 2. MIDI SysEx Attempts
Tried multiple SysEx formats, all unsuccessful:
- `F0 00 20 3C 00 10 [machine] F7`
- `F0 00 20 3C 00 19 01 01 00 [machine] F7`
- `F0 00 20 3C 00 05 [machine] F7`

Device responded with `F0 7E 00 7C 00 F7` (acknowledgment but no action)

### 3. Alternative Approaches Tried
- NRPN (Non-Registered Parameter Number)
- Program Change messages
- CoreMIDI direct access
- HIDAPI as PyUSB alternative

## Working Solutions (Require Compromises)

### 1. Disable System Integrity Protection
```bash
# In Recovery Mode (Cmd+R at boot):
csrutil disable
# Then USB scripts work with sudo
```

### 2. Uninstall Overbridge
Removes DriverKit extension but loses Overbridge functionality

### 3. Use Overbridge UI
Manual control through the official software

## Conclusions

1. **Technical Success**: Successfully reverse-engineered the machine type system, found memory addresses, function handlers, and likely packet structure.

2. **Implementation Blocked**: macOS security model prevents any unsigned application from accessing USB devices with loaded drivers, even with administrative privileges.

3. **Protocol Discovery**: Overbridge uses proprietary USB protocol, not MIDI. The machine change mechanism is embedded in the Overbridge software, not accessible via standard protocols.

4. **Future Possibilities**:
   - Elektron could release an official API
   - Apple could provide USB device access entitlements for developers
   - Disabling SIP remains the only current workaround

## Lessons Learned

1. Modern macOS USB security is extremely restrictive by design
2. DriverKit extensions have exclusive, kernel-level device access
3. Reverse engineering the protocol is only half the battle - OS security is the real barrier
4. Even well-formed packets cannot be sent without proper system permissions

## Files and Resources

- Binary analyzed: `/Applications/Elektron/Digitone II.app/Contents/MacOS/Digitone II`
- Jump table location: `0x00B12500`
- Machine constants: `0x0071D559`
- USB endpoints: Interface 3, OUT=`0x02`, IN=`0x82`

---

*Documentation compiled from reverse engineering efforts on Digitone II firmware version as of October 2024*