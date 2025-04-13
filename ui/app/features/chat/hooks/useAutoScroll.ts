import { useRef, useEffect } from 'react';
import type { RefObject, DependencyList } from 'react';

/**
 * Custom hook that scrolls an element into view whenever dependencies change.
 * Useful for auto-scrolling chat lists or logs.
 *
 * @param dependencies An array of dependencies. The scroll effect triggers when any of these change.
 * @returns A ref object (`React.RefObject<T | null>`) to be attached to the scrollable container's target element (e.g., a div at the end of the list).
 */
export const useAutoScroll = <T extends HTMLElement>(
  dependencies: DependencyList
): RefObject<T | null> => {
  const scrollRef = useRef<T>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, dependencies); // Trigger scroll when dependencies change

  return scrollRef;
};
