import { useMemo, useEffect } from 'react';
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
  const midiHookResult = useMidi();
  const { midiDevices, selectedDevice, isInitializing, error } = midiHookResult;

  // Debug the entire hook result
  useEffect(() => {
    console.log('🔍 useMidiDeviceValidation: useMidi() returned:', {
      selectedDevice,
      midiDevices,
      isInitializing,
      error
    });
  }, [selectedDevice, midiDevices, isInitializing, error]);

  // Debug effect to monitor selectedDevice changes in validation hook
  useEffect(() => {
    console.log('🔍 useMidiDeviceValidation: selectedDevice effect triggered with:', selectedDevice);
  }, [selectedDevice]);

  const validDevices = useMemo(() => {
    const result = midiDevices.filter(device => {
      if (device === NO_DEVICES_MESSAGE) return false;
      
      // Use the same detection logic as the API
      return detectSynthType(device) !== null;
    });
    console.log('🔍 useMidiDeviceValidation: validDevices calculated:', result);
    return result;
  }, [midiDevices]);

  const hasValidDevice = useMemo(() => {
    if (isInitializing || !selectedDevice || selectedDevice === NO_DEVICES_MESSAGE) {
      console.log('🔍 useMidiDeviceValidation: hasValidDevice = false (no device/initializing)', {
        isInitializing,
        selectedDevice,
        isNoDevicesMessage: selectedDevice === NO_DEVICES_MESSAGE
      });
      return false;
    }
    
    // Use the same detection logic as the API
    const synthType = detectSynthType(selectedDevice);
    const isValid = synthType !== null;
    console.log('🎯 useMidiDeviceValidation: validation result:', {
      selectedDevice,
      synthType,
      isValid
    });
    return isValid;
  }, [selectedDevice, isInitializing]);

  console.log('🔍 useMidiDeviceValidation: returning values:', {
    hasValidDevice,
    selectedDevice,
    validDevices
  });

  return {
    hasValidDevice,
    isInitializing,
    midiDevices,
    selectedDevice,
    validDevices,
    error,
  };
}; 