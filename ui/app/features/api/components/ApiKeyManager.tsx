// src/features/api/components/ApiKeyManager.tsx
import React from 'react';
import type { ChangeEvent, KeyboardEvent } from 'react';
import { Key } from 'lucide-react'; // Import the icon

interface ApiKeyManagerProps {
  /** The current API key (empty string if not set). */
  apiKey: string;
  /** Whether the input field is visible. */
  showInput: boolean;
  /** The current value in the input field. */
  inputValue: string;
  /** Handler for input field value changes. */
  onInputChange: (event: ChangeEvent<HTMLInputElement>) => void;
  /** Handler for saving the entered API key. */
  onSave: () => void;
  /** Handler for toggling the input visibility (or clearing the key if set). */
  onToggle: () => void;
  /** Handler for explicitly clearing the API key. */
  onClear: () => void;
  /** Optional: Flag to disable interactions. */
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
  onToggle, // This handles both showing input AND triggering clear based on apiKey presence
  disabled = false,
}) => {
  const hasApiKey = !!apiKey;

  // Handler for Enter key press in the input field
  const handleInputKeyPress = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault(); // Prevent potential form submission
      onSave();
    }
  };

  // Determine button text and action based on whether a key exists
  const buttonText = hasApiKey ? 'DELETE API KEY' : 'SET API KEY';
  const buttonAction = onToggle; // The toggle handler decides whether to clear or show input

  return (
    <div className="flex flex-col items-end text-xs"> {/* Align content to the right */}
      {/* Main Toggle/Clear Button */}
      <button
        onClick={buttonAction}
        disabled={disabled}
        className={`flex items-center mb-1 ${
          hasApiKey
            ? 'text-red-400 hover:text-red-500' // Style for delete action
            : 'text-blue-400 hover:text-indigo-400' // Style for set action
        } transition-colors disabled:opacity-50 disabled:cursor-not-allowed`}
        aria-label={buttonText}
      >
        <Key size={14} className="mr-1" />
        {buttonText}
      </button>

      {/* Conditional Input Field and Save Button */}
      {showInput && !hasApiKey && ( // Only show if toggled AND no key is currently set
        <div className="flex w-full max-w-xs mt-1"> {/* Control width */}
          <input
            type="text" // Use password type? Might be better for keys. type="password"
            value={inputValue}
            onChange={onInputChange}
            onKeyDown={handleInputKeyPress}
            placeholder="Enter your API key"
            disabled={disabled}
            className="flex-1 p-2 rounded-l-md bg-gray-700 border border-gray-600 text-white text-xs focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 disabled:opacity-50"
            aria-label="API Key Input"
            autoFocus // Focus the input when it appears
          />
          <button
            onClick={onSave}
            disabled={disabled || inputValue.trim() === ''} // Disable if input is empty
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