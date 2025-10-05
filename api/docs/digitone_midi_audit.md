# Digitone II MIDI Implementation Audit

## Summary

This document compares the implemented MIDI tools against the official Digitone II MIDI specification (Appendix C).

## Coverage Analysis

### ✅ Implemented Sections

#### C.4 FILTER PARAMETERS
**File:** `filter_tool.py`
- ✅ Attack Time (CC 20)
- ✅ Decay Time (CC 21)
- ✅ Sustain Level (CC 22)
- ✅ Release Time (CC 23)
- ✅ Frequency (CC 16)
- ✅ Env. Depth (CC 24)
- ⚠️ **MISSING:** Data entry knob F (CC 17) - spec shows "machine dependent"
- ⚠️ **MISSING:** Data entry knob G (CC 18) - spec shows "machine dependent"
- ⚠️ **MISSING:** Env. Delay (CC 19)
- ⚠️ **MISSING:** Key Tracking (CC 26)
- ⚠️ **MISSING:** Base (CC 27)
- ⚠️ **MISSING:** Width (CC 28)
- ⚠️ **MISSING:** Env. Reset (CC 25)

**Implementation Note:** The filter_tool.py implements CC 17 and CC 18 as "resonance" and "type" respectively, but the spec shows these as "machine dependent" parameters F and G.

#### C.5 AMP PARAMETERS
**File:** `amp_fx_tool.py`
- ✅ Attack Time (CC 84)
- ✅ Hold Time (CC 85)
- ✅ Decay Time (CC 86)
- ✅ Sustain Level (CC 87) - **NOTE:** Spec shows CC 86 for both Decay and Sustain, likely a typo. Implementation uses CC 87.
- ✅ Release Time (CC 88)
- ✅ Env. Reset (CC 92)
- ✅ Mode (CC 91)
- ✅ Pan (CC 89)
- ✅ Volume (CC 90)

#### C.7 FX PARAMETERS
**File:** `amp_fx_tool.py`
- ✅ Bit Reduction (CC 78)
- ✅ Overdrive (CC 81)
- ✅ Sample Rate Reduction (CC 79)
- ✅ SRR Routing (CC 80)
- ✅ Overdrive Routing (CC 82)
- ✅ Delay Send (CC 30)
- ✅ Reverb Send (CC 31)
- ✅ Chorus Send (CC 29)

#### C.8 MOD PARAMETERS

##### LFO 1
**File:** `lfo_tool.py`
- ✅ Speed (CC 102)
- ✅ Multiplier (CC 103)
- ✅ Fade In/Out (CC 104)
- ✅ Destination (CC 105)
- ✅ Waveform (CC 106)
- ✅ Start Phase/Slew (CC 107)
- ✅ Trig Mode (CC 108)
- ✅ Depth (CC 109)

##### LFO 2
**File:** `lfo_tool.py`
- ✅ Speed (CC 111)
- ✅ Multiplier (CC 112)
- ✅ Fade In/Out (CC 113)
- ✅ Destination (CC 114)
- ✅ Waveform (CC 115)
- ✅ Start Phase/Slew (CC 116)
- ✅ Trig Mode (CC 117)
- ✅ Depth (CC 118)

### ❌ Missing Sections

#### C.1 TRACK PARAMETERS
- ❌ Mute (CC 94)
- ❌ Track level (CC 95)

#### C.2 TRIG PARAMETERS
- ❌ Note (CC 3)
- ❌ Velocity (CC 4)
- ❌ Length (CC 5)
- ❌ Filter Trig (CC 13)
- ❌ LFO Trig (CC 14)
- ❌ Portamento Time (CC 9)
- ❌ Portamento On/Off (CC 65)

#### C.3 SOURCE PARAMETERS
The spec defines machine-dependent parameters across 4 SYN pages (CC 40-77). These are implemented in machine-specific tools:

##### SYN PAGE 1 (CC 40-47)
- ✅ Implemented in `fm_tone_tool.py`, `fm_drum_tool.py`, `wavetone_tool.py`, `swarmer_tool.py`

##### SYN PAGE 2 (CC 48-55)
- ✅ Implemented in machine-specific tools

##### SYN PAGE 3 (CC 56-63)
- ✅ Implemented in machine-specific tools

##### SYN PAGE 4 (CC 70-77)
- ✅ Implemented in `fm_tone_tool.py` (CC 70-77)
- ⚠️ **PARTIAL:** Only FM Tone machine implements Page 4 parameters

#### C.6 EUCLIDEAN SEQUENCER PARAMETERS
**COMPLETELY MISSING**
- ❌ Pulse Generator 1
- ❌ Pulse Generator 2
- ❌ Euclidean Mode On/Off
- ❌ Rotation Generator 1
- ❌ Rotation Generator 2
- ❌ Track Rotation
- ❌ Boolean Operator

Note: All use NRPN MSB 3 with different LSB values (8-14)

#### C.8 MOD PARAMETERS - LFO 3
**COMPLETELY MISSING**
- ❌ Speed (NRPN MSB 1, LSB 58)
- ❌ Multiplier (NRPN MSB 1, LSB 59)
- ❌ Fade In/Out (NRPN MSB 1, LSB 60)
- ❌ Destination (NRPN MSB 1, LSB 61)
- ❌ Waveform (NRPN MSB 1, LSB 62)
- ❌ Start Phase/Slew (NRPN MSB 1, LSB 70)
- ❌ Trig Mode (NRPN MSB 1, LSB 71)
- ❌ Depth (NRPN MSB 1, LSB 72)

Note: LFO 3 uses NRPN only (no CC support)

#### C.9 SEND FX PARAMETERS
**COMPLETELY MISSING**

##### DELAY
- ❌ Delay Time (CC 21, NRPN 2/0)
- ❌ Pingpong (CC 22, NRPN 2/1)
- ❌ Stereo Width (CC 23, NRPN 2/2)
- ❌ Feedback (CC 24, NRPN 2/3)
- ❌ Highpass Filter (CC 25, NRPN 2/4)
- ❌ Lowpass Filter (CC 26, NRPN 2/5)
- ❌ Reverb Send (CC 27, NRPN 2/6)
- ❌ Mix Volume (CC 28, NRPN 2/7)

##### REVERB
- ❌ Predelay (CC 29, NRPN 2/8)
- ❌ Decay Time (CC 30, NRPN 2/9)
- ❌ Shelving Freq (CC 31, NRPN 2/10)
- ❌ Shelving Gain (CC 89, NRPN 2/11)
- ❌ Highpass Filter (CC 90, NRPN 2/12)
- ❌ Lowpass Filter (CC 91, NRPN 2/13)
- ❌ Mix Volume (CC 92, NRPN 2/15)

##### CHORUS
- ❌ Depth (CC 16, NRPN 2/41)
- ❌ Speed (CC 9, NRPN 2/42)
- ❌ High Pass Filter (CC 70, NRPN 2/43)
- ❌ Width (CC 71, NRPN 2/44)
- ❌ Delay Send (CC 12, NRPN 2/45)
- ❌ Reverb Send (CC 13, NRPN 2/46)
- ❌ Mix Volume (CC 14, NRPN 2/47)

#### C.10 MIXER PARAMETERS
**COMPLETELY MISSING**

##### COMPRESSOR
- ❌ Threshold (CC 111, NRPN 2/16)
- ❌ Attack Time (CC 112, NRPN 2/17)
- ❌ Release Time (CC 113, NRPN 2/18)
- ❌ Makeup Gain (CC 114, NRPN 2/19)
- ❌ Pattern Volume (CC 119, NRPN 2/24)
- ❌ Ratio (CC 115, NRPN 2/20)
- ❌ Sidechain Source (CC 116, NRPN 2/21)
- ❌ Sidechain Filter (CC 117, NRPN 2/22)
- ❌ Dry/Wet Mix (CC 118, NRPN 2/23)

##### EXTERNAL IN MIXER
- ❌ All parameters (CC 72-82, NRPN 2/30-40)

#### C.11 VAL PARAMETERS
**COMPLETELY MISSING**
- ❌ VAL1-VAL16 (CC 70-85, NRPN 1/16-67)

Note: These are for MIDI tracks only

#### C.12 MISC PARAMETERS
**COMPLETELY MISSING**
- ❌ Pattern Mute (CC 110, NRPN 1/109)
- ❌ Master Overdrive (CC 17, NRPN 2/50)

## Issues Identified

### 1. CC Number Conflicts
The documentation shows some CC number conflicts that need investigation:

- **CC 17-18**: Spec shows as "machine dependent" for Filter, but `filter_tool.py` implements them as resonance and type
- **CC 86**: Spec shows for both Decay Time and Sustain Level (likely spec typo)
- **CC 89-92**: Used in both AMP parameters and REVERB parameters (different NRPN MSB values distinguish them)

### 2. Filter Implementation Discrepancy
The `filter_tool.py` implements:
- CC 17 as "resonance"
- CC 18 as "type"

But the spec shows:
- CC 17 as "Data entry knob F (machine dependent)"
- CC 18 as "Data entry knob G (machine dependent)"

This suggests the current implementation may be mapping these incorrectly or the documentation uses a simplified naming convention.

### 3. Missing Filter Parameters
Several filter parameters from the spec are not implemented:
- Env. Delay (CC 19)
- Env. Reset (CC 25)
- Key Tracking (CC 26)
- Base (CC 27)
- Width (CC 28)

### 4. NRPN Support
The current implementation only uses CC values. The spec indicates NRPN support for higher resolution control, particularly for:
- LFO 3 (NRPN only, no CC)
- Euclidean Sequencer parameters (NRPN only)
- All parameters that need 14-bit resolution

## Recommendations

### Priority 1: Core Functionality
1. Add missing Track parameters (Mute, Track level)
2. Add missing Trig parameters (especially Portamento)
3. Complete Filter implementation
4. Add LFO 3 support (requires NRPN implementation)

### Priority 2: Global Effects
1. Implement Send FX parameters (Delay, Reverb, Chorus)
2. Implement Compressor parameters
3. Add Pattern Mute and Master Overdrive

### Priority 3: Advanced Features
1. Implement Euclidean Sequencer parameters
2. Add MIDI track VAL parameters
3. Add External Input Mixer parameters

### Priority 4: Technical Improvements
1. Implement NRPN message support
2. Investigate and resolve CC number conflicts
3. Add validation for CC/NRPN ranges
4. Document machine-specific parameter mappings

## Machine-Specific Tool Coverage

### FM Tone (`fm_tone_tool.py`)
- ✅ Complete implementation of all 4 SYN pages
- ✅ All operator controls
- ✅ Envelope controls
- Coverage: ~28 parameters

### FM Drum (`fm_drum_tool.py`)
- ✅ Complete drum synthesis parameters
- ✅ Operator and envelope controls
- ✅ Noise and transient controls
- Coverage: ~28 parameters

### Wavetone (`wavetone_tool.py`)
- ✅ Oscillator 1 & 2 controls
- ✅ Modulation parameters
- ✅ Noise controls
- Coverage: ~21 parameters

### Swarmer (`swarmer_tool.py`)
- ✅ All swarmer-specific parameters
- Coverage: ~8 parameters

## Overall Statistics

- **Implemented Parameters:** ~93 (from machine tools + amp/fx + filter + LFO1/2)
- **Missing Parameters:** ~60+ (Track, Trig, Euclidean, LFO3, Send FX, Mixer, VAL, MISC)
- **Coverage:** Approximately 60% of specification
- **NRPN Support:** 0% (not implemented)

## Conclusion

The current implementation covers the core synthesis parameters well, with good support for:
- Machine-specific synthesis parameters (FM Tone, FM Drum, Wavetone, Swarmer)
- Amplitude and basic FX controls
- Filter envelope and frequency
- LFO 1 and LFO 2

However, significant gaps exist in:
- Sequencer/performance controls (Track, Trig, Euclidean)
- Global effects processing (Send FX parameters)
- Master section (Compressor, Mixer)
- High-resolution control (NRPN)
- Advanced features (LFO 3, MIDI track VAL parameters)

The implementation appears focused on sound design and synthesis rather than sequencer control and global processing.
