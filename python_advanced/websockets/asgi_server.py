#!/usr/bin/env python3
"""ASGI WebSocket echo server using Starlette."""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """Serve the homepage with the required heading."""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(websocket):
    """Accept WebSocket connections and echo incoming text messages."""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)