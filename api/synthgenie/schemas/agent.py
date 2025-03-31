from pydantic import BaseModel


class AgentResponse(BaseModel):
    response: str
    token_usage: int


class ToolCallResult(BaseModel):
    client_id: str
    tool_call_id: str
    result: dict[str, any]
