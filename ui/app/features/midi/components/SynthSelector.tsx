import React from 'react';
import { detectSynthType, getSynthDisplayName, getAvailableSynths } from '../../api/utils/getApiBaseUrl';
import type { SynthType } from '../../api/types';

interface SynthSelectorProps {
  /** Array of all detected MIDI devices */
  midiDevices: string[];
  /** Currently selected device */
  selectedDevice: string;
  /** Function to change selected device */
  onSynthChange: (synthType: SynthType) => void;
  /** Whether the selector is disabled */
  disabled?: boolean;
  /** Aria label for accessibility */
  ariaLabel?: string;
}

const NO_DEVICES_MESSAGE = 'No MIDI devices detected';

/**
 * A dropdown component for selecting between supported synthesizers.
 * Shows user-friendly synth names and handles the mapping to actual devices.
 */
export const SynthSelector: React.FC<SynthSelectorProps> = ({
  midiDevices,
  selectedDevice,
  onSynthChange,
  disabled = false,
  ariaLabel = 'Select Synthesizer',
}) => {
  const hasDevices = midiDevices.length > 0 && midiDevices[0] !== NO_DEVICES_MESSAGE;
  
  // Get available synths that have connected devices
  const availableSynths = getAvailableSynths().filter(({ synthType }) => {
    return midiDevices.some(device => detectSynthType(device) === synthType);
  });
  
  // Get the currently selected synth type
  const selectedSynthType = selectedDevice ? detectSynthType(selectedDevice) : null;
  
  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const synthType = e.target.value as SynthType;
    onSynthChange(synthType);
  };

  return (
    <div className="relative inline-block">
      <select
        value={selectedSynthType || ''}
        onChange={handleChange}
        disabled={disabled || !hasDevices || availableSynths.length === 0}
        aria-label={ariaLabel}
        className={`
          appearance-none
          bg-transparent
          border-none
          focus:outline-none
          text-gray-400
          hover:text-gray-300
          text-sm
          cursor-pointer
          py-1 pr-6 pl-2
          rounded
          text-right
          disabled:opacity-50
          disabled:cursor-not-allowed
          transition-colors
        `}
        style={{ direction: 'rtl' }}
      >
        {!hasDevices || availableSynths.length === 0 ? (
          <option value="" disabled style={{ direction: 'ltr', textAlign: 'left' }}>
            {!hasDevices ? NO_DEVICES_MESSAGE : 'No supported synths found'}
          </option>
        ) : (
          availableSynths.map(({ synthType, displayName }) => (
            <option
              key={synthType}
              value={synthType}
              className="bg-gray-700 text-white"
              style={{ direction: 'ltr', textAlign: 'left' }}
            >
              {displayName}
            </option>
          ))
        )}
      </select>

      <div className={`
          pointer-events-none 
          absolute inset-y-0 right-0 flex items-center px-1
          ${disabled || !hasDevices || availableSynths.length === 0 ? 'text-gray-600' : 'text-gray-400'}
        `}
      >
        <svg className="h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
          <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
        </svg>
      </div>
    </div>
  );
}; 