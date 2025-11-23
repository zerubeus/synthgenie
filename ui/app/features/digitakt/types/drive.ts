/**
 * Drive data model types for Digitakt +Drive
 */

/**
 * Path represented as array of directory names
 * e.g., ['samples', 'kicks'] represents '/samples/kicks'
 */
export type Path = string[];

/**
 * Item type - either Directory, File, or Unknown
 */
export type Item =
  | { kind: 'directory'; entries: Entry[] }
  | { kind: 'file'; size: number; hash: number }
  | { kind: 'unknown'; data: unknown };

/**
 * Entry in the file system
 * Contains both metadata and item-specific data
 */
export interface Entry {
  name: string;
  path: Path;
  locked: boolean;
  item: Item;
  itemSize: number; // Computed total size (for directories, sum of contents)
}

/**
 * The +Drive root
 */
export interface Drive {
  root: Entry;
}

/**
 * Hash+Size tuple for identifying files
 * Files in project sample pools are referenced by (hash, size) not path
 */
export type HashSize = readonly [hash: number, size: number];

/**
 * Map of (hash, size) -> list of file paths
 * Multiple files can have same hash if uploaded multiple times
 */
export type FileNamesByHash = Map<string, Path[]>;

/**
 * Statistics about drive usage
 */
export interface DriveStats {
  totalSize: number;
  fileCount: number;
  dirCount: number;
  lockedCount: number;
}

/**
 * Create an empty drive
 */
export function emptyDrive(): Drive {
  return {
    root: {
      name: '/',
      path: [],
      locked: false,
      item: { kind: 'directory', entries: [] },
      itemSize: 0,
    },
  };
}

/**
 * Check if drive is empty
 */
export function isEmptyDrive(drive: Drive): boolean {
  return drive.root.item.kind === 'directory' && drive.root.item.entries.length === 0;
}

/**
 * Get entry at path
 */
export function getEntry(path: Path, drive: Drive): Entry | null {
  let current: Entry = drive.root;

  for (const name of path) {
    if (current.item.kind !== 'directory') {
      return null;
    }
    const next = current.item.entries.find((e) => e.name === name);
    if (!next) {
      return null;
    }
    current = next;
  }

  return current;
}

/**
 * Check if entry is a directory
 */
export function isDirectory(entry: Entry): boolean {
  return entry.item.kind === 'directory';
}

/**
 * Get sub-entries of an entry (if it's a directory)
 */
export function getSubEntries(entry: Entry): Entry[] | null {
  return entry.item.kind === 'directory' ? entry.item.entries : null;
}

/**
 * Enumerate all entries depth-first (for deletion)
 * Does not include the entry at the path itself
 */
export function contentEntriesDepthFirst(path: Path, drive: Drive): Entry[] {
  const entry = getEntry(path, drive);
  if (!entry) {
    return [];
  }

  const result: Entry[] = [];

  function traverse(e: Entry): void {
    if (e.item.kind === 'directory') {
      // Recurse into subdirectories first (depth-first)
      for (const subEntry of e.item.entries) {
        traverse(subEntry);
      }
    }
    result.push(e);
  }

  // Traverse children but don't include the entry itself
  if (entry.item.kind === 'directory') {
    for (const subEntry of entry.item.entries) {
      traverse(subEntry);
    }
  }

  return result;
}

/**
 * Create hash+size key for map lookups
 */
export function hashSizeKey(hash: number, size: number): string {
  return `${hash}:${size}`;
}

/**
 * Build a map of (hash, size) -> paths for all files in drive
 * Used for finding duplicates and sample pool resolution
 */
export function fileNamesByHash(drive: Drive): FileNamesByHash {
  const map = new Map<string, Path[]>();

  function traverse(entry: Entry): void {
    if (entry.item.kind === 'file') {
      const key = hashSizeKey(entry.item.hash, entry.item.size);
      const paths = map.get(key) || [];
      paths.push(entry.path);
      map.set(key, paths);
    } else if (entry.item.kind === 'directory') {
      for (const subEntry of entry.item.entries) {
        traverse(subEntry);
      }
    }
  }

  traverse(drive.root);
  return map;
}

/**
 * Find all files with duplicate (hash, size)
 * Returns map of (hash, size) -> paths for files that appear more than once
 */
export function findDuplicates(drive: Drive): FileNamesByHash {
  const allFiles = fileNamesByHash(drive);
  const duplicates = new Map<string, Path[]>();

  for (const [key, paths] of allFiles.entries()) {
    if (paths.length > 1) {
      duplicates.set(key, paths);
    }
  }

  return duplicates;
}

/**
 * Calculate drive statistics
 */
export function calculateStats(drive: Drive): DriveStats {
  let totalSize = 0;
  let fileCount = 0;
  let dirCount = 0;
  let lockedCount = 0;

  function traverse(entry: Entry): void {
    if (entry.item.kind === 'file') {
      totalSize += entry.item.size;
      fileCount++;
      if (entry.locked) lockedCount++;
    } else if (entry.item.kind === 'directory') {
      dirCount++;
      if (entry.locked) lockedCount++;
      for (const subEntry of entry.item.entries) {
        traverse(subEntry);
      }
    }
  }

  traverse(drive.root);

  return { totalSize, fileCount, dirCount, lockedCount };
}
