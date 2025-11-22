/**
 * Device test component to probe the Digitakt and find correct device ID
 */

import { useState } from 'react';

export function DeviceTest() {
  const [result, setResult] = useState<string>('');

  const testDeviceId = async (deviceId: number) => {
    setResult(`Testing device ID 0x${deviceId.toString(16).padStart(2, '0')}...`);

    try {
      // Get MIDI access directly
      const access = await navigator.requestMIDIAccess({ sysex: true });

      // Find Digitakt output
      let digitaktOutput: MIDIOutput | null = null;
      access.outputs.forEach((output) => {
        if (output.name && output.name.toLowerCase().includes('digitakt')) {
          digitaktOutput = output;
        }
      });

      if (!digitaktOutput) {
        setResult('No Digitakt output found');
        return;
      }

      // Device request: F0 00 20 3C [deviceId] 00 01 F7
      const message = new Uint8Array([
        0xF0,           // SysEx start
        0x00, 0x20, 0x3C, // Elektron manufacturer ID
        deviceId,       // Device ID to test
        0x00,           // Sub ID
        0x01,           // Device request command
        0xF7            // SysEx end
      ]);

      console.log(`Sending test with device ID 0x${deviceId.toString(16)}:`,
        Array.from(message).map(b => '0x' + b.toString(16).padStart(2, '0')).join(' '));

      digitaktOutput.send(message);

      setResult(`Sent test for device ID 0x${deviceId.toString(16).padStart(2, '0')} - check console for response`);
    } catch (err) {
      setResult(`Error: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  };

  const testCommonIds = async () => {
    const commonIds = [
      0x10, // Digitakt (original)
      0x11, // Possible Digitakt II
      0x12, // Another possible ID
      0x0C, // Digitone
      0x0E, // Analog Rytm
      0x0F, // Analog Four
    ];

    for (const id of commonIds) {
      await testDeviceId(id);
      await new Promise(resolve => setTimeout(resolve, 1000));
    }
  };

  return (
    <div className="bg-yellow-50 border border-yellow-200 rounded p-4 mb-4">
      <h3 className="font-semibold text-gray-900 mb-2">Device ID Test</h3>
      <p className="text-sm text-gray-700 mb-3">
        The Digitakt II might use a different device ID than the original Digitakt.
        Try these tests to find the correct ID:
      </p>

      <div className="flex gap-2 mb-3">
        <button
          onClick={testCommonIds}
          className="px-3 py-1 bg-yellow-600 text-white rounded text-sm hover:bg-yellow-700"
        >
          Test Common IDs
        </button>

        <button
          onClick={() => testDeviceId(0x10)}
          className="px-3 py-1 bg-gray-600 text-white rounded text-sm hover:bg-gray-700"
        >
          Test 0x10 (Digitakt)
        </button>

        <button
          onClick={() => testDeviceId(0x11)}
          className="px-3 py-1 bg-gray-600 text-white rounded text-sm hover:bg-gray-700"
        >
          Test 0x11 (DT II?)
        </button>

        <button
          onClick={() => testDeviceId(0x12)}
          className="px-3 py-1 bg-gray-600 text-white rounded text-sm hover:bg-gray-700"
        >
          Test 0x12
        </button>
      </div>

      {result && (
        <div className="text-sm text-gray-700 bg-white p-2 rounded font-mono">
          {result}
        </div>
      )}

      <p className="text-xs text-gray-600 mt-2">
        Watch the browser console for incoming SysEx responses. If you see a response (starting with 0xf0),
        note the 5th byte - that's the device ID!
      </p>
    </div>
  );
}
