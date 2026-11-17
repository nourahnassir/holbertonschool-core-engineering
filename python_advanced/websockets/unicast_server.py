#!/usr/bin/env python3
"""A WebSocket server implementing unicast communication."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

# Global set to keep track of connected clients
connected_clients = set()


async def unicast_handler(websocket):
    """Handle incoming messages and respond only to the sender with a prefix."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Send response only to the originating connection
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    """Start the unicast WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(unicast_handler, "127.0.0.1", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
