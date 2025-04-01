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

## SQL Implementation

The application uses Python's built-in `sqlite3` module for direct SQL queries instead of an ORM. The database schema is initialized at application startup with the following tables:

### API Keys

The `api_keys` table stores API key information:

```sql
CREATE TABLE IF NOT EXISTS api_keys (
    key TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Database Connection

Database connections are managed with a context manager to ensure proper resource cleanup:

```python
@contextlib.contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    try:
        yield conn
    finally:
        conn.close()
```

## Scaling Considerations

While SQLite is sufficient for development and small-scale deployments, you might consider migrating to PostgreSQL or another database system for production use with higher traffic loads.

To switch to PostgreSQL, you would need to:

1. Update the database module to support PostgreSQL connections
2. Modify the SQL queries as needed for PostgreSQL compatibility
3. Update the `DATABASE_URL` environment variable:

   ```bash
   export DATABASE_URL="postgresql://user:password@localhost/synthgenie"
   ```

4. Install the PostgreSQL driver:

   ```bash
   uv pip install psycopg2-binary
   ```
