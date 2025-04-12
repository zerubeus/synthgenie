// src/features/api/hooks/useSynthGenieApi.ts
import { useMutation } from '@tanstack/react-query';
import type { UseMutationResult } from '@tanstack/react-query';
import type { MidiAction } from '../types'; // Import the return type
import { getApiBaseUrl } from '../utils/getApiBaseUrl'; // Import the URL utility

// Define the type for the mutation function's input variable
type PromptInput = string;

// Define the structure of potential known API errors
// Extend this as needed based on your API's error responses
interface ApiError extends Error {
  status?: number; // Optional HTTP status code
}

/**
 * Custom hook to provide a mutation function for sending prompts to the
 * SynthGenie API (`/agent/prompt`). Handles the fetch request, headers,
 * and basic response/error handling.
 *
 * @param apiKey The current API key to use for the request header.
 *               The mutation will fail if the key is missing or invalid.
 * @returns A TanStack Query UseMutationResult object for the prompt mutation.
 *          Includes status flags (isLoading, isError, etc.), data, error, and the mutate function.
 */
export const useSynthGenieApi = (
  apiKey: string | null | undefined
): UseMutationResult<MidiAction[], ApiError, PromptInput> => {
  const mutationFn = async (prompt: PromptInput): Promise<MidiAction[]> => {
    // --- Pre-flight check: API Key ---
    if (!apiKey) {
      // Throw an error that can be caught by onError or checked in the calling component
      const error: ApiError = new Error('No API key set');
      throw error;
    }

    const apiBaseUrl = getApiBaseUrl();
    const endpoint = `${apiBaseUrl}/agent/prompt`;

    // --- Perform Fetch Request ---
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': apiKey, // Include the API key in the header
      },
      body: JSON.stringify({ prompt }), // Send prompt in the request body
    });

    // --- Handle Response Status ---
    if (!response.ok) {
      let error: ApiError;
      if (response.status === 401) {
        // Specific error for Unauthorized
        error = new Error('Invalid API key');
        error.status = 401;
      } else {
        // Generic error for other non-OK statuses
        error = new Error(
          `Network response was not ok (Status: ${response.status})`
        );
        error.status = response.status;
        // You could try to parse error details from response.json() here if your API provides them
        // try {
        //   const errorData = await response.json();
        //   error.message = errorData.message || error.message;
        // } catch (parseError) { /* Ignore if body isn't valid JSON */ }
      }
      throw error; // Throw the constructed error
    }

    // --- Process Successful Response ---
    // Parse the JSON response body, expecting an array of MidiAction objects
    try {
      const data = await response.json();
      // Optional: Add validation here to ensure data matches MidiAction[] structure
      if (!Array.isArray(data)) {
        // Basic check
        throw new Error('API response was not an array as expected.');
      }
      return data as MidiAction[];
    } catch (jsonError) {
      console.error('Failed to parse API response JSON:', jsonError);
      const error: ApiError = new Error('Failed to parse API response.');
      throw error;
    }
  };

  // --- Return useMutation hook ---
  // Note: onSuccess and onError are typically handled in the component/hook
  // *using* this mutation hook (like useChatMessages), allowing UI-specific side effects there.
  return useMutation<MidiAction[], ApiError, PromptInput>({
    mutationFn,
    // You could configure retry logic, etc. here if needed
    // retry: false,
  });
};
