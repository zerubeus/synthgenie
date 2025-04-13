import React from 'react';

interface MidiDeviceSelectorProps {
  devices: string[];
  selectedDevice: string;
  onChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
  disabled?: boolean;
  ariaLabel?: string;
}

const NO_DEVICES_MESSAGE = 'No MIDI devices detected';

/**
 * A dropdown component for selecting an available MIDI output device.
 */
export const MidiDeviceSelector: React.FC<MidiDeviceSelectorProps> = ({
  devices,
  selectedDevice,
  onChange,
  disabled = false,
  ariaLabel = 'Select MIDI Output Device',
}) => {
  const hasDevices = devices.length > 0 && devices[0] !== NO_DEVICES_MESSAGE;

  return (
    <div className="relative inline-block">
      <select
        value={selectedDevice}
        onChange={onChange}
        disabled={disabled || !hasDevices}
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
        {!hasDevices ? (
          <option value="" disabled style={{ direction: 'ltr', textAlign: 'left' }}>
             {NO_DEVICES_MESSAGE}
          </option>
        ) : (
          devices.map((device) => (
            <option
              key={device}
              value={device}
              className="bg-gray-700 text-white"
              style={{ direction: 'ltr', textAlign: 'left' }}
            >
              {device}
            </option>
          ))
        )}
      </select>

      <div className={`
          pointer-events-none 
          absolute inset-y-0 right-0 flex items-center px-1
          ${disabled || !hasDevices ? 'text-gray-600' : 'text-gray-400'}
        `}
      >
        <svg className="h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
          <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
        </svg>
      </div>
    </div>
  );
};
