# Database Configuration

SynthGenie API uses SQLite as the database backend for storing API keys and other data. This solution was chosen for its minimal overhead and simplicity.

## Database Setup

The database is automatically created and initialized when the application starts. By default, it creates a file named `synthgenie.db` in the application's root directory.

## Configuration

You can configure the database connection using environment variables:

```bash
# Use SQLite file database (default)
export DATABASE_URL="sqlite:///./synthgenie.db"

# For in-memory SQLite (testing)
export DATABASE_URL="sqlite:///:memory:"
```

## Models

The database currently includes the following models:

### API Keys

The `api_keys` table stores API key information:

| Column     | Type     | Description                     |
| ---------- | -------- | ------------------------------- |
| key        | String   | The API key (primary key)       |
| user_id    | String   | User ID associated with the key |
| created_at | DateTime | When the API key was created    |

## Scaling Considerations

While SQLite is sufficient for development and small-scale deployments, you might consider migrating to PostgreSQL or another database system for production use with higher traffic loads.

To switch to PostgreSQL, you would:

1. Update the `DATABASE_URL` environment variable:

   ```bash
   export DATABASE_URL="postgresql://user:password@localhost/synthgenie"
   ```

2. Install the PostgreSQL driver using uv:

   ```bash
   uv pip install psycopg2-binary
   ```

   Or add it to your pyproject.toml:

   ```toml
   dependencies = [
       # ... existing dependencies
       "psycopg2-binary>=2.9.9"
   ]
   ```

3. Remove the SQLite-specific connection arguments in `synthgenie/db/__init__.py`
