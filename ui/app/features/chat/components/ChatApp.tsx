import React, { useState, useRef, useEffect } from 'react';
import type { ChangeEvent, KeyboardEvent } from 'react';
import { Send, User, Bot, Trash2, Copy } from 'lucide-react';

type Message = {
  role: 'user' | 'assistant';
  content: string;
};

const ChatApp = () => {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', content: 'Hello! How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedDevice, setSelectedDevice] = useState('');
  const [midiDevices, setMidiDevices] = useState<string[]>(['No MIDI devices detected']);
  
  // Detect MIDI devices on component mount
  useEffect(() => {
    if (navigator.requestMIDIAccess) {
      navigator.requestMIDIAccess()
        .then(access => {
          const devices: string[] = [];
          access.inputs.forEach(input => {
            devices.push(input.name || `MIDI Device ${devices.length + 1}`);
          });
          
          if (devices.length > 0) {
            setMidiDevices(devices);
            setSelectedDevice(devices[0]);
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

  const handleSendMessage = () => {
    if (input.trim() === '') return;

    // Add user message
    setMessages([...messages, { role: 'user', content: input }]);
    
    // Clear input
    setInput('');
    
    // Simulate AI response with tool-specific responses
    setIsLoading(true);
    setTimeout(() => {
      const synthResponses = [
        "I've adjusted the oscillator parameters on your connected device. How does it sound?",
        "I've sent the new patch to your MIDI device. Would you like to make any changes?",
        "Your settings have been applied to the synthesizer. Would you like to add some effects?",
        "I've updated the envelope settings on your device. Try playing a few notes to hear the difference.",
        "I've modified the filter cutoff and resonance. Does that get closer to the sound you're looking for?",
        "I've sent a new waveform combination to your synth. Let me know if you want to explore more options.",
        "I've applied those LFO settings to your device. The modulation should create that evolving texture you wanted."
      ];
      
      const deviceResponses = selectedDevice ? synthResponses : [
        "It looks like you don't have any MIDI devices connected. Would you like help setting one up?",
        "I can still help you design sounds, but you'll need to connect a MIDI device to hear them in real-time.",
        "Without a connected MIDI device, I can provide theoretical sound design advice. What type of sound are you trying to create?"
      ];
      const randomResponse = deviceResponses[Math.floor(Math.random() * deviceResponses.length)];
      
      setMessages(prev => [...prev, { role: 'assistant', content: randomResponse }]);
      setIsLoading(false);
    }, 1500);
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
    <div className="flex flex-col h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 p-4 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-gray-800">
          Synthgenie {selectedDevice && <span className="text-blue-500 font-medium">MIDI</span>}
        </h1>
        <button 
          onClick={clearChat}
          className="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-100 rounded-full"
          aria-label="Clear chat"
          title="Clear chat"
        >
          <Trash2 size={20} />
        </button>
      </header>

      {/* Chat Area */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message, index) => (
          <div 
            key={index} 
            className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div className={`
              max-w-3xl p-4 rounded-lg flex gap-3 items-start
              ${message.role === 'user' 
                ? 'bg-blue-500 text-white rounded-br-none' 
                : 'bg-white border border-gray-200 shadow-sm rounded-bl-none'
              }
            `}>
              <div className={`
                flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center
                ${message.role === 'user' ? 'bg-blue-600' : 'bg-gray-100'}
              `}>
                {message.role === 'user' 
                  ? <User size={14} className="text-white" /> 
                  : <Bot size={14} className="text-gray-600" />
                }
              </div>
              <div className="flex-1">
                <p className={`whitespace-pre-wrap ${message.role === 'user' ? 'text-white' : 'text-gray-800'}`}>
                  {message.content}
                </p>
                {message.role === 'assistant' && (
                  <button 
                    onClick={() => copyMessage(message.content)}
                    className="mt-2 text-gray-400 hover:text-gray-600"
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
            <div className="max-w-3xl p-4 rounded-lg flex gap-3 items-start bg-white border border-gray-200 shadow-sm rounded-bl-none">
              <div className="flex-shrink-0 w-6 h-6 rounded-full bg-gray-100 flex items-center justify-center">
                <Bot size={14} className="text-gray-600" />
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 rounded-full bg-gray-300 animate-bounce" style={{ animationDelay: '0ms' }}></div>
                <div className="w-2 h-2 rounded-full bg-gray-300 animate-bounce" style={{ animationDelay: '300ms' }}></div>
                <div className="w-2 h-2 rounded-full bg-gray-300 animate-bounce" style={{ animationDelay: '600ms' }}></div>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="p-4 bg-white border-t border-gray-200">
        <div className="max-w-4xl mx-auto relative">
          <div className="border border-gray-300 rounded-lg bg-white overflow-hidden focus-within:ring-2 focus-within:ring-blue-500 focus-within:border-blue-500">
            <textarea
              ref={inputRef}
              className="w-full p-3 pb-12 resize-none outline-none min-h-20 overflow-hidden border-none"
              placeholder="Type your message..."
              value={input}
              onChange={handleTextAreaInput}
              onKeyDown={handleKeyPress}
            />
            
            {/* Send button and tool selector inside textarea */}
            <div className="absolute bottom-3 right-3 flex items-center gap-3">              
              {/* Tool Selector as dropdown without border */}
              <div className="relative inline-block">
                <select
                  value={selectedDevice}
                  onChange={(e) => setSelectedDevice(e.target.value)}
                  className="appearance-none bg-transparent pr-6 border-none focus:outline-none text-gray-700 text-right"
                  style={{ direction: "rtl", paddingRight: "1.5rem" }}
                >
                  {midiDevices.map((device) => (
                    <option key={device} value={device} style={{ direction: "ltr", textAlign: "right" }}>
                      {device}
                    </option>
                  ))}
                </select>
                <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center">
                  <svg className="h-4 w-4 text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
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
                    ? 'text-gray-400 cursor-not-allowed'
                    : 'text-blue-500 hover:text-blue-600'
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