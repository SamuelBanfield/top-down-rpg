import websockets
import asyncio

async def receive_message(websocket):
    async for message in websocket:
        print(message)

async def main():
    async with websockets.serve(receive_message, "0.0.0.0", 8000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())