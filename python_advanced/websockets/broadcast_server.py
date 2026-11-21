#!/usr/bin/env python3
"""WebSocket broadcast server."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

HOST = "127.0.0.1"
PORT = 8765

CONNECTED_CLIENTS = set()


async def broadcast(message):
    """Send a prefixed message to all currently connected clients."""
    if not CONNECTED_CLIENTS:
        return

    formatted_message = f"B:{message}"
    clients_snapshot = list(CONNECTED_CLIENTS)

    for client in clients_snapshot:
        if client in CONNECTED_CLIENTS:
            try:
                await client.send(formatted_message)
            except ConnectionClosed:
                CONNECTED_CLIENTS.discard(client)


async def handle_client(websocket):
    """Register a client, relay incoming messages, and clean up on exit."""
    CONNECTED_CLIENTS.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        CONNECTED_CLIENTS.discard(websocket)


async def main():
    """Start the WebSocket broadcast server."""
    async with websockets.serve(handle_client, HOST, PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
