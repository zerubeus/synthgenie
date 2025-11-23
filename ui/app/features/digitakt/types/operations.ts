/**
 * Operation queue types for managing sequential MIDI operations
 */

import type { Path } from './drive';

/**
 * Queue action types
 * Operations that can be queued for sequential execution
 */
export type QueueAction =
  | { type: 'ListDir'; path: Path; recursive: boolean }
  | { type: 'CreateDir'; path: Path }
  | { type: 'DeleteDir'; path: Path }
  | { type: 'DeleteFile'; path: Path }
  | { type: 'RenameItem'; from: Path; to: Path }
  | { type: 'ReadFile'; path: Path; destination: string }
  | { type: 'WriteFile'; path: Path; data: File | Blob };

/**
 * Operation status
 */
export type OperationStatus = 'pending' | 'in_progress' | 'completed' | 'failed';

/**
 * Queued operation with status tracking
 */
export interface QueuedOperation {
  id: string;
  action: QueueAction;
  status: OperationStatus;
  progress?: number; // 0-100 for file transfers
  error?: string;
  createdAt: number;
  completedAt?: number;
}

/**
 * Operation queue state
 */
export interface OperationQueue {
  operations: QueuedOperation[];
  current: QueuedOperation | null;
  paused: boolean;
}

/**
 * Progress information for long-running operations
 */
export interface OperationProgress {
  total: number;
  current: number;
  message: string;
}

/**
 * File transfer state
 */
export interface FileTransfer {
  path: Path;
  totalSize: number;
  transferred: number;
  fd: number; // File descriptor
  direction: 'upload' | 'download';
  status: 'opening' | 'transferring' | 'closing' | 'completed' | 'failed';
  error?: string;
}
