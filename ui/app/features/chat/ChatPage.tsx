import React from 'react';
import ChatApp from './components/ChatApp';

export default function ChatPage() {
  return (
    <div className="min-h-screen bg-black bg-gradient-to-b from-gray-950 to-gray-900 text-white flex items-center justify-center p-6">
      <div className="w-full max-w-5xl">
        <ChatApp />
      </div>
    </div>
  );
} 