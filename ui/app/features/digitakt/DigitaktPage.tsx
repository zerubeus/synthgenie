/**
 * Digitakt +Drive Management Page
 * Main page for managing Digitakt samples and file system
 */

import { useState } from 'react';
import { useDigitaktDrive } from './hooks/useDigitaktDrive';
import { useDigitaktSysEx } from './hooks/useDigitaktSysEx';
import { useFileOperations } from './hooks/useFileOperations';
import { DriveExplorer } from './components/DriveExplorer';
import type { Path } from './types/drive';

export default function DigitaktPage() {
  const sysex = useDigitaktSysEx();
  const drive = useDigitaktDrive();
  const fileOps = useFileOperations();
  const [selectedPath, setSelectedPath] = useState<Path | null>(null);

  const handleScanDrive = async () => {
    try {
      await drive.scanDrive();
    } catch (err) {
      console.error('Scan failed:', err);
    }
  };

  const handleCreateFolder = async () => {
    const folderName = prompt('Enter folder name:');
    if (!folderName) return;

    try {
      const path = selectedPath || [];
      await fileOps.createDirectory([...path, folderName]);
      await drive.refreshPath(path);
    } catch (err) {
      console.error('Create folder failed:', err);
      alert(`Failed to create folder: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  };

  const handleRename = async () => {
    if (!selectedPath || selectedPath.length === 0) {
      alert('Please select an item to rename');
      return;
    }

    const currentName = selectedPath[selectedPath.length - 1];
    const newName = prompt('Enter new name:', currentName);
    if (!newName || newName === currentName) return;

    try {
      await fileOps.renameItem(selectedPath, newName);
      const parentPath = selectedPath.slice(0, -1);
      await drive.refreshPath(parentPath);
      setSelectedPath([...parentPath, newName]);
    } catch (err) {
      console.error('Rename failed:', err);
      alert(`Failed to rename: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  };

  const handleMoveToTrash = async () => {
    if (!selectedPath || selectedPath.length === 0) {
      alert('Please select an item to move to trash');
      return;
    }

    if (!confirm(`Move "${selectedPath[selectedPath.length - 1]}" to trash?`)) {
      return;
    }

    try {
      await fileOps.moveToTrash(selectedPath);
      const parentPath = selectedPath.slice(0, -1);
      await drive.refreshPath(parentPath);
      setSelectedPath(null);
    } catch (err) {
      console.error('Move to trash failed:', err);
      alert(`Failed to move to trash: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  };

  const handleEmptyTrash = async () => {
    if (!confirm('Are you sure you want to permanently delete all items in trash?')) {
      return;
    }

    try {
      await fileOps.emptyTrash(drive.drive);
      await drive.refreshPath(['TRASH']);
    } catch (err) {
      console.error('Empty trash failed:', err);
      alert(`Failed to empty trash: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-sm p-6 mb-6">
          <h1 className="text-3xl font-bold text-gray-900 mb-4">Digitakt +Drive Manager</h1>

          {/* Connection Status */}
          <div className="flex items-center gap-4 mb-4">
            <div className="flex items-center gap-2">
              <div className={`w-3 h-3 rounded-full ${sysex.isConnected ? 'bg-green-500' : 'bg-red-500'}`} />
              <span className="text-sm text-gray-700">
                {sysex.isConnected ? `Connected: ${sysex.selectedDevice}` : 'Not connected'}
              </span>
            </div>

            {sysex.devices.length > 1 && (
              <select
                value={sysex.selectedDevice || ''}
                onChange={(e) => sysex.selectDevice(e.target.value)}
                className="text-sm border border-gray-300 rounded px-2 py-1"
              >
                {sysex.devices.map((device) => (
                  <option key={device} value={device}>
                    {device}
                  </option>
                ))}
              </select>
            )}
          </div>

          {/* Error Display */}
          {(sysex.error || drive.error) && (
            <div className="bg-red-50 border border-red-200 rounded p-3 mb-4">
              <p className="text-sm text-red-700">{sysex.error || drive.error}</p>
            </div>
          )}

          {/* Actions */}
          <div className="flex flex-wrap gap-2">
            <button
              onClick={handleScanDrive}
              disabled={!sysex.isConnected || drive.isScanning}
              className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {drive.isScanning ? 'Scanning...' : 'Scan +Drive'}
            </button>

            <button
              onClick={handleCreateFolder}
              disabled={!sysex.isConnected}
              className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              New Folder
            </button>

            <button
              onClick={handleRename}
              disabled={!selectedPath}
              className="px-4 py-2 bg-yellow-600 text-white rounded hover:bg-yellow-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Rename
            </button>

            <button
              onClick={handleMoveToTrash}
              disabled={!selectedPath}
              className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Move to Trash
            </button>

            <button
              onClick={handleEmptyTrash}
              disabled={!sysex.isConnected}
              className="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Empty Trash
            </button>
          </div>
        </div>

        {/* Drive Explorer */}
        <div className="bg-white rounded-lg shadow-sm p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">File Browser</h2>

          {drive.isScanning && (
            <div className="text-center py-12">
              <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600" />
              <p className="mt-4 text-gray-600">Scanning +Drive... {drive.scanProgress}%</p>
            </div>
          )}

          {!drive.isScanning && (
            <DriveExplorer
              drive={drive.drive}
              selectedPath={selectedPath}
              onSelectPath={setSelectedPath}
            />
          )}
        </div>
      </div>
    </div>
  );
}
