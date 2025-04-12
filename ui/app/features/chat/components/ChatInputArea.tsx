// src/features/chat/components/ChatInputArea.tsx
import React, { useRef, useEffect } from 'react';
import type { ChangeEvent, KeyboardEvent } from 'react';
import { Send } from 'lucide-react';
// Import custom hooks if you created them, e.g.:
// import { useTextAreaAutoSize } from '../hooks/useTextAreaAutoSize';

interface ChatInputAreaProps {
  /** Current value of the text input. */
  input: string;
  /** Callback to update the input value. */
  setInput: (value: string) => void;
  /** Callback to trigger sending the message. */
  onSendMessage: () => void;
  /** Indicates if a message is currently being processed (disables input/button). */
  isLoading: boolean;
  /** The rendered MIDI Device Selector component. */
  midiDeviceSelector: React.ReactNode;
  /** The rendered API Key Manager component UI. */
  apiKeyManager: React.ReactNode;
}

/**
 * Renders the chat input area including the textarea, send button,
 * MIDI device selector, and API key management UI.
 */
const ChatInputArea: React.FC<ChatInputAreaProps> = ({
  input,
  setInput,
  onSendMessage,
  isLoading,
  midiDeviceSelector, // Render this prop directly
  apiKeyManager,    // Render this prop directly
}) => {
  const inputRef = useRef<HTMLTextAreaElement>(null);

  // --- Focus Input on Initial Mount ---
  // (Consider if this focus logic should live here or in the parent ChatView)
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  // --- Auto-adjust textarea height ---
  // (This could be moved to a useTextAreaAutoSize hook)
  const handleTextAreaInput = (e: ChangeEvent<HTMLTextAreaElement>) => {
    const target = e.target;
    setInput(target.value);

    // Reset height to recalculate scrollHeight correctly
    target.style.height = 'auto';
    // Set height based on content, respecting min-height via CSS
    target.style.height = `${target.scrollHeight}px`;
  };

  // --- Handle Enter Key Press ---
  const handleKeyPress = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault(); // Prevent default Enter behavior (new line)
      if (input.trim() !== '' && !isLoading) {
        onSendMessage();
        // Reset height after sending
        if (inputRef.current) {
            inputRef.current.style.height = 'auto'; // Or back to min-height if needed
        }
      }
    }
  };

  // --- Handle Send Button Click ---
  const handleSendClick = () => {
    if (input.trim() !== '' && !isLoading) {
      onSendMessage();
      // Reset height after sending
      if (inputRef.current) {
          inputRef.current.style.height = 'auto'; // Or back to min-height if needed
      }
    }
  };

  const isSendDisabled = input.trim() === '' || isLoading;

  return (
    <div className="p-4 bg-gray-800 border-t border-gray-700 flex-shrink-0">
      {/* Textarea container with focus ring */}
      <div className="relative">
        <div className="border border-gray-700 rounded-lg bg-gray-900 overflow-hidden focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-offset-gray-800 focus-within:ring-blue-500 focus-within:border-blue-500 transition-shadow duration-150">
          <textarea
            ref={inputRef}
            className="w-full p-3 pr-28 pb-4 resize-none outline-none min-h-[5rem] max-h-[15rem] overflow-y-auto border-none bg-transparent text-white placeholder-gray-500 disabled:opacity-60" // Added max-h, adjusted padding
            placeholder="Type your message..."
            value={input}
            onChange={handleTextAreaInput}
            onKeyDown={handleKeyPress}
            disabled={isLoading}
            rows={1} // Start with one row, auto-sizing will handle expansion
          />

          {/* Controls inside the textarea container */}
          <div className="absolute bottom-3 right-3 flex items-center gap-2">
            {/* MIDI Selector */}
            {/* Render the component passed via props */}
            {midiDeviceSelector}

            {/* Send Button */}
            <button
              onClick={handleSendClick}
              disabled={isSendDisabled}
              className={`p-2 rounded-lg flex-shrink-0 transition-colors duration-150 ease-in-out ${
                isSendDisabled
                  ? 'text-gray-600 cursor-not-allowed'
                  : 'text-blue-400 hover:text-indigo-400 hover:bg-gray-700'
              }`}
              aria-label="Send message"
              title="Send message"
            >
              <Send size={20} />
            </button>
          </div>
        </div>
      </div>

      {/* Hint text and API Key Manager */}
      <div className="flex justify-between items-start mt-2 gap-4"> {/* Use items-start for better alignment if API manager grows */}
        <p className="text-xs text-gray-500 pt-1 flex-shrink-0"> {/* Added pt-1 */}
          Enter to send, Shift+Enter for new line
        </p>

        {/* API Key Management UI */}
        {/* Render the component passed via props */}
        <div className="flex-shrink"> {/* Allow API manager to take space but not push hint text away excessively */}
             {apiKeyManager}
        </div>
      </div>
    </div>
  );
};

export { ChatInputArea };