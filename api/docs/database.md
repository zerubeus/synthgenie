# Database Documentation

## Overview

SynthGenie uses PostgreSQL as its primary database with pgvector extension for vector operations. The database stores API keys, tracks usage, and other application data.

## Configuration

The database connection is configured using environment variables:

- `DB_HOST`: Database host address
- `DB_PORT`: Database port
- `POSTGRES_DB`: Database name
- `POSTGRES_USER`: Database username
- `POSTGRES_PASSWORD`: Database password
- `DATABASE_URL`: Full connection string (constructed from above variables if not provided)

## Schema

### Tables

#### api_keys

Stores API keys for authentication and authorization.

| Column     | Type      | Description                     |
| ---------- | --------- | ------------------------------- |
| key        | TEXT      | Primary key, the API key itself |
| user_id    | TEXT      | Associated user identifier      |
| created_at | TIMESTAMP | When the API key was created    |

#### api_key_usage

Tracks usage statistics for API keys.

| Column        | Type      | Description                          |
| ------------- | --------- | ------------------------------------ |
| key           | TEXT      | Primary key, foreign key to api_keys |
| request_count | INTEGER   | Number of requests made with key     |
| last_used_at  | TIMESTAMP | When the key was last used           |

## Connection Management

The application uses a connection management system with retry capabilities:

- Maximum retry attempts: 5 (default)
- Retry delay: 2 seconds (default)
- Auto-commit is disabled by default

## Initialization

Database initialization creates the required tables if they don't exist. This process is handled by the `initialize_db()` function in the application codebase.
