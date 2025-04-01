# SynthGenie API

API for controlling Elektron Digitone synthesizer parameters using AI.

## Installation

SynthGenie API uses [uv](https://github.com/astral-sh/uv) for dependency management.

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) installed

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/synthgenie-api.git
   cd synthgenie-api
   ```

2. Install dependencies using uv:

   ```bash
   uv pip install -e .
   ```

3. Set up environment variables (copy .env.example to .env and modify):
   ```bash
   cp .env.example .env
   ```

## Running the API

Start the development server:

```bash
uvicorn synthgenie.app:app --reload
```

## API Authentication

The API uses API key-based authentication. You'll need an admin API key to generate user API keys.

```bash
# Set the admin API key
export ADMIN_API_KEY="your-secure-admin-key"
```

See the [API Authentication documentation](docs/api_authentication.md) for more details.

## Database

SynthGenie uses SQLite by default for simplicity and minimal overhead. The database is automatically created when the application starts.

See the [Database documentation](docs/database.md) for more details and scaling options.

## Development

Install development dependencies:

```bash
uv pip install -e ".[dev]"
```

## Domain Restrictions

By default, the API only accepts requests from synthgenie.com and its subdomains. For development:

```bash
# Allow local development
export ENVIRONMENT=development

# Skip domain verification entirely
export SKIP_DOMAIN_CHECK=true
```
