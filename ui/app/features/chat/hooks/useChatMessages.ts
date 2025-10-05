import type { UseMutationResult } from '@tanstack/react-query';
import type { RefObject } from 'react';
import { useCallback, useEffect, useState } from 'react';
import type { SynthGenieResponse } from '../../api/types';
import type { Message } from '../types';
import { getInitialWelcomeMessage } from '../utils/chatUtils';
import { useAutoScroll } from './useAutoScroll';

interface UseChatMessagesProps {
  promptMutation: UseMutationResult<
    SynthGenieResponse[],
    Error,
    {
      prompt: string;
      deviceName: string;
    },
    unknown
  >;
  sendMidiMessage: (response: SynthGenieResponse) => void;
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
 *
 * Note: Each prompt is treated independently with no history sent to backend.
 */
export const useChatMessages = ({
  promptMutation,
  sendMidiMessage,
  apiKey,
  selectedDevice,
}: UseChatMessagesProps): UseChatMessagesReturn => {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', content: getInitialWelcomeMessage(selectedDevice) }
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
      const responses = promptMutation.data;
      const responseLines: string[] = [];

      // Handle array of responses
      responses.forEach((response, index) => {
        const { used_tool, midi_channel, value, midi_cc, midi_cc_lsb, nrpn_msb, nrpn_lsb } =
          response;

        // Determine message type for display
        let messageType = '';
        if (
          nrpn_msb !== null &&
          nrpn_msb !== undefined &&
          nrpn_lsb !== null &&
          nrpn_lsb !== undefined
        ) {
          messageType = `NRPN MSB ${nrpn_msb}, LSB ${nrpn_lsb}`;
        } else if (
          midi_cc !== null &&
          midi_cc !== undefined &&
          midi_cc_lsb !== null &&
          midi_cc_lsb !== undefined
        ) {
          messageType = `High-Res CC ${midi_cc}/${midi_cc_lsb}`;
        } else if (midi_cc !== null && midi_cc !== undefined) {
          messageType = `CC ${midi_cc}`;
        } else {
          messageType = 'Unknown format';
        }

        const responseText = `${index + 1}. ${used_tool} (${messageType}, Ch ${midi_channel}, Val ${value})`;
        responseLines.push(responseText);

        try {
          sendMidiMessage(response);
        } catch (midiError) {
          console.error('Error sending MIDI message:', midiError, response);
          responseLines.push(`   -> Error sending MIDI for this action.`);
        }
      });

      const responseContent = `Sent ${responses.length} MIDI action${responses.length > 1 ? 's' : ''}:\n${responseLines.join('\n')}`;

      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: responseContent,
        },
      ]);

      promptMutation.reset();
    }
  }, [
    promptMutation.isSuccess,
    promptMutation.data,
    sendMidiMessage,
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
          default:
            // Check for specific error statuses
            if ('status' in error) {
              switch (error.status) {
                case 422:
                  errorMessage =
                    error.message ||
                    'This prompt is not about sound design. Please try a different request.';
                  break;
                case 400:
                  if (error.message.includes('Unsupported synthesizer')) {
                    errorMessage = `Your synthesizer (${selectedDevice}) is not supported. Please connect a Moog or Elektron Digitone device.`;
                  } else {
                    errorMessage = error.message;
                  }
                  break;
                default:
                  errorMessage =
                    error.message ||
                    'There was a problem communicating with the SynthGenie service.';
                  break;
              }
            } else {
              errorMessage = error.message;
            }
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
    selectedDevice,
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

    if (!selectedDevice) {
      setMessages((prev) => [
        ...prev,
        { role: 'user', content: trimmedInput },
        {
          role: 'assistant',
          content: 'Please select a MIDI device before sending messages.',
        },
      ]);
      setInput('');
      return;
    }

    setMessages((prev) => [...prev, { role: 'user', content: trimmedInput }]);

    // Send only the current prompt without any history
    promptMutation.mutate({
      prompt: trimmedInput,
      deviceName: selectedDevice,
    });
    setInput('');
  }, [input, isLoading, promptMutation, apiKey, selectedDevice, messages, setMessages, setInput]);

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
