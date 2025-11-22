/**
 * SysEx message types for Digitakt +Drive communication
 * Ported from elk-herd/src/SysEx/Message.elm
 */

export type Fd = number; // File descriptor

/**
 * Directory entry as returned by DirList API
 */
export interface DirEntry {
  hash: number;      // Content hash (32-bit)
  size: number;      // File size in bytes
  locked: boolean;   // Whether the file/folder is locked
  type: 'f' | 'd';  // 'f' for file, 'd' for directory
  name: string;      // Name (Windows-1252 encoding)
}

/**
 * Elektron SysEx messages
 * Request/Response pairs for the Digitakt file system API
 */
export type ElkMessage =
  // Device information (0x0n)
  | { type: 'DeviceRequest' }
  | { type: 'DeviceResponse'; productId: number; msgs: number[]; deviceName: string }
  | { type: 'VersionRequest' }
  | { type: 'VersionResponse'; build: string; version: string }

  // Directory operations (0x1n)
  | { type: 'DirListRequest'; path: string }
  | { type: 'DirListResponse'; entries: DirEntry[] }
  | { type: 'DirCreateRequest'; path: string }
  | { type: 'DirCreateResponse'; ok: boolean }
  | { type: 'DirDeleteRequest'; path: string }
  | { type: 'DirDeleteResponse'; ok: boolean }

  // File operations (0x2n)
  | { type: 'FileDeleteRequest'; path: string }
  | { type: 'FileDeleteResponse'; ok: boolean }
  | { type: 'ItemRenameRequest'; from: string; to: string }
  | { type: 'ItemRenameResponse'; ok: boolean }
  | { type: 'SampleFileInfoRequest'; hash: number; size: number }
  | { type: 'SampleFileInfoResponse'; ok: boolean; size: number; hash: number; path: string }

  // Read files from device (0x3n)
  | { type: 'FileReadOpenRequest'; path: string }
  | { type: 'FileReadOpenResponse'; ok: boolean; fd: Fd; totalLen: number }
  | { type: 'FileReadCloseRequest'; fd: Fd }
  | { type: 'FileReadCloseResponse'; fd: Fd; totalLen: number }
  | { type: 'FileReadRequest'; fd: Fd; chunkLen: number; chunkStart: number }
  | { type: 'FileReadResponse'; ok: boolean; fd: Fd; chunkLen: number; chunkStart: number; chunkEnd: number; data: Uint8Array }

  // Write files to device (0x4n)
  | { type: 'FileWriteOpenRequest'; totalLen: number; path: string }
  | { type: 'FileWriteOpenResponse'; ok: boolean; fd: Fd }
  | { type: 'FileWriteCloseRequest'; fd: Fd; totalLen: number }
  | { type: 'FileWriteCloseResponse'; ok: boolean; fd: Fd; totalLen: number }
  | { type: 'FileWriteRequest'; fd: Fd; chunkLen: number; chunkStart: number; data: Uint8Array }
  | { type: 'FileWriteResponse'; ok: boolean; writtenLen: number }

  // Error/Unknown
  | { type: 'Unknown'; id: number; data: Uint8Array }
  | { type: 'TimeOut' };

/**
 * Message ID constants (matching elk-herd API IDs)
 */
export const MessageId = {
  // Device info
  DeviceRequest: 0x01,
  DeviceResponse: 0x81,
  VersionRequest: 0x02,
  VersionResponse: 0x82,

  // Directory operations
  DirListRequest: 0x10,
  DirListResponse: 0x90,
  DirCreateRequest: 0x11,
  DirCreateResponse: 0x91,
  DirDeleteRequest: 0x12,
  DirDeleteResponse: 0x92,

  // File operations
  FileDeleteRequest: 0x20,
  FileDeleteResponse: 0xA0,
  ItemRenameRequest: 0x21,
  ItemRenameResponse: 0xA1,
  SampleFileInfoRequest: 0x23,
  SampleFileInfoResponse: 0xA3,

  // Read operations
  FileReadOpenRequest: 0x30,
  FileReadOpenResponse: 0xB0,
  FileReadCloseRequest: 0x31,
  FileReadCloseResponse: 0xB1,
  FileReadRequest: 0x32,
  FileReadResponse: 0xB2,

  // Write operations
  FileWriteOpenRequest: 0x40,
  FileWriteOpenResponse: 0xC0,
  FileWriteCloseRequest: 0x41,
  FileWriteCloseResponse: 0xC1,
  FileWriteRequest: 0x42,
  FileWriteResponse: 0xC2,
} as const;

/**
 * Elektron manufacturer ID
 */
export const ELEKTRON_MANUFACTURER_ID = [0x00, 0x20, 0x3C] as const;

/**
 * Device IDs for Elektron devices
 */
export const DeviceId = {
  Digitakt: 0x0C,    // 12 in decimal
  Digitakt2: 0x2A,   // 42 in decimal
} as const;

/**
 * SysEx header for Elektron devices
 * Format: F0 00 20 3C [device_id] 00 [message id] [data...] F7
 * Note: Device ID will be set dynamically based on detected device
 */
export const SYSEX_START = 0xF0;
export const SYSEX_END = 0xF7;
export const SYSEX_SUB_ID = 0x00;

/**
 * Chunk size for file transfers (bytes)
 * elk-herd uses 512 bytes per chunk
 */
export const FILE_CHUNK_SIZE = 512;
