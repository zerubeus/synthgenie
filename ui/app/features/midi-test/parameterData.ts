// Auto-generated from Digitone parameter definitions
// This file contains all parameter configurations for MIDI testing

export interface ParamConfig {
  cc_msb: number;
  nrpn_msb?: number;
  nrpn_lsb?: number | string;
  min_val?: number;
  max_val?: number;
  min_midi?: number;
  max_midi?: number;
  default?: number | string;
  options?: string[];
  needsScaling?: boolean; // For parameters where Digitone expects scaled values (ratio offset: 0-1999 UI but 0-255 MIDI)
}

export interface ParamSet {
  [key: string]: ParamConfig | any;
}

export const DIGITONE_PARAMS: Record<string, ParamSet> = {
  // ========== FM TONE ==========
  'FM_TONE_Page1': {
    'ALGO': { cc_msb: 40, nrpn_lsb: 1, nrpn_msb: 73, max_midi: 7, min_val: 1, max_val: 8, default: 1 },
    'C': { cc_msb: 41, nrpn_lsb: 1, nrpn_msb: 74, max_midi: 18, min_val: 0.25, max_val: 16, default: 1.00 },
    'A': { cc_msb: 42, nrpn_lsb: 1, nrpn_msb: 75, max_midi: 35, min_val: 0.25, max_val: 16, default: 1.00 },
    'B': { cc_msb: 43, nrpn_lsb: 76, nrpn_msb: 1, max_midi: 360, default: 1.00 },
    'HARM': { cc_msb: 44, nrpn_lsb: 77, nrpn_msb: 1, min_midi: 4596, max_midi: 11530, min_val: -26.00, max_val: 26.00, default: 0.00 },
    'DTUN': { cc_msb: 45, nrpn_lsb: 78, nrpn_msb: 1, min_midi: 0, max_midi: 12700, min_val: 0.00, max_val: 127.00, default: 0.00 },
    'FDBK': { cc_msb: 46, nrpn_lsb: 1, nrpn_msb: 79, max_midi: 127, default: 0 },
    'MIX': { cc_msb: 47, nrpn_lsb: 1, nrpn_msb: 80, max_midi: 127, min_val: -63, max_val: 63, default: -63 },
  },
  'FM_TONE_Page2_A': {
    'A.ATK': { cc_msb: 48, nrpn_lsb: 1, nrpn_msb: 81, default: 0 },
    'A.DEC': { cc_msb: 49, nrpn_lsb: 1, nrpn_msb: 82, default: 32 },
    'A.END': { cc_msb: 50, nrpn_lsb: 1, nrpn_msb: 83, default: 127 },
    'A.LEV': { cc_msb: 51, nrpn_lsb: 1, nrpn_msb: 84, default: 0 },
  },
  'FM_TONE_Page2_B': {
    'B.ATK': { cc_msb: 52, nrpn_lsb: 1, nrpn_msb: 85, default: 0 },
    'B.DEC': { cc_msb: 53, nrpn_lsb: 1, nrpn_msb: 86, default: 32 },
    'B.END': { cc_msb: 54, nrpn_lsb: 1, nrpn_msb: 87, default: 127 },
    'B.LEV': { cc_msb: 55, nrpn_lsb: 1, nrpn_msb: 88, default: 0 },
  },
  'FM_TONE_Page3': {
    'ADEL': { cc_msb: 56, nrpn_lsb: 1, nrpn_msb: 89, default: 0 },
    'ATRG': { cc_msb: 57, nrpn_lsb: 1, nrpn_msb: 90, max_midi: 1, default: 1 },
    'ARST': { cc_msb: 58, nrpn_lsb: 1, nrpn_msb: 91, max_midi: 1, default: 1 },
    'PHRT': { cc_msb: 59, nrpn_lsb: 1, nrpn_msb: 92, max_midi: 4, options: ['off', 'all', 'c', 'a+b', 'a+b2'], default: 'all' },
    'BDEL': { cc_msb: 60, nrpn_lsb: 1, nrpn_msb: 93, default: 0 },
    'BTRG': { cc_msb: 61, nrpn_lsb: 1, nrpn_msb: 94, max_midi: 1, default: 1 },
    'BRST': { cc_msb: 62, nrpn_lsb: 1, nrpn_msb: 95, max_midi: 1, default: 1 },
  },
  'FM_TONE_Page4_Ratio': {
    'C.RATIO': { cc_msb: 70, nrpn_lsb: 97, nrpn_msb: 1, min_midi: 0, max_midi: 1999, min_val: -1.000, max_val: 0.999, default: 0.000, needsScaling: true },
    'A.RATIO': { cc_msb: 71, nrpn_lsb: 98, nrpn_msb: 1, min_midi: 0, max_midi: 1999, min_val: -1.000, max_val: 0.999, default: 0.000, needsScaling: true },
    'B1.RATIO': { cc_msb: 72, nrpn_lsb: 99, nrpn_msb: 1, min_midi: 0, max_midi: 1999, min_val: -1.000, max_val: 0.999, default: 0.000, needsScaling: true },
    'B2.RATIO': { cc_msb: 73, nrpn_lsb: 100, nrpn_msb: 1, min_midi: 0, max_midi: 1999, min_val: -1.000, max_val: 0.999, default: 0.000, needsScaling: true },
  },
  'FM_TONE_Page4_KeyTrack': {
    'A.KTRK': { cc_msb: 75, nrpn_lsb: 1, nrpn_msb: 102, default: 0 },
    'B1.KTRK': { cc_msb: 76, nrpn_lsb: 1, nrpn_msb: 103, default: 0 },
    'B2.KTRK': { cc_msb: 77, nrpn_lsb: 1, nrpn_msb: 104, default: 0 },
  },

  // ========== WAVETONE ==========
  'WAVETONE_Page1': {
    'TUN1': { cc_msb: 40, nrpn_lsb: 1, nrpn_msb: 73, min_val: -5, max_val: 5, default: 0 },
    'WAV1': { cc_msb: 41, nrpn_lsb: 1, nrpn_msb: 74, min_val: 0, max_val: 120, default: 0 },
    'PD1': { cc_msb: 42, nrpn_lsb: 1, nrpn_msb: 75, min_val: 0, max_val: 100, default: 50 },
    'LEV1': { cc_msb: 43, nrpn_lsb: 1, nrpn_msb: 76, min_val: 0, max_val: 127, default: 100 },
    'TUN2': { cc_msb: 44, nrpn_lsb: 1, nrpn_msb: 77, min_val: -5, max_val: 5, default: 0 },
    'WAV2': { cc_msb: 45, nrpn_lsb: 1, nrpn_msb: 78, min_val: 0, max_val: 120, default: 0 },
    'PD2': { cc_msb: 46, nrpn_lsb: 1, nrpn_msb: 79, min_val: 0, max_val: 100, default: 50 },
    'LEV2': { cc_msb: 47, nrpn_lsb: 1, nrpn_msb: 80, min_val: 0, max_val: 127, default: 100 },
  },
  'WAVETONE_Page2': {
    'OFS1': { cc_msb: 48, nrpn_lsb: 1, nrpn_msb: 81, min_val: -10, max_val: 10, default: 0 },
    'TBL1': { cc_msb: 49, nrpn_lsb: 1, nrpn_msb: 82, max_midi: 1, options: ['prim', 'harm'], default: 'prim' },
    'MOD': { cc_msb: 50, nrpn_lsb: 1, nrpn_msb: 83, max_midi: 3, options: ['off', 'ring mod', 'ring mod fixed', 'hard sync'], default: 'off' },
    'RSET': { cc_msb: 51, nrpn_lsb: 1, nrpn_msb: 84, max_midi: 2, options: ['off', 'on', 'random'], default: 'on' },
    'OFS2': { cc_msb: 52, nrpn_lsb: 1, nrpn_msb: 85, min_val: -10, max_val: 10, default: 0 },
    'TBL2': { cc_msb: 53, nrpn_lsb: 1, nrpn_msb: 86, max_midi: 1, options: ['prim', 'harm'], default: 'prim' },
    'DRIF': { cc_msb: 55, nrpn_lsb: 1, nrpn_msb: 88, default: 0 },
  },
  'WAVETONE_Page3': {
    'ATK': { cc_msb: 56, nrpn_lsb: 1, nrpn_msb: 89, default: 0 },
    'HOLD': { cc_msb: 57, nrpn_lsb: 1, nrpn_msb: 90, default: 127 },
    'DEC': { cc_msb: 58, nrpn_lsb: 1, nrpn_msb: 91, default: 127 },
    'NLEV': { cc_msb: 59, nrpn_lsb: 1, nrpn_msb: 92, default: 0 },
    'BASE': { cc_msb: 60, nrpn_lsb: 1, nrpn_msb: 93, default: 0 },
    'WDTH': { cc_msb: 61, nrpn_lsb: 1, nrpn_msb: 94, default: 127 },
    'TYPE': { cc_msb: 62, nrpn_lsb: 1, nrpn_msb: 95, max_midi: 2, options: ['grain nose', 'tuned noise', 'sample and hold noise'], default: 0 },
    'CHAR': { cc_msb: 63, nrpn_lsb: 1, nrpn_msb: 96, default: 0 },
  },

  // ========== FM DRUM ==========
  'FM_DRUM_Page1': {
    'TUNE': { cc_msb: 40, nrpn_lsb: 1, nrpn_msb: 73, min_val: -60, max_val: 60, default: 0 },
    'STIM': { cc_msb: 41, nrpn_lsb: 1, nrpn_msb: 74 },
    'SDEP': { cc_msb: 42, nrpn_lsb: 1, nrpn_msb: 75 },
    'ALGO': { cc_msb: 43, nrpn_lsb: 1, nrpn_msb: 76, max_midi: 6, min_val: 1, max_val: 7, default: 1 },
    'OP.C': { cc_msb: 44, nrpn_lsb: 1, nrpn_msb: 77 },
    'OP.AB': { cc_msb: 45, nrpn_lsb: 1, nrpn_msb: 78 },
    'FDBK': { cc_msb: 46, nrpn_lsb: 1, nrpn_msb: 79, max_midi: 127 },
    'FOLD': { cc_msb: 47, nrpn_lsb: 1, nrpn_msb: 80 },
  },
  'FM_DRUM_Page2': {
    'RATIO1': { cc_msb: 48, nrpn_lsb: 1, nrpn_msb: 81, min_val: 0.001, max_val: 31.75, default: 0.500 },
    'DEC1': { cc_msb: 49, nrpn_lsb: 1, nrpn_msb: 82 },
    'END1': { cc_msb: 50, nrpn_lsb: 1, nrpn_msb: 83 },
    'MOD1': { cc_msb: 51, nrpn_lsb: 1, nrpn_msb: 84 },
    'RATIO2': { cc_msb: 52, nrpn_lsb: 1, nrpn_msb: 85, min_val: 0.001, max_val: 31.75, default: 0.500 },
    'DEC2': { cc_msb: 53, nrpn_lsb: 1, nrpn_msb: 86 },
    'END2': { cc_msb: 54, nrpn_lsb: 1, nrpn_msb: 87 },
    'MOD2': { cc_msb: 55, nrpn_lsb: 1, nrpn_msb: 88 },
  },
  'FM_DRUM_Page3': {
    'HOLD': { cc_msb: 56, nrpn_lsb: 1, nrpn_msb: 89 },
    'DEC': { cc_msb: 57, nrpn_lsb: 1, nrpn_msb: 90 },
    'PH.C': { cc_msb: 58, nrpn_lsb: 1, nrpn_msb: 91, max_midi: 91 },
    'LEV': { cc_msb: 59, nrpn_lsb: 1, nrpn_msb: 92 },
    'NRST': { cc_msb: 62, nrpn_lsb: 1, nrpn_msb: 95, max_midi: 1 },
    'NRM': { cc_msb: 63, nrpn_lsb: 1, nrpn_msb: 96, max_midi: 1 },
  },
  'FM_DRUM_Page4': {
    'NHLD': { cc_msb: 70, nrpn_lsb: 1, nrpn_msb: 97 },
    'NDEC': { cc_msb: 71, nrpn_lsb: 1, nrpn_msb: 98 },
    'TRAN': { cc_msb: 72, nrpn_lsb: 1, nrpn_msb: 99, max_midi: 124 },
    'TLEV': { cc_msb: 73, nrpn_lsb: 1, nrpn_msb: 100 },
    'BASE': { cc_msb: 74, nrpn_lsb: 1, nrpn_msb: 101 },
    'WDTH': { cc_msb: 75, nrpn_lsb: 1, nrpn_msb: 102 },
    'GRAN': { cc_msb: 76, nrpn_lsb: 1, nrpn_msb: 103 },
    'NLEV': { cc_msb: 77, nrpn_lsb: 1, nrpn_msb: 104 },
  },

  // ========== SWARMER ==========
  'SWARMER': {
    'TUNE': { cc_msb: 40, nrpn_msb: 1, nrpn_lsb: 73, min_val: -60, max_val: 60, default: 0 },
    'SWRM': { cc_msb: 41, nrpn_msb: 1, nrpn_lsb: 74, min_val: 0, max_val: 120, default: 80 },
    'DET': { cc_msb: 42, nrpn_msb: 1, nrpn_lsb: 75, default: 70 },
    'MIX': { cc_msb: 43, nrpn_msb: 1, nrpn_lsb: 76, default: 127 },
    'M.OCT': { cc_msb: 44, nrpn_msb: 1, nrpn_lsb: 77, max_midi: 2, default: 0 },
    'MAIN': { cc_msb: 45, nrpn_msb: 1, nrpn_lsb: 78, min_val: 0, max_val: 120, default: 80 },
    'ANIM': { cc_msb: 46, nrpn_msb: 1, nrpn_lsb: 79, default: 15 },
    'N.MOD': { cc_msb: 47, nrpn_msb: 1, nrpn_lsb: 80, default: 20 },
  },

  // ========== FILTER ==========
  'FILTER': {
    'ATK': { cc_msb: 20, nrpn_lsb: 1, nrpn_msb: 16 },
    'DEC': { cc_msb: 21, nrpn_lsb: 1, nrpn_msb: 17, default: 64 },
    'SUS': { cc_msb: 22, nrpn_lsb: 1, nrpn_msb: 18 },
    'REL': { cc_msb: 23, nrpn_lsb: 1, nrpn_msb: 19, default: 64 },
    'FREQ': { cc_msb: 16, nrpn_lsb: 1, nrpn_msb: 20, default: 127 },
    'RESO': { cc_msb: 17, nrpn_lsb: 1, nrpn_msb: 21 },
    'TYPE': { cc_msb: 18, nrpn_lsb: 1, nrpn_msb: 22 },
    'ENV.Depth': { cc_msb: 24, nrpn_lsb: 1, nrpn_msb: 26, min_val: -64, max_val: 64 },
    'ENV.Delay': { cc_msb: 19, nrpn_lsb: 1, nrpn_msb: 23 },
    'KEY.Tracking': { cc_msb: 26, nrpn_lsb: 1, nrpn_msb: 69 },
    'BASE': { cc_msb: 27, nrpn_lsb: 1, nrpn_msb: 24 },
    'WDTH': { cc_msb: 28, nrpn_lsb: 1, nrpn_msb: 25 },
    'Env.Reset': { cc_msb: 25, nrpn_lsb: 1, nrpn_msb: 68, max_midi: 1, options: ['off', 'on'], default: 'off' },
  },

  // ========== AMP ==========
  'AMP': {
    'ATK': { cc_msb: 84, nrpn_lsb: 1, nrpn_msb: 30, default: 8 },
    'HOLD': { cc_msb: 85, nrpn_lsb: 1, nrpn_msb: 31, default: 127 },
    'DEC': { cc_msb: 86, nrpn_lsb: 1, nrpn_msb: 32, default: 32 },
    'SUS': { cc_msb: 87, nrpn_lsb: 1, nrpn_msb: 33, default: 96 },
    'REL': { cc_msb: 88, nrpn_lsb: 1, nrpn_msb: 34, default: 24 },
    'Env.RSET': { cc_msb: 92, nrpn_lsb: 1, nrpn_msb: 41, max_midi: 1, options: ['off', 'on'], default: 'on' },
    'MODE': { cc_msb: 91, nrpn_lsb: 1, nrpn_msb: 40, max_midi: 1, options: ['AHD', 'ADSR'], default: 'ADSR' },
    'PAN': { cc_msb: 89, nrpn_lsb: 1, nrpn_msb: 38, min_val: -64, max_val: 64, default: 0 },
    'VOL': { cc_msb: 90, nrpn_lsb: 1, nrpn_msb: 39, default: 110 },
  },

  // ========== LFO ==========
  'LFO': {
    'SPD': { cc_msb: 102, nrpn_lsb: 1, nrpn_msb: 42, default: 48 },
    'MULT': { cc_msb: 103, nrpn_lsb: 1, nrpn_msb: 43, max_midi: 11, min_val: 1, max_val: 2000, default: 2 },
    'FADE': { cc_msb: 104, nrpn_lsb: 1, nrpn_msb: 44, min_val: -64, max_val: 63, default: 0 },
    'DEST': { cc_msb: 105, nrpn_lsb: 1, nrpn_msb: 45, max_midi: 50, min_midi: 25, default: 'none' },
    'WAVE': { cc_msb: 106, nrpn_lsb: 1, nrpn_msb: 46, max_midi: 6, options: ['tri', 'sine', 'sqr', 'saw', 'expo', 'ramp', 'rand'], default: 'sine' },
    'SPH': { cc_msb: 107, nrpn_lsb: 1, nrpn_msb: 47 },
    'MODE': { cc_msb: 108, nrpn_lsb: 1, nrpn_msb: 48, max_midi: 4 },
    'DEPTH': { cc_msb: 109, nrpn_lsb: 1, nrpn_msb: 49, min_val: -64, max_val: 64, default: 0 },
  },

  // ========== FX ==========
  'FX': {
    'BR': { cc_msb: 78, nrpn_lsb: 1, nrpn_msb: 5, default: 0 },
    'OVER': { cc_msb: 81, nrpn_lsb: 1, nrpn_msb: 8, default: 0 },
    'SRR': { cc_msb: 79, nrpn_lsb: 1, nrpn_msb: 6, default: 0 },
    'SR.RT': { cc_msb: 80, nrpn_lsb: 1, nrpn_msb: 7, max_midi: 1, options: ['pre', 'post'], default: 'pre' },
    'OD.RT': { cc_msb: 82, nrpn_lsb: 1, nrpn_msb: 9, max_midi: 1, options: ['pre', 'post'], default: 'pre' },
    'DEL': { cc_msb: 30, nrpn_lsb: 1, nrpn_msb: 36, default: 0 },
    'REV': { cc_msb: 31, nrpn_lsb: 1, nrpn_msb: 37, default: 0 },
    'CHR': { cc_msb: 29, nrpn_lsb: 1, nrpn_msb: 35, default: 0 },
  },
};
