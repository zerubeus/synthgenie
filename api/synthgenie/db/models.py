"""
Database models and helper functions.
"""

from uuid import uuid4
from typing import Dict, Any


def generate_uuid() -> str:
    """Generate a UUID string."""
    return str(uuid4())


def format_api_key(row: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format an API key row from the database.

    Args:
        row: Database row as dictionary

    Returns:
        Formatted API key information
    """
    if not row:
        return None

    return {
        "key": row["key"],
        "user_id": row["user_id"],
        "created_at": row["created_at"],
    }
