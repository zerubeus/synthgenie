// src/features/midi/types/index.ts

/**
 * Represents the connection status of a MIDI port (e.g., whether it's available for use).
 */
export type MIDIPortConnectionState = 'open' | 'closed' | 'pending';

/**
 * Represents the state of the physical device associated with a MIDI port
 * (e.g., whether it's plugged in or unplugged).
 */
export type MIDIPortDeviceState = 'connected' | 'disconnected';

/**
 * Base properties common to both MIDIInput and MIDIOutput ports.
 * Based on the Web MIDI API MIDIPort interface.
 */
export interface MIDIPort {
  /** A unique ID assigned by the system to the port. */
  id: string;
  /** The manufacturer of the device, if provided by the system or driver. */
  manufacturer?: string;
  /** The system-provided name of the port. Can be null if unavailable. */
  name: string | null;
  /** The type of the port ('input' or 'output'). */
  type: 'input' | 'output';
  /** The version of the underlying hardware or software, if available. */
  version?: string;
  /** The current state of the device ('connected' or 'disconnected'). */
  state: MIDIPortDeviceState;
  /** The current connection status of the port ('open', 'closed', or 'pending'). */
  connection: MIDIPortConnectionState;
  // Note: The 'onstatechange' property exists but using addEventListener on MIDIAccess is preferred.
}

/**
 * Represents a MIDI input port, capable of receiving MIDI messages.
 * Extends the base MIDIPort interface.
 */
export interface MIDIInput extends MIDIPort {
  type: 'input';
  // Add 'onmidimessage' property definition if you plan to receive MIDI input messages.
  // onmidimessage: ((event: MIDIMessageEvent) => void) | null;
}

/**
 * Represents a MIDI output port, capable of sending MIDI messages.
 * Extends the base MIDIPort interface.
 */
export interface MIDIOutput extends MIDIPort {
  type: 'output';

  /**
   * Enqueues MIDI message(s) to be sent to the output port.
   * @param data A sequence of MIDI data bytes (e.g., [0x90, 0x40, 0x7f] for Note On).
   *             Can be a number array or a Uint8Array.
   * @param timestamp Optional DOMHighResTimeStamp specifying when the message(s) should be sent.
   *                  If omitted, messages are sent immediately.
   */
  send: (data: number[] | Uint8Array, timestamp?: DOMHighResTimeStamp) => void;

  /**
   * Clears any MIDI messages currently queued to be sent from this port but not yet dispatched.
   */
  clear: () => void;
}

/**
 * Represents access to the system's MIDI services, obtained via `navigator.requestMIDIAccess`.
 * Provides maps of available input and output ports and handles state changes.
 * Extends EventTarget to allow for addEventListener/removeEventListener usage.
 */
export interface MIDIAccess extends EventTarget {
  /** A Map containing all currently available MIDI input ports, keyed by their unique IDs. */
  inputs: Map<string, MIDIInput>;
  /** A Map containing all currently available MIDI output ports, keyed by their unique IDs. */
  outputs: Map<string, MIDIOutput>;
  /** Indicates whether System Exclusive (SysEx) messages are permitted to be sent or received. */
  sysexEnabled: boolean;
  // Note: The 'onstatechange' property exists but using addEventListener('statechange', ...) is preferred.
  // onstatechange: ((event: Event) => void) | null;
}

/** Optional: Define the structure of a MIDIMessageEvent if needed for input handling */
/*
export interface MIDIMessageEvent extends Event {
  // The time when the event occurred
  receivedTime: DOMHighResTimeStamp;
  // A Uint8Array containing the MIDI data bytes of the received message(s).
  data: Uint8Array;
}
*/
