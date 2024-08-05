import asyncio
import time
from websockets.server import serve
import mouse
from src.common.funcs import read_conf

async def read_mouse(websocket):
    """Read mouse and send info with websocket"""
    while True:
        position = str(mouse.get_position())
        await websocket.send(position)
        await asyncio.sleep(0.4)
        time.sleep(0.4)

async def serve_socket(port:int = 1916, ip:str = "127.0.0.1"):
    """Connect and serve websocke"""
    conf = read_conf()
    ip = conf["websockets"]["mousemove"]["ip"]
    port = conf["websockets"]["mousemove"]["port"]
    async with serve(read_mouse, ip, port):
        await asyncio.Future()  # run forever

