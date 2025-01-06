import websockets
import asyncio

async def receive_message(websocket):
    for message in websocket:
        print(message)

async def main():
    async with websockets.serve(receive_message, "0.0.0.0", 8001):
        await asyncio.Future()