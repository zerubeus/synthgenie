import { useMemo } from 'react';
import { useMidi } from './useMidi';
import { detectSynthType } from '../../api/utils/getApiBaseUrl';

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
 * Valid devices must be supported by the API (Moog Subsequent 37 or Elektron Digitone).
 */
export const useMidiDeviceValidation = (): UseMidiDeviceValidationReturn => {
  const { midiDevices, selectedDevice, isInitializing, error } = useMidi();

  const validDevices = useMemo(() => {
    const valid = midiDevices.filter(device => {
      if (device === NO_DEVICES_MESSAGE) return false;
      
      // Use the same detection logic as the API
      const synthType = detectSynthType(device);
      console.log('🔍 Device validation:', { device, synthType });
      return synthType !== null;
    });
    
    console.log('✅ Valid devices found:', valid);
    return valid;
  }, [midiDevices]);

  const hasValidDevice = useMemo(() => {
    if (isInitializing || !selectedDevice || selectedDevice === NO_DEVICES_MESSAGE) {
      console.log('❌ No valid device - initializing or no selection:', {
        isInitializing,
        selectedDevice,
        isNoDevicesMessage: selectedDevice === NO_DEVICES_MESSAGE
      });
      return false;
    }
    
    // Use the same detection logic as the API
    const synthType = detectSynthType(selectedDevice);
    const isValid = synthType !== null;
    
    console.log('🎯 Selected device validation:', {
      selectedDevice,
      synthType,
      isValid
    });
    
    return isValid;
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