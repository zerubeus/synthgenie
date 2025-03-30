import React, { useEffect, useState } from 'react';
import moogOneSvg from '../../../assets/moog-one.svg';

export function Welcome() {
  const [imageLoaded, setImageLoaded] = useState(false);
  
  useEffect(() => {
    // Trigger fade-in effect after component mounts
    const timer = setTimeout(() => {
      setImageLoaded(true);
    }, 500);
    
    return () => clearTimeout(timer);
  }, []);

  // Embed an image of a synthesizer with a dark background
  const synthImageUrl = moogOneSvg;

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] w-full p-6">      
      <div className="relative z-10 text-center max-w-5xl mx-auto p-8">
        <h1 className="text-5xl md:text-7xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400 mb-4">
          Synthgenie
        </h1>
        
        <p className="text-xl md:text-2xl text-gray-400 mb-10">
          Your AI sound designer — connect your synth, let's shape the sound
        </p>
        
        {/* Synth image with fade-in effect */}
        <div 
          className={`relative mx-auto max-w-4xl transition-all duration-3000 ease-out ${
            imageLoaded ? 'opacity-100 scale-100 blur-0 translate-y-0' : 'opacity-0 scale-50 blur-md translate-y-20'
          }`}
        >
          {/* Glow effect behind the synth */}
          <div className="absolute inset-0 bg-blue-500/20 blur-xl rounded-full -z-10 scale-90 opacity-70"></div>
          
          <img 
            src={synthImageUrl} 
            alt="Moog One Synthesizer" 
            className="w-full h-auto rounded-lg shadow-2xl transform-gpu filter brightness-90 contrast-125 saturate-75 hue-rotate-15"
            style={{ mixBlendMode: 'lighten' }}
          />
        </div>
      </div>
    </div>
  );
}
