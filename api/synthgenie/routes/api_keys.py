import os

import psycopg2
from fastapi import APIRouter, Depends, HTTPException, Security

from synthgenie.db.connection import get_db
from synthgenie.models.api_key import get_all_api_key_usage, get_api_key_usage, get_user_api_keys
from synthgenie.schemas.api_key import ApiKeyRequest, ApiKeyResponse, ApiKeyUsage, RevokeRequest
from synthgenie.services.auth import get_api_key, register_api_key, revoke_api_key

router = APIRouter(prefix='/api-keys', tags=['api-keys'])


@router.post('/generate', response_model=ApiKeyResponse)
async def create_api_key(
    request: ApiKeyRequest,
    admin_key: str = Security(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
):
    """
    Generate a new API key for a user.
    Only accessible with admin API key.
    """
    # Check if using admin key
    admin_api_key = os.getenv('ADMIN_API_KEY')
    if not admin_api_key or admin_key != admin_api_key:
        raise HTTPException(status_code=403, detail='Only admin can generate API keys')

    api_key = register_api_key(conn, request.user_id)
    return ApiKeyResponse(api_key=api_key, message=f'API key generated for user {request.user_id}')


@router.delete('/revoke', response_model=ApiKeyResponse)
async def delete_api_key(
    request: RevokeRequest,
    admin_key: str = Security(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
):
    """
    Revoke an API key.
    Only accessible with admin API key.
    """
    # Check if using admin key
    admin_api_key = os.getenv('ADMIN_API_KEY')
    if not admin_api_key or admin_key != admin_api_key:
        raise HTTPException(status_code=403, detail='Only admin can revoke API keys')

    if revoke_api_key(conn, request.api_key):
        return ApiKeyResponse(api_key=request.api_key, message='API key successfully revoked')

    raise HTTPException(status_code=404, detail='API key not found')


@router.get('/list/{user_id}', response_model=list[str])
async def list_user_api_keys(
    user_id: str,
    admin_key: str = Security(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
):
    """
    List all API keys for a user.
    Only accessible with admin API key.
    """
    # Check if using admin key
    admin_api_key = os.getenv('ADMIN_API_KEY')
    if not admin_api_key or admin_key != admin_api_key:
        raise HTTPException(status_code=403, detail='Only admin can list API keys')

    api_keys = get_user_api_keys(conn, user_id)
    return [key['key'] for key in api_keys]


@router.get('/usage', response_model=list[ApiKeyUsage])
async def get_all_usage_stats(
    admin_key: str = Security(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
):
    """
    Get usage statistics for all API keys.
    Only accessible with admin API key.
    """
    # Check if using admin key
    admin_api_key = os.getenv('ADMIN_API_KEY')
    if not admin_api_key or admin_key != admin_api_key:
        raise HTTPException(status_code=403, detail='Only admin can view usage statistics')

    return get_all_api_key_usage(conn)


@router.get('/usage/{api_key_value}', response_model=ApiKeyUsage)
async def get_key_usage_stats(
    api_key_value: str,
    current_api_key: str = Security(get_api_key),
    conn: psycopg2.extensions.connection = Depends(get_db),
):
    """
    Get usage statistics for a specific API key.
    Accessible by admin or the owner of the API key.
    """
    admin_api_key = os.getenv('ADMIN_API_KEY')
    is_admin = admin_api_key and current_api_key == admin_api_key
    is_key_owner = current_api_key == api_key_value

    # Allow access if admin or the owner of the API key
    if not (is_admin or is_key_owner):
        raise HTTPException(
            status_code=403,
            detail='You can only view usage statistics for your own API key',
        )

    usage = get_api_key_usage(conn, api_key_value)
    if not usage:
        raise HTTPException(status_code=404, detail='API key not found or no usage data')

    return usage
