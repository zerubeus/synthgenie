import os
import psycopg2
import psycopg2.extras
import logging
import time

logger = logging.getLogger(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
)

logger.info(f"Database connection URL: {DATABASE_URL}")


def get_connection(max_retries=5, retry_delay=2):
    """
    Get a database connection with retry mechanism.

    Args:
        max_retries: Maximum number of connection attempts
        retry_delay: Seconds to wait between retries

    Returns:
        psycopg2 connection object
    """
    retry_count = 0
    last_error = None

    while retry_count < max_retries:
        try:
            logger.info(
                f"Attempting database connection (attempt {retry_count + 1}/{max_retries})"
            )
            conn = psycopg2.connect(DATABASE_URL)
            conn.autocommit = False
            logger.info("Database connection successful")
            return conn
        except Exception as e:
            last_error = e
            retry_count += 1
            logger.error(f"Error connecting to PostgreSQL: {e}")

            if retry_count < max_retries:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)

    logger.error(f"Failed to connect to database after {max_retries} attempts")
    logger.error(f"Database URL: {DATABASE_URL}")
    raise last_error


def initialize_db():
    """Initialize the database with required tables."""
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS api_keys (
            key TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        )

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
        conn.cursor_factory = psycopg2.extras.RealDictCursor
        yield conn
    finally:
        if conn:
            conn.close()
