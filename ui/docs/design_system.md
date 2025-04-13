# SynthGenie Design System

## Color Palette

### Background Colors

- **Black**: `#000000` (`bg-black`) - Used for main background
- **Gray-950**: `#0B0F1A` (`bg-gray-950`) - Used for dark backgrounds, gradient starting point
- **Gray-900**: `#111827` (`bg-gray-900`) - Used for component backgrounds
- **Gray-800**: `#1F2937` (`bg-gray-800`) - Used for borders and secondary backgrounds

### Brand Colors (Gradient)

- **Blue-400**: `#60A5FA` (`from-blue-400`) - Start of gradient
- **Indigo-400**: `#818CF8` (`via-indigo-400`) - Middle of gradient
- **Purple-400**: `#A78BFA` (`to-purple-400`) - End of gradient

### Accent Colors

- **Blue-400**: `#60A5FA` - Text highlights
- **Blue-500**: `#3B82F6` - UI elements, backgrounds
- **Blue-600**: `#2563EB` - Buttons, interactive elements
- **Indigo-400**: `#818CF8` - Secondary elements
- **Indigo-600**: `#4F46E5` - Buttons, interactive elements

### Text Colors

- **White**: `#FFFFFF` - Primary text on dark backgrounds
- **Gray-100**: `#F3F4F6` - Primary text in dark UI components
- **Gray-200**: `#E5E7EB` - Secondary text in dark UI components
- **Gray-400**: `#9CA3AF` - Tertiary text, less important information
- **Gray-500**: `#6B7280` - Disabled text, subtle information

## Typography

### Font Family

```css
--font-sans:
  'Inter', ui-sans-serif, system-ui, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
  'Segoe UI Symbol', 'Noto Color Emoji';
```

Primary font: **Inter**

### Text Styles

- **Headings**: Bold, gradient text (blue to purple)
- **Body text**: Regular weight, white or gray depending on hierarchy
- **Button text**: Medium weight, white or contextual colors

## UI Components

### Buttons

- Primary: Gradient background from blue-600 to indigo-600
- Secondary: Gray-800 with hover states
- Interactive hover effects with opacity and color transitions

### Chat Messages

- User messages: Blue gradient backgrounds
- Assistant messages: Gray-800 backgrounds with border

### Cards/Containers

- Rounded corners (rounded-lg, rounded-xl)
- Subtle borders (border-gray-800)
- Drop shadows for depth (shadow-md, shadow-2xl)
