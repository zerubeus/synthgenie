/**
 * This file contains utility functions specifically related to the chat feature,
 * such as formatting messages or generating specific content.
 */

/**
 * Generates the initial welcome message displayed by the assistant.
 * The message content includes details about supported features and varies slightly
 * to mention the connected MIDI device if one is selected.
 *
 * IMPORTANT: The returned string contains HTML elements (`<strong>`, `<a>`).
 * Ensure it is rendered using `dangerouslySetInnerHTML` in the receiving component
 * and that the source of this content is trusted.
 *
 * @param selectedDevice - The name of the currently selected MIDI device,
 *                         or null/undefined if no device is selected.
 * @returns The formatted welcome message string containing HTML.
 */
export const getInitialWelcomeMessage = (
  selectedDevice?: string | null
): string => {
  // Determine the device-specific part of the greeting
  // Using <strong> to make the device name stand out more visually
  const deviceContext = selectedDevice
    ? ` connected to <strong>"${selectedDevice}"</strong>`
    : '';

  // Construct the full message using template literals for readability
  // Includes line breaks (\n\n) which will be respected by `whitespace-pre-wrap` CSS
  const welcomeMessage = `Hello! I'm Synthgenie${deviceContext}.\n\nCurrently supporting <strong>Digitone 2</strong> FM synthesizer only.\nConnect via USB and get an API key from our <a href="https://discord.gg/aB4N9Zue" target="_blank" rel="noopener noreferrer" class="inline-flex items-center text-indigo-400 hover:text-purple-400">Discord</a> to join the beta.\nOnly the <strong>Wavetone machine</strong> and <strong>multi-mode filter</strong> are currently supported and need to be pre-set before prompting.`;

  return welcomeMessage;
};
