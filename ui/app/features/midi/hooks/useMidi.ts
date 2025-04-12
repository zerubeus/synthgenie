// src/features/midi/hooks/useMidi.ts
import { useState, useEffect, useCallback, useRef } from 'react';
import type { MIDIAccess, MIDIOutput } from '../types'; // Import types from the feature's type definition

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
  /** Indicates if MIDI access is currently being initialized. */
  isInitializing: boolean;
  /** Stores any error message encountered during initialization. */
  error: string | null;
}

/**
 * Custom hook to manage Web MIDI API interactions. Handles device discovery,
 * selection, state changes, and sending MIDI CC messages.
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

  // --- Send MIDI CC Function ---
  const sendMidiCC = useCallback(
    (channel: number, cc: number, value: number) => {
      if (!selectedDevice || selectedDevice === NO_DEVICES_MESSAGE) {
        console.warn('Cannot send MIDI CC: No device selected.');
        return;
      }

      const output = outputsRef.current.get(selectedDevice); // Use ref here

      if (output) {
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
          // Optional: Set an error state or notify the user
          setError(
            `Failed to send MIDI to ${selectedDevice}. It might be disconnected.`
          );
          // Attempt to re-scan devices in case of error?
          // updateMidiDevices(midiAccess);
        }
      } else {
        console.warn(
          `Cannot send MIDI CC: Selected device "${selectedDevice}" not found in outputs map.`
        );
        // This indicates a potential state inconsistency. Re-scan might be needed.
        setError(
          `MIDI inconsistency: Selected device "${selectedDevice}" not found. Please re-select.`
        );
        updateMidiDevices(midiAccess); // Attempt to refresh state
      }
    },
    [selectedDevice, midiAccess, updateMidiDevices] // Depend on selectedDevice, access (for potential rescan), and update function
    // Note: We don't depend on midiOutputs directly, using outputsRef instead.
  );

  // --- Return Hook Values ---
  return {
    midiDevices,
    selectedDevice,
    setSelectedDevice,
    sendMidiCC,
    isInitializing,
    error,
  };
};

// --- Type Definitions (Should live in features/midi/types/index.ts) ---
/*
// src/features/midi/types/index.ts

// Basic Web MIDI API Interfaces (add more properties as needed)
export interface MIDIInput {
  id: string;
  name: string | null;
  manufacturer?: string;
  type: 'input';
  state: 'connected' | 'disconnected';
  connection: 'open' | 'closed' | 'pending';
  // Add onmidimessage handler type if needed
}

export interface MIDIOutput {
  id: string;
  name: string | null;
  manufacturer?: string;
  type: 'output';
  state: 'connected' | 'disconnected';
  connection: 'open' | 'closed' | 'pending';
  send: (data: number[] | Uint8Array, timestamp?: number) => void;
  clear: () => void;
}

// Define MIDIAccess interface based on actual Web MIDI API usage
export interface MIDIAccess extends EventTarget {
  inputs: Map<string, MIDIInput>;
  outputs: Map<string, MIDIOutput>;
  sysexEnabled: boolean;
  // onstatechange: ((event: Event) => void) | null; // Use addEventListener instead
}

*/
