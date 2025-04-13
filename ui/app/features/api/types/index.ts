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
 * Represents the structure of a MIDI action returned by the SynthGenie API.
 */
export type MidiAction = {
  used_tool: string;
  midi_cc: number;
  midi_channel: number;
  value: number;
};
