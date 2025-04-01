import React, { useState, useRef, useEffect } from 'react';
import type { ChangeEvent, KeyboardEvent } from 'react';
import { Send, User, Bot, Trash2, Copy } from 'lucide-react';
import { useMutation } from '@tanstack/react-query';

// Simple WebMidi interfaces
interface MIDIInput {
  name: string | null;
}

interface MIDIOutput {
  name: string | null;
  send: (data: number[]) => void;
}

interface MIDIAccess {
  inputs: Map<string, MIDIInput>;
  outputs: Map<string, MIDIOutput>;
}

type Message = {
  role: 'user' | 'assistant';
  content: string;
};

type MidiAction = {
  used_tool: string;
  midi_cc: number;
  midi_channel: number;
  value: number;
};

const ChatApp = () => {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', content: 'Hello! How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedDevice, setSelectedDevice] = useState('');
  const [midiDevices, setMidiDevices] = useState<string[]>(['No MIDI devices detected']);
  const [midiAccess, setMidiAccess] = useState<MIDIAccess | null>(null);
  const [midiOutputs, setMidiOutputs] = useState<Map<string, MIDIOutput>>(new Map());
  
  // Detect MIDI devices on component mount
  useEffect(() => {
    if (navigator.requestMIDIAccess) {
      navigator.requestMIDIAccess()
        .then(access => {
          setMidiAccess(access as unknown as MIDIAccess);
          const devices: string[] = [];
          const outputs = new Map<string, MIDIOutput>();
          
          access.outputs.forEach((output: MIDIOutput) => {
            const name = output.name || `MIDI Device ${devices.length + 1}`;
            devices.push(name);
            outputs.set(name, output);
          });
          
          if (devices.length > 0) {
            setMidiDevices(devices);
            setSelectedDevice(devices[0]);
            setMidiOutputs(outputs);
          }
        })
        .catch(err => {
          console.error('MIDI access denied:', err);
        });
    }
  }, []);
  
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Focus input field on component mount
  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []);
  
  // Update welcome message when device changes
  useEffect(() => {
    if (selectedDevice && messages.length === 1 && messages[0].role === 'assistant') {
      setMessages([{ 
        role: 'assistant', 
        content: `Hello! I'm Synthgenie connected to "${selectedDevice}". How can I help you create amazing sounds today?` 
      }]);
    }
  }, [selectedDevice]);

  // Send MIDI message to device
  const sendMidiCC = (channel: number, cc: number, value: number) => {
    if (!midiAccess || !selectedDevice) return;
    
    const output = midiOutputs.get(selectedDevice);
    if (output) {
      // MIDI CC message: 0xB0 (176) is the status byte for Control Change on channel 1
      // For other channels, add the channel number - 1 to the status byte
      const statusByte = 176 + (channel - 1);
      output.send([statusByte, cc, value]);
      console.log(`MIDI CC sent: Channel ${channel}, CC ${cc}, Value ${value}`);
    }
  };

  // API request mutation using TanStack Query
  const promptMutation = useMutation({
    mutationFn: async (prompt: string) => {
      const response = await fetch('http://localhost:8080/agent/prompt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      
      return response.json() as Promise<MidiAction[]>;
    },
    onSuccess: (data) => {
      // Process the returned MIDI actions
      let responseContent = '';
      
      // Execute MIDI commands and build response message
      data.forEach((action) => {
        // Add the action to the response content
        responseContent += `${action.used_tool} -> ${action.value}\n`;
        
        // Send the MIDI command
        sendMidiCC(action.midi_channel, action.midi_cc, action.value);
      });
      
      // Add the assistant's response to the messages
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: responseContent.trim() 
      }]);
      
      setIsLoading(false);
    },
    onError: (error) => {
      console.error('Error sending prompt:', error);
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Sorry, there was an error processing your request. Please try again.' 
      }]);
      setIsLoading(false);
    }
  });

  const handleSendMessage = () => {
    if (input.trim() === '') return;

    // Add user message
    setMessages([...messages, { role: 'user', content: input }]);
    
    // Clear input
    setInput('');
    
    // Set loading state
    setIsLoading(true);
    
    // Send prompt to API
    promptMutation.mutate(input);
  };

  // Auto-adjust textarea height
  const handleTextAreaInput = (e: ChangeEvent<HTMLTextAreaElement>) => {
    const target = e.target;
    setInput(target.value);
    
    // Reset height to auto to get the correct scrollHeight
    target.style.height = 'auto';
    // Set the height to match content (scrollHeight includes padding)
    target.style.height = `${target.scrollHeight}px`;
  };

  const handleKeyPress = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const clearChat = () => {
    setMessages([{ 
      role: 'assistant', 
      content: selectedDevice 
        ? `Hello! I'm Synthgenie connected to "${selectedDevice}". How can I help you create amazing sounds today?` 
        : 'Hello! How can I help you today?' 
    }]);
  };

  const copyMessage = (content: string) => {
    navigator.clipboard.writeText(content);
    // You could add a toast notification here
  };

  return (
    <div className="flex flex-col rounded-xl overflow-hidden shadow-2xl bg-gray-900 border border-gray-800">
      {/* Header */}
      <header className="bg-gray-900 border-b border-gray-800 p-4 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400">
          Synthgenie {selectedDevice && <span className="text-blue-400 font-medium">MIDI</span>}
        </h1>
        <button 
          onClick={clearChat}
          className="p-2 text-gray-400 hover:text-blue-400 hover:bg-gray-800 rounded-full"
          aria-label="Clear chat"
          title="Clear chat"
        >
          <Trash2 size={20} />
        </button>
      </header>

      {/* Chat Area */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-gray-900 h-[60vh]">
        {messages.map((message, index) => (
          <div 
            key={index} 
            className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div className={`
              max-w-3xl p-4 rounded-lg flex gap-3 items-start
              ${message.role === 'user' 
                ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-br-none' 
                : 'bg-gray-800 border border-gray-700 shadow-sm rounded-bl-none text-gray-200'
              }
            `}>
              <div className={`
                flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center
                ${message.role === 'user' ? 'bg-blue-500' : 'bg-gray-700'}
              `}>
                {message.role === 'user' 
                  ? <User size={14} className="text-white" /> 
                  : <Bot size={14} className="text-gray-300" />
                }
              </div>
              <div className="flex-1">
                <p className={`whitespace-pre-wrap text-white`}>
                  {message.content}
                </p>
                {message.role === 'assistant' && (
                  <button 
                    onClick={() => copyMessage(message.content)}
                    className="mt-2 text-gray-400 hover:text-blue-400"
                    title="Copy to clipboard"
                  >
                    <Copy size={14} />
                  </button>
                )}
              </div>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="max-w-3xl p-4 rounded-lg flex gap-3 items-start bg-gray-800 border border-gray-700 shadow-sm rounded-bl-none">
              <div className="flex-shrink-0 w-6 h-6 rounded-full bg-gray-700 flex items-center justify-center">
                <Bot size={14} className="text-gray-300" />
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 rounded-full bg-blue-400 animate-bounce" style={{ animationDelay: '0ms' }}></div>
                <div className="w-2 h-2 rounded-full bg-indigo-400 animate-bounce" style={{ animationDelay: '300ms' }}></div>
                <div className="w-2 h-2 rounded-full bg-purple-400 animate-bounce" style={{ animationDelay: '600ms' }}></div>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="p-4 bg-gray-800 border-t border-gray-700">
        <div className="relative">
          <div className="border border-gray-700 rounded-lg bg-gray-900 overflow-hidden focus-within:ring-2 focus-within:ring-blue-500 focus-within:border-blue-500">
            <textarea
              ref={inputRef}
              className="w-full p-3 pb-12 resize-none outline-none min-h-20 overflow-hidden border-none bg-gray-900 text-white placeholder-gray-500"
              placeholder="Type your message..."
              value={input}
              onChange={handleTextAreaInput}
              onKeyDown={handleKeyPress}
              disabled={isLoading}
            />
            
            {/* Send button and tool selector inside textarea */}
            <div className="absolute bottom-3 right-3 flex items-center gap-3">              
              {/* Tool Selector as dropdown without border */}
              <div className="relative inline-block">
                <select
                  value={selectedDevice}
                  onChange={(e) => setSelectedDevice(e.target.value)}
                  className="appearance-none bg-transparent pr-6 border-none focus:outline-none text-gray-400 text-right"
                  style={{ direction: "rtl", paddingRight: "1.5rem" }}
                >
                  {midiDevices.map((device) => (
                    <option key={device} value={device} style={{ direction: "ltr", textAlign: "right" }}>
                      {device}
                    </option>
                  ))}
                </select>
                <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center">
                  <svg className="h-4 w-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
                  </svg>
                </div>
              </div>
              
              {/* Send button */}
              <button
                onClick={handleSendMessage}
                disabled={input.trim() === '' || isLoading}
                className={`p-2 rounded-lg flex-shrink-0 ${
                  input.trim() === '' || isLoading
                    ? 'text-gray-600 cursor-not-allowed'
                    : 'text-blue-400 hover:text-indigo-400'
                }`}
                aria-label="Send message"
              >
                <Send size={20} />
              </button>
            </div>
          </div>
        </div>
        
        <p className="text-xs text-center text-gray-500 mt-2">
          Press Enter to send, Shift+Enter for a new line
        </p>
      </div>
    </div>
  );
};

export default ChatApp; 