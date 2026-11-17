#!/usr/bin/env python3
"""A WebSocket server with message validation."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def validation_handler(websocket):
    """Validate incoming messages and respond accordingly."""
    try:
        async for message in websocket:
            # Check if message is empty after stripping whitespace
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        # Handle client disconnection gracefully
        pass


async def main():
    """Start the validation WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(validation_handler, "127.0.0.1", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
