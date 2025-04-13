import React from 'react';
import type { ChangeEvent } from 'react';

// --- Feature Hooks ---
import { useMidi } from '../midi/hooks/useMidi';
import { useApiKey } from '../api/hooks/useApiKey';
import { useSynthGenieApi } from '../api/hooks/useSynthGenieApi';
import { useChatMessages } from './hooks/useChatMessages';

// --- UI Components ---
import { ChatHeader } from './components/ChatHeader';
import { MessageList } from './components/MessageList';
import { ChatInputArea } from './components/ChatInputArea';
import { MidiDeviceSelector } from '../midi/components/MidiDeviceSelector';
import { ApiKeyManager } from '../api/components/ApiKeyManager';

/**
 * The main view component for the SynthGenie Chat application.
 * It integrates MIDI device handling, API key management, API communication,
 * and the chat message display and input logic.
 */
const ChatView: React.FC = () => {
  const {
    apiKey,
    showApiKeyInput,
    apiKeyInputValue,
    setApiKeyInputValue,
    handleSaveApiKey,
    handleApiKeyToggle,
    handleClearApiKey,
  } = useApiKey();

  const {
    midiDevices,
    selectedDevice,
    setSelectedDevice,
    sendMidiCC,
  } = useMidi();

  const promptMutation = useSynthGenieApi(apiKey);

  const {
    messages,
    input,
    isLoading,
    messagesEndRef,
    setInput,
    handleSendMessage,
    clearChat,
    copyMessage,
  } = useChatMessages({
    promptMutation,
    sendMidiCC,
    apiKey,
    selectedDevice,
  });

  const midiSelectorComponent = (
    <MidiDeviceSelector
      devices={midiDevices}
      selectedDevice={selectedDevice || ''}
      onChange={(e: ChangeEvent<HTMLSelectElement>) => setSelectedDevice(e.target.value)}
      disabled={isLoading}
    />
  );

  const apiKeyManagerComponent = (
    <ApiKeyManager
      apiKey={apiKey}
      showInput={showApiKeyInput}
      inputValue={apiKeyInputValue}
      onInputChange={(e: ChangeEvent<HTMLInputElement>) => setApiKeyInputValue(e.target.value)}
      onSave={handleSaveApiKey}
      onToggle={handleApiKeyToggle}
      onClear={handleClearApiKey}
      disabled={isLoading}
    />
  );


  return (
    <div className="flex flex-col h-screen rounded-xl overflow-hidden shadow-2xl bg-gray-900 border border-gray-800">

      <ChatHeader
        selectedDevice={selectedDevice}
        onClearChat={clearChat}
      />

      <MessageList
        messages={messages}
        isLoading={isLoading}
        messagesEndRef={messagesEndRef}
        onCopyMessage={copyMessage}
      />

      <ChatInputArea
        input={input}
        setInput={setInput}
        onSendMessage={handleSendMessage}
        isLoading={isLoading}
        midiDeviceSelector={midiSelectorComponent}
        apiKeyManager={apiKeyManagerComponent}
      />

    </div>
  );
};

export default ChatView;