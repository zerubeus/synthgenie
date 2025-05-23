# 🎵 SynthGenie Frontend

**Your AI Sound Designer for Synthesizers**

SynthGenie is an intelligent sound design assistant that connects to your MIDI synthesizers and helps you craft the perfect sounds through natural language conversations. Simply describe the sound you want, and SynthGenie will automatically adjust your synthesizer's parameters via MIDI Control Change messages.

## 🎯 Project Goals

SynthGenie aims to democratize sound design by:

- **Bridging the gap** between musical ideas and technical implementation
- **Simplifying synthesizer programming** through conversational AI
- **Enabling rapid sound exploration** without deep technical knowledge
- **Supporting professional workflows** with precise MIDI control
- **Preserving the tactile experience** of hardware synthesizers

## 🛠️ Core Features

### 🎹 Enhanced MIDI Integration
- **Real-time device detection** via Web MIDI API
- **Automatic parameter mapping** for supported synthesizers
- **Multiple MIDI message types**: Standard CC, High-Resolution CC (14-bit), and NRPN
- **Bidirectional communication** with hardware devices
- **Multi-channel MIDI support** (1-16 channels)
- **Intelligent message routing** based on synthesizer capabilities

### 🤖 AI-Powered Sound Design
- **Natural language processing** for sound descriptions
- **Intelligent parameter translation** from text to MIDI values
- **Context-aware suggestions** based on synthesizer capabilities
- **Real-time parameter adjustment** during conversations
- **Synthesizer-specific optimization** for Moog and Elektron devices

### 🔒 Device Access Control
- **Restricted access** to users with compatible MIDI devices
- **Supported devices**: 
  - **Moog Subsequent 37/25** (with high-resolution CC and NRPN support)
  - **Elektron Digitone series** (standard CC support)
- **Real-time device validation** and status monitoring
- **Graceful fallback** for unsupported browsers/devices

### 🎨 Modern User Interface
- **Dark theme** optimized for studio environments
- **Responsive design** for desktop and tablet use
- **Real-time chat interface** with message history
- **Visual feedback** for MIDI operations and device status
- **Gradient branding** matching the SynthGenie aesthetic

## 🏗️ Architecture & Technology Stack

### Frontend Framework
- **React 19** with TypeScript for type safety
- **React Router 7** for client-side routing and SSR support
- **Vite** for fast development and optimized builds
- **TailwindCSS 4** for utility-first styling

### State Management
- **TanStack Query** for server state management and caching
- **React Hooks** for local component state
- **Custom hooks** for feature-specific logic

### MIDI Integration
- **Web MIDI API** for direct hardware communication
- **Custom MIDI hooks** for device management and message handling
- **Real-time device monitoring** with automatic reconnection
- **Multi-format MIDI support** (CC, High-Res CC, NRPN)

### API Communication
- **RESTful API** integration with the SynthGenie backend
- **Synthesizer-specific endpoints** for optimized parameter mapping
- **API key authentication** for secure access
- **Error handling** with user-friendly messages
- **Environment-based** endpoint configuration

## 📁 Project Structure

```
ui/
├── app/                          # Main application code
│   ├── features/                 # Feature-based organization
│   │   ├── api/                  # API integration
│   │   │   ├── components/       # API-related UI components
│   │   │   ├── hooks/            # API hooks (useSynthGenieApi)
│   │   │   ├── types/            # API type definitions
│   │   │   └── utils/            # API utilities (endpoint detection)
│   │   ├── chat/                 # Chat functionality
│   │   │   ├── components/       # Chat UI components
│   │   │   │   ├── ChatHeader.tsx
│   │   │   │   ├── MessageList.tsx
│   │   │   │   ├── ChatInputArea.tsx
│   │   │   │   └── MidiAccessRestriction.tsx
│   │   │   ├── hooks/            # Chat state management
│   │   │   │   ├── useChatMessages.ts
│   │   │   │   └── useAutoScroll.ts
│   │   │   ├── types/            # Chat type definitions
│   │   │   ├── utils/            # Chat utilities
│   │   │   └── ChatView.tsx      # Main chat interface
│   │   ├── midi/                 # MIDI functionality
│   │   │   ├── components/       # MIDI UI components
│   │   │   │   └── MidiDeviceSelector.tsx
│   │   │   ├── hooks/            # MIDI hooks
│   │   │   │   ├── useMidi.ts    # Enhanced MIDI functionality
│   │   │   │   └── useMidiDeviceValidation.ts
│   │   │   └── types/            # MIDI type definitions
│   │   └── welcome/              # Welcome page
│   │       ├── components/       # Welcome UI components
│   │       └── WelcomePage.tsx   # Landing page
│   ├── shared/                   # Shared components and utilities
│   │   ├── components/           # Reusable UI components
│   │   └── types/                # Global type definitions
│   ├── styles/                   # Global styles and CSS
│   │   └── global.css            # TailwindCSS imports and custom styles
│   ├── assets/                   # Static assets (images, icons)
│   ├── root.tsx                  # Root component with providers
│   └── routes.tsx                # Application routing configuration
├── public/                       # Static public assets
│   ├── favicon.svg               # Musical note favicon
│   └── favicon.ico               # Fallback favicon
├── docs/                         # Documentation
│   └── design_system.md          # Design system guidelines
├── package.json                  # Dependencies and scripts
├── bun.lockb                     # Bun lock file
├── tsconfig.json                 # TypeScript configuration
├── vite.config.ts                # Vite build configuration
├── react-router.config.ts        # React Router configuration
└── README.md                     # This file
```

### Feature-Based Organization

Each feature is self-contained with its own:
- **Components**: UI elements specific to the feature
- **Hooks**: Custom React hooks for state management
- **Types**: TypeScript definitions for the feature
- **Utils**: Helper functions and utilities

## 🔌 API Integration

### SynthGenie API

The frontend communicates with the SynthGenie API to process natural language sound design requests. The API now supports synthesizer-specific endpoints and enhanced MIDI message formats.

#### Base URLs
- **Production**: `https://api.synthgenie.com`
- **Development**: `http://localhost:8080` (configurable)

#### Authentication
All API requests require an API key passed in the `X-API-Key` header.

#### Endpoints

The API now features synthesizer-specific endpoints for optimized parameter mapping:

##### POST `/agent/sub37/prompt`
Processes natural language requests for Moog Subsequent 37 synthesizers.

##### POST `/agent/digitone/prompt`
Processes natural language requests for Elektron Digitone synthesizers.

**Request:**
```json
{
  "prompt": "Make the filter more resonant and add some vibrato"
}
```

**Response (New Format):**
```json
{
  "used_tool": "set_filter_cutoff",
  "midi_channel": 1,
  "value": 100,
  "midi_cc": 74,
  "midi_cc_lsb": null,
  "nrpn_msb": null,
  "nrpn_lsb": null
}
```

**High-Resolution CC Example:**
```json
{
  "used_tool": "set_amp_eg_attack_time",
  "midi_channel": 3,
  "value": 8192,
  "midi_cc": 28,
  "midi_cc_lsb": 60,
  "nrpn_msb": null,
  "nrpn_lsb": null
}
```

**NRPN Example:**
```json
{
  "used_tool": "set_arp_rate",
  "midi_channel": 3,
  "value": 10000,
  "midi_cc": null,
  "midi_cc_lsb": null,
  "nrpn_msb": 3,
  "nrpn_lsb": 19
}
```

#### Error Handling
- **401**: Invalid or missing API key
- **422**: Query is not about sound design
- **400**: Invalid request format or unsupported synthesizer
- **500**: Server error

### Environment Configuration

Create a `.env` file for local development:

```env
# API Configuration
VITE_API_ENV=local          # Use 'local' for development
VITE_API_HOST=localhost     # API host (default: localhost)
VITE_API_PORT=8080          # API port (default: 8080)

# Development
NODE_ENV=development
```

## 🚀 Getting Started

### Prerequisites

- **Bun** 1.0+ (package manager)
- **Compatible MIDI device** (Moog Subsequent 37 or Elektron Digitone series)
- **Modern browser** with Web MIDI API support (Chrome, Edge, Opera)
- **SynthGenie API key** (contact support for access)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/synthgenie-ui.git
   cd synthgenie-ui
   ```

2. **Install dependencies:**
   ```bash
   bun install
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start development server:**
   ```bash
   bun dev
   ```

5. **Open in browser:**
   Navigate to `http://localhost:5173`

### Production Build

```bash
# Build for production
bun build

# Start production server
bun start
```

## 🎹 Using SynthGenie

### 1. Connect Your MIDI Device

1. **Power on** your Moog Subsequent 37 or Elektron Digitone synthesizer
2. **Connect via USB** or MIDI interface to your computer
3. **Open SynthGenie** in a supported browser
4. **Grant MIDI permissions** when prompted
5. **Select your device** from the dropdown menu

### 2. Set Your API Key

1. Click the **"SET API KEY"** button in the chat interface
2. **Enter your API key** (contact support if you don't have one)
3. **Save** the key (stored locally in your browser)

### 3. Start Designing Sounds

Once connected, you can start describing sounds in natural language:

#### Example Prompts:
- *"Make the filter more aggressive and add some distortion"*
- *"I want a warm, analog bass sound with slow attack"*
- *"Add vibrato to the oscillator and increase the resonance"*
- *"Create a bright lead sound with fast envelope"*
- *"Make it sound more vintage and warm"*

#### What Happens:
1. **Device Detection**: System automatically detects your synthesizer type
2. **Endpoint Selection**: Routes request to appropriate API endpoint
3. **AI Processing**: Your prompt is processed by synthesizer-specific AI
4. **Parameter Translation**: AI converts description to appropriate MIDI format
5. **MIDI Transmission**: Parameters sent using optimal message type (CC/High-Res CC/NRPN)
6. **Real-time Feedback**: You hear the changes immediately
7. **Chat History**: All actions are logged in the conversation

### 4. Supported Devices & MIDI Formats

#### Moog Subsequent 37/25
- **Standard CC**: Basic parameter control (0-127)
- **High-Resolution CC**: 14-bit precision (0-16383) for smooth parameter changes
- **NRPN**: Non-Registered Parameter Numbers for advanced synthesis parameters
- **Automatic format selection** based on parameter requirements

#### Elektron Digitone Series
- **Standard CC**: Parameter control optimized for Elektron's CC mapping
- **Multi-timbral support** across multiple MIDI channels

*Note: Device names must contain "moog", "subsequent", "sub37", or "digitone" (case-insensitive) to be recognized.*

## 🔧 Development

### Available Scripts

```bash
# Development
bun dev              # Start development server
bun build            # Build for production
bun start            # Start production server

# Code Quality
bun lint             # Run ESLint
bun test             # Run tests with Vitest

# Type Checking
bunx tsc --noEmit    # Check TypeScript types
```

### Key Development Patterns

#### Enhanced Custom Hooks
- **useMidi**: Core MIDI device management with multi-format support
- **useMidiDeviceValidation**: Device access control with synthesizer detection
- **useChatMessages**: Chat state and API integration with new response format
- **useApiKey**: API key management with localStorage
- **useSynthGenieApi**: Enhanced API hook with endpoint routing

#### Component Architecture
- **Feature-based organization** for scalability
- **Compound components** for complex UI elements
- **Render props** for flexible component composition
- **TypeScript** for type safety throughout

#### State Management
- **TanStack Query** for server state and caching
- **React hooks** for local component state
- **Context providers** for global state when needed

### Adding New Features

1. **Create feature directory** under `app/features/`
2. **Add components, hooks, types** as needed
3. **Export from feature index** for clean imports
4. **Update routing** in `app/routes.tsx` if needed
5. **Add tests** for critical functionality

## 🎨 Design System

SynthGenie follows a consistent design system documented in `docs/design_system.md`:

### Color Palette
- **Background**: Black (#000000) to Gray-900 (#111827)
- **Brand Gradient**: Blue-400 → Indigo-400 → Purple-400
- **Accent**: Blue-500/600 for interactive elements
- **Text**: White to Gray-400 hierarchy

### Typography
- **Font**: Inter (Google Fonts)
- **Headings**: Bold with gradient text
- **Body**: Regular weight, contextual colors

### Components
- **Rounded corners** (rounded-lg, rounded-xl)
- **Subtle borders** (border-gray-800)
- **Drop shadows** for depth
- **Hover effects** with smooth transitions

## 🔒 Security & Privacy

### API Key Management
- **Local storage only** - keys never leave your browser
- **No server-side storage** of user credentials
- **Secure transmission** via HTTPS
- **Easy key rotation** through the UI

### MIDI Security
- **Browser permission required** for MIDI access
- **Local device communication** only
- **No data transmission** of MIDI messages to servers
- **User-controlled** device selection and permissions

## 🐛 Troubleshooting

### Common Issues

#### MIDI Device Not Detected
1. **Check browser support** (Chrome, Edge, Opera recommended)
2. **Verify device connection** and power
3. **Grant MIDI permissions** when prompted
4. **Try refreshing** the page
5. **Check device name** contains supported synthesizer identifiers

#### API Key Issues
1. **Verify key format** (contact support if unsure)
2. **Check network connection** to API
3. **Clear browser cache** and re-enter key
4. **Check browser console** for detailed error messages

#### Chat Not Working
1. **Ensure valid MIDI device** is selected
2. **Verify API key** is set correctly
3. **Check browser console** for errors
4. **Try clearing chat** and starting fresh

#### Unsupported Synthesizer Errors
1. **Verify device name** contains "moog", "subsequent", "sub37", or "digitone"
2. **Check MIDI device connection**
3. **Try reconnecting the device**
4. **Contact support** if your supported device isn't recognized

### Browser Compatibility

| Browser | MIDI Support | Recommended |
|---------|--------------|-------------|
| Chrome  | ✅ Full      | ✅ Yes      |
| Edge    | ✅ Full      | ✅ Yes      |
| Opera   | ✅ Full      | ✅ Yes      |
| Firefox | ❌ None      | ❌ No       |
| Safari  | ❌ None      | ❌ No       |

## 📞 Support

### Getting Help
- **Documentation**: Check this README and `docs/` folder
- **Issues**: Open a GitHub issue for bugs or feature requests
- **API Access**: Contact support for API key requests
- **Community**: Join our Discord for community support

### Contributing
We welcome contributions! Please see `CONTRIBUTING.md` for guidelines.

### License
This project is licensed under the MIT License - see `LICENSE` file for details.

---

**Built with ❤️ for the synthesizer community**

*SynthGenie - Where AI meets analog*
