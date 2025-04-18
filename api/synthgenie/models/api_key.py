from typing import List, Optional, Dict, Any
import secrets
import psycopg2
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def create_api_key(conn, user_id: str) -> Dict[str, Any]:
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
        "INSERT INTO api_keys (key, user_id) VALUES (%s, %s)", (api_key_value, user_id)
    )
    conn.commit()

    # Return the API key as a dictionary
    return {
        "key": api_key_value,
        "user_id": user_id,
        "created_at": datetime.now().isoformat(),
    }


def get_api_key(conn, key: str) -> Optional[Dict[str, Any]]:
    """
    Get an API key by its value.

    Args:
        conn: Database connection
        key: API key value

    Returns:
        The API key information if found, None otherwise
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM api_keys WHERE key = %s", (key,))
    row = cursor.fetchone()
    return row if row else None


def get_user_api_keys(conn, user_id: str) -> List[Dict[str, Any]]:
    """
    Get all API keys for a user.

    Args:
        conn: Database connection
        user_id: User ID

    Returns:
        List of API keys for the user
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM api_keys WHERE user_id = %s", (user_id,))
    return list(cursor.fetchall())


def delete_api_key(conn, key: str) -> bool:
    """
    Delete an API key.

    Args:
        conn: Database connection
        key: API key value

    Returns:
        True if the key was deleted, False otherwise
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM api_keys WHERE key = %s", (key,))
    conn.commit()
    return cursor.rowcount > 0


def track_api_key_usage(conn, key: str) -> None:
    """
    Track usage of an API key by incrementing its request counter.

    Args:
        conn: Database connection
        key: API key value
    """
    cursor = conn.cursor()

    try:
        # Check if key exists in usage table
        cursor.execute("SELECT key FROM api_key_usage WHERE key = %s", (key,))
        exists = cursor.fetchone()

        if exists:
            # Update existing record
            cursor.execute(
                "UPDATE api_key_usage SET request_count = request_count + 1, last_used_at = CURRENT_TIMESTAMP WHERE key = %s",
                (key,),
            )
        else:
            # Insert new record
            cursor.execute(
                "INSERT INTO api_key_usage (key, request_count, last_used_at) VALUES (%s, 1, CURRENT_TIMESTAMP)",
                (key,),
            )

        conn.commit()
    except psycopg2.Error as e:
        # Log error but don't fail the request
        logger.error(f"Error tracking API key usage: {e}")
        conn.rollback()


def get_api_key_usage(conn, key: str) -> Optional[Dict[str, Any]]:
    """
    Get usage statistics for an API key.

    Args:
        conn: Database connection
        key: API key value

    Returns:
        Dictionary with usage statistics if found, None otherwise
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM api_key_usage WHERE key = %s", (key,))
    row = cursor.fetchone()
    return row if row else None


def get_all_api_key_usage(conn) -> List[Dict[str, Any]]:
    """
    Get usage statistics for all API keys.

    Args:
        conn: Database connection

    Returns:
        List of dictionaries with usage statistics
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT a.key, a.user_id, a.created_at, COALESCE(u.request_count, 0) as request_count, u.last_used_at
        FROM api_keys a
        LEFT JOIN api_key_usage u ON a.key = u.key
    """
    )
    return list(cursor.fetchall())
