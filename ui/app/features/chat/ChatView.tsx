// src/features/chat/ChatView.tsx
import React from 'react';
import type { ChangeEvent } from 'react'; // Import ChangeEvent type

// --- Feature Hooks ---
import { useMidi } from '../midi/hooks/useMidi';
import { useApiKey } from '../api/hooks/useApiKey';
import { useSynthGenieApi } from '../api/hooks/useSynthGenieApi';
import { useChatMessages } from './hooks/useChatMessages';

// --- UI Components ---
import { ChatHeader } from './components/ChatHeader';
import { MessageList } from './components/MessageList';
import { ChatInputArea } from './components/ChatInputArea';
import { MidiDeviceSelector } from '../midi/components/MidiDeviceSelector'; // To render within InputArea
import { ApiKeyManager } from '../api/components/ApiKeyManager';         // To render within InputArea

/**
 * The main view component for the SynthGenie Chat application.
 * It integrates MIDI device handling, API key management, API communication,
 * and the chat message display and input logic.
 */
const ChatView: React.FC = () => {
  // --- Initialize Hooks ---

  // 1. API Key Management Hook
  const {
    apiKey,
    showApiKeyInput,
    apiKeyInputValue,
    setApiKeyInputValue,
    handleSaveApiKey, // Renamed for clarity from 'saveApiKey' if needed
    handleApiKeyToggle, // Renamed for clarity from 'toggleShowApiKeyInput' if needed
    handleClearApiKey, // Renamed for clarity from 'clearApiKey' if needed
  } = useApiKey(); // Assuming useApiKey hook exports these

  // 2. MIDI Handling Hook
  const {
    midiDevices,
    selectedDevice,
    setSelectedDevice,
    sendMidiCC,
    // midiAccess, // Usually not needed directly in the view
    // midiOutputs, // Usually not needed directly in the view
  } = useMidi();

  // 3. SynthGenie API Mutation Hook (depends on apiKey)
  const promptMutation = useSynthGenieApi(apiKey); // Use the result directly

  // 4. Chat Message & Flow Logic Hook (depends on others)
  const {
    messages,
    input,
    isLoading, // Derived from promptMutation.isPending within the hook
    messagesEndRef,
    setInput,
    handleSendMessage, // Hook's internal send logic
    clearChat,
    copyMessage,
  } = useChatMessages({
    promptMutation, // Pass the mutation object
    sendMidiCC,     // Pass the MIDI sending function
    apiKey,         // Pass API key status for checks
    selectedDevice, // Pass device for context/welcome message
  });

  // --- Render Logic ---

  // Prepare the component nodes to pass into ChatInputArea
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
    // Main container - flex column, takes full height, defines background
    <div className="flex flex-col h-screen rounded-xl overflow-hidden shadow-2xl bg-gray-900 border border-gray-800">

      {/* 1. Header Area */}
      <ChatHeader
        selectedDevice={selectedDevice}
        onClearChat={clearChat} // Pass the clearChat handler from useChatMessages
      />

      {/* 2. Message List Area (Should grow to fill available space) */}
      <MessageList
        messages={messages}
        isLoading={isLoading}
        messagesEndRef={messagesEndRef}
        onCopyMessage={copyMessage}
      />

      {/* 3. Input Area (Fixed height at the bottom) */}
      <ChatInputArea
        input={input}
        setInput={setInput}
        onSendMessage={handleSendMessage} // Pass the send handler from useChatMessages
        isLoading={isLoading}
        midiDeviceSelector={midiSelectorComponent} // Pass the rendered component
        apiKeyManager={apiKeyManagerComponent}     // Pass the rendered component
      />

    </div>
  );
};

export default ChatView; // Or named export: export { ChatView };