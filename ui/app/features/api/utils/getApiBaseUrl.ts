/**
 * Determines the base URL for the SynthGenie API based on the environment.
 * Checks for local development environment variables.
 *
 * @returns The base URL string (e.g., 'http://localhost:8080' or 'https://api.synthgenie.com').
 */
export const getApiBaseUrl = (): string => {
  // Check if running in development mode AND specifically targeting the local API
  // Ensure VITE_API_ENV is set in your .env.development or similar
  const isLocal =
    process.env.NODE_ENV === 'development' &&
    process.env.VITE_API_ENV === 'local';

  // Return the appropriate URL
  return isLocal ? 'http://localhost:8080' : 'https://api.synthgenie.com';
};
