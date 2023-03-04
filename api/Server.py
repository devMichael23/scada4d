from server.Imports import *
from server.Manager import Manager as mng
from server.AccessParams import AccessParams_t as mode
from api.Vars import *
from api.SCADAVars import SCADAVar


async def serverInitStart(server: mng):
    await server.createServer("opc.tcp://0.0.0.0:4840/", "Server Room")
    node = await server.addNode("Room #1")
    return node


async def currentTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(room, "Current_Temp", 50, int64_t, mode.rh())
    return SCADAVar(var)


async def hiTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(room, "Current_Temp", 50, int64_t, mode.wr())
    return SCADAVar(var)


async def hiHiTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(room, "Current_Temp", 50, int64_t, mode.wr())
    return SCADAVar(var)


async def loTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(room, "Current_Temp", 50, int64_t, mode.wr())
    return SCADAVar(var)


async def loLoTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(room, "Current_Temp", 50, int64_t, mode.wr())
    return SCADAVar(var)


async def setupTemp(server: mng, room) -> SCADAVar:
    return await currentTemp(server, room), \
        await hiTemp(server, room), \
        await hiHiTemp(server, room), \
        await loTemp(server, room), \
        await loLoTemp(server, room)