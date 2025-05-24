import { useMutation } from '@tanstack/react-query';
import { getApiBaseUrl, detectSynthType, getSynthEndpoint } from '../utils/getApiBaseUrl';
import type { UseMutationResult } from '@tanstack/react-query';

import type { SynthGenieResponse, SynthGenieAmbiguousResponse } from '../types';
import { isSynthGenieResponse, isSynthGenieAmbiguousResponse } from '../types';

type PromptInput = {
  prompt: string;
  deviceName: string;
};

interface ApiError extends Error {
  status?: number;
}

/**
 * Custom hook to provide a mutation function for sending prompts to the
 * SynthGenie API. Automatically detects synthesizer type and uses the
 * appropriate endpoint. Handles the new response format with multiple
 * MIDI message types.
 *
 * @param apiKey The current API key to use for the request header.
 *               The mutation will fail if the key is missing or invalid.
 * @returns A TanStack Query UseMutationResult object for the prompt mutation.
 *          Includes status flags (isLoading, isError, etc.), data, error, and the mutate function.
 */
export const useSynthGenieApi = (
  apiKey: string | null | undefined
): UseMutationResult<SynthGenieResponse[], ApiError, PromptInput> => {
  const mutationFn = async (input: PromptInput): Promise<SynthGenieResponse[]> => {
    if (!apiKey) {
      const error: ApiError = new Error('No API key set');
      throw error;
    }

    // Detect synthesizer type from device name
    const synthType = detectSynthType(input.deviceName);
    if (!synthType) {
      const error: ApiError = new Error(`Unsupported synthesizer: ${input.deviceName}`);
      error.status = 400;
      throw error;
    }

    const apiBaseUrl = getApiBaseUrl();
    const endpoint = `${apiBaseUrl}${getSynthEndpoint(synthType)}`;

    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': apiKey,
      },
      body: JSON.stringify({ prompt: input.prompt }),
    });

    if (!response.ok) {
      let error: ApiError;
      
      if (response.status === 401) {
        error = new Error('Invalid API key');
        error.status = 401;
      } else if (response.status === 422) {
        // Handle the "not about sound design" error
        try {
          const errorData = await response.json();
          error = new Error(errorData.detail || 'This prompt is not about sound design.');
          error.status = 422;
        } catch {
          error = new Error('This prompt is not about sound design.');
          error.status = 422;
        }
      } else {
        error = new Error(`Network response was not ok (Status: ${response.status})`);
        error.status = response.status;
      }
      throw error;
    }

    try {
      const data = await response.json();
      
      // Check if response is ambiguous (fallback for non-422 ambiguous responses)
      if (isSynthGenieAmbiguousResponse(data)) {
        const error: ApiError = new Error(data.message);
        error.status = 422;
        throw error;
      }
      
      // Validate that we got an array of SynthGenieResponse objects
      if (!Array.isArray(data)) {
        throw new Error('API response was not an array as expected.');
      }
      
      // Validate each item in the array
      for (const item of data) {
        if (!isSynthGenieResponse(item)) {
          throw new Error('API response contains invalid item format.');
        }
      }
      
      return data as SynthGenieResponse[];
    } catch (jsonError) {
      console.error('Failed to parse API response JSON:', jsonError);
      const error: ApiError = new Error('Failed to parse API response.');
      throw error;
    }
  };

  return useMutation<SynthGenieResponse[], ApiError, PromptInput>({
    mutationFn,
  });
};
