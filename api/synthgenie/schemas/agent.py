from pydantic import BaseModel


class SynthGenieResponse(BaseModel):
    used_tool: str
    midi_cc: int
    midi_channel: int
    value: int
