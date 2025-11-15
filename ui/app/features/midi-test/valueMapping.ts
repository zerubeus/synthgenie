import type { ParamConfig } from './parameterData';

export interface ValueMapping {
  midi: number;
  display: string;
}

/**
 * Calculate the display value for a given MIDI value based on parameter configuration
 */
export function midiToDisplay(midiValue: number, param: ParamConfig): string {
  // Handle parameters with explicit options (categorical)
  if (param.options && param.options.length > 0) {
    const maxMidi = param.max_midi ?? param.options.length - 1;
    const index = Math.min(midiValue, maxMidi);
    return param.options[index] || String(midiValue);
  }

  // Handle parameters with min_val/max_val range mapping
  if (param.min_val !== undefined && param.max_val !== undefined) {
    const minMidi = param.min_midi ?? 0;
    const maxMidi = param.max_midi ?? 127;

    // Special case: RATIO OFFSET parameters use formula: (midi - 1000) / 1000
    // These have specific characteristics: min_midi=0, max_midi=1999, range=-1.000 to +0.999
    if (minMidi === 0 && maxMidi === 1999 && param.min_val === -1.0 && Math.abs(param.max_val - 0.999) < 0.01) {
      const displayValue = (midiValue - 1000) / 1000.0;
      return displayValue.toFixed(3);
    }

    // Linear interpolation for other parameters
    const range = maxMidi - minMidi;
    const valueRange = param.max_val - param.min_val;

    if (range === 0) return String(param.min_val);

    const normalizedMidi = (midiValue - minMidi) / range;
    const displayValue = param.min_val + (normalizedMidi * valueRange);

    // Determine decimal places based on the parameter range
    if (Math.abs(valueRange) < 10) {
      return displayValue.toFixed(3);
    } else if (Math.abs(valueRange) < 100) {
      return displayValue.toFixed(2);
    } else {
      return displayValue.toFixed(0);
    }
  }

  // Default: MIDI value maps directly to display value
  return String(midiValue);
}

/**
 * Calculate the MIDI value for a given display value based on parameter configuration
 */
export function displayToMidi(displayValue: number | string, param: ParamConfig): number {
  // Handle parameters with explicit options (categorical)
  if (param.options && param.options.length > 0) {
    const index = param.options.indexOf(String(displayValue));
    return index >= 0 ? index : 0;
  }

  // Handle parameters with min_val/max_val range mapping
  if (param.min_val !== undefined && param.max_val !== undefined) {
    const minMidi = param.min_midi ?? 0;
    const maxMidi = param.max_midi ?? 127;

    const numericDisplay = typeof displayValue === 'number' ? displayValue : parseFloat(displayValue);

    // Special case: RATIO OFFSET parameters use formula: midi = (display * 1000) + 1000
    if (minMidi === 0 && maxMidi === 1999 && param.min_val === -1.0 && Math.abs(param.max_val - 0.999) < 0.01) {
      const midiValue = (numericDisplay * 1000) + 1000;
      return Math.round(midiValue);
    }

    // Linear interpolation (inverse)
    const valueRange = param.max_val - param.min_val;

    if (valueRange === 0) return minMidi;

    const normalizedValue = (numericDisplay - param.min_val) / valueRange;
    const midiValue = minMidi + (normalizedValue * (maxMidi - minMidi));

    return Math.round(midiValue);
  }

  // Default: display value is the MIDI value
  return typeof displayValue === 'number' ? displayValue : parseInt(displayValue, 10);
}

/**
 * Generate all value mappings for a parameter (for dropdowns/sliders)
 * Only generates full mappings for small ranges (<= 100 values) used in dropdowns.
 * For larger ranges, returns just min/max for slider configuration.
 */
export function generateValueMappings(param: ParamConfig, fullMapping: boolean = false): ValueMapping[] {
  const minMidi = param.min_midi ?? 0;
  const maxMidi = param.max_midi ?? 127;
  const count = maxMidi - minMidi + 1;

  // For large ranges (>100), only return min/max unless full mapping is explicitly requested
  // This avoids generating thousands of mappings unnecessarily
  if (!fullMapping && count > 100) {
    return [
      {
        midi: minMidi,
        display: midiToDisplay(minMidi, param),
      },
      {
        midi: maxMidi,
        display: midiToDisplay(maxMidi, param),
      },
    ];
  }

  // For small ranges or when full mapping is requested, generate all values
  const values: ValueMapping[] = [];
  for (let midi = minMidi; midi <= maxMidi; midi++) {
    values.push({
      midi,
      display: midiToDisplay(midi, param),
    });
  }

  return values;
}

/**
 * Get the count of possible values for a parameter
 */
export function getValueCount(param: ParamConfig): number {
  if (param.options && param.options.length > 0) {
    return param.options.length;
  }

  const minMidi = param.min_midi ?? 0;
  const maxMidi = param.max_midi ?? 127;

  return maxMidi - minMidi + 1;
}

/**
 * Get the minimum MIDI value for a parameter
 */
export function getMinMidiValue(param: ParamConfig): number {
  return param.min_midi ?? 0;
}

/**
 * Get the maximum MIDI value for a parameter
 */
export function getMaxMidiValue(param: ParamConfig): number {
  return param.max_midi ?? 127;
}

/**
 * Scale MIDI value for parameters that need it (Ratio Offset bug workaround)
 *
 * The Digitone firmware has a bug where ratio offset parameters (NRPN 1:97-100)
 * apply the formula: received_value * 1000 / 8192
 * We must multiply by 8.192 (8192/1000) to compensate.
 *
 * Testing showed:
 * - Sending 1999 directly → Digitone receives 244 (1999*1000/8192≈244)
 * - Sending 1999*8=15992 → Digitone receives 1952 (15992*1000/8192≈1952)
 * - Sending 1999*8.192=16376 → Digitone receives 1999 ✓
 */
export function scaleForDigitone(value: number, param: ParamConfig): number {
  if (!param.needsScaling) {
    return value;
  }

  // For ratio offset parameters: multiply by 8192/1000 to compensate for Digitone's formula
  // Digitone does: received * 1000 / 8192, so we do: value * 8192 / 1000
  // Clamp to 14-bit NRPN max (16383)
  const scaledValue = Math.min(16383, Math.floor(value * 8192 / 1000));

  console.log(`[SCALING] ${value} → ${scaledValue} (×8.192 for Digitone bug, NRPN ${param.nrpn_msb}:${param.nrpn_lsb})`);

  return scaledValue;
}
