# MIDI Synthesizer AI Controller Backend

## Overview

The MIDI Synthesizer AI Controller backend is built using FastAPI and PydanticAI, providing an intelligent interface for controlling MIDI synthesizers through natural language. The system enables users to describe the sounds they want to create, and the AI agent translates these requests into specific MIDI parameter adjustments.

## Architecture

The backend consists of several key components:

1. **FastAPI Application**: Provides HTTP and WebSocket endpoints for client communication
2. **PydanticAI Agent**: Powers the natural language understanding and tool-calling capabilities
3. **Connection Manager**: Handles WebSocket connections and tool execution between backend and frontend
4. **MIDI Tool System**: Defines synthesizer operations that can be called by the AI

## Core Components

### FastAPI Application

The application exposes several endpoints:

- `POST /agent/chat`: Process user messages through the AI agent
- `POST /agent/tool-result`: Receive tool execution results from client
- `WebSocket /ws/{client_id}`: Real-time bidirectional communication channel
- `GET /health`: Health check endpoint

CORS middleware is configured to allow cross-origin requests from frontend applications.

### Connection Manager

The `ConnectionManager` class handles:

- Tracking active WebSocket connections by client ID
- Managing pending tool call futures for asynchronous execution
- Sending messages to clients
- Resolving tool calls when results are received

This enables the asynchronous execution model where the agent can request MIDI operations that are performed in the browser.

### PydanticAI Agent

The agent is configured with:

- A synthesizer-specific system prompt
- Multiple MIDI parameter control tools
- Context dependency injection to maintain client association

The agent analyzes user requests, determines the appropriate synthesizer parameters to adjust, and orchestrates tool calls to achieve the desired sound.

### MIDI Tool System

Each MIDI tool:

1. Receives parameters from the AI
2. Creates an asyncio future to await the result
3. Sends the command to the client via WebSocket
4. Waits for the result with a timeout
5. Returns a descriptive result to the AI

Tools are defined for common synthesizer operations such as:

- Setting oscillator waveforms and pitch
- Adjusting filter parameters
- Configuring amplitude envelopes
- Applying effects

## Data Flow

1. **User Request Flow**:

   - User sends natural language request via WebSocket or HTTP endpoint
   - Request is processed by the PydanticAI agent
   - Agent may call multiple tools sequentially
   - Final response is sent back to the user

2. **Tool Execution Flow**:

   - Agent decides to call a tool
   - Backend creates an asyncio future for the result
   - Tool command is sent to client via WebSocket
   - Client executes MIDI operation and returns result
   - Future is resolved with the result
   - Agent continues processing with the result

3. **WebSocket Communication**:
   - Real-time bidirectional communication
   - JSON messages with typed payloads
   - Support for tool calls, tool results, and text responses

## Technical Specifications

### Dependencies

- **FastAPI**: Web framework for API endpoints
- **Uvicorn**: ASGI server implementation
- **PydanticAI**: AI agent framework with structured tool calling
- **Pydantic**: Data validation and settings management
- **WebSockets**: Real-time communication protocol

### Tool Definition Example

```python
@midi_agent.tool
async def set_oscillator_waveform(
    ctx: RunContext[Dict[str, Any]],
    oscillator: int,
    waveform_value: int,
    track: int = 1
) -> str:
    """
    Set the waveform for an oscillator.

    Args:
        oscillator: Oscillator number (1 or 2)
        waveform_value: Waveform value (0-127)
            - 0   = Sine
            - 40  = Triangle
            - 80  = Saw
            - 3   = Square
        track: Track number (1-16)
    """
    client_id = ctx.deps.get("client_id")
    tool_call_id = str(uuid.uuid4())

    # Create a future to wait for the result
    future = manager.create_pending_tool_call(tool_call_id)

    # Send the command to the client
    await manager.send_message(client_id, {
        "type": "tool_call",
        "tool": "set_oscillator_waveform",
        "tool_call_id": tool_call_id,
        "params": {
            "oscillator": oscillator,
            "waveform_value": waveform_value,
            "track": track
        }
    })

    # Wait for the result with a timeout
    try:
        result = await asyncio.wait_for(future, timeout=10.0)
        return f"Set oscillator {oscillator} waveform to {waveform_value} on track {track}. {result.get('details', '')}"
    except asyncio.TimeoutError:
        return f"Operation timed out when setting oscillator {oscillator} waveform"
```

## Message Formats

### WebSocket Messages

**From server to client:**

Tool call:

```json
{
  "type": "tool_call",
  "tool": "set_oscillator_waveform",
  "tool_call_id": "550e8400-e29b-41d4-a716-446655440000",
  "params": {
    "oscillator": 1,
    "waveform_value": 80,
    "track": 1
  }
}
```

Agent response:

```json
{
  "type": "agent_response",
  "response": "I've set up a saw wave on oscillator 1 with a medium attack and short decay as you requested.",
  "token_usage": 423
}
```

**From client to server:**

User message:

```json
{
  "type": "user_message",
  "message": "Can you create a bass sound with a saw wave?"
}
```

Tool result:

```json
{
  "type": "tool_result",
  "tool_call_id": "550e8400-e29b-41d4-a716-446655440000",
  "result": {
    "success": true,
    "details": "Waveform set successfully"
  }
}
```

## Configuration Options

The backend can be configured through environment variables:

- `PORT`: Server port (default: 8000)
- `HOST`: Server host (default: 0.0.0.0)
- `OPENAI_API_KEY`: OpenAI API key for the PydanticAI agent
- `ALLOWED_ORIGINS`: Comma-separated list of allowed CORS origins
- `DEBUG`: Enable debug mode (default: false)

## Deployment

The application can be deployed using:

1. **Docker**:

   ```
   docker build -t midi-synth-ai .
   docker run -p 8000:8000 -e OPENAI_API_KEY=your_key midi-synth-ai
   ```

2. **Direct**:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Security Considerations

- Use HTTPS in production
- Implement proper authentication for WebSocket connections
- Restrict CORS to known frontend origins
- Validate all user inputs with Pydantic models
- Use API keys with proper scope limitations
- Implement rate limiting to prevent abuse

## Performance Considerations

- The WebSocket connection enables low-latency communication
- Tool execution is asynchronous with timeouts to prevent hanging
- PydanticAI agent execution can be tuned for token usage

## Extending the System

To add new synthesizer capabilities:

1. Define new tool functions decorated with `@midi_agent.tool`
2. Document parameters clearly in the tool docstring
3. Implement corresponding MIDI execution in the frontend
4. Update the system prompt to inform the AI about new capabilities
