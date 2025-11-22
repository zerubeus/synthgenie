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
          className={`flex items-center gap-3 py-2 px-3 cursor-pointer border-b border-gray-900 hover:bg-gray-900 transition-colors ${
            isSelected ? 'bg-orange-950 border-orange-900' : ''
          }`}
          style={{ paddingLeft: `${depth * 20 + 12}px` }}
          onClick={() => {
            if (isDir) {
              toggleExpanded(entry.path);
            }
            onSelectPath(entry.path);
          }}
        >
          {/* Expand/Collapse Icon */}
          {isDir && (
            <span className="text-orange-500 w-3 flex-shrink-0 text-xs font-bold">
              {expanded ? '▼' : '▶'}
            </span>
          )}
          {!isDir && <span className="w-3 flex-shrink-0" />}

          {/* Icon */}
          <span className="text-xs flex-shrink-0 text-gray-500 font-bold uppercase tracking-wider">
            {isDir ? '[DIR]' : '[WAV]'}
          </span>

          {/* Name */}
          <span className="text-sm text-gray-200 flex-1 truncate font-mono uppercase tracking-wide">
            {entry.name}
          </span>

          {/* Size */}
          {!isDir && (
            <span className="text-xs text-gray-500 flex-shrink-0 font-mono">
              {formatSize(entry.itemSize)}
            </span>
          )}

          {/* Locked indicator */}
          {entry.locked && (
            <span className="text-xs flex-shrink-0 text-orange-500 font-bold uppercase tracking-wider">[LCK]</span>
          )}
        </div>

        {/* Children (if directory and expanded) */}
        {isDir && expanded && entry.item.kind === 'directory' && (
          <div>
            {entry.item.entries.length === 0 ? (
              <div
                className="text-xs text-gray-600 italic py-2 uppercase tracking-wide"
                style={{ paddingLeft: `${(depth + 1) * 20 + 28}px` }}
              >
                [Empty]
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
    <div className="border border-gray-800 rounded overflow-auto max-h-[600px] bg-black digitakt-scrollbar">
      {drive.root.item.kind === 'directory' && drive.root.item.entries.length === 0 ? (
        <div className="text-center py-12 text-gray-500">
          <p className="uppercase tracking-wide text-sm">No Files Found</p>
          <p className="text-xs mt-2 text-gray-600 uppercase tracking-wider">Click "Scan +Drive" to Load Files</p>
        </div>
      ) : (
        <div className="p-0">
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
