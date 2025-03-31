# Connection manager for WebSockets
import asyncio
import json
from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}
        self.pending_tool_calls: dict[str, asyncio.Future] = {}

    async def connect(self, client_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    async def send_message(self, client_id: str, message: any):
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(json.dumps(message))

    def create_pending_tool_call(self, call_id: str) -> asyncio.Future:
        future = asyncio.Future()
        self.pending_tool_calls[call_id] = future
        return future

    def resolve_tool_call(self, call_id: str, result: any):
        if call_id in self.pending_tool_calls:
            future = self.pending_tool_calls.pop(call_id)
            if not future.done():
                future.set_result(result)
