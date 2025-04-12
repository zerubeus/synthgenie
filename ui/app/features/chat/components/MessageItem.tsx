// src/features/chat/components/MessageItem.tsx
import React from 'react';
import { User, Bot, Copy } from 'lucide-react';
import type { Message } from '../types'; // Use 'import type'

interface MessageItemProps {
  /** The message object to display. */
  message: Message;
  /** Callback function triggered when the copy icon is clicked on an assistant message. */
  onCopyMessage: (content: string) => void;
}

/**
 * Renders a single chat message bubble, styled based on the sender's role.
 * Includes an icon, the message content (supporting basic HTML), and a copy button for assistant messages.
 */
const MessageItem: React.FC<MessageItemProps> = ({ message, onCopyMessage }) => {
  const { role, content } = message;
  const isUser = role === 'user';

  const handleCopyClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.stopPropagation();
    onCopyMessage(content);
  };

  const bubbleClasses = `
    max-w-3xl p-4 rounded-lg flex gap-3 items-start shadow-md
    ${isUser
      ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-br-none'
      : 'bg-gray-800 border border-gray-700 text-gray-200 rounded-bl-none'
    }
  `;

  const iconContainerClasses = `
    flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center mt-0.5
    ${isUser ? 'bg-blue-500' : 'bg-gray-700'}
  `;

  const icon = isUser
    ? <User size={14} className="text-white" />
    : <Bot size={14} className="text-gray-300" />;

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div className={bubbleClasses}>
        <div className={iconContainerClasses}>
          {icon}
        </div>

        <div className="flex-1 min-w-0">
          <p
            className={`whitespace-pre-wrap break-words ${isUser ? 'text-white' : 'text-gray-100'}`}
            dangerouslySetInnerHTML={{ __html: content }}
          >
          </p>

          {!isUser && (
            <button
              onClick={handleCopyClick}
              className="mt-2 p-1 -ml-1 text-gray-400 hover:text-blue-400 rounded hover:bg-gray-700 transition-colors duration-150"
              title="Copy to clipboard"
              aria-label="Copy message content to clipboard"
            >
              <Copy size={14} />
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export { MessageItem };