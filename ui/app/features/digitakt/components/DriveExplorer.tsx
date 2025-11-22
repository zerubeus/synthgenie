/**
 * DriveExplorer component - displays file tree for Digitakt +Drive
 */

import { useState } from 'react';
import type { Drive, Entry, Path } from '../types/drive';
import { pathsEqual } from '../utils/pathUtils';

interface DriveExplorerProps {
  drive: Drive;
  selectedPath: Path | null;
  onSelectPath: (path: Path) => void;
}

export function DriveExplorer({ drive, selectedPath, onSelectPath }: DriveExplorerProps) {
  const [expandedPaths, setExpandedPaths] = useState<Set<string>>(new Set([JSON.stringify([])]));

  const toggleExpanded = (path: Path) => {
    const pathKey = JSON.stringify(path);
    setExpandedPaths((prev) => {
      const next = new Set(prev);
      if (next.has(pathKey)) {
        next.delete(pathKey);
      } else {
        next.add(pathKey);
      }
      return next;
    });
  };

  const isExpanded = (path: Path) => {
    return expandedPaths.has(JSON.stringify(path));
  };

  const renderEntry = (entry: Entry, depth: number = 0) => {
    const isDir = entry.item.kind === 'directory';
    const isSelected = selectedPath && pathsEqual(entry.path, selectedPath);
    const expanded = isExpanded(entry.path);

    return (
      <div key={JSON.stringify(entry.path)}>
        {/* Entry Row */}
        <div
          className={`flex items-center gap-2 py-1 px-2 cursor-pointer hover:bg-gray-100 ${
            isSelected ? 'bg-blue-100' : ''
          }`}
          style={{ paddingLeft: `${depth * 20 + 8}px` }}
          onClick={() => {
            if (isDir) {
              toggleExpanded(entry.path);
            }
            onSelectPath(entry.path);
          }}
        >
          {/* Expand/Collapse Icon */}
          {isDir && (
            <span className="text-gray-500 w-4 flex-shrink-0">
              {expanded ? '▼' : '▶'}
            </span>
          )}
          {!isDir && <span className="w-4 flex-shrink-0" />}

          {/* Icon */}
          <span className="text-lg flex-shrink-0">
            {isDir ? '📁' : '🎵'}
          </span>

          {/* Name */}
          <span className="text-sm text-gray-900 flex-1 truncate">
            {entry.name}
          </span>

          {/* Size */}
          {!isDir && (
            <span className="text-xs text-gray-500 flex-shrink-0">
              {formatSize(entry.itemSize)}
            </span>
          )}

          {/* Locked indicator */}
          {entry.locked && (
            <span className="text-sm flex-shrink-0">🔒</span>
          )}
        </div>

        {/* Children (if directory and expanded) */}
        {isDir && expanded && entry.item.kind === 'directory' && (
          <div>
            {entry.item.entries.length === 0 ? (
              <div
                className="text-xs text-gray-400 italic py-1"
                style={{ paddingLeft: `${(depth + 1) * 20 + 28}px` }}
              >
                (empty)
              </div>
            ) : (
              entry.item.entries.map((child) => renderEntry(child, depth + 1))
            )}
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="border border-gray-200 rounded overflow-auto max-h-[600px]">
      {drive.root.item.kind === 'directory' && drive.root.item.entries.length === 0 ? (
        <div className="text-center py-12 text-gray-500">
          <p>No files found.</p>
          <p className="text-sm mt-2">Click "Scan +Drive" to load files from your Digitakt.</p>
        </div>
      ) : (
        <div className="p-2">
          {drive.root.item.kind === 'directory' &&
            drive.root.item.entries.map((entry) => renderEntry(entry, 0))}
        </div>
      )}
    </div>
  );
}

/**
 * Format file size in human-readable format
 */
function formatSize(bytes: number): string {
  if (bytes === 0) return '0 B';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return `${(bytes / Math.pow(k, i)).toFixed(1)} ${sizes[i]}`;
}
