import { useMutation } from '@tanstack/react-query';
import type { UseMutationResult } from '@tanstack/react-query';
import type { MidiAction } from '../types';
import { getApiBaseUrl } from '../utils/getApiBaseUrl';

type PromptInput = string;

interface ApiError extends Error {
  status?: number;
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
    if (!apiKey) {
      const error: ApiError = new Error('No API key set');
      throw error;
    }

    const apiBaseUrl = getApiBaseUrl();
    const endpoint = `${apiBaseUrl}/agent/prompt`;

    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': apiKey,
      },
      body: JSON.stringify({ prompt }),
    });

    if (!response.ok) {
      let error: ApiError;
      if (response.status === 401) {
        error = new Error('Invalid API key');
        error.status = 401;
      } else {
        error = new Error(
          `Network response was not ok (Status: ${response.status})`
        );
        error.status = response.status;
      }
      throw error;
    }

    try {
      const data = await response.json();
      if (!Array.isArray(data)) {
        throw new Error('API response was not an array as expected.');
      }
      return data as MidiAction[];
    } catch (jsonError) {
      console.error('Failed to parse API response JSON:', jsonError);
      const error: ApiError = new Error('Failed to parse API response.');
      throw error;
    }
  };

  return useMutation<MidiAction[], ApiError, PromptInput>({
    mutationFn,
  });
};
