import { useState, useCallback, useEffect } from 'react';

const API_KEY_STORAGE_KEY = 'synthgenie_api_key';

interface UseApiKeyReturn {
  apiKey: string;
  apiKeyInputValue: string;
  showApiKeyInput: boolean;
  setApiKeyInputValue: React.Dispatch<React.SetStateAction<string>>;
  handleApiKeyToggle: () => void;
  handleSaveApiKey: () => void;
  handleClearApiKey: () => void;
}

/**
 * Custom hook to manage the SynthGenie API key state, including
 * persistence in localStorage and handling the input UI visibility.
 */
export const useApiKey = (): UseApiKeyReturn => {
  const [apiKey, setApiKey] = useState<string>(() => {
    try {
      return localStorage.getItem(API_KEY_STORAGE_KEY) || '';
    } catch (error) {
      console.error('Error reading API key from localStorage:', error);
      return '';
    }
  });

  const [showApiKeyInput, setShowApiKeyInput] = useState(false);
  const [apiKeyInputValue, setApiKeyInputValue] = useState('');

  useEffect(() => {
    try {
      if (apiKey) {
        localStorage.setItem(API_KEY_STORAGE_KEY, apiKey);
      } else {
        localStorage.removeItem(API_KEY_STORAGE_KEY);
      }
    } catch (error) {
      console.error('Error writing API key to localStorage:', error);
    }
  }, [apiKey]);

  const handleClearApiKey = useCallback(() => {
    setApiKey('');
    setShowApiKeyInput(false);
    setApiKeyInputValue('');
    console.log('API Key cleared.');
  }, []);

  const handleApiKeyToggle = useCallback(() => {
    if (apiKey) {
      handleClearApiKey();
    } else {
      setShowApiKeyInput(true);
      setApiKeyInputValue('');
    }
  }, [apiKey, handleClearApiKey]);

  const handleSaveApiKey = useCallback(() => {
    const trimmedKey = apiKeyInputValue.trim();
    if (trimmedKey) {
      setApiKey(trimmedKey);
      setShowApiKeyInput(false);
      setApiKeyInputValue('');
    } else {
      console.warn('Attempted to save an empty API key.');
    }
  }, [apiKeyInputValue]);

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
