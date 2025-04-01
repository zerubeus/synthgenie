import os
from fastapi import HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
import sqlite3

from synthgenie.db.connection import get_db
from synthgenie.db.crud import get_api_key as db_get_api_key
from synthgenie.db.crud import create_api_key as db_create_api_key
from synthgenie.db.crud import delete_api_key as db_delete_api_key

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def get_api_key(
    api_key_header: str = Security(api_key_header),
    conn: sqlite3.Connection = Depends(get_db),
) -> str:
    """
    Validate API key from header.
    """
    if api_key_header is None:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Missing API Key")

    # Check API key against environment variable first (for admin access)
    admin_api_key = os.getenv("ADMIN_API_KEY")
    if admin_api_key and api_key_header == admin_api_key:
        return api_key_header

    # Then check against registered API keys in database
    api_key = db_get_api_key(conn, api_key_header)
    if api_key:
        return api_key_header

    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid API Key")


def register_api_key(conn: sqlite3.Connection, user_id: str) -> str:
    """
    Register a new API key for a user.
    """
    api_key = db_create_api_key(conn, user_id)
    return api_key["key"]


def revoke_api_key(conn: sqlite3.Connection, api_key: str) -> bool:
    """
    Revoke an API key.
    """
    return db_delete_api_key(conn, api_key)
