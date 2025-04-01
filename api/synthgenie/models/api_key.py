from typing import List, Optional, Dict, Any
import secrets
import sqlite3
from datetime import datetime


def create_api_key(conn: sqlite3.Connection, user_id: str) -> Dict[str, Any]:
    """
    Create a new API key for a user.

    Args:
        conn: Database connection
        user_id: User ID to associate with the API key

    Returns:
        Dictionary containing the API key information
    """
    # Generate a secure API key
    api_key_value = secrets.token_urlsafe(32)

    # Create the API key in the database
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO api_keys (key, user_id) VALUES (?, ?)", (api_key_value, user_id)
    )
    conn.commit()

    # Return the API key as a dictionary
    return {
        "key": api_key_value,
        "user_id": user_id,
        "created_at": datetime.now().isoformat(),
    }


def get_api_key(conn: sqlite3.Connection, key: str) -> Optional[Dict[str, Any]]:
    """
    Get an API key by its value.

    Args:
        conn: Database connection
        key: API key value

    Returns:
        The API key information if found, None otherwise
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM api_keys WHERE key = ?", (key,))
    row = cursor.fetchone()
    return dict(row) if row else None


def get_user_api_keys(conn: sqlite3.Connection, user_id: str) -> List[Dict[str, Any]]:
    """
    Get all API keys for a user.

    Args:
        conn: Database connection
        user_id: User ID

    Returns:
        List of API keys for the user
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM api_keys WHERE user_id = ?", (user_id,))
    return [dict(row) for row in cursor.fetchall()]


def delete_api_key(conn: sqlite3.Connection, key: str) -> bool:
    """
    Delete an API key.

    Args:
        conn: Database connection
        key: API key value

    Returns:
        True if the key was deleted, False otherwise
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM api_keys WHERE key = ?", (key,))
    conn.commit()
    return cursor.rowcount > 0
