from server.Imports import *
from server.Manager import Manager as mng
from server.AccessParams import AccessParams_t as mode
from api.Vars import *
from api.SCADAVars import SCADAVar


async def serverInitStart(server: mng):
    await server.createServer("opc.tcp://0.0.0.0:4840/", "Server Room")
    node = await server.addNode("Room #1")
    return node


async def initCurrentTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "Current_Temp", 50, int64_t, mode.rh())

    return SCADAVar(var)


async def initHiTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "Hi_Temp", 70, int64_t, mode.wr())

    return SCADAVar(var)


async def initHiHiTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "HiHi_Temp", 90, int64_t, mode.wr())

    return SCADAVar(var)


async def initLoTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "Lo_Temp", 40, int64_t, mode.wr())

    return SCADAVar(var)


async def initLoLoTemp(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "LoLo_Temp", 25, int64_t, mode.wr())

    return SCADAVar(var)


async def initIsServerHarmed(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "isServerHarmed", false_t, bool_t, mode.read())

    return SCADAVar(var)


async def initFailureProbability(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "FailureProbability", 10, int64_t, mode.wr())

    return SCADAVar(var)


async def initRefrigerantActive(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "RefrigerantActive", false_t, bool_t, mode.wr())

    return SCADAVar(var)


async def initIsOnCoolingWithServer(server: mng, room) -> SCADAVar:
    var = await server.addVariableToObject(
        room, "IsOnCoolingWithServer", false_t, bool_t, mode.read())

    return SCADAVar(var)
