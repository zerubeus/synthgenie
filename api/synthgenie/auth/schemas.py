from datetime import datetime

from pydantic import BaseModel


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
    last_used_at: datetime | None = None
