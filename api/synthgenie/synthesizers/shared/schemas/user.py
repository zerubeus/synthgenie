from pydantic import BaseModel


class UserPrompt(BaseModel):
    prompt: str
