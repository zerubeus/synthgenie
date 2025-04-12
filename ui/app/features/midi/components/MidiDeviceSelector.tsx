// src/features/midi/components/MidiDeviceSelector.tsx
import React from 'react';

// Define the expected props for the component
interface MidiDeviceSelectorProps {
  /** An array of MIDI device name strings. */
  devices: string[];
  /** The currently selected MIDI device name. */
  selectedDevice: string;
  /** Callback function triggered when the selection changes. */
  onChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
  /** Optional: Flag to disable the selector. */
  disabled?: boolean;
  /** Optional: Aria-label for accessibility. */
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
    // Relative container for positioning the custom arrow
    <div className="relative inline-block">
      <select
        value={selectedDevice}
        onChange={onChange}
        disabled={disabled || !hasDevices} // Disable if no real devices or explicitly disabled
        aria-label={ariaLabel}
        className={`
          appearance-none          // Remove default browser styling
          bg-transparent           // Blend with parent background
          border-none              // No border needed here usually
          focus:outline-none       // Remove default focus outline
          text-gray-400            // Text color
          hover:text-gray-300
          text-sm                  // Font size
          cursor-pointer           // Indicate interactivity
          py-1 pr-6 pl-2             // Padding (right padding makes space for arrow)
          rounded                  // Optional: slight rounding
          text-right               // Align text to the right
          disabled:opacity-50      // Style when disabled
          disabled:cursor-not-allowed
          transition-colors
        `}
        // Apply right-to-left direction to position text near the arrow,
        // but ensure options render correctly left-to-right inside.
        style={{ direction: 'rtl' }}
      >
        {!hasDevices ? (
          // Show a disabled placeholder if no devices are found
          <option value="" disabled style={{ direction: 'ltr', textAlign: 'left' }}>
             {NO_DEVICES_MESSAGE}
          </option>
        ) : (
          // Map over the available device names
          devices.map((device) => (
            <option
              key={device}
              value={device}
              // Style options for normal LTR reading within the RTL select
              className="bg-gray-700 text-white" // Style dropdown options
              style={{ direction: 'ltr', textAlign: 'left' }} // Correct option text alignment
            >
              {device}
            </option>
          ))
        )}
      </select>

      {/* Custom dropdown arrow */}
      <div className={`
          pointer-events-none      // Prevent interaction with the arrow itself
          absolute inset-y-0 right-0 flex items-center px-1 // Position on the right
          ${disabled || !hasDevices ? 'text-gray-600' : 'text-gray-400'} // Dim arrow when disabled
        `}
      >
        <svg className="h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
          <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
        </svg>
      </div>
    </div>
  );
};

// Optional: export default MidiDeviceSelector;