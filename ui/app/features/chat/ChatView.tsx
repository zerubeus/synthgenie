import React, { useCallback } from 'react';
import type { ChangeEvent } from 'react';
import { detectSynthType } from '../api/utils/getApiBaseUrl';
import type { SynthType } from '../api/types';

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
import { SynthSelector } from '../midi/components/SynthSelector';
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

  const { setSelectedDevice, sendMidiMessage } = useMidi();
  
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
    sendMidiMessage,
    apiKey,
    selectedDevice,
  });

  // Simplified device change handler
  const handleDeviceChange = useCallback((e: ChangeEvent<HTMLSelectElement>) => {
    const newDevice = e.target.value;
    console.log('🎹 Device switch attempt:', {
      fromDevice: selectedDevice,
      toDevice: newDevice,
    });
    setSelectedDevice(newDevice);
    console.log('✅ setSelectedDevice called with:', newDevice);
  }, [selectedDevice, setSelectedDevice]);

  // Synth change handler - finds a device of the selected synth type
  const handleSynthChange = useCallback((synthType: SynthType) => {
    console.log('🎛️ Synth switch attempt:', {
      fromDevice: selectedDevice,
      toSynthType: synthType,
    });
    
    // Find a device that matches the selected synth type
    const matchingDevice = midiDevices.find(device => detectSynthType(device) === synthType);
    
    if (matchingDevice) {
      setSelectedDevice(matchingDevice);
      console.log('✅ setSelectedDevice called with:', matchingDevice);
    } else {
      console.warn('⚠️ No device found for synth type:', synthType);
    }
  }, [selectedDevice, setSelectedDevice, midiDevices]);

  // Add effect to monitor selectedDevice changes
  React.useEffect(() => {
    console.log('📱 ChatView selectedDevice state changed to:', selectedDevice);
  }, [selectedDevice]);

  // Show restriction screen if no valid device is connected
  if (!hasValidDevice) {
    return (
      <MidiAccessRestriction
        midiDevices={midiDevices}
        selectedDevice={selectedDevice || ''}
        onDeviceChange={handleDeviceChange}
        validDevices={validDevices}
        isInitializing={isInitializing}
        error={error}
      />
    );
  }

  // Render normal chat interface when valid device is connected
  const synthSelectorComponent = (
    <SynthSelector
      midiDevices={midiDevices}
      selectedDevice={selectedDevice || ''}
      onSynthChange={handleSynthChange}
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
        midiDeviceSelector={synthSelectorComponent}
        apiKeyManager={apiKeyManagerComponent}
      />
    </div>
  );
};

export default ChatView;
