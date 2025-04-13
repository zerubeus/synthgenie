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
