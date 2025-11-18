# NRPN Fine-Grained Control Fix Guide

## Problem Description

Several Digitone parameters were configured to use MIDI CC (Control Change) messages instead of NRPN (Non-Registered Parameter Number) messages. This caused value jumping and lack of precision when controlling parameters via MIDI.

**Root Cause:**
- CC messages provide only 0-127 values (128 discrete steps)
- NRPN messages provide 0-16383 values (16,384 discrete steps)
- Parameters with large ranges (e.g., -60 to +60 semitones, -10 to +10 Hz) need NRPN for smooth control

**Symptoms:**
- Parameter values "jump" when using sliders in the MIDI test UI
- Physical Digitone displays unexpected or coarse values
- Lack of decimal precision (e.g., only integer values instead of -5.00, -4.99, -4.98...)

---

## How to Identify Parameters Needing NRPN

### In Frontend (`ui/app/features/midi-test/parameterData.ts`)

**Problem Signs:**
```typescript
// ❌ WRONG - Missing min_midi/max_midi
'TUN1': { cc_msb: 40, nrpn_msb: 73, nrpn_lsb: 1, min_val: -5, max_val: 5, default: 0 }

// ❌ WRONG - NRPN order reversed (MSB and LSB swapped)
'TUNE': { cc_msb: 40, nrpn_lsb: 1, nrpn_msb: 73, min_val: -60, max_val: 60, default: 0 }
```

**Fixed:**
```typescript
// ✅ CORRECT - Has min_midi/max_midi, correct NRPN order
'TUN1': { cc_msb: 40, nrpn_msb: 1, nrpn_lsb: 73, min_midi: 0, max_midi: 16383, min_val: -5.00, max_val: 5.00, default: 0.00 }
```

### In Backend Tool Files (`api/synthgenie/synthesizers/digitone/tools/*.py`)

**Problem Signs:**
```python
# ❌ WRONG - Uses midi_cc instead of NRPN
return SynthGenieResponse(
    used_tool='set_wavetone_osc1_pitch',
    midi_cc=40,  # Should use nrpn_msb/nrpn_lsb
    midi_channel=midi_channel,
    value=value,
)
```

**Fixed:**
```python
# ✅ CORRECT - Uses NRPN
return SynthGenieResponse(
    used_tool='set_wavetone_osc1_pitch',
    nrpn_msb=1,
    nrpn_lsb=73,
    midi_channel=midi_channel,
    value=value,
)
```

### In Backend Data Files (`api/synthgenie/data/*.py`)

**Problem Signs:**
```python
# ❌ WRONG - Missing min_midi/max_midi, reversed NRPN order
'TUN1': {
    'cc_msb': 40,
    'nrpn_lsb': '1',  # Should be LSB number, not '1'
    'nrpn_msb': 73,   # Should be MSB=1
    'max_val': 5,
    'min_val': -5,
    'default': 0,
}
```

**Fixed:**
```python
# ✅ CORRECT - Has MIDI range, correct NRPN order
'TUN1': {
    'cc_msb': 40,
    'nrpn_msb': 1,
    'nrpn_lsb': '73',
    'min_midi': 0,
    'max_midi': 16383,
    'max_val': 5.00,
    'min_val': -5.00,
    'default': 0.00,
}
```

---

## Fix Pattern (Step-by-Step)

When you identify a parameter that needs NRPN fine-grained control, follow these steps:

### Step 1: Update Frontend Parameter Data

**File:** `/ui/app/features/midi-test/parameterData.ts`

```typescript
// Before
'PARAM': { cc_msb: XX, nrpn_lsb: 1, nrpn_msb: YY, min_val: MIN, max_val: MAX, default: 0 }

// After
'PARAM': {
  cc_msb: XX,
  nrpn_msb: 1,        // Fix order: MSB first
  nrpn_lsb: YY,       // LSB second
  min_midi: 0,        // Add MIDI range
  max_midi: 16383,    // Full 14-bit NRPN
  min_val: MIN,       // Add decimals if appropriate
  max_val: MAX,
  default: 0.00       // Add decimals if appropriate
}
```

### Step 2: Update Backend Data

**File:** `/api/synthgenie/data/[machine_name].py`

```python
# Before
'param': {
    'cc_msb': XX,
    'nrpn_lsb': '1',
    'nrpn_msb': YY,
    'max_val': MAX,
    'min_val': MIN,
    'default': 0,
}

# After
'param': {
    'cc_msb': XX,
    'nrpn_msb': 1,      # Fix order: MSB first (integer, not string)
    'nrpn_lsb': 'YY',   # LSB second (string for consistency)
    'min_midi': 0,      # Add MIDI range
    'max_midi': 16383,  # Full 14-bit NRPN
    'max_val': MAX,
    'min_val': MIN,
    'default': 0.00,    # Add decimals if appropriate
}
```

### Step 3: Update Backend Tool Function

**File:** `/api/synthgenie/synthesizers/digitone/tools/[machine_name]_tool.py`

```python
# Before
def set_param(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Args:
        value (int): Value ranging from 0 to 127.  # Wrong range
            - 0 maps to MIN
            - 64 maps to 0
            - 127 maps to MAX
    """
    return SynthGenieResponse(
        used_tool='set_param',
        midi_cc=XX,  # Wrong - uses CC
        midi_channel=midi_channel,
        value=value,
    )

# After
def set_param(ctx: RunContext, value: int, midi_channel: int) -> SynthGenieResponse:
    """
    Set the [parameter description].

    This parameter uses NRPN (1:YY) for full 14-bit resolution with fine-grained control.

    Args:
        ctx (RunContext): The run context containing dependencies.
        value (int): MIDI value ranging from 0 to 16383.
            This parameter uses NRPN (1:YY) for full 14-bit resolution.
            Maps to display values from MIN to MAX.
            Formula: display = ((value / 16383) * RANGE) + MIN
            - 0 = MIN
            - 8191 = ~0 (approximately)
            - 16383 = MAX
            Display range: MIN to MAX with fine precision.
            Default is 0.00 (MIDI ~8191).
        midi_channel (int): The MIDI channel (track) to set the parameter for. 1-16
    """
    return SynthGenieResponse(
        used_tool='set_param',
        nrpn_msb=1,   # Correct - uses NRPN
        nrpn_lsb=YY,  # LSB from documentation
        midi_channel=midi_channel,
        value=value,
    )
```

---

## NRPN Address Pattern

For Digitone track parameters, the NRPN addressing follows this pattern:

- **MSB**: Always `1` (indicates track parameter)
- **LSB**: Varies by parameter (73, 74, 75, 76, 77, etc.)

**Example NRPN Addresses:**
- TUN1 (WAVETONE): `1:73`
- TUN2 (WAVETONE): `1:77`
- OFS1 (WAVETONE): `1:81`
- OFS2 (WAVETONE): `1:85`
- TUNE (FM_DRUM): `1:73`

**Finding NRPN Address:**
Check `/api/docs/digitone.md` for the parameter's NRPN MSB:LSB value.

---

## Parameters Already Fixed

### WAVETONE Machine

**Page 1:**
- ✅ `TUN1` - Oscillator 1 tune (-5.00 to +5.00 semitones)
- ✅ `TUN2` - Oscillator 2 tune (-5.00 to +5.00 semitones)

**Page 2:**
- ✅ `OFS1` - Oscillator 1 offset (-10.00 to +10.00 Hz)
- ✅ `OFS2` - Oscillator 2 offset (-10.00 to +10.00 Hz)

### FM_DRUM Machine

**Page 1:**
- ✅ `TUNE` - Oscillator pitch (-60 to +60 semitones)

---

## Testing Checklist

After applying the fix to a parameter:

1. **Reload the MIDI test page** in the frontend
2. **Select the fixed parameter** in the UI
3. **Verify slider range**:
   - Min value displays correctly (e.g., -5.00)
   - Max value displays correctly (e.g., +5.00)
   - Slider has many positions (not jumping)
4. **Test on physical Digitone**:
   - Move slider slowly and verify smooth value changes on Digitone screen
   - Verify decimal values appear (e.g., -4.73, 0.00, +3.21)
   - No unexpected value jumps
5. **Test backend API** (if applicable):
   - LLM agent can set parameter with NRPN
   - Values translate correctly to Digitone

---

## Common Mistakes to Avoid

1. ❌ **Forgetting to swap NRPN MSB/LSB order**
   - WAVETONE parameters had them reversed (LSB=1, MSB=73)
   - Correct order: MSB=1, LSB=73

2. ❌ **Using string for MSB instead of integer**
   - Wrong: `'nrpn_msb': '1'`
   - Correct: `'nrpn_msb': 1`

3. ❌ **Forgetting to update tool function**
   - Parameter data is updated but tool still uses `midi_cc`
   - Must change tool to use `nrpn_msb` and `nrpn_lsb`

4. ❌ **Not updating both frontend and backend**
   - Both must be in sync for testing and API to work correctly

5. ❌ **Wrong MIDI range**
   - Don't guess ranges like 0-1000
   - Use full 14-bit range: 0-16383

---

## Quick Reference: Files to Update

For any parameter requiring NRPN fine-grained control:

1. **Frontend:** `/ui/app/features/midi-test/parameterData.ts`
2. **Backend Data:** `/api/synthgenie/data/[machine]_[params].py`
3. **Backend Tool:** `/api/synthgenie/synthesizers/digitone/tools/[machine]_tool.py`

All three files must be updated for the fix to work completely.

---

## Formula Reference

### Linear Mapping (Most Parameters)

```python
# MIDI to Display
display = ((midi_value / 16383) * (max_val - min_val)) + min_val

# Examples:
# TUN1: ((value / 16383) * 10.0) - 5.0
# OFS1: ((value / 16383) * 20.0) - 10.0
# TUNE: ((value / 16383) * 120.0) - 60.0
```

### Special Cases

Some parameters like FM ratio offsets use non-linear formulas (e.g., `(midi - 1000) / 1000`). Check existing implementations for the correct formula.

---

## When to Use NRPN vs CC

**Use NRPN (0-16383) when:**
- Parameter range is large (e.g., -60 to +60)
- Decimal precision is needed (e.g., -5.00 to +5.00)
- Parameter has documented NRPN support in Digitone docs
- User reports "value jumping" or "not precise enough"

**Use CC (0-127) when:**
- Parameter has 128 or fewer discrete values
- Parameter is categorical/options (e.g., waveform selector)
- Digitone documentation only lists CC, not NRPN

---

## Related Documentation

- `/api/docs/digitone.md` - Complete Digitone parameter reference with NRPN addresses
- Git commit `58c9b02` - Fix HARM parameter range and mappings
- Git commit `c450da4` - Add fine-grained NRPN control for FM B ratio
- Git commit `c036b82` - Add NRPN support for parameter testing

---

**Last Updated:** 2025-01-16
**Status:** Active - Use this guide when fixing parameter precision issues
