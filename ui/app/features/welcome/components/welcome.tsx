import React, { useEffect, useState } from 'react';
import moogOneSvg from '../../../assets/moog-one.svg';

export function Welcome() {
  const [imageLoaded, setImageLoaded] = useState(false);
  
  useEffect(() => {
    const timer = setTimeout(() => {
      setImageLoaded(true);
    }, 500);
    
    return () => clearTimeout(timer);
  }, []);

  const synthImageUrl = moogOneSvg;

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] w-full p-6">      
      <div className="relative z-10 text-center max-w-5xl mx-auto p-8">
        <h1 className="text-5xl md:text-7xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400 mb-4">
          SynthGenie
        </h1>
        
        <p className="text-xl md:text-2xl text-gray-400 mb-6">
          Your AI sound designer — connect your synth, let's shape the sound
        </p>
        
        <div className="mb-10 p-4 bg-gray-800/50 rounded-lg border border-gray-700 max-w-2xl mx-auto">
          <p className="text-sm text-gray-300">
            <span className="text-blue-400 font-medium">🎹 MIDI Required:</span> Connect a Moog or Elektron Digitone device to access the chat
          </p>
        </div>
        
        <div 
          className={`relative mx-auto max-w-4xl transition-all duration-3000 ease-out ${
            imageLoaded ? 'opacity-100 scale-100 blur-0 translate-y-0' : 'opacity-0 scale-50 blur-md translate-y-20'
          }`}
        >
          <div className="absolute inset-0 bg-blue-500/20 blur-xl rounded-full -z-10 scale-90 opacity-70"></div>
          
          <div className="relative">
            <img 
              src={synthImageUrl} 
              alt="Moog One Synthesizer" 
              className="w-full h-auto rounded-lg shadow-2xl transform-gpu filter brightness-90 contrast-125 saturate-75 hue-rotate-15 color-wave"
              style={{ mixBlendMode: 'lighten' }}
            />
            
            <style dangerouslySetInnerHTML={{ __html: `
              @keyframes colorWave {
                0% { 
                  filter: brightness(0.9) contrast(1.25) saturate(0.75) hue-rotate(15deg);
                }
                25% { 
                  filter: brightness(0.9) contrast(1.3) saturate(1.2) hue-rotate(60deg);
                }
                50% { 
                  filter: brightness(0.85) contrast(1.4) saturate(1.0) hue-rotate(180deg);
                }
                75% { 
                  filter: brightness(0.9) contrast(1.3) saturate(1.1) hue-rotate(270deg);
                }
                100% { 
                  filter: brightness(0.9) contrast(1.25) saturate(0.75) hue-rotate(15deg);
                }
              }
              
              .color-wave {
                animation: colorWave 15s infinite ease-in-out;
              }
            `}} />
          </div>
        </div>
      </div>
    </div>
  );
}
