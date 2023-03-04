from server.Imports import *
from server.Manager import Manager as mng
from server.AccessParams import AccessParams as mode


async def serverInitStart(server: mng):
    await server.createServer("opc.tcp://0.0.0.0:4840/", "Server Room")
    node = await server.addNode("Room #1")
    return node

