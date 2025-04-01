from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ApiKeyResponse(BaseModel):
    api_key: str
    message: str


class ApiKeyRequest(BaseModel):
    user_id: str


class RevokeRequest(BaseModel):
    api_key: str


class ApiKeyUsage(BaseModel):
    key: str
    request_count: int
    last_used_at: Optional[datetime] = None
