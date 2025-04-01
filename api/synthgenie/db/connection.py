import sqlite3
import os
import contextlib
from typing import Iterator, Dict, Any

# Create SQLite database connection
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./synthgenie.db")

# Extract the database file path from the URL
if DATABASE_URL.startswith("sqlite:///"):
    if DATABASE_URL == "sqlite:///:memory:":
        DATABASE_PATH = ":memory:"
    else:
        DATABASE_PATH = DATABASE_URL.replace("sqlite:///", "")
else:
    raise ValueError(f"Unsupported database URL: {DATABASE_URL}")


@contextlib.contextmanager
def get_db_connection() -> Iterator[sqlite3.Connection]:
    """Get a database connection."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    try:
        yield conn
    finally:
        conn.close()


def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> Dict[str, Any]:
    """Convert a row to a dictionary."""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def initialize_db():
    """Initialize the database with required tables."""
    with get_db_connection() as conn:
        conn.execute(
            """
        CREATE TABLE IF NOT EXISTS api_keys (
            key TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        )
        conn.commit()


def get_db():
    """Get database connection for dependency injection."""
    with get_db_connection() as conn:
        conn.row_factory = dict_factory
        yield conn
