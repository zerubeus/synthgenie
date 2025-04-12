// src/features/chat/hooks/useTextAreaAutoSize.ts
import { useRef, useEffect } from 'react';
import type { RefObject } from 'react';

/**
 * Custom hook to automatically adjust the height of a textarea based on its content.
 *
 * It listens for changes in the `value` prop and updates the textarea's height
 * style property to match its scrollHeight, respecting CSS min/max-height.
 *
 * @param value The current string value of the textarea.
 * @returns A ref object (`React.RefObject<HTMLTextAreaElement>`) that should be
 *          assigned to the `ref` prop of the target textarea element.
 *
 * @example
 * const [inputValue, setInputValue] = useState("");
 * const textAreaRef = useTextAreaAutoSize(inputValue);
 *
 * return (
 *   <textarea
 *     ref={textAreaRef}
 *     value={inputValue}
 *     onChange={(e) => setInputValue(e.target.value)}
 *     rows={1} // Start with minimum rows
 *     className="your-tailwind-classes min-h-[...] max-h-[...] overflow-y-auto" // Set limits via CSS
 *     placeholder="Type here..."
 *   />
 * )
 */
export const useTextAreaAutoSize = (
  value: string
): RefObject<HTMLTextAreaElement | null> => {
  // Create a ref to attach to the textarea element
  const textAreaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    const textArea = textAreaRef.current;

    if (textArea) {
      // --- Reset height temporarily to get the correct scrollHeight ---
      // This ensures that the scrollHeight calculation isn't based on a previously
      // larger height (important when text is deleted).
      textArea.style.height = 'auto'; // Can also use '0px' or rely on CSS min-height

      // --- Calculate the scroll height ---
      // scrollHeight includes padding but not border or margin.
      const scrollHeight = textArea.scrollHeight;

      // --- Set the height to the calculated scroll height ---
      // The browser will respect the CSS `min-height` and `max-height` properties.
      // If scrollHeight exceeds max-height, `overflow-y: auto` (set via CSS)
      // should activate the scrollbar.
      textArea.style.height = `${scrollHeight}px`;

      // --- Optional: Adjust overflow style directly (Alternative to CSS) ---
      // Generally, it's better to control overflow via CSS (`overflow-y: auto` combined with `max-height`).
      // Uncomment this block if you prefer direct style manipulation.
      /*
      const computedStyle = window.getComputedStyle(textArea);
      const maxHeight = parseInt(computedStyle.maxHeight, 10);

      if (maxHeight && scrollHeight >= maxHeight) {
        // If content reaches or exceeds max-height, ensure scrollbar is visible
        if (textArea.style.overflowY !== 'auto') { // Avoid unnecessary style changes
            textArea.style.overflowY = 'auto';
        }
      } else {
        // Otherwise, hide the scrollbar (if content fits within max-height)
         if (textArea.style.overflowY !== 'hidden') { // Avoid unnecessary style changes
             textArea.style.overflowY = 'hidden';
         }
      }
      */
    }
  }, [value]); // Re-run this effect whenever the textarea value changes

  // Return the ref object so the component can attach it to the textarea
  return textAreaRef;
};

// Default export is also fine if preferred
// export default useTextAreaAutoSize;
