// src/features/midi/hooks/useMidi.ts
import { useState, useEffect, useCallback, useRef } from 'react';
import type { MIDIAccess, MIDIOutput } from '../types'; // Import types from the feature's type definition
import type { SynthGenieResponse } from '../../api/types';

// --- Constants ---
const NO_DEVICES_MESSAGE = 'No MIDI devices detected';
const MIDI_CC_STATUS_BYTE_BASE = 0xb0; // 176 in decimal (Control Change base for channel 1)

// --- Hook Return Type ---
interface UseMidiReturn {
  /** Array of detected MIDI output device names. */
  midiDevices: string[];
  /** The name of the currently selected MIDI output device. */
  selectedDevice: string;
  /** Function to update the selected MIDI device. */
  setSelectedDevice: React.Dispatch<React.SetStateAction<string>>;
  /** Function to send a MIDI Control Change (CC) message to the selected device. */
  sendMidiCC: (channel: number, cc: number, value: number) => void;
  /** Function to send a MIDI message based on SynthGenieResponse data. */
  sendMidiMessage: (response: SynthGenieResponse) => void;
  /** Function to send a high-resolution MIDI CC message (14-bit). */
  sendHighResCC: (channel: number, ccMsb: number, ccLsb: number, value: number) => void;
  /** Function to send an NRPN message. */
  sendNRPN: (channel: number, nrpnMsb: number, nrpnLsb: number, value: number) => void;
  /** Indicates if MIDI access is currently being initialized. */
  isInitializing: boolean;
  /** Stores any error message encountered during initialization. */
  error: string | null;
}

/**
 * Custom hook to manage Web MIDI API interactions. Handles device discovery,
 * selection, state changes, and sending different types of MIDI messages.
 */
export const useMidi = (): UseMidiReturn => {
  // --- State ---
  const [midiAccess, setMidiAccess] = useState<MIDIAccess | null>(null);
  const [midiOutputs, setMidiOutputs] = useState<Map<string, MIDIOutput>>(
    new Map()
  );
  const [midiDevices, setMidiDevices] = useState<string[]>([
    NO_DEVICES_MESSAGE,
  ]);
  const [selectedDevice, setSelectedDevice] = useState<string>(''); // Start empty, set on discovery
  const [isInitializing, setIsInitializing] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Use a ref to hold the outputs map to avoid including it in useCallback dependencies
  // where its identity might change frequently.
  const outputsRef = useRef(midiOutputs);
  useEffect(() => {
    outputsRef.current = midiOutputs;
  }, [midiOutputs]);

  // --- Device Update Logic ---
  const updateMidiDevices = useCallback((access: MIDIAccess | null) => {
    if (!access) {
      setMidiDevices([NO_DEVICES_MESSAGE]);
      setMidiOutputs(new Map());
      setSelectedDevice('');
      outputsRef.current = new Map();
      return;
    }

    const detectedDevices: string[] = [];
    const detectedOutputs = new Map<string, MIDIOutput>();
    let deviceIndex = 0; // For naming unnamed devices

    access.outputs.forEach((output: MIDIOutput) => {
      // Provide a default name if missing
      const name = output.name || `MIDI Output ${++deviceIndex}`;
      detectedDevices.push(name);
      detectedOutputs.set(name, output);
    });

    setMidiOutputs(detectedOutputs);
    outputsRef.current = detectedOutputs; // Update ref immediately

    if (detectedDevices.length > 0) {
      setMidiDevices(detectedDevices);
      // If no device is selected OR the previously selected device disappeared, select the first one
      setSelectedDevice((currentSelected) => {
        if (!currentSelected || !detectedDevices.includes(currentSelected)) {
          return detectedDevices[0]; // Default to the first available device
        }
        return currentSelected; // Keep current selection if still valid
      });
    } else {
      setMidiDevices([NO_DEVICES_MESSAGE]);
      setSelectedDevice(''); // No devices, clear selection
    }
  }, []); // No dependencies needed as it uses the 'access' argument

  // --- MIDI Initialization Effect ---
  useEffect(() => {
    let accessInstance: MIDIAccess | null = null;

    const onMidiStateChange = () => {
      console.log('MIDI state changed. Re-scanning devices...');
      if (accessInstance) {
        // Re-scan using the existing access object
        updateMidiDevices(accessInstance);
      }
    };

    const initializeMidi = async () => {
      setIsInitializing(true);
      setError(null);
      if (navigator.requestMIDIAccess) {
        try {
          // Explicitly cast to unknown first if types mismatch significantly
          accessInstance =
            (await navigator.requestMIDIAccess()) as unknown as MIDIAccess;
          console.log('MIDI Access Granted:', accessInstance);
          setMidiAccess(accessInstance);
          updateMidiDevices(accessInstance); // Initial device scan

          // Listen for future device connections/disconnections
          accessInstance.addEventListener('statechange', onMidiStateChange);
        } catch (err) {
          console.error('MIDI access denied or unavailable:', err);
          setError(
            `MIDI Error: ${err instanceof Error ? err.message : String(err)}`
          );
          setMidiAccess(null);
          updateMidiDevices(null); // Reset state on error
        } finally {
          setIsInitializing(false);
        }
      } else {
        console.warn('Web MIDI API not supported in this browser.');
        setError('Web MIDI API is not supported by your browser.');
        updateMidiDevices(null); // Reset state
        setIsInitializing(false);
      }
    };

    initializeMidi();

    // --- Cleanup ---
    return () => {
      // Remove the event listener when the component unmounts
      if (accessInstance) {
        accessInstance.removeEventListener('statechange', onMidiStateChange);
        console.log('Removed MIDI statechange listener.');
        // Note: We don't typically 'close' MIDIAccess itself.
      }
    };
  }, [updateMidiDevices]); // Include updateMidiDevices in dependency array

  // --- Helper function to get selected output ---
  const getSelectedOutput = useCallback((): MIDIOutput | null => {
    if (!selectedDevice || selectedDevice === NO_DEVICES_MESSAGE) {
      console.warn('Cannot send MIDI: No device selected.');
      return null;
    }

    const output = outputsRef.current.get(selectedDevice);
    if (!output) {
      console.warn(
        `Cannot send MIDI: Selected device "${selectedDevice}" not found in outputs map.`
      );
      setError(
        `MIDI inconsistency: Selected device "${selectedDevice}" not found. Please re-select.`
      );
      updateMidiDevices(midiAccess); // Attempt to refresh state
      return null;
    }

    return output;
  }, [selectedDevice, midiAccess, updateMidiDevices]);

  // --- Send Standard MIDI CC Function ---
  const sendMidiCC = useCallback(
    (channel: number, cc: number, value: number) => {
      const output = getSelectedOutput();
      if (!output) return;

      // Basic validation/clamping
      const midiChannel = Math.max(1, Math.min(16, Math.floor(channel))); // Ensure 1-16
      const controlChange = Math.max(0, Math.min(127, Math.floor(cc))); // Ensure 0-127
      const ccValue = Math.max(0, Math.min(127, Math.floor(value))); // Ensure 0-127

      // Calculate MIDI status byte (0xB0 = CC for channel 1)
      const statusByte = MIDI_CC_STATUS_BYTE_BASE + (midiChannel - 1);
      const midiMessage = [statusByte, controlChange, ccValue];

      try {
        output.send(midiMessage);
        console.log(
          `MIDI CC Sent to "${selectedDevice}": Ch ${midiChannel}, CC ${controlChange}, Val ${ccValue} (Raw: ${midiMessage})`
        );
      } catch (sendError) {
        console.error(
          `Error sending MIDI message to "${selectedDevice}":`,
          sendError,
          midiMessage
        );
        setError(
          `Failed to send MIDI to ${selectedDevice}. It might be disconnected.`
        );
      }
    },
    [selectedDevice, getSelectedOutput]
  );

  // --- Send High-Resolution MIDI CC Function ---
  const sendHighResCC = useCallback(
    (channel: number, ccMsb: number, ccLsb: number, value: number) => {
      const output = getSelectedOutput();
      if (!output) return;

      // Basic validation/clamping
      const midiChannel = Math.max(1, Math.min(16, Math.floor(channel))); // Ensure 1-16
      const msbCC = Math.max(0, Math.min(127, Math.floor(ccMsb))); // Ensure 0-127
      const lsbCC = Math.max(0, Math.min(127, Math.floor(ccLsb))); // Ensure 0-127
      const highResValue = Math.max(0, Math.min(16383, Math.floor(value))); // Ensure 0-16383

      // Split value into MSB and LSB
      const msb = (highResValue >> 7) & 0x7F; // Most significant 7 bits
      const lsb = highResValue & 0x7F; // Least significant 7 bits

      // Calculate MIDI status byte
      const statusByte = MIDI_CC_STATUS_BYTE_BASE + (midiChannel - 1);

      try {
        // First reset both controllers to 0 to ensure proper initialization
        const resetMsbMessage = [statusByte, msbCC, 0];
        const resetLsbMessage = [statusByte, lsbCC, 0];
        
        // Then send the actual values - LSB first, then MSB
        const lsbMessage = [statusByte, lsbCC, lsb];
        const msbMessage = [statusByte, msbCC, msb];

        // Send messages in the correct order
        output.send(resetMsbMessage);
        output.send(resetLsbMessage);
        output.send(lsbMessage);
        output.send(msbMessage);

        console.log(
          `High-Res CC Sent to "${selectedDevice}": Ch ${midiChannel}, MSB CC ${msbCC}, LSB CC ${lsbCC}, Val ${highResValue} (msb=${msb}, lsb=${lsb})`
        );
      } catch (sendError) {
        console.error(
          `Error sending high-res CC message to "${selectedDevice}":`,
          sendError
        );
        setError(
          `Failed to send high-res CC to ${selectedDevice}. It might be disconnected.`
        );
      }
    },
    [selectedDevice, getSelectedOutput]
  );

  // --- Send NRPN Function ---
  const sendNRPN = useCallback(
    (channel: number, nrpnMsb: number, nrpnLsb: number, value: number) => {
      const output = getSelectedOutput();
      if (!output) return;

      // Basic validation/clamping
      const midiChannel = Math.max(1, Math.min(16, Math.floor(channel))); // Ensure 1-16
      const nrpnMsbValue = Math.max(0, Math.min(127, Math.floor(nrpnMsb))); // Ensure 0-127
      const nrpnLsbValue = Math.max(0, Math.min(127, Math.floor(nrpnLsb))); // Ensure 0-127
      const nrpnValue = Math.max(0, Math.min(16383, Math.floor(value))); // Ensure 0-16383

      // Split value into MSB and LSB
      const valueMsb = (nrpnValue >> 7) & 0x7F; // Most significant 7 bits
      const valueLsb = nrpnValue & 0x7F; // Least significant 7 bits

      // Calculate MIDI status byte
      const statusByte = MIDI_CC_STATUS_BYTE_BASE + (midiChannel - 1);

      try {
        // Send NRPN messages in the correct order:
        // 1. NRPN MSB (CC 99)
        // 2. NRPN LSB (CC 98)
        // 3. Data Entry MSB (CC 6)
        // 4. Data Entry LSB (CC 38)
        const nrpnMsbMessage = [statusByte, 99, nrpnMsbValue];
        const nrpnLsbMessage = [statusByte, 98, nrpnLsbValue];
        const dataMsbMessage = [statusByte, 6, valueMsb];
        const dataLsbMessage = [statusByte, 38, valueLsb];

        output.send(nrpnMsbMessage);
        output.send(nrpnLsbMessage);
        output.send(dataMsbMessage);
        output.send(dataLsbMessage);

        console.log(
          `NRPN Sent to "${selectedDevice}": Ch ${midiChannel}, NRPN MSB ${nrpnMsbValue}, NRPN LSB ${nrpnLsbValue}, Val ${nrpnValue} (msb=${valueMsb}, lsb=${valueLsb})`
        );
      } catch (sendError) {
        console.error(
          `Error sending NRPN message to "${selectedDevice}":`,
          sendError
        );
        setError(
          `Failed to send NRPN to ${selectedDevice}. It might be disconnected.`
        );
      }
    },
    [selectedDevice, getSelectedOutput]
  );

  // --- Send MIDI Message based on SynthGenieResponse ---
  const sendMidiMessage = useCallback(
    (response: SynthGenieResponse) => {
      const { midi_channel, value, midi_cc, midi_cc_lsb, nrpn_msb, nrpn_lsb } = response;

      // Determine message type and send accordingly
      if (nrpn_msb !== null && nrpn_msb !== undefined && 
          nrpn_lsb !== null && nrpn_lsb !== undefined) {
        // NRPN message
        sendNRPN(midi_channel, nrpn_msb, nrpn_lsb, value);
      } else if (midi_cc !== null && midi_cc !== undefined &&
                 midi_cc_lsb !== null && midi_cc_lsb !== undefined) {
        // High-resolution CC message
        sendHighResCC(midi_channel, midi_cc, midi_cc_lsb, value);
      } else if (midi_cc !== null && midi_cc !== undefined) {
        // Standard CC message
        sendMidiCC(midi_channel, midi_cc, value);
      } else {
        console.warn('Invalid MIDI message format in response:', response);
        setError('Received invalid MIDI message format from server.');
      }
    },
    [sendMidiCC, sendHighResCC, sendNRPN]
  );

  // --- Return Hook Values ---
  return {
    midiDevices,
    selectedDevice,
    setSelectedDevice,
    sendMidiCC,
    sendMidiMessage,
    sendHighResCC,
    sendNRPN,
    isInitializing,
    error,
  };
};

