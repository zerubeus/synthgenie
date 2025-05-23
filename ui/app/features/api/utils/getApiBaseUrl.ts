import type { SynthType } from '../types';

/**
 * Determines the base URL for the SynthGenie API based on the environment.
 * Checks for local development environment variables.
 *
 * @returns The base URL string (e.g., 'http://localhost:8080' or 'https://api.synthgenie.com').
 */
export const getApiBaseUrl = (): string => {
  const isLocal =
    import.meta.env.MODE === 'development' &&
    import.meta.env.VITE_API_ENV === 'local';

  if (isLocal) {
    const localPort = import.meta.env.VITE_API_PORT || '8080';
    const localHost = import.meta.env.VITE_API_HOST || 'localhost';
    return `http://${localHost}:${localPort}`;
  }

  return 'https://api.synthgenie.com';
};

/**
 * Detects the synthesizer type from a device name.
 * 
 * @param deviceName The name of the MIDI device
 * @returns The synthesizer type or null if not supported
 */
export const detectSynthType = (deviceName: string): SynthType | null => {
  const name = deviceName.toLowerCase();
  
  if (name.includes('moog') || name.includes('subsequent') || name.includes('sub37')) {
    return 'sub37';
  }
  
  if (name.includes('digitone')) {
    return 'digitone';
  }
  
  return null;
};

/**
 * Gets the appropriate API endpoint for a synthesizer type.
 * 
 * @param synthType The synthesizer type
 * @returns The API endpoint path
 */
export const getSynthEndpoint = (synthType: SynthType): string => {
  switch (synthType) {
    case 'sub37':
      return '/agent/sub37/prompt';
    case 'digitone':
      return '/agent/digitone/prompt';
    default:
      throw new Error(`Unsupported synthesizer type: ${synthType}`);
  }
};
