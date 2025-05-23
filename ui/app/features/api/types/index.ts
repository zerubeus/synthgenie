/**
 * Determines the base URL for the SynthGenie API based on the environment.
 * Checks for local development environment variables.
 *
 * @returns The base URL string (e.g., 'http://localhost:8080' or 'https://api.synthgenie.com').
 */
export const getApiBaseUrl = (): string => {
  const isLocal =
    process.env.NODE_ENV === 'development' &&
    process.env.VITE_API_ENV === 'local';

  return isLocal ? 'http://localhost:8080' : 'https://api.synthgenie.com';
};

/**
 * Supported synthesizer types for API endpoints
 */
export type SynthType = 'sub37' | 'digitone';

/**
 * New API response structure from SynthGenie API that supports multiple MIDI message types
 */
export type SynthGenieResponse = {
  used_tool: string;
  midi_channel: number;
  value: number;
  midi_cc?: number | null;
  midi_cc_lsb?: number | null;
  nrpn_msb?: number | null;
  nrpn_lsb?: number | null;
};

/**
 * Response when the user query is ambiguous or not related to sound design
 */
export type SynthGenieAmbiguousResponse = {
  message: string;
};

/**
 * Union type for all possible API responses
 */
export type ApiResponse = SynthGenieResponse | SynthGenieAmbiguousResponse;

/**
 * Legacy MIDI action type for backward compatibility
 * @deprecated Use SynthGenieResponse instead
 */
export type MidiAction = {
  used_tool: string;
  midi_cc: number;
  midi_channel: number;
  value: number;
};

/**
 * Type guard to check if response is a SynthGenieResponse
 */
export const isSynthGenieResponse = (response: ApiResponse): response is SynthGenieResponse => {
  return 'used_tool' in response && 'midi_channel' in response && 'value' in response;
};

/**
 * Type guard to check if response is ambiguous
 */
export const isSynthGenieAmbiguousResponse = (response: ApiResponse): response is SynthGenieAmbiguousResponse => {
  return 'message' in response && !('used_tool' in response);
};
