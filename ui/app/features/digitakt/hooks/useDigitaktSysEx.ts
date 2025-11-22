/**
 * Hook for Digitakt SysEx communication over MIDI
 * Handles sending/receiving SysEx messages with queue management
 */

import { useState, useEffect, useCallback, useRef } from 'react';
import type { ElkMessage } from '../types/sysex';
import { buildMessage, parseMessage } from '../utils/sysex';

const RESPONSE_TIMEOUT_MS = 5000; // 5 seconds timeout for responses

interface UseDigitaktSysExReturn {
  /** Send a SysEx message and wait for response */
  sendMessage: (message: ElkMessage) => Promise<ElkMessage>;
  /** Check if connected to Digitakt */
  isConnected: boolean;
  /** Currently selected Digitakt device */
  selectedDevice: string | null;
  /** Available Digitakt devices */
  devices: string[];
  /** Select a Digitakt device */
  selectDevice: (deviceName: string) => void;
  /** Connection error if any */
  error: string | null;
  /** Whether MIDI is initializing */
  isInitializing: boolean;
}

/**
 * Custom hook for Digitakt SysEx communication
 */
export function useDigitaktSysEx(): UseDigitaktSysExReturn {
  const [midiAccess, setMidiAccess] = useState<MIDIAccess | null>(null);
  const [devices, setDevices] = useState<string[]>([]);
  const [selectedDevice, setSelectedDevice] = useState<string | null>(null);
  const [isInitializing, setIsInitializing] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const midiInputRef = useRef<MIDIInput | null>(null);
  const midiOutputRef = useRef<MIDIOutput | null>(null);
  const pendingResponseRef = useRef<{
    resolve: (msg: ElkMessage) => void;
    reject: (error: Error) => void;
    timeout: NodeJS.Timeout;
  } | null>(null);

  // Initialize MIDI access
  useEffect(() => {
    let accessInstance: MIDIAccess | null = null;

    const initMidi = async () => {
      setIsInitializing(true);
      setError(null);

      if (!navigator.requestMIDIAccess) {
        setError('Web MIDI API not supported in this browser');
        setIsInitializing(false);
        return;
      }

      try {
        accessInstance = await navigator.requestMIDIAccess({ sysex: true });
        setMidiAccess(accessInstance);

        // Update devices
        updateDevices(accessInstance);

        // Listen for device changes
        accessInstance.addEventListener('statechange', () => {
          if (accessInstance) {
            updateDevices(accessInstance);
          }
        });
      } catch (err) {
        console.error('MIDI access error:', err);
        setError(err instanceof Error ? err.message : 'Failed to access MIDI');
      } finally {
        setIsInitializing(false);
      }
    };

    initMidi();

    return () => {
      // Cleanup
      if (midiInputRef.current) {
        midiInputRef.current.onmidimessage = null;
      }
      if (accessInstance) {
        accessInstance.removeEventListener('statechange', () => {});
      }
    };
  }, []);

  // Update available devices
  const updateDevices = useCallback((access: MIDIAccess) => {
    const digitaktDevices: string[] = [];

    access.inputs.forEach((input) => {
      if (input.name && input.name.toLowerCase().includes('digitakt')) {
        digitaktDevices.push(input.name);
      }
    });

    setDevices(digitaktDevices);

    // Auto-select first device if none selected
    if (digitaktDevices.length > 0 && !selectedDevice) {
      setSelectedDevice(digitaktDevices[0]);
    } else if (digitaktDevices.length === 0) {
      setSelectedDevice(null);
    } else if (selectedDevice && !digitaktDevices.includes(selectedDevice)) {
      // Selected device disappeared
      setSelectedDevice(digitaktDevices[0] || null);
    }
  }, [selectedDevice]);

  // Setup MIDI input/output when device selected
  useEffect(() => {
    if (!midiAccess || !selectedDevice) {
      midiInputRef.current = null;
      midiOutputRef.current = null;
      return;
    }

    // Find matching input and output
    let input: MIDIInput | null = null;
    let output: MIDIOutput | null = null;

    midiAccess.inputs.forEach((i) => {
      if (i.name === selectedDevice) {
        input = i;
      }
    });

    midiAccess.outputs.forEach((o) => {
      if (o.name === selectedDevice) {
        output = o;
      }
    });

    if (!input || !output) {
      setError(`Could not find input/output for ${selectedDevice}`);
      return;
    }

    midiInputRef.current = input;
    midiOutputRef.current = output;

    // Setup message listener
    input.onmidimessage = (event: MIDIMessageEvent) => {
      if (event.data) {
        handleMidiMessage(event.data);
      }
    };

    console.log(`Connected to Digitakt: ${selectedDevice}`);
  }, [midiAccess, selectedDevice]);

  // Handle incoming MIDI messages
  const handleMidiMessage = useCallback((data: Uint8Array) => {
    // Ignore clock and other realtime messages
    if (data[0] >= 0xF8) return;

    // Only process SysEx messages
    if (data[0] === 0xF0) {
      try {
        const message = parseMessage(data);

        if (pendingResponseRef.current) {
          clearTimeout(pendingResponseRef.current.timeout);
          pendingResponseRef.current.resolve(message);
          pendingResponseRef.current = null;
        }
      } catch (err) {
        console.error('Parse error:', err);
      }
    }
  }, []);

  // Send SysEx message and wait for response
  const sendMessage = useCallback(
    async (message: ElkMessage): Promise<ElkMessage> => {
      if (!midiOutputRef.current) {
        throw new Error('No MIDI output available');
      }

      // Check if there's already a pending response
      if (pendingResponseRef.current) {
        throw new Error('Another message is pending. Please wait.');
      }

      // Build and send message
      const data = buildMessage(message);

      return new Promise((resolve, reject) => {
        const timeout = setTimeout(() => {
          pendingResponseRef.current = null;
          reject(new Error('Response timeout'));
        }, RESPONSE_TIMEOUT_MS);

        pendingResponseRef.current = { resolve, reject, timeout };

        try {
          midiOutputRef.current!.send(data);
        } catch (err) {
          clearTimeout(timeout);
          pendingResponseRef.current = null;
          reject(err);
        }
      });
    },
    []
  );

  // Select device
  const selectDevice = useCallback((deviceName: string) => {
    if (devices.includes(deviceName)) {
      setSelectedDevice(deviceName);
      setError(null);
    } else {
      setError(`Device not found: ${deviceName}`);
    }
  }, [devices]);

  return {
    sendMessage,
    isConnected: !!midiOutputRef.current,
    selectedDevice,
    devices,
    selectDevice,
    error,
    isInitializing,
  };
}
