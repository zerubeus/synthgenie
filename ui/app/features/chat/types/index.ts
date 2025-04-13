/**
 * Represents the role of the sender of a chat message.
 * - 'user': The end-user interacting with the application.
 * - 'assistant': The AI assistant (SynthGenie) or system-generated messages (like errors or status updates).
 */
export type MessageRole = 'user' | 'assistant';

/**
 * Represents a single message within the chat conversation.
 */
export type Message = {
  /**
   * The role of the entity that originated the message.
   * Determines the styling and alignment of the message bubble.
   * @see MessageRole
   */
  role: MessageRole;

  /**
   * The text content of the message.
   * This string may contain basic HTML elements (e.g., `<a>`, `<strong>`)
   * for rendering links or emphasis, especially in system messages.
   * Use `dangerouslySetInnerHTML` with caution and ensure content safety.
   */
  content: string;

  /**
   * Optional unique identifier for the message.
   * Highly recommended for stable list rendering in React, especially
   * if messages could potentially be deleted or re-ordered in the future.
   * Using the array index as a key is less ideal.
   */
  id?: string | number;

  /**
   * Optional timestamp indicating when the message was created or received.
   * Can be used for display purposes (e.g., "Sent 2 minutes ago") or sorting.
   * Could be a Date object, Unix timestamp (number), or ISO string.
   */
  timestamp?: Date | number | string;
};
