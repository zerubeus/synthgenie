/**
 * Path manipulation utilities for Digitakt +Drive
 * Based on elk-herd/src/Elektron/Path.elm
 */

import type { Path } from '../types/drive';

/**
 * Root path (empty array represents '/')
 */
export const ROOT_PATH: Path = [];

/**
 * Trash path where deleted items go
 */
export const TRASH_PATH: Path = ['TRASH'];

/**
 * Factory samples path
 */
export const FACTORY_PATH: Path = ['FACTORY'];

/**
 * Convert path array to string representation
 * @example pathToString(['samples', 'kicks']) => '/samples/kicks'
 * @example pathToString([]) => '/'
 */
export function pathToString(path: Path): string {
  if (path.length === 0) {
    return '/';
  }
  return '/' + path.join('/');
}

/**
 * Convert string path to Path array
 * @example stringToPath('/samples/kicks') => ['samples', 'kicks']
 * @example stringToPath('/') => []
 */
export function stringToPath(str: string): Path {
  if (str === '/' || str === '') {
    return [];
  }
  const cleaned = str.startsWith('/') ? str.slice(1) : str;
  return cleaned.split('/').filter((s) => s !== '' && s !== '.' && s !== '..');
}

/**
 * Get the basename (last component) of a path
 * @example baseName(['samples', 'kicks']) => 'kicks'
 * @example baseName([]) => ''
 */
export function baseName(path: Path): string {
  return path.length > 0 ? path[path.length - 1] : '';
}

/**
 * Get the parent directory path
 * @example dirPath(['samples', 'kicks']) => ['samples']
 * @example dirPath(['samples']) => []
 * @example dirPath([]) => []
 */
export function dirPath(path: Path): Path {
  return path.slice(0, -1);
}

/**
 * Create a sub-path by appending a name
 * @example subPath(['samples'], 'kicks') => ['samples', 'kicks']
 * @example subPath([], 'samples') => ['samples']
 */
export function subPath(path: Path, name: string): Path {
  return [...path, name];
}

/**
 * Get path depth (number of components)
 * @example pathDepth(['samples', 'kicks']) => 2
 * @example pathDepth([]) => 0
 */
export function pathDepth(path: Path): number {
  return path.length;
}

/**
 * Check if path `prefix` is a prefix of path `path`
 * @example startsWith(['samples'], ['samples', 'kicks']) => true
 * @example startsWith(['samples', 'kicks'], ['samples']) => false
 */
export function startsWith(prefix: Path, path: Path): boolean {
  if (prefix.length > path.length) {
    return false;
  }
  for (let i = 0; i < prefix.length; i++) {
    if (prefix[i] !== path[i]) {
      return false;
    }
  }
  return true;
}

/**
 * Find the deepest common ancestor of two paths
 * @example deepestCommonAncestor(['a', 'b', 'c'], ['a', 'b', 'd']) => ['a', 'b']
 * @example deepestCommonAncestor(['a', 'b'], ['a', 'b', 'c']) => ['a', 'b']
 * @example deepestCommonAncestor(['a'], ['b']) => []
 */
export function deepestCommonAncestor(p: Path, q: Path): Path {
  const result: Path = [];
  const minLen = Math.min(p.length, q.length);

  for (let i = 0; i < minLen; i++) {
    if (p[i] === q[i]) {
      result.push(p[i]);
    } else {
      break;
    }
  }

  return result;
}

/**
 * Check if path is in trash
 */
export function isInTrash(path: Path): boolean {
  return startsWith(TRASH_PATH, path);
}

/**
 * Check if paths are equal
 */
export function pathsEqual(p1: Path, p2: Path): boolean {
  if (p1.length !== p2.length) {
    return false;
  }
  for (let i = 0; i < p1.length; i++) {
    if (p1[i] !== p2[i]) {
      return false;
    }
  }
  return true;
}

/**
 * Generate a unique name by appending a number if needed
 * @example makeUniqueName('samples', ['foo', 'samples']) => 'samples 1'
 * @example makeUniqueName('samples', ['foo', 'samples', 'samples 1']) => 'samples 2'
 */
export function makeUniqueName(baseName: string, existingNames: string[]): string {
  if (!existingNames.includes(baseName)) {
    return baseName;
  }

  let counter = 1;
  while (existingNames.includes(`${baseName} ${counter}`)) {
    counter++;
  }
  return `${baseName} ${counter}`;
}
