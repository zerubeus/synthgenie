/**
 * Hook for managing Digitakt +Drive state and operations
 * Handles drive scanning, tree building, and state management
 */

import { useState, useCallback } from 'react';
import { useDigitaktSysEx } from './useDigitaktSysEx';
import type { Drive, Entry, Item, Path } from '../types/drive';
import type { DirEntry } from '../types/sysex';
import { emptyDrive, getEntry } from '../types/drive';
import { pathToString, subPath, ROOT_PATH } from '../utils/pathUtils';

interface UseDigitaktDriveReturn {
  /** Current drive state */
  drive: Drive;
  /** Whether drive is currently being scanned */
  isScanning: boolean;
  /** Scan progress (0-100) */
  scanProgress: number;
  /** Error message if any */
  error: string | null;
  /** Start scanning the +Drive */
  scanDrive: () => Promise<void>;
  /** Refresh a specific path */
  refreshPath: (path: Path) => Promise<void>;
  /** Get entry at path */
  getEntryAt: (path: Path) => Entry | null;
}

/**
 * Custom hook for Digitakt +Drive management
 */
export function useDigitaktDrive(): UseDigitaktDriveReturn {
  const sysex = useDigitaktSysEx();
  const [drive, setDrive] = useState<Drive>(emptyDrive());
  const [isScanning, setIsScanning] = useState(false);
  const [scanProgress, setScanProgress] = useState(0);
  const [error, setError] = useState<string | null>(null);

  /**
   * Build Entry from DirEntry and path
   * Directories are initially created with empty entries[] - they get filled by subsequent scans
   */
  const buildEntry = useCallback((dirEntry: DirEntry, parentPath: Path): Entry => {
    const entryPath = subPath(parentPath, dirEntry.name);
    const item: Item =
      dirEntry.type === 'd'
        ? { kind: 'directory', entries: [] }  // Empty initially - will be filled by scanning this directory
        : { kind: 'file', size: dirEntry.size, hash: dirEntry.hash };

    return {
      name: dirEntry.name,
      path: entryPath,
      locked: dirEntry.locked,
      item,
      itemSize: dirEntry.type === 'd' ? 0 : dirEntry.size,  // Directories start at 0, will be computed after scanning
    };
  }, []);

  /**
   * Merge new entries into existing drive tree (like elk-herd's setRawEntries)
   * Returns updated drive and list of subdirectories that need to be scanned
   */
  const mergeEntries = useCallback(
    (path: Path, newDirEntries: DirEntry[], currentDrive: Drive): { drive: Drive; dirsToScan: Path[] } => {
      const pathStr = pathToString(path);

      // Deduplicate entries by name (in case Digitakt sends duplicates)
      const uniqueEntries = new Map<string, DirEntry>();
      for (const dirEntry of newDirEntries) {
        if (!uniqueEntries.has(dirEntry.name)) {
          uniqueEntries.set(dirEntry.name, dirEntry);
        }
      }

      // Build entries from raw dir entries
      const newEntries: Entry[] = Array.from(uniqueEntries.values()).map((de) =>
        buildEntry(de, path)
      );

      // Find which subdirectories need to be scanned
      const dirsToScan: Path[] = newEntries
        .filter((e) => e.item.kind === 'directory')
        .map((e) => e.path);

      // Update the drive tree at this path - pass newEntries as parameter to avoid closure issues
      const updateAtPath = (
        entry: Entry,
        targetPath: Path,
        entriesToInsert: Entry[],
        depth: number = 0
      ): Entry => {
        // If we're at the target path, update this directory's entries
        if (depth === targetPath.length) {
          if (entry.item.kind === 'directory') {
            const totalSize = entriesToInsert.reduce((sum, e) => sum + e.itemSize, 0);
            return {
              ...entry,
              item: { kind: 'directory', entries: entriesToInsert },
              itemSize: totalSize,
            };
          }
          return entry;
        }

        // Otherwise, recurse into the appropriate child
        if (entry.item.kind === 'directory') {
          const targetName = targetPath[depth];
          const updatedEntries = entry.item.entries.map((child) =>
            child.name === targetName
              ? updateAtPath(child, targetPath, entriesToInsert, depth + 1)
              : child
          );
          const totalSize = updatedEntries.reduce((sum, e) => sum + e.itemSize, 0);
          return {
            ...entry,
            item: { kind: 'directory', entries: updatedEntries },
            itemSize: totalSize,
          };
        }

        return entry;
      };

      const updatedRoot = updateAtPath(currentDrive.root, path, newEntries);

      return {
        drive: { root: updatedRoot },
        dirsToScan,
      };
    },
    [buildEntry]
  );

  /**
   * Scan the entire +Drive iteratively (like elk-herd does)
   * Uses a queue to process directories one at a time
   */
  const scanDrive = useCallback(async () => {
    if (isScanning) {
      console.warn('Scan already in progress');
      return;
    }

    if (!sysex.isConnected) {
      setError('Not connected to Digitakt');
      return;
    }

    setIsScanning(true);
    setScanProgress(0);
    setError(null);

    try {
      // Start with empty drive
      let currentDrive: Drive = emptyDrive();

      // Queue of paths to scan
      const queue: Path[] = [ROOT_PATH];
      const scanned = new Set<string>();

      while (queue.length > 0) {
        const path = queue.shift()!;
        const pathStr = pathToString(path);

        // Skip if already scanned
        if (scanned.has(pathStr)) {
          continue;
        }
        scanned.add(pathStr);

        // Request directory listing
        const response = await sysex.sendMessage({
          type: 'DirListRequest',
          path: pathStr,
        });

        if (response.type !== 'DirListResponse') {
          throw new Error(`Unexpected response: ${response.type}`);
        }

        // Merge entries and get subdirectories to scan
        const { drive: updatedDrive, dirsToScan } = mergeEntries(
          path,
          response.entries,
          currentDrive
        );

        currentDrive = updatedDrive;

        // Add subdirectories to queue
        queue.push(...dirsToScan);

        // Update progress only (not drive state - we'll do that at the end)
        const progress = Math.floor((scanned.size / (scanned.size + queue.length)) * 100);
        setScanProgress(progress);
      }

      // Set the final drive state once at the end
      setDrive(currentDrive);

      setScanProgress(100);
    } catch (err) {
      const errorMsg = err instanceof Error ? err.message : 'Scan failed';
      setError(errorMsg);
      console.error('Drive scan error:', err);
    } finally {
      setIsScanning(false);
    }
  }, [isScanning, sysex.isConnected, mergeEntries, sysex]);

  /**
   * Refresh a specific path (non-recursive)
   */
  const refreshPath = useCallback(
    async (path: Path) => {
      if (!sysex.isConnected) {
        setError('Not connected to Digitakt');
        return;
      }

      try {
        const pathStr = pathToString(path);
        console.log(`Refreshing path: ${pathStr}`);

        const response = await sysex.sendMessage({
          type: 'DirListRequest',
          path: pathStr,
        });

        if (response.type !== 'DirListResponse') {
          throw new Error(`Unexpected response: ${response.type}`);
        }

        // TODO: Implement proper immutable update of drive tree
        // For now, refreshPath doesn't update the state - user needs to rescan
        // Implementing this correctly requires rebuilding the entire path from root
        // to maintain React immutability

        console.log(`Path refreshed: ${pathStr}`);
      } catch (err) {
        const errorMsg = err instanceof Error ? err.message : 'Refresh failed';
        setError(errorMsg);
        console.error('Path refresh error:', err);
      }
    },
    [sysex, buildEntry]
  );

  /**
   * Get entry at path
   */
  const getEntryAt = useCallback(
    (path: Path): Entry | null => {
      return getEntry(path, drive);
    },
    [drive]
  );

  return {
    drive,
    isScanning,
    scanProgress,
    error,
    scanDrive,
    refreshPath,
    getEntryAt,
  };
}
