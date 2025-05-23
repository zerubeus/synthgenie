import { useMemo } from 'react';
import { useMidi } from './useMidi';

// Valid device keywords (case-insensitive)
const VALID_DEVICE_KEYWORDS = ['moog', 'digitone'];
const NO_DEVICES_MESSAGE = 'No MIDI devices detected';

interface UseMidiDeviceValidationReturn {
  /** Whether a valid MIDI device is connected and selected */
  hasValidDevice: boolean;
  /** Whether MIDI is still initializing */
  isInitializing: boolean;
  /** Array of all detected MIDI devices */
  midiDevices: string[];
  /** Currently selected device */
  selectedDevice: string;
  /** Array of valid devices found */
  validDevices: string[];
  /** Error message if any */
  error: string | null;
}

/**
 * Hook to validate if the user has a valid MIDI device connected.
 * Valid devices must contain "moog" or "digitone" in their name (case-insensitive).
 */
export const useMidiDeviceValidation = (): UseMidiDeviceValidationReturn => {
  const { midiDevices, selectedDevice, isInitializing, error } = useMidi();

  const validDevices = useMemo(() => {
    return midiDevices.filter(device => {
      if (device === NO_DEVICES_MESSAGE) return false;
      
      const deviceNameLower = device.toLowerCase();
      return VALID_DEVICE_KEYWORDS.some(keyword => 
        deviceNameLower.includes(keyword.toLowerCase())
      );
    });
  }, [midiDevices]);

  const hasValidDevice = useMemo(() => {
    if (isInitializing || !selectedDevice || selectedDevice === NO_DEVICES_MESSAGE) {
      return false;
    }
    
    const selectedDeviceLower = selectedDevice.toLowerCase();
    return VALID_DEVICE_KEYWORDS.some(keyword => 
      selectedDeviceLower.includes(keyword.toLowerCase())
    );
  }, [selectedDevice, isInitializing]);

  return {
    hasValidDevice,
    isInitializing,
    midiDevices,
    selectedDevice,
    validDevices,
    error,
  };
}; 