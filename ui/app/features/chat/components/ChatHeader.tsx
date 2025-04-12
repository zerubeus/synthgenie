// src/features/chat/components/ChatHeader.tsx
import React from 'react';
import { Trash2 } from 'lucide-react';

interface ChatHeaderProps {
  /** The name of the currently selected MIDI device, if any. */
  selectedDevice: string | null | undefined;
  /** Callback function to trigger when the clear chat button is clicked. */
  onClearChat: () => void;
}

/**
 * Displays the header for the Chat application, including the title
 * and a button to clear the chat history.
 */
const ChatHeader: React.FC<ChatHeaderProps> = ({
  selectedDevice,
  onClearChat,
}) => {
  return (
    <header className="bg-gray-900 border-b border-gray-800 p-4 flex justify-between items-center flex-shrink-0">
      <div>
        <h1 className="text-xl sm:text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400">
          SynthGenie{' '}
          {selectedDevice && (
            <span className="text-blue-400 font-medium text-lg sm:text-xl align-middle">
              MIDI
            </span>
          )}
        </h1>
        {selectedDevice && (
           <p className="text-xs text-gray-500 mt-1">Connected to: {selectedDevice}</p>
        )}
      </div>

      <button
        onClick={onClearChat}
        className="p-2 text-gray-400 hover:text-blue-400 hover:bg-gray-800 rounded-full transition-colors duration-150 ease-in-out"
        aria-label="Clear chat"
        title="Clear chat"
      >
        <Trash2 size={20} />
      </button>
    </header>
  );
};

export { ChatHeader };