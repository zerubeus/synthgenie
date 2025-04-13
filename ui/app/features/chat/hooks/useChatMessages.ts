import { useState, useEffect, useCallback } from 'react';
import type { RefObject } from 'react';
import type { UseMutationResult } from '@tanstack/react-query';
import type { Message } from '../types';
import type { MidiAction } from '../../api/types';
import { getInitialWelcomeMessage } from '../utils/chatUtils';
import { useAutoScroll } from './useAutoScroll';

interface UseChatMessagesProps {
  promptMutation: UseMutationResult<MidiAction[], Error, string, unknown>;
  sendMidiCC: (channel: number, cc: number, value: number) => void;
  apiKey: string | null | undefined;
  selectedDevice: string | null | undefined;
}

interface UseChatMessagesReturn {
  messages: Message[];
  input: string;
  isLoading: boolean;
  messagesEndRef: RefObject<HTMLDivElement | null>;
  setInput: React.Dispatch<React.SetStateAction<string>>;
  handleSendMessage: () => void;
  clearChat: () => void;
  copyMessage: (content: string) => void;
}

/**
 * Custom hook to manage chat state, messages, input, loading,
 * and interactions with API mutation and MIDI sending.
 */
export const useChatMessages = ({
  promptMutation,
  sendMidiCC,
  apiKey,
  selectedDevice,
}: UseChatMessagesProps): UseChatMessagesReturn => {
  const [messages, setMessages] = useState<Message[]>(() => [
    { role: 'assistant', content: getInitialWelcomeMessage(selectedDevice) },
  ]);

  const [input, setInput] = useState('');
  const isLoading = promptMutation.isPending;

  const messagesEndRef = useAutoScroll<HTMLDivElement>([messages]); // Use the hook

  useEffect(() => {
    if (messages.length === 1 && messages[0].role === 'assistant') {
      const currentWelcomeMessage = getInitialWelcomeMessage(selectedDevice);
      if (messages[0].content !== currentWelcomeMessage) {
        setMessages([{ role: 'assistant', content: currentWelcomeMessage }]);
      }
    }
  }, [selectedDevice, messages]);

  useEffect(() => {
    if (promptMutation.isSuccess && promptMutation.data) {
      const data = promptMutation.data;
      let responseContent = '';

      if (Array.isArray(data)) {
        data.forEach((action) => {
          responseContent += `Sent: ${action.used_tool} (CC ${action.midi_cc}, Ch ${action.midi_channel}, Val ${action.value})\n`;
          try {
            sendMidiCC(action.midi_channel, action.midi_cc, action.value);
          } catch (midiError) {
            console.error('Error sending MIDI CC:', midiError, action);
            responseContent += `  -> Error sending MIDI for this action.\n`;
          }
        });
      } else {
        console.warn('Received non-array data on mutation success:', data);
        responseContent = "Received data, but couldn't process actions.";
      }

      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: responseContent.trim() || 'Action processed.',
        },
      ]);

      promptMutation.reset();
    }
  }, [
    promptMutation.isSuccess,
    promptMutation.data,
    sendMidiCC,
    promptMutation.reset,
    promptMutation,
  ]);

  useEffect(() => {
    if (promptMutation.isError && promptMutation.error) {
      const error = promptMutation.error;
      console.error('Error sending prompt:', error);
      let errorMessage = 'Sorry, an unexpected error occurred. Please try again.';

      if (error instanceof Error) {
        switch (error.message) {
          case 'No API key set':
            errorMessage = 'Please set your API key using the button below.';
            break;
          case 'Invalid API key':
            errorMessage = 'Your API key appears to be invalid. Please check and update it.';
            break;
          case 'Network response was not ok':
            errorMessage =
              'There was a problem communicating with the SynthGenie service (Network Error).';
            break;
          default:
            break;
        }
      } else {
        errorMessage = 'An unknown error occurred.';
      }

      setMessages((prev) => [...prev, { role: 'assistant', content: errorMessage }]);

      promptMutation.reset();
    }
  }, [
    promptMutation.isError,
    promptMutation.error,
    promptMutation.reset,
    setMessages,
    promptMutation,
  ]);

  const handleSendMessage = useCallback(() => {
    const trimmedInput = input.trim();
    if (trimmedInput === '' || isLoading) return;

    if (!apiKey) {
      setMessages((prev) => [
        ...prev,
        { role: 'user', content: trimmedInput },
        {
          role: 'assistant',
          content:
            'Please set your API key using the "SET API KEY" button below before sending messages.',
        },
      ]);
      setInput('');
      return;
    }

    setMessages((prev) => [...prev, { role: 'user', content: trimmedInput }]);
    promptMutation.mutate(trimmedInput);
    setInput('');
  }, [input, isLoading, promptMutation, apiKey, setMessages, setInput]);

  const clearChat = useCallback(() => {
    setMessages([{ role: 'assistant', content: getInitialWelcomeMessage(selectedDevice) }]);
    if (promptMutation.isError || promptMutation.isSuccess) {
      promptMutation.reset();
    }
    setInput('');
  }, [selectedDevice, setMessages, setInput, promptMutation]);

  const copyMessage = useCallback((content: string) => {
    if (!navigator.clipboard) {
      console.warn('Clipboard API not available.');
      alert('Clipboard access is not available or denied in this browser.');
      return;
    }
    navigator.clipboard.writeText(content).then(
      () => {
        console.log('Content copied to clipboard successfully.');
      },
      (err) => {
        console.error('Failed to copy content to clipboard: ', err);
        alert('Failed to copy message. See console for details.');
      }
    );
  }, []);

  return {
    messages,
    input,
    isLoading,
    messagesEndRef,
    setInput,
    handleSendMessage,
    clearChat,
    copyMessage,
  };
};
