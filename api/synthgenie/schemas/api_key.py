from pydantic import BaseModel


class ApiKeyResponse(BaseModel):
    api_key: str
    message: str


class ApiKeyRequest(BaseModel):
    user_id: str


class RevokeRequest(BaseModel):
    api_key: str
