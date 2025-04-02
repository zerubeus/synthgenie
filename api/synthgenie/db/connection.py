import os
import psycopg2
import psycopg2.extras
import logging

logger = logging.getLogger(__name__)

# Get database connection URL from environment
DATABASE_URL = os.getenv("DB_URL")

# Create a connection pool
_connection_pool = None


def get_connection():
    """Get a database connection from the pool."""
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(DATABASE_URL)
        # Set autocommit mode
        conn.autocommit = False
        return conn
    except Exception as e:
        logger.error(f"Error connecting to PostgreSQL: {e}")
        raise


def initialize_db():
    """Initialize the database with required tables."""
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Create API keys table
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS api_keys (
            key TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        )

        # Create API key usage table
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS api_key_usage (
            key TEXT PRIMARY KEY,
            request_count INTEGER DEFAULT 0,
            last_used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (key) REFERENCES api_keys(key) ON DELETE CASCADE
        )
        """
        )

        conn.commit()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


def dict_factory(cursor, row):
    """Convert a row to a dictionary."""
    return dict(row)


def get_db():
    """Get database connection for dependency injection."""
    conn = None
    try:
        conn = get_connection()
        # Use RealDictCursor to return rows as dictionaries
        conn.cursor_factory = psycopg2.extras.RealDictCursor
        yield conn
    finally:
        if conn:
            conn.close()
