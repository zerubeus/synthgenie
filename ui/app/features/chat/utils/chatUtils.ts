/**
 * This file contains utility functions specifically related to the chat feature,
 * such as formatting messages or generating specific content.
 */

import { detectSynthType, getDeviceDisplayName, getSynthDisplayName } from '../../api/utils/getApiBaseUrl';

/**
 * Generates the initial welcome message displayed by the assistant.
 * The message content includes details about supported features and varies based on
 * the connected MIDI device type.
 *
 * IMPORTANT: The returned string contains HTML elements (`<strong>`, `<a>`).
 * Ensure it is rendered using `dangerouslySetInnerHTML` in the receiving component
 * and that the source of this content is trusted.
 *
 * @param selectedDevice - The name of the currently selected MIDI device,
 *                         or null/undefined if no device is selected.
 * @returns The formatted welcome message string containing HTML.
 */
export const getInitialWelcomeMessage = (selectedDevice?: string | null): string => {
  // Determine the device-specific part of the greeting
  // Using <strong> to make the device name stand out more visually
  const deviceDisplayName = selectedDevice ? getDeviceDisplayName(selectedDevice) : null;
  const deviceContext = deviceDisplayName ? ` connected to <strong>"${deviceDisplayName}"</strong>` : '';

  // Detect the synthesizer type to customize the message
  const synthType = selectedDevice ? detectSynthType(selectedDevice) : null;
  
  let deviceSpecificInfo = '';
  
  if (synthType === 'sub37') {
    deviceSpecificInfo = `Currently supporting <strong>${getSynthDisplayName('sub37')}</strong> synthesizers with advanced MIDI control.\nSupports standard CC, high-resolution CC (14-bit), and NRPN messages for precise parameter control.`;
  } else if (synthType === 'digitone') {
    deviceSpecificInfo = `Currently supporting <strong>${getSynthDisplayName('digitone')}</strong> FM synthesizers.\nSupports standard MIDI CC messages for real-time parameter control.`;
  } else {
    deviceSpecificInfo = `Supporting <strong>${getSynthDisplayName('sub37')}</strong> and <strong>${getSynthDisplayName('digitone')}</strong> synthesizers.\nConnect a supported device via USB to get started.`;
  }

  // Construct the full message using template literals for readability
  // Includes line breaks (\n\n) which will be respected by `whitespace-pre-wrap` CSS
  const welcomeMessage = `Hello! I'm SynthGenie${deviceContext}.\n\n${deviceSpecificInfo}\n\nGet an API key from our <a href="https://discord.gg/ZFuSuegBMS" target="_blank" rel="noopener noreferrer" class="inline-flex items-center text-indigo-400 hover:text-purple-400">Discord</a> to join the beta and start designing sounds with natural language!`;

  return welcomeMessage;
};
