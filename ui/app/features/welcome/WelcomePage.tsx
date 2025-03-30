import React from 'react';
import { Link } from "react-router";
import { Welcome } from './components/welcome';

export function meta() {
  return [
    { title: "Synthgenie" },
    { name: "description", content: "Your AI sound designer for synthesizers" },
  ];
}

export default function WelcomePage() {
  return (
    <div className="min-h-screen bg-black bg-gradient-to-b from-gray-950 to-gray-900 text-white">
      <Welcome />
      
      <div className="flex justify-center pb-16">
        <Link 
          to="/chat" 
          className="group relative px-8 py-4 overflow-hidden rounded-full bg-blue-600 text-white font-medium text-lg shadow-lg hover:shadow-xl transition-all duration-300 hover:bg-blue-700"
        >
          <span className="relative z-10">Try Synthgenie Chat</span>
          <span className="absolute inset-0 w-full h-full bg-gradient-to-r from-blue-500 to-indigo-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></span>
          <span className="absolute -inset-x-2 bottom-0 h-1/3 bg-black/20"></span>
          <span className="absolute -right-2 top-2 w-1/3 h-1/2 bg-white/20 blur-md rounded-full transform rotate-45 opacity-50 group-hover:animate-pulse"></span>
        </Link>
      </div>
    </div>
  );
} 