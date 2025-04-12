// src/features/chat/components/MessageList.tsx
import React from 'react';
import type { RefObject } from 'react';
import { Bot } from 'lucide-react';
import type { Message } from '../types';
import { MessageItem } from './MessageItem';

interface MessageListProps {
  /** The array of messages to display. */
  messages: Message[];
  /** Whether the assistant is currently processing. */
  isLoading: boolean;
  /** Ref object pointing to the element used for auto-scrolling. */
  messagesEndRef: RefObject<HTMLDivElement | null>;
  /** Callback function to handle copying message content. */
  onCopyMessage: (content: string) => void;
}

/**
 * Renders the scrollable list of chat messages and the loading indicator.
 */
const MessageList: React.FC<MessageListProps> = ({
  messages,
  isLoading,
  messagesEndRef,
  onCopyMessage,
}) => {
  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-gray-900 h-[60vh]">
      {messages.map((message, index) => (
        <MessageItem
          key={message.id ?? index}
          message={message}
          onCopyMessage={onCopyMessage}
        />
      ))}

      {isLoading && (
        <div className="flex justify-start">
          <div className="max-w-3xl p-4 rounded-lg flex gap-3 items-start bg-gray-800 border border-gray-700 shadow-sm rounded-bl-none">
            <div className="flex-shrink-0 w-6 h-6 rounded-full bg-gray-700 flex items-center justify-center">
              <Bot size={14} className="text-gray-300" />
            </div>
            <div className="flex items-center space-x-2 pt-1">
              <div className="w-2 h-2 rounded-full bg-blue-400 animate-bounce" style={{ animationDelay: '0ms' }}></div>
              <div className="w-2 h-2 rounded-full bg-indigo-400 animate-bounce" style={{ animationDelay: '200ms' }}></div>
              <div className="w-2 h-2 rounded-full bg-purple-400 animate-bounce" style={{ animationDelay: '400ms' }}></div>
            </div>
          </div>
        </div>
      )}

      <div ref={messagesEndRef} />
    </div>
  );
};

export { MessageList };