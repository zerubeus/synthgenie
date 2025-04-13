import React, { useRef, useEffect } from 'react';
import type { ChangeEvent, KeyboardEvent } from 'react';
import { Send } from 'lucide-react';

interface ChatInputAreaProps {
  input: string;
  setInput: (value: string) => void;
  onSendMessage: () => void;
  isLoading: boolean;
  midiDeviceSelector: React.ReactNode;
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
  midiDeviceSelector,
  apiKeyManager,
}) => {
  const inputRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleTextAreaInput = (e: ChangeEvent<HTMLTextAreaElement>) => {
    const target = e.target;
    setInput(target.value);

    target.style.height = 'auto';
    target.style.height = `${target.scrollHeight}px`;
  };

  const handleKeyPress = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (input.trim() !== '' && !isLoading) {
        onSendMessage();
        if (inputRef.current) {
            inputRef.current.style.height = 'auto';
        }
      }
    }
  };

  const handleSendClick = () => {
    if (input.trim() !== '' && !isLoading) {
      onSendMessage();
      if (inputRef.current) {
          inputRef.current.style.height = 'auto';
      }
    }
  };

  const isSendDisabled = input.trim() === '' || isLoading;

  return (
    <div className="p-4 bg-gray-800 border-t border-gray-700 flex-shrink-0">
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
            rows={1}
          />

          <div className="absolute bottom-3 right-3 flex items-center gap-2">
            {midiDeviceSelector}
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

      <div className="flex justify-between items-start mt-2 gap-4">
        <p className="text-xs text-gray-500 pt-1 flex-shrink-0">
          Enter to send, Shift+Enter for new line
        </p>

        <div className="flex-shrink">
             {apiKeyManager}
        </div>
      </div>
    </div>
  );
};

export { ChatInputArea };