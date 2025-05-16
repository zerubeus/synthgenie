import os

from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from psycopg2.extensions import connection as PgConnection
from starlette.status import HTTP_403_FORBIDDEN

from synthgenie.db.connection import get_db
from synthgenie.models.api_key import create_api_key, delete_api_key, get_api_key_from_db

API_KEY_NAME = 'X-API-Key'
_api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def get_api_key(
    api_key_header: str | None = Security(_api_key_header),
    conn: PgConnection = Depends(get_db),
) -> str:
    """
    Validate API key from header.
    """
    if api_key_header is None:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail='Missing API Key')

    # Check API key against environment variable first (for admin access)
    admin_api_key = os.getenv('ADMIN_API_KEY')
    if admin_api_key and api_key_header == admin_api_key:
        return api_key_header

    # Then check against registered API keys in database
    api_key_data = get_api_key_from_db(conn, api_key_header)
    if api_key_data:
        return api_key_header

    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail='Invalid API Key')


def register_api_key(conn: PgConnection, user_id: str) -> str:
    """
    Register a new API key for a user.
    """
    api_key = create_api_key(conn, user_id)
    return api_key['key']


def revoke_api_key(conn: PgConnection, api_key: str) -> bool:
    """
    Revoke an API key.
    """
    return delete_api_key(conn, api_key)
