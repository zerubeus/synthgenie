import logging
import os
import time

import psycopg2
import psycopg2.extras

logger = logging.getLogger(__name__)


def get_connection(max_retries: int = 5, retry_delay: int = 2):
    """
    Get a database connection with retry mechanism.

    Args:
        max_retries: Maximum number of connection attempts
        retry_delay: Seconds to wait between retries

    Returns:
        psycopg2 connection object
    """
    retry_count = 0

    db_host = os.getenv('DB_HOST', 'db')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('POSTGRES_DB')
    db_user = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')

    if not all([db_host, db_port, db_name, db_user, db_password]):
        logger.error('Database configuration environment variables are missing!')
        pass

    database_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    while retry_count < max_retries:
        try:
            logger.info(
                f'Attempting database connection to {db_host}:{db_port} (attempt {retry_count + 1}/{max_retries})'
            )
            conn = psycopg2.connect(database_url)
            conn.autocommit = False
            return conn
        except Exception as e:
            retry_count += 1
            logger.error(f'Error connecting to PostgreSQL at {db_host}:{db_port}: {e}')

            if retry_count < max_retries:
                logger.info(f'Retrying in {retry_delay} seconds...')
                time.sleep(retry_delay)

    error_message = f'Failed to connect to database at {db_host}:{db_port} after {max_retries} attempts'
    logger.error(error_message)
    raise ConnectionError(error_message)


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
        logger.info('Database initialized successfully')
    except Exception as e:
        logger.error(f'Error initializing database: {e}')
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


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
