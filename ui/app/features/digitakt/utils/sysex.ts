/**
 * SysEx message encoding/decoding utilities for Digitakt +Drive
 */

import type { ElkMessage, DirEntry } from '../types/sysex';
import { MessageId, SYSEX_START, SYSEX_END, SYSEX_SUB_ID, ELEKTRON_MANUFACTURER_ID, DeviceId } from '../types/sysex';

/**
 * Windows-1252 character encoding for Elektron devices
 * Elektron uses Windows-1252 encoding for file names
 */

// Windows-1252 code point mapping (for characters 0x80-0x9F)
const WIN1252_MAP: Record<number, number> = {
  0x80: 0x20AC, // €
  0x82: 0x201A, // ‚
  0x83: 0x0192, // ƒ
  0x84: 0x201E, // „
  0x85: 0x2026, // …
  0x86: 0x2020, // †
  0x87: 0x2021, // ‡
  0x88: 0x02C6, // ˆ
  0x89: 0x2030, // ‰
  0x8A: 0x0160, // Š
  0x8B: 0x2039, // ‹
  0x8C: 0x0152, // Œ
  0x8E: 0x017D, // Ž
  0x91: 0x2018, // '
  0x92: 0x2019, // '
  0x93: 0x201C, // "
  0x94: 0x201D, // "
  0x95: 0x2022, // •
  0x96: 0x2013, // –
  0x97: 0x2014, // —
  0x98: 0x02DC, // ˜
  0x99: 0x2122, // ™
  0x9A: 0x0161, // š
  0x9B: 0x203A, // ›
  0x9C: 0x0153, // œ
  0x9E: 0x017E, // ž
  0x9F: 0x0178, // Ÿ
};

const WIN1252_REVERSE_MAP = new Map<number, number>();
for (const [byte, codePoint] of Object.entries(WIN1252_MAP)) {
  WIN1252_REVERSE_MAP.set(codePoint, parseInt(byte));
}

/**
 * Encode a string to Windows-1252 bytes
 */
export function encodeWin1252(str: string): Uint8Array {
  const bytes: number[] = [];
  for (let i = 0; i < str.length; i++) {
    const codePoint = str.charCodeAt(i);
    if (codePoint <= 0x7F || (codePoint >= 0xA0 && codePoint <= 0xFF)) {
      // Direct mapping for ASCII and Latin-1 supplement
      bytes.push(codePoint);
    } else if (WIN1252_REVERSE_MAP.has(codePoint)) {
      // Special Windows-1252 characters
      bytes.push(WIN1252_REVERSE_MAP.get(codePoint)!);
    } else {
      // Replacement character
      bytes.push(0x3F); // '?'
    }
  }
  return new Uint8Array(bytes);
}

/**
 * Decode Windows-1252 bytes to string
 */
export function decodeWin1252(bytes: Uint8Array): string {
  const chars: string[] = [];
  for (let i = 0; i < bytes.length; i++) {
    const byte = bytes[i];
    if (byte <= 0x7F || (byte >= 0xA0 && byte <= 0xFF)) {
      // Direct mapping
      chars.push(String.fromCharCode(byte));
    } else if (WIN1252_MAP[byte]) {
      // Special Windows-1252 characters
      chars.push(String.fromCharCode(WIN1252_MAP[byte]));
    } else {
      // Replacement
      chars.push('?');
    }
  }
  return chars.join('');
}

/**
 * Builder utilities for creating byte arrays
 */

function buildUint32BE(value: number): number[] {
  return [
    (value >>> 24) & 0xFF,
    (value >>> 16) & 0xFF,
    (value >>> 8) & 0xFF,
    value & 0xFF,
  ];
}

function buildString0Win1252(str: string): number[] {
  const encoded = encodeWin1252(str);
  return [...encoded, 0x00]; // Null-terminated
}

function buildBool(value: boolean): number {
  return value ? 0x01 : 0x00;
}

/**
 * Parser utilities for reading byte arrays
 */

class ByteParser {
  private offset = 0;

  constructor(private data: Uint8Array) {}

  byte(): number {
    if (this.offset >= this.data.length) {
      throw new Error('Unexpected end of data');
    }
    return this.data[this.offset++];
  }

  bool(): boolean {
    const b = this.byte();
    if (b === 0x00) return false;
    if (b === 0x01) return true;
    throw new Error(`Invalid boolean byte: ${b}`);
  }

  uint32BE(): number {
    const b0 = this.byte();
    const b1 = this.byte();
    const b2 = this.byte();
    const b3 = this.byte();
    return (b0 << 24) | (b1 << 16) | (b2 << 8) | b3;
  }

  string0Win1252(): string {
    const bytes: number[] = [];
    while (this.offset < this.data.length) {
      const b = this.byte();
      if (b === 0x00) break; // Null terminator
      bytes.push(b);
    }
    return decodeWin1252(new Uint8Array(bytes));
  }

  rest(): Uint8Array {
    const remaining = this.data.slice(this.offset);
    this.offset = this.data.length;
    return remaining;
  }

  hasMore(): boolean {
    return this.offset < this.data.length;
  }
}

/**
 * Encode 8-bit data to 7-bit MIDI format
 */
function encode7bit(data8: Uint8Array): Uint8Array {
  const len8 = data8.length;
  const len7 = len8 + Math.ceil(len8 / 7);
  const buf = new Uint8Array(len7);

  let w = 0;
  for (let r = 0; r < len8; r += 7) {
    const s = data8.slice(r, r + 7);
    const hi = s.reduce((a, b, i) => a | ((b & 0x80) >> (i + 1)), 0);

    buf[w++] = hi;
    for (const x of s) {
      buf[w++] = x & 0x7f;
    }
  }

  return buf;
}

/**
 * Decode 7-bit MIDI format to 8-bit data
 */
function decode7bit(data: Uint8Array): Uint8Array {
  const result: number[] = [];
  let r = 0;

  while (r < data.length) {
    const hi = data[r++];
    let chunkSize = Math.min(7, data.length - r);

    for (let i = 0; i < chunkSize; i++) {
      const lowBits = data[r++];
      const highBit = ((hi << (i + 1)) & 0x80);
      result.push(highBit | lowBits);
    }
  }

  return new Uint8Array(result);
}

/**
 * Wrap message payload in SysEx envelope with 7-bit encoding
 * Format: F0 00 20 3C 10 00 [7-bit encoded payload] F7
 */
export function wrapSysEx(payload: number[]): Uint8Array {
  const data8 = new Uint8Array(payload);
  const len8 = data8.length;
  const len7 = len8 + Math.ceil(len8 / 7);
  const buf = new Uint8Array(6 + len7 + 1);

  // Elektron SysEx header (same for all Elektron devices)
  buf.set([0xF0, 0x00, 0x20, 0x3C, 0x10, 0x00], 0);

  // 7-bit encode the payload
  let w = 6;
  for (let r = 0; r < len8; r += 7) {
    const s = data8.slice(r, r + 7);
    const hi = s.reduce((a, b, i) => a | ((b & 0x80) >> (i + 1)), 0);

    buf[w++] = hi;
    for (const x of s) {
      buf[w++] = x & 0x7f;
    }
  }

  // SysEx end
  buf[6 + len7] = 0xF7;

  return buf;
}

/**
 * Unwrap SysEx envelope and decode 7-bit payload
 */
export function unwrapSysEx(data: Uint8Array): Uint8Array | null {
  // Check start byte
  if (data[0] !== SYSEX_START) {
    return null;
  }

  // Check manufacturer ID
  if (data[1] !== ELEKTRON_MANUFACTURER_ID[0] ||
      data[2] !== ELEKTRON_MANUFACTURER_ID[1] ||
      data[3] !== ELEKTRON_MANUFACTURER_ID[2]) {
    return null;
  }

  // Check end byte
  if (data[data.length - 1] !== SYSEX_END) {
    return null;
  }

  // Extract and decode 7-bit payload (skip header: 6 bytes, and end: 1 byte)
  const encoded = data.slice(6, -1);
  return decode7bit(encoded);
}

// Global message counter for request/response matching
let messageIdCounter = 1;

/**
 * Build SysEx message from ElkMessage
 * Wraps the message with msgId and respId (0) before encoding
 */
export function buildMessage(msg: ElkMessage): Uint8Array {
  // Increment message ID
  const msgId = messageIdCounter++;

  // Build the inner message payload
  const innerPayload: number[] = [];

  switch (msg.type) {
    case 'DirListRequest':
      innerPayload.push(MessageId.DirListRequest, ...buildString0Win1252(msg.path));
      break;

    case 'DirCreateRequest':
      innerPayload.push(MessageId.DirCreateRequest, ...buildString0Win1252(msg.path));
      break;

    case 'DirDeleteRequest':
      innerPayload.push(MessageId.DirDeleteRequest, ...buildString0Win1252(msg.path));
      break;

    case 'FileDeleteRequest':
      innerPayload.push(MessageId.FileDeleteRequest, ...buildString0Win1252(msg.path));
      break;

    case 'ItemRenameRequest':
      innerPayload.push(
        MessageId.ItemRenameRequest,
        ...buildString0Win1252(msg.from),
        ...buildString0Win1252(msg.to)
      );
      break;

    case 'SampleFileInfoRequest':
      innerPayload.push(
        MessageId.SampleFileInfoRequest,
        ...buildUint32BE(msg.hash),
        ...buildUint32BE(msg.size)
      );
      break;

    case 'FileReadOpenRequest':
      innerPayload.push(MessageId.FileReadOpenRequest, ...buildString0Win1252(msg.path));
      break;

    case 'FileReadCloseRequest':
      innerPayload.push(MessageId.FileReadCloseRequest, ...buildUint32BE(msg.fd));
      break;

    case 'FileReadRequest':
      innerPayload.push(
        MessageId.FileReadRequest,
        ...buildUint32BE(msg.fd),
        ...buildUint32BE(msg.chunkLen),
        ...buildUint32BE(msg.chunkStart)
      );
      break;

    case 'FileWriteOpenRequest':
      innerPayload.push(
        MessageId.FileWriteOpenRequest,
        ...buildUint32BE(msg.totalLen),
        ...buildString0Win1252(msg.path)
      );
      break;

    case 'FileWriteCloseRequest':
      innerPayload.push(
        MessageId.FileWriteCloseRequest,
        ...buildUint32BE(msg.fd),
        ...buildUint32BE(msg.totalLen)
      );
      break;

    case 'FileWriteRequest':
      innerPayload.push(
        MessageId.FileWriteRequest,
        ...buildUint32BE(msg.fd),
        ...buildUint32BE(msg.chunkLen),
        ...buildUint32BE(msg.chunkStart),
        ...msg.data
      );
      break;

    case 'DeviceRequest':
      innerPayload.push(MessageId.DeviceRequest);
      break;

    case 'VersionRequest':
      innerPayload.push(MessageId.VersionRequest);
      break;

    default:
      throw new Error(`Cannot build message of type: ${(msg as ElkMessage).type}`);
  }

  // Build full payload: msgId (uint16be) + respId (uint16be, always 0 for requests) + message
  const fullPayload = [
    ...buildUint16BE(msgId),
    ...buildUint16BE(0), // respId = 0 for requests
    ...innerPayload
  ];

  return wrapSysEx(fullPayload);
}

function buildUint16BE(value: number): number[] {
  return [
    (value >>> 8) & 0xFF,
    value & 0xFF,
  ];
}

/**
 * Parse SysEx message to ElkMessage
 * First extracts msgId and respId, then parses the actual message
 */
export function parseMessage(data: Uint8Array): ElkMessage {
  const payload = unwrapSysEx(data);
  if (!payload || payload.length === 0) {
    return { type: 'Unknown', id: 0, data: new Uint8Array() };
  }

  const parser = new ByteParser(payload);

  // Extract msgId and respId (uint16be each)
  const msgIdHi = parser.byte();
  const msgIdLo = parser.byte();
  const msgId = (msgIdHi << 8) | msgIdLo;

  const respIdHi = parser.byte();
  const respIdLo = parser.byte();
  const respId = (respIdHi << 8) | respIdLo;

  // Now parse the actual message
  const messageType = parser.byte();

  try {
    switch (messageType) {
      case MessageId.DirListResponse: {
        const entries: DirEntry[] = [];
        while (parser.hasMore()) {
          const hash = parser.uint32BE();
          const size = parser.uint32BE();
          const locked = parser.bool();
          const typeByte = parser.byte();
          // Digitakt uses uppercase: 'D' = 0x44 (68) for directory, 'F' = 0x46 (70) for file
          const type = typeByte === 0x44 ? 'd' : 'f';
          const name = parser.string0Win1252();
          entries.push({ hash, size, locked, type, name });
        }
        return { type: 'DirListResponse', entries };
      }

      case MessageId.DirCreateResponse:
        return { type: 'DirCreateResponse', ok: parser.bool() };

      case MessageId.DirDeleteResponse:
        return { type: 'DirDeleteResponse', ok: parser.bool() };

      case MessageId.FileDeleteResponse:
        return { type: 'FileDeleteResponse', ok: parser.bool() };

      case MessageId.ItemRenameResponse:
        return { type: 'ItemRenameResponse', ok: parser.bool() };

      case MessageId.SampleFileInfoResponse: {
        const ok = parser.bool();
        const size = parser.uint32BE(); // Note: size/hash order is reversed in response
        const hash = parser.uint32BE();
        const path = parser.string0Win1252();
        return { type: 'SampleFileInfoResponse', ok, size, hash, path };
      }

      case MessageId.FileReadOpenResponse: {
        const ok = parser.bool();
        const fd = parser.uint32BE();
        const totalLen = parser.uint32BE();
        return { type: 'FileReadOpenResponse', ok, fd, totalLen };
      }

      case MessageId.FileReadCloseResponse: {
        const fd = parser.uint32BE();
        const totalLen = parser.uint32BE();
        return { type: 'FileReadCloseResponse', fd, totalLen };
      }

      case MessageId.FileReadResponse: {
        const ok = parser.bool();
        const fd = parser.uint32BE();
        const chunkLen = parser.uint32BE();
        const chunkStart = parser.uint32BE();
        const chunkEnd = parser.uint32BE();
        const data = parser.rest();
        return { type: 'FileReadResponse', ok, fd, chunkLen, chunkStart, chunkEnd, data };
      }

      case MessageId.FileWriteOpenResponse: {
        const ok = parser.bool();
        const fd = parser.uint32BE();
        return { type: 'FileWriteOpenResponse', ok, fd };
      }

      case MessageId.FileWriteCloseResponse: {
        const ok = parser.bool();
        const fd = parser.uint32BE();
        const totalLen = parser.uint32BE();
        return { type: 'FileWriteCloseResponse', ok, fd, totalLen };
      }

      case MessageId.FileWriteResponse: {
        const ok = parser.bool();
        const writtenLen = parser.uint32BE();
        return { type: 'FileWriteResponse', ok, writtenLen };
      }

      case MessageId.DeviceResponse: {
        const productId = parser.byte();
        const msgCount = parser.byte();
        const msgs: number[] = [];
        for (let i = 0; i < msgCount; i++) {
          msgs.push(parser.byte());
        }
        const deviceName = parser.string0Win1252();
        return { type: 'DeviceResponse', productId, msgs, deviceName };
      }

      case MessageId.VersionResponse: {
        const build = parser.string0Win1252();
        const version = parser.string0Win1252();
        return { type: 'VersionResponse', build, version };
      }

      default:
        return { type: 'Unknown', id: messageType, data: parser.rest() };
    }
  } catch (error) {
    console.error('Error parsing message:', error);
    return { type: 'Unknown', id: messageType, data: parser.rest() };
  }
}

/**
 * Validate a file/folder name for Windows-1252 compatibility
 */
export function isValidName(name: string): boolean {
  if (name.length === 0 || name.length > 255) {
    return false;
  }
  // Check for invalid characters
  const invalidChars = /[<>:"/\\|?*\x00-\x1F]/;
  if (invalidChars.test(name)) {
    return false;
  }
  // Check if name is . or ..
  if (name === '.' || name === '..') {
    return false;
  }
  return true;
}
