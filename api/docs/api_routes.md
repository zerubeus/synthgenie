# API Routes Documentation

## Overview

SynthGenie API provides endpoints for AI-assisted synthesizer parameter control and API key management. All endpoints require valid API key authentication.

## Base URL

The API is hosted at `https://api.synthgenie.com` (production) or `http://localhost:8000` (development).

## Authentication

All API endpoints require authentication using an API key. Include your API key in the request header:

```
X-API-Key: your_api_key_here
```

## Endpoints

### Agent Routes

#### POST `/agent/prompt`

Process a user prompt with the SynthGenie AI agent.

**Description**: The agent interprets natural language prompts and returns synthesizer parameter changes.

**Request Body**:

```json
{
  "prompt": "string"
}
```

**Response**:

```json
[
  {
    "used_tool": "string",
    "midi_cc": "integer",
    "midi_channel": "integer",
    "value": "integer"
  }
]
```

**Authentication**: Requires valid API key

**Rate Limiting**: Limited to 64 requests per session

### API Key Management

#### POST `/api-keys/generate`

Generate a new API key for a user.

**Description**: Creates a new API key associated with the specified user ID.

**Request Body**:

```json
{
  "user_id": "string"
}
```

**Response**:

```json
{
  "api_key": "string",
  "message": "string"
}
```

**Authentication**: Requires admin API key

#### DELETE `/api-keys/revoke`

Revoke an existing API key.

**Description**: Invalidates and removes an API key from the system.

**Request Body**:

```json
{
  "api_key": "string"
}
```

**Response**:

```json
{
  "api_key": "string",
  "message": "string"
}
```

**Authentication**: Requires admin API key

#### GET `/api-keys/list/{user_id}`

List all API keys for a specific user.

**Description**: Returns all active API keys associated with the specified user ID.

**Path Parameters**:

- `user_id`: User identifier

**Response**: Array of API key strings

```json
["string"]
```

**Authentication**: Requires admin API key

#### GET `/api-keys/usage`

Get usage statistics for all API keys.

**Description**: Returns usage data for all API keys in the system.

**Response**: Array of usage statistics

```json
[
  {
    "key": "string",
    "request_count": "integer",
    "last_used_at": "timestamp"
  }
]
```

**Authentication**: Requires admin API key

#### GET `/api-keys/usage/{api_key_value}`

Get usage statistics for a specific API key.

**Description**: Returns usage data for the specified API key.

**Path Parameters**:

- `api_key_value`: The API key to check

**Response**:

```json
{
  "key": "string",
  "request_count": "integer",
  "last_used_at": "timestamp"
}
```

**Authentication**: Requires admin API key or ownership of the specified API key
