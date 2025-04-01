import os
import sqlite3
from fastapi import APIRouter, HTTPException, Security, Depends
from pydantic import BaseModel

from synthgenie.auth.api_key import get_api_key, register_api_key, revoke_api_key
from synthgenie.db.connection import get_db
from synthgenie.db.crud import get_user_api_keys

router = APIRouter(prefix="/api-keys", tags=["api-keys"])


class ApiKeyResponse(BaseModel):
    api_key: str
    message: str


class ApiKeyRequest(BaseModel):
    user_id: str


class RevokeRequest(BaseModel):
    api_key: str


@router.post("/generate", response_model=ApiKeyResponse)
async def create_api_key(
    request: ApiKeyRequest,
    admin_key: str = Security(get_api_key),
    conn: sqlite3.Connection = Depends(get_db),
):
    """
    Generate a new API key for a user.
    Only accessible with admin API key.
    """
    # Check if using admin key
    admin_api_key = os.getenv("ADMIN_API_KEY")
    if not admin_api_key or admin_key != admin_api_key:
        raise HTTPException(status_code=403, detail="Only admin can generate API keys")

    api_key = register_api_key(conn, request.user_id)
    return ApiKeyResponse(
        api_key=api_key, message=f"API key generated for user {request.user_id}"
    )


@router.delete("/revoke", response_model=ApiKeyResponse)
async def delete_api_key(
    request: RevokeRequest,
    admin_key: str = Security(get_api_key),
    conn: sqlite3.Connection = Depends(get_db),
):
    """
    Revoke an API key.
    Only accessible with admin API key.
    """
    # Check if using admin key
    admin_api_key = os.getenv("ADMIN_API_KEY")
    if not admin_api_key or admin_key != admin_api_key:
        raise HTTPException(status_code=403, detail="Only admin can revoke API keys")

    if revoke_api_key(conn, request.api_key):
        return ApiKeyResponse(
            api_key=request.api_key, message="API key successfully revoked"
        )

    raise HTTPException(status_code=404, detail="API key not found")


@router.get("/list/{user_id}", response_model=list[str])
async def list_user_api_keys(
    user_id: str,
    admin_key: str = Security(get_api_key),
    conn: sqlite3.Connection = Depends(get_db),
):
    """
    List all API keys for a user.
    Only accessible with admin API key.
    """
    # Check if using admin key
    admin_api_key = os.getenv("ADMIN_API_KEY")
    if not admin_api_key or admin_key != admin_api_key:
        raise HTTPException(status_code=403, detail="Only admin can list API keys")

    api_keys = get_user_api_keys(conn, user_id)
    return [key["key"] for key in api_keys]
