import React from 'react';
import type { ChangeEvent } from 'react';
import { MidiDeviceSelector } from '../../midi/components/MidiDeviceSelector';

interface MidiAccessRestrictionProps {
  /** Array of all detected MIDI devices */
  midiDevices: string[];
  /** Currently selected device */
  selectedDevice: string;
  /** Function to change selected device */
  onDeviceChange: (e: ChangeEvent<HTMLSelectElement>) => void;
  /** Array of valid devices found */
  validDevices: string[];
  /** Whether MIDI is still initializing */
  isInitializing: boolean;
  /** Error message if any */
  error: string | null;
}

/**
 * Component displayed when user doesn't have a valid MIDI device connected.
 * Shows requirements and device selector.
 */
export const MidiAccessRestriction: React.FC<MidiAccessRestrictionProps> = ({
  midiDevices,
  selectedDevice,
  onDeviceChange,
  validDevices,
  isInitializing,
  error,
}) => {
  return (
    <div className="flex flex-col h-screen bg-gray-900 border border-gray-800 overflow-hidden shadow-2xl">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-4">
        <h1 className="text-xl font-bold text-white">SynthGenie Chat</h1>
        <p className="text-blue-100 text-sm">MIDI Device Required</p>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex items-center justify-center p-8">
        <div className="max-w-md w-full space-y-6 text-center">
          {/* Lock Icon */}
          <div className="mx-auto w-16 h-16 bg-gray-800 rounded-full flex items-center justify-center">
            <svg className="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>

          {/* Title */}
          <h2 className="text-2xl font-bold bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400 bg-clip-text text-transparent">
            Valid MIDI Device Required
          </h2>

          {/* Description */}
          <div className="space-y-4 text-gray-300">
            <p>
              To access SynthGenie Chat, you need a compatible MIDI device connected and selected.
            </p>
            
            <div className="bg-gray-800 rounded-lg p-4 text-left">
              <h3 className="font-semibold text-white mb-2">Supported Devices:</h3>
              <ul className="space-y-1 text-sm">
                <li className="flex items-center">
                  <span className="w-2 h-2 bg-blue-400 rounded-full mr-2"></span>
                  Devices containing "Moog" in the name
                </li>
                <li className="flex items-center">
                  <span className="w-2 h-2 bg-indigo-400 rounded-full mr-2"></span>
                  Devices containing "Digitone" in the name
                </li>
              </ul>
            </div>

            {/* Current Status */}
            <div className="bg-gray-800 rounded-lg p-4">
              <h3 className="font-semibold text-white mb-2">Current Status:</h3>
              
              {isInitializing ? (
                <div className="flex items-center text-yellow-400">
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-yellow-400 mr-2"></div>
                  Scanning for MIDI devices...
                </div>
              ) : error ? (
                <div className="text-red-400">
                  <p className="text-sm">{error}</p>
                </div>
              ) : validDevices.length > 0 ? (
                <div className="text-green-400">
                  <p className="text-sm">✓ Valid devices found: {validDevices.length}</p>
                  <ul className="text-xs mt-1 space-y-1">
                    {validDevices.map((device, index) => (
                      <li key={index} className="text-green-300">• {device}</li>
                    ))}
                  </ul>
                </div>
              ) : (
                <div className="text-red-400">
                  <p className="text-sm">✗ No valid devices detected</p>
                </div>
              )}
            </div>
          </div>

          {/* Device Selector */}
          <div className="space-y-2">
            <label className="block text-sm font-medium text-gray-300">
              Select MIDI Device:
            </label>
            <MidiDeviceSelector
              devices={midiDevices}
              selectedDevice={selectedDevice}
              onChange={onDeviceChange}
              disabled={isInitializing}
            />
          </div>

          {/* Help Text */}
          <div className="text-xs text-gray-500 space-y-2">
            <p>
              Make sure your MIDI device is connected and powered on.
            </p>
            <p>
              If you don't see your device, try refreshing the page or reconnecting your device.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}; 