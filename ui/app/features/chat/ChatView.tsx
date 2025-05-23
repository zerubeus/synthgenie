import React from 'react';
import type { ChangeEvent } from 'react';

// --- Feature Hooks ---
import { useMidi } from '../midi/hooks/useMidi';
import { useMidiDeviceValidation } from '../midi/hooks/useMidiDeviceValidation';
import { useApiKey } from '../api/hooks/useApiKey';
import { useSynthGenieApi } from '../api/hooks/useSynthGenieApi';
import { useChatMessages } from './hooks/useChatMessages';

// --- UI Components ---
import { ChatHeader } from './components/ChatHeader';
import { MessageList } from './components/MessageList';
import { ChatInputArea } from './components/ChatInputArea';
import { MidiAccessRestriction } from './components/MidiAccessRestriction';
import { MidiDeviceSelector } from '../midi/components/MidiDeviceSelector';
import { ApiKeyManager } from '../api/components/ApiKeyManager';

/**
 * The main view component for the SynthGenie Chat application.
 * It integrates MIDI device handling, API key management, API communication,
 * and the chat message display and input logic.
 * 
 * Access is restricted to users with valid MIDI devices (containing "moog" or "digitone").
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

  const { setSelectedDevice, sendMidiCC } = useMidi();
  
  const {
    hasValidDevice,
    isInitializing,
    midiDevices,
    selectedDevice,
    validDevices,
    error,
  } = useMidiDeviceValidation();

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

  // Show restriction screen if no valid device is connected
  if (!hasValidDevice) {
    return (
      <MidiAccessRestriction
        midiDevices={midiDevices}
        selectedDevice={selectedDevice || ''}
        onDeviceChange={(e: ChangeEvent<HTMLSelectElement>) => setSelectedDevice(e.target.value)}
        validDevices={validDevices}
        isInitializing={isInitializing}
        error={error}
      />
    );
  }

  // Render normal chat interface when valid device is connected
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
    <div className="flex flex-col h-screen overflow-hidden shadow-2xl bg-gray-900 border border-gray-800">
      <ChatHeader selectedDevice={selectedDevice} onClearChat={clearChat} />

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
