from imports.General import *


async def initServerStart(serverManager: mng):
    await serverManager.createServer("opc.tcp://0.0.0.0:1984/", "Server Room")
    node = await serverManager.addNode("Room #1")
    return node


async def initCurrentTemp(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "Current_Temp", 50, int64_t, mode.rh())

    return SCADAVar(var)


async def initHiTemp(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "Hi_Temp", 70, int64_t, mode.wr())

    return SCADAVar(var)


async def initHiHiTemp(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "HiHi_Temp", 90, int64_t, mode.wr())

    return SCADAVar(var)


async def initLoTemp(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "Lo_Temp", 40, int64_t, mode.wr())

    return SCADAVar(var)


async def initLoLoTemp(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "LoLo_Temp", 25, int64_t, mode.wr())

    return SCADAVar(var)


async def initIsServerHarmed(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "isServerHarmed", false_t, bool_t, mode.read())

    return SCADAVar(var)


async def initFailureProbability(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "FailureProbability", 10, int64_t, mode.wr())

    return SCADAVar(var)


async def initRefrigerantActive(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "RefrigerantActive", false_t, bool_t, mode.wr())

    return SCADAVar(var)


async def initIsOnCoolingWithServer(serverManager: mng, room) -> SCADAVar:
    var = await serverManager.addVariableToObject(
        room, "IsOnCoolingWithServer", false_t, bool_t, mode.read())

    return SCADAVar(var)
