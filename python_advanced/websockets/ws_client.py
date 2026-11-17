#!/usr/bin/env python3
"""A simple WebSocket client."""
import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket server, send text, receive response, and close."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Main entry point to run the client demo."""
    uri = "ws://localhost:8765"
    response = await connect_and_send(uri, "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
