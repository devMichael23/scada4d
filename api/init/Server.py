from core.Core import CoreManager
from core.SCADAVars import SCADAVar
from core.Vars import *


async def initServerStart(core: CoreManager):
    await core.coreCreateServer()
    node = await core.coreAddNode("Room #1")
    return node


async def initCurrentTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "Current_Temp", 50, int64_t, core.getCoreModeRdHis())

    return SCADAVar(var)


async def initHiTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "Hi_Temp", 70, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initHiHiTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "HiHi_Temp", 90, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initLoTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "Lo_Temp", 40, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initLoLoTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "LoLo_Temp", 25, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initIsServerHarmed(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "isServerHarmed", false_t, bool_t, core.getCoreModeRead())

    return SCADAVar(var)


async def initFailureProbability(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "FailureProbability", 10, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initRefrigerantActive(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "RefrigerantActive", false_t, bool_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initIsOnCoolingWithServer(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "IsOnCoolingWithServer", false_t, bool_t, core.getCoreModeRead())

    return SCADAVar(var)
