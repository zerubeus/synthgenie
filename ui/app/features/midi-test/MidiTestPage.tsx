import React, { useState, useEffect } from 'react';
import type { ChangeEvent } from 'react';
import { useMidi } from '../midi/hooks/useMidi';
import { SynthSelector } from '../midi/components/SynthSelector';
import { detectSynthType } from '../api/utils/getApiBaseUrl';
import type { SynthType } from '../api/types';
import { DIGITONE_PARAMS } from './parameterData';
import type { ParamConfig } from './parameterData';
import valueMappings from './valueMappings.json';

interface ValueMapping {
  midi: number;
  display: string;
}

interface ParamMapping {
  cc: number;
  function: string;
  values: ValueMapping[];
}

const MidiTestPage: React.FC = () => {
  const {
    midiDevices,
    selectedDevice,
    setSelectedDevice,
    sendMidiCC,
    sendNRPN,
    sendHighResCC,
    isInitializing,
    error,
  } = useMidi();

  const [selectedParamSet, setSelectedParamSet] = useState<string>(
    Object.keys(DIGITONE_PARAMS)[0]
  );
  const [selectedParam, setSelectedParam] = useState<string>(
    Object.keys(DIGITONE_PARAMS[Object.keys(DIGITONE_PARAMS)[0]])[0]
  );
  const [selectedMappedValue, setSelectedMappedValue] = useState<number>(0);
  const [freeValue, setFreeValue] = useState<string>('64');
  const [midiChannel, setMidiChannel] = useState<number>(1);
  const [lastSent, setLastSent] = useState<string>('');

  const currentParams = DIGITONE_PARAMS[selectedParamSet];
  const currentParam = currentParams[selectedParam] as ParamConfig;

  // Find value mapping for current parameter
  const currentMapping = Object.entries(valueMappings as Record<string, ParamMapping>).find(
    ([key, mapping]) => mapping.cc === currentParam?.cc_msb
  )?.[1];

  const handleSynthChange = (synthType: SynthType) => {
    const matchingDevice = midiDevices.find(
      (device) => detectSynthType(device) === synthType
    );
    if (matchingDevice) {
      setSelectedDevice(matchingDevice);
    }
  };

  const handleSendMapped = () => {
    if (!currentParam || !selectedDevice) return;

    sendMidiCC(midiChannel, currentParam.cc_msb, selectedMappedValue);

    const displayValue = currentMapping?.values.find(v => v.midi === selectedMappedValue)?.display || selectedMappedValue;
    setLastSent(
      `Sent MAPPED: ${selectedParamSet}.${selectedParam} | CC=${currentParam.cc_msb} | MIDI Value=${selectedMappedValue} | Display="${displayValue}" | Channel=${midiChannel}`
    );
  };

  const handleSendFree = () => {
    if (!currentParam || !selectedDevice) return;

    const numValue = parseFloat(freeValue) || 0;
    sendMidiCC(midiChannel, currentParam.cc_msb, numValue);

    setLastSent(
      `Sent FREE: ${selectedParamSet}.${selectedParam} | CC=${currentParam.cc_msb} | MIDI Value=${freeValue} | Channel=${midiChannel}`
    );
  };

  const handleParamSetChange = (e: ChangeEvent<HTMLSelectElement>) => {
    const newSet = e.target.value;
    setSelectedParamSet(newSet);
    // Set first param of the new set
    const firstParam = Object.keys(DIGITONE_PARAMS[newSet])[0];
    setSelectedParam(firstParam);
  };

  const handleParamChange = (e: ChangeEvent<HTMLSelectElement>) => {
    setSelectedParam(e.target.value);
  };

  if (isInitializing) {
    return (
      <div className="flex items-center justify-center h-screen bg-gray-900">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-400 mx-auto mb-4"></div>
          <p className="text-gray-400">Initializing MIDI...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-screen bg-gray-900">
        <div className="text-center text-red-400">
          <p className="text-xl mb-2">MIDI Error</p>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6 text-blue-400">
          MIDI Parameter Test
        </h1>

        {/* Device Selector */}
        <div className="mb-6 bg-gray-800 p-6 rounded-lg border border-gray-700">
          <h2 className="text-xl font-semibold mb-4 text-gray-300">
            MIDI Device
          </h2>
          <SynthSelector
            midiDevices={midiDevices}
            selectedDevice={selectedDevice || ''}
            onSynthChange={handleSynthChange}
            disabled={false}
          />
          {selectedDevice && (
            <p className="mt-2 text-sm text-gray-400">
              Connected: {selectedDevice}
            </p>
          )}
        </div>

        {/* Parameter Selection */}
        <div className="bg-gray-800 p-6 rounded-lg border border-gray-700 mb-6">
          <h2 className="text-xl font-semibold mb-4 text-gray-300">
            Parameter Selection
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            {/* Parameter Set */}
            <div>
              <label className="block text-sm font-medium text-gray-400 mb-2">
                Parameter Set
              </label>
              <select
                value={selectedParamSet}
                onChange={handleParamSetChange}
                className="w-full bg-gray-700 border border-gray-600 text-gray-100 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                {Object.keys(DIGITONE_PARAMS).map((set) => (
                  <option key={set} value={set}>
                    {set}
                  </option>
                ))}
              </select>
            </div>

            {/* Parameter */}
            <div>
              <label className="block text-sm font-medium text-gray-400 mb-2">
                Parameter
              </label>
              <select
                value={selectedParam}
                onChange={handleParamChange}
                className="w-full bg-gray-700 border border-gray-600 text-gray-100 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                {Object.keys(currentParams).map((param) => (
                  <option key={param} value={param}>
                    {param}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Parameter Info */}
          {currentParam && (
            <div className="bg-gray-700 p-4 rounded-lg mb-4">
              <h3 className="text-sm font-semibold text-gray-300 mb-2">
                Parameter Details
              </h3>
              <div className="grid grid-cols-2 gap-2 text-sm">
                <div>
                  <span className="text-gray-400">CC MSB:</span>{' '}
                  <span className="text-blue-400">{currentParam.cc_msb}</span>
                </div>
                {currentParam.nrpn_msb !== undefined && (
                  <div>
                    <span className="text-gray-400">NRPN MSB:</span>{' '}
                    <span className="text-blue-400">
                      {currentParam.nrpn_msb}
                    </span>
                  </div>
                )}
                {currentParam.nrpn_lsb !== undefined && (
                  <div>
                    <span className="text-gray-400">NRPN LSB:</span>{' '}
                    <span className="text-blue-400">
                      {currentParam.nrpn_lsb}
                    </span>
                  </div>
                )}
                {currentParam.default !== undefined && (
                  <div>
                    <span className="text-gray-400">Default:</span>{' '}
                    <span className="text-blue-400">
                      {currentParam.default}
                    </span>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* Mapped Values Section */}
          {currentMapping && currentMapping.values.length > 0 && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold text-green-400 mb-3">
                Mapped Values (from tool definition)
              </h3>
              <div className="grid grid-cols-1 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-400 mb-2">
                    Select Expected Value
                  </label>
                  <select
                    value={selectedMappedValue}
                    onChange={(e) => setSelectedMappedValue(Number(e.target.value))}
                    className="w-full bg-gray-700 border border-green-500 text-gray-100 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-green-500"
                  >
                    {currentMapping.values.map((v) => (
                      <option key={v.midi} value={v.midi}>
                        MIDI {v.midi} = {v.display}
                      </option>
                    ))}
                  </select>
                </div>
                <button
                  onClick={handleSendMapped}
                  disabled={!selectedDevice}
                  className="w-full bg-green-600 hover:bg-green-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold py-3 px-6 rounded-lg transition-colors"
                >
                  Send Mapped Value
                </button>
              </div>
            </div>
          )}

          {/* Free Value Section */}
          <div className="mb-6 border-t border-gray-700 pt-6">
            <h3 className="text-lg font-semibold text-yellow-400 mb-3">
              Free Value (test any MIDI value)
            </h3>
            <div className="grid grid-cols-1 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-400 mb-2">
                  Manual MIDI Value (any number)
                </label>
                <input
                  type="text"
                  value={freeValue}
                  onChange={(e) => {
                    const val = e.target.value;
                    // Allow empty, numbers with optional decimal point
                    if (val === '' || /^\d*\.?\d*$/.test(val)) {
                      setFreeValue(val);
                    }
                  }}
                  className="w-full bg-gray-700 border border-yellow-500 text-gray-100 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-500"
                  placeholder="Enter any value (int or float)"
                />
              </div>
              <div className="grid grid-cols-4 gap-2">
                <button
                  onClick={handleSendFree}
                  disabled={!selectedDevice}
                  className="bg-yellow-600 hover:bg-yellow-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold py-2 px-3 rounded-lg transition-colors text-xs"
                >
                  CC MSB only
                </button>
                <button
                  onClick={() => {
                    if (!currentParam || !selectedDevice) return;
                    const numValue = Math.floor(parseFloat(freeValue) || 0);
                    // Send CC MSB + LSB (CC+32)
                    const ccLsb = currentParam.cc_msb + 32;
                    const msb = (numValue >> 7) & 0x7F;
                    const lsb = numValue & 0x7F;
                    sendMidiCC(midiChannel, currentParam.cc_msb, msb);
                    sendMidiCC(midiChannel, ccLsb, lsb);
                    setLastSent(`Sent CC MSB+LSB: ${selectedParamSet}.${selectedParam} | CC MSB=${currentParam.cc_msb}(val=${msb}) LSB=${ccLsb}(val=${lsb}) | Total=${numValue} | Ch=${midiChannel}`);
                  }}
                  disabled={!selectedDevice}
                  className="bg-orange-600 hover:bg-orange-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold py-2 px-3 rounded-lg transition-colors text-xs"
                >
                  CC MSB+LSB
                </button>
                <button
                  onClick={() => {
                    if (!currentParam || !selectedDevice) return;
                    const numValue = Math.floor(parseFloat(freeValue) || 0);
                    const nrpnMsb = typeof currentParam.nrpn_msb === 'number' ? currentParam.nrpn_msb : 1;
                    const nrpnLsb = typeof currentParam.nrpn_lsb === 'number' ? currentParam.nrpn_lsb : (typeof currentParam.nrpn_lsb === 'string' ? parseInt(currentParam.nrpn_lsb) : 76);
                    sendNRPN(midiChannel, nrpnMsb, nrpnLsb, numValue);
                    setLastSent(`Sent NRPN: ${selectedParamSet}.${selectedParam} | NRPN MSB=${nrpnMsb} LSB=${nrpnLsb} | Value=${numValue} | Channel=${midiChannel}`);
                  }}
                  disabled={!selectedDevice}
                  className="bg-purple-600 hover:bg-purple-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold py-2 px-3 rounded-lg transition-colors text-xs"
                >
                  NRPN
                </button>
                <button
                  onClick={() => {
                    if (!currentParam || !selectedDevice) return;
                    const numValue = Math.floor(parseFloat(freeValue) || 0);
                    const ccLsb = currentParam.cc_msb + 32; // LSB is typically MSB + 32
                    sendHighResCC(midiChannel, currentParam.cc_msb, ccLsb, numValue);
                    setLastSent(`Sent HighRes CC: ${selectedParamSet}.${selectedParam} | CC MSB=${currentParam.cc_msb} LSB=${ccLsb} | Value=${numValue} | Channel=${midiChannel}`);
                  }}
                  disabled={!selectedDevice}
                  className="bg-indigo-600 hover:bg-indigo-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold py-2 px-3 rounded-lg transition-colors text-xs"
                >
                  Hi-Res CC
                </button>
              </div>
            </div>
          </div>

          {/* MIDI Channel */}
          <div>
            <label className="block text-sm font-medium text-gray-400 mb-2">
              MIDI Channel (1-16)
            </label>
            <select
              value={midiChannel}
              onChange={(e) => setMidiChannel(Number(e.target.value))}
              className="w-full bg-gray-700 border border-gray-600 text-gray-100 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              {Array.from({ length: 16 }, (_, i) => i + 1).map((ch) => (
                <option key={ch} value={ch}>
                  Channel {ch}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Last Sent Info */}
        {lastSent && (
          <div className="mt-6 bg-green-900 border border-green-700 text-green-100 p-4 rounded-lg">
            <h3 className="font-semibold mb-1">Last Message Sent</h3>
            <p className="text-sm font-mono">{lastSent}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default MidiTestPage;
