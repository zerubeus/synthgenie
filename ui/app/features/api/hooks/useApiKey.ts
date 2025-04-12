// src/features/api/hooks/useApiKey.ts
import { useState, useCallback, useEffect } from 'react';

const API_KEY_STORAGE_KEY = 'synthgenie_api_key';

interface UseApiKeyReturn {
  /** The currently stored API key, or an empty string if not set. */
  apiKey: string;
  /** The temporary value entered in the API key input field. */
  apiKeyInputValue: string;
  /** Whether the API key input field should be visible. */
  showApiKeyInput: boolean;
  /** Function to update the temporary input value. */
  setApiKeyInputValue: React.Dispatch<React.SetStateAction<string>>;
  /** Toggles the visibility of the API key input field. */
  handleApiKeyToggle: () => void;
  /** Saves the temporary input value as the new API key. */
  handleSaveApiKey: () => void;
  /** Clears the currently stored API key. */
  handleClearApiKey: () => void;
}

/**
 * Custom hook to manage the SynthGenie API key state, including
 * persistence in localStorage and handling the input UI visibility.
 */
export const useApiKey = (): UseApiKeyReturn => {
  // Initialize API key from localStorage on initial render
  const [apiKey, setApiKey] = useState<string>(() => {
    try {
      return localStorage.getItem(API_KEY_STORAGE_KEY) || '';
    } catch (error) {
      console.error('Error reading API key from localStorage:', error);
      return ''; // Fallback to empty string on error
    }
  });

  const [showApiKeyInput, setShowApiKeyInput] = useState(false);
  const [apiKeyInputValue, setApiKeyInputValue] = useState('');

  // Persist API key to localStorage whenever it changes
  useEffect(() => {
    try {
      if (apiKey) {
        localStorage.setItem(API_KEY_STORAGE_KEY, apiKey);
      } else {
        // Ensure removal if apiKey becomes empty/null
        localStorage.removeItem(API_KEY_STORAGE_KEY);
      }
    } catch (error) {
      console.error('Error writing API key to localStorage:', error);
    }
  }, [apiKey]);

  const handleApiKeyToggle = useCallback(() => {
    if (apiKey) {
      // If key exists, the toggle action should clear it
      handleClearApiKey(); // Call the clear handler directly
    } else {
      // If no key exists, show the input field
      setShowApiKeyInput(true);
      setApiKeyInputValue(''); // Clear previous input value
    }
  }, [apiKey]); // Depends on apiKey state

  const handleSaveApiKey = useCallback(() => {
    const trimmedKey = apiKeyInputValue.trim();
    if (trimmedKey) {
      setApiKey(trimmedKey); // Update state, which triggers useEffect for localStorage
      setShowApiKeyInput(false); // Hide input after saving
      setApiKeyInputValue(''); // Clear the temporary input value
    } else {
      // Optional: Add feedback if input is empty?
      console.warn('Attempted to save an empty API key.');
    }
  }, [apiKeyInputValue]); // Depends on the temporary input value

  const handleClearApiKey = useCallback(() => {
    setApiKey(''); // Update state to empty string
    setShowApiKeyInput(false); // Ensure input is hidden
    setApiKeyInputValue(''); // Clear temporary input value
    // localStorage is handled by the useEffect triggered by setApiKey('')
    console.log('API Key cleared.');
  }, []); // No dependencies needed

  return {
    apiKey,
    apiKeyInputValue,
    showApiKeyInput,
    setApiKeyInputValue,
    handleApiKeyToggle,
    handleSaveApiKey,
    handleClearApiKey,
  };
};
