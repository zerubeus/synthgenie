# API Authentication

The SynthGenie API uses API key-based authentication to secure its endpoints.

## Setting up API Keys

### Admin API Key

The system requires an admin API key which is used to generate and manage user API keys. Set the admin key in your environment variables:

```bash
export ADMIN_API_KEY="your-secure-admin-key"
```

If not explicitly set, the application will generate a temporary admin key when started and output it to the console.

## Managing API Keys

### Generate API Key

To generate a new API key for a user:

```bash
curl -X POST "http://localhost:8000/api-keys/generate" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-admin-key" \
  -d '{"user_id": "user123"}'
```

Response:

```json
{
  "api_key": "generated-api-key-for-user",
  "message": "API key generated for user user123"
}
```

### Revoke API Key

To revoke an existing API key:

```bash
curl -X DELETE "http://localhost:8000/api-keys/revoke" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-admin-key" \
  -d '{"api_key": "key-to-revoke"}'
```

## Using API Keys

All protected endpoints require the API key to be included in the request header:

```bash
curl -X POST "http://localhost:8000/agent/prompt" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{"prompt": "Set FM ratio to 2:1"}'
```

## Security Considerations

- Always use HTTPS in production
- Store API keys securely
- Rotate API keys periodically
- In production, implement rate limiting based on API key
- Use a persistent database to store API keys instead of in-memory storage

## Domain Restrictions

The API implements domain restrictions in two ways:

### 1. CORS Policy

CORS (Cross-Origin Resource Sharing) settings are configured to only allow browser-based requests from the following domains:

- https://synthgenie.com (main domain)
- https://www.synthgenie.com
- https://api.synthgenie.com
- Additional subdomains can be added to the allowed list in the application configuration

During development, requests from local environments (localhost) are also permitted when the `ENVIRONMENT` environment variable is set to `development`:

```bash
export ENVIRONMENT=development
```

### 2. Domain Verification Middleware

In addition to CORS, the API uses a custom middleware that verifies the `Origin` and `Referer` headers to ensure requests come from synthgenie.com or its subdomains.

This middleware provides deeper protection than CORS alone because:

- It works with non-browser clients
- It validates all subdomains of synthgenie.com automatically
- It checks both Origin and Referer headers

For development or testing purposes, you can disable domain verification by setting:

```bash
export SKIP_DOMAIN_CHECK=true
```

To modify the domain verification settings, update the middleware configuration in `synthgenie/app.py`.
