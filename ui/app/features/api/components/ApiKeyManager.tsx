import React from 'react';
import type { ChangeEvent, KeyboardEvent } from 'react';

import { Key } from 'lucide-react';

interface ApiKeyManagerProps {
  apiKey: string;
  showInput: boolean;
  inputValue: string;
  onInputChange: (event: ChangeEvent<HTMLInputElement>) => void;
  onSave: () => void;
  onToggle: () => void;
  onClear: () => void;
  disabled?: boolean;
}

/**
 * UI component for managing the SynthGenie API Key.
 * Provides a button to set/delete the key and an input field for entry.
 */
export const ApiKeyManager: React.FC<ApiKeyManagerProps> = ({
  apiKey,
  showInput,
  inputValue,
  onInputChange,
  onSave,
  onToggle,
  disabled = false,
}) => {
  const hasApiKey = !!apiKey;

  const handleInputKeyPress = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      onSave();
    }
  };

  const buttonText = hasApiKey ? 'DELETE API KEY' : 'SET API KEY';
  const buttonAction = onToggle;

  return (
    <div className="flex flex-col items-end text-xs">
      <button
        onClick={buttonAction}
        disabled={disabled}
        className={`flex items-center mb-1 ${
          hasApiKey ? 'text-red-400 hover:text-red-500' : 'text-blue-400 hover:text-indigo-400'
        } transition-colors disabled:opacity-50 disabled:cursor-not-allowed`}
        aria-label={buttonText}
      >
        <Key size={14} className="mr-1" />
        {buttonText}
      </button>

      {showInput && !hasApiKey && (
        <div className="flex w-full max-w-xs mt-1">
          <input
            type="text"
            value={inputValue}
            onChange={onInputChange}
            onKeyDown={handleInputKeyPress}
            placeholder="Enter your API key"
            disabled={disabled}
            className="flex-1 p-2 rounded-l-md bg-gray-700 border border-gray-600 text-white text-xs focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 disabled:opacity-50"
            aria-label="API Key Input"
            autoFocus
          />
          <button
            onClick={onSave}
            disabled={disabled || inputValue.trim() === ''}
            className="bg-blue-500 hover:bg-blue-600 text-white rounded-r-md px-3 py-1 text-xs font-medium focus:outline-none focus:ring-1 focus:ring-blue-500 focus:ring-offset-1 focus:ring-offset-gray-800 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            aria-label="Save API Key"
          >
            Save
          </button>
        </div>
      )}
    </div>
  );
};
