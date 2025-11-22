/**
 * Hook for file operations on Digitakt +Drive
 * Handles rename, move, create directory, trash operations
 */

import { useCallback } from 'react';
import { useDigitaktSysEx } from './useDigitaktSysEx';
import type { Path, Drive } from '../types/drive';
import { contentEntriesDepthFirst } from '../types/drive';
import { pathToString, TRASH_PATH, subPath, baseName, dirPath } from '../utils/pathUtils';
import { isValidName } from '../utils/sysex';

interface UseFileOperationsReturn {
  /** Create a new directory */
  createDirectory: (path: Path) => Promise<boolean>;
  /** Rename a file or directory */
  renameItem: (fromPath: Path, newName: string) => Promise<boolean>;
  /** Move item to trash */
  moveToTrash: (path: Path) => Promise<boolean>;
  /** Empty trash (delete all items in /TRASH) */
  emptyTrash: (drive: Drive) => Promise<boolean>;
  /** Delete a file */
  deleteFile: (path: Path) => Promise<boolean>;
  /** Delete a directory */
  deleteDirectory: (path: Path) => Promise<boolean>;
}

/**
 * Custom hook for file operations
 */
export function useFileOperations(): UseFileOperationsReturn {
  const sysex = useDigitaktSysEx();

  /**
   * Create a new directory
   */
  const createDirectory = useCallback(
    async (path: Path): Promise<boolean> => {
      if (!sysex.isConnected) {
        throw new Error('Not connected to Digitakt');
      }

      const pathStr = pathToString(path);
      console.log(`Creating directory: ${pathStr}`);

      try {
        const response = await sysex.sendMessage({
          type: 'DirCreateRequest',
          path: pathStr,
        });

        if (response.type !== 'DirCreateResponse') {
          throw new Error(`Unexpected response: ${response.type}`);
        }

        if (!response.ok) {
          throw new Error('Failed to create directory');
        }

        console.log(`Directory created: ${pathStr}`);
        return true;
      } catch (err) {
        console.error(`Error creating directory ${pathStr}:`, err);
        throw err;
      }
    },
    [sysex]
  );

  /**
   * Rename a file or directory
   */
  const renameItem = useCallback(
    async (fromPath: Path, newName: string): Promise<boolean> => {
      if (!sysex.isConnected) {
        throw new Error('Not connected to Digitakt');
      }

      // Validate new name
      if (!isValidName(newName)) {
        throw new Error('Invalid name. Cannot contain: < > : " / \\ | ? *');
      }

      const parent = dirPath(fromPath);
      const toPath = subPath(parent, newName);

      const fromStr = pathToString(fromPath);
      const toStr = pathToString(toPath);

      console.log(`Renaming: ${fromStr} -> ${toStr}`);

      try {
        const response = await sysex.sendMessage({
          type: 'ItemRenameRequest',
          from: fromStr,
          to: toStr,
        });

        if (response.type !== 'ItemRenameResponse') {
          throw new Error(`Unexpected response: ${response.type}`);
        }

        if (!response.ok) {
          throw new Error('Failed to rename item');
        }

        console.log(`Item renamed: ${fromStr} -> ${toStr}`);
        return true;
      } catch (err) {
        console.error(`Error renaming ${fromStr}:`, err);
        throw err;
      }
    },
    [sysex]
  );

  /**
   * Move item to trash
   */
  const moveToTrash = useCallback(
    async (path: Path): Promise<boolean> => {
      if (!sysex.isConnected) {
        throw new Error('Not connected to Digitakt');
      }

      const name = baseName(path);
      const trashPath = subPath(TRASH_PATH, name);

      const fromStr = pathToString(path);
      const toStr = pathToString(trashPath);

      console.log(`Moving to trash: ${fromStr} -> ${toStr}`);

      try {
        // First ensure /TRASH directory exists
        try {
          await createDirectory(TRASH_PATH);
        } catch {
          // Trash might already exist, continue
        }

        // Rename to move to trash
        const response = await sysex.sendMessage({
          type: 'ItemRenameRequest',
          from: fromStr,
          to: toStr,
        });

        if (response.type !== 'ItemRenameResponse') {
          throw new Error(`Unexpected response: ${response.type}`);
        }

        if (!response.ok) {
          throw new Error('Failed to move to trash');
        }

        console.log(`Moved to trash: ${fromStr}`);
        return true;
      } catch (err) {
        console.error(`Error moving to trash ${fromStr}:`, err);
        throw err;
      }
    },
    [sysex, createDirectory]
  );

  /**
   * Delete a file
   */
  const deleteFile = useCallback(
    async (path: Path): Promise<boolean> => {
      if (!sysex.isConnected) {
        throw new Error('Not connected to Digitakt');
      }

      const pathStr = pathToString(path);
      console.log(`Deleting file: ${pathStr}`);

      try {
        const response = await sysex.sendMessage({
          type: 'FileDeleteRequest',
          path: pathStr,
        });

        if (response.type !== 'FileDeleteResponse') {
          throw new Error(`Unexpected response: ${response.type}`);
        }

        if (!response.ok) {
          throw new Error('Failed to delete file');
        }

        console.log(`File deleted: ${pathStr}`);
        return true;
      } catch (err) {
        console.error(`Error deleting file ${pathStr}:`, err);
        throw err;
      }
    },
    [sysex]
  );

  /**
   * Delete a directory
   */
  const deleteDirectory = useCallback(
    async (path: Path): Promise<boolean> => {
      if (!sysex.isConnected) {
        throw new Error('Not connected to Digitakt');
      }

      const pathStr = pathToString(path);
      console.log(`Deleting directory: ${pathStr}`);

      try {
        const response = await sysex.sendMessage({
          type: 'DirDeleteRequest',
          path: pathStr,
        });

        if (response.type !== 'DirDeleteResponse') {
          throw new Error(`Unexpected response: ${response.type}`);
        }

        if (!response.ok) {
          throw new Error('Failed to delete directory');
        }

        console.log(`Directory deleted: ${pathStr}`);
        return true;
      } catch (err) {
        console.error(`Error deleting directory ${pathStr}:`, err);
        throw err;
      }
    },
    [sysex]
  );

  /**
   * Empty trash - delete all items in /TRASH
   * Must delete depth-first (files before directories)
   */
  const emptyTrash = useCallback(
    async (drive: Drive): Promise<boolean> => {
      if (!sysex.isConnected) {
        throw new Error('Not connected to Digitakt');
      }

      console.log('Emptying trash...');

      try {
        // Get all entries in trash depth-first
        const entries = contentEntriesDepthFirst(TRASH_PATH, drive);

        // Delete each entry (files first, then directories due to depth-first order)
        for (const entry of entries) {
          if (entry.item.kind === 'file') {
            await deleteFile(entry.path);
          } else if (entry.item.kind === 'directory') {
            await deleteDirectory(entry.path);
          }
        }

        console.log('Trash emptied');
        return true;
      } catch (err) {
        console.error('Error emptying trash:', err);
        throw err;
      }
    },
    [sysex, deleteFile, deleteDirectory]
  );

  return {
    createDirectory,
    renameItem,
    moveToTrash,
    emptyTrash,
    deleteFile,
    deleteDirectory,
  };
}
