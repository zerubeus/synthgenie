import React, { useEffect, useState } from 'react';
import synthImage from '../../../assets/subsequent37top.png';

export function Welcome() {
  const [imageLoaded, setImageLoaded] = useState(false);
  const [imageError, setImageError] = useState(false);
  
  useEffect(() => {
    // Log the image path for debugging
    console.log("Synth image path:", synthImage);
    
    // Trigger fade-in effect after component mounts
    const timer = setTimeout(() => {
      setImageLoaded(true);
    }, 500);
    
    return () => clearTimeout(timer);
  }, []);

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
          className={`relative mx-auto max-w-4xl transition-all duration-1000 ease-in-out ${
            imageLoaded ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'
          }`}
        >
          {/* Glow effect behind the synth */}
          <div className="absolute inset-0 bg-blue-500/20 blur-xl rounded-full -z-10 scale-90 opacity-70"></div>
          
          {!imageError ? (
            <img 
              src={synthImage} 
              alt="Moog Subsequent 37 Synthesizer" 
              className="w-full h-auto rounded-lg shadow-2xl"
              onLoad={() => console.log("Image loaded successfully")}
              onError={(e) => {
                console.error("Failed to load synth image:", e);
                setImageError(true);
              }}
            />
          ) : (
            <div className="w-full aspect-[3/1] bg-gray-800 rounded-lg shadow-2xl flex items-center justify-center">
              <p className="text-white text-xl">Moog Subsequent 37 Synthesizer</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
