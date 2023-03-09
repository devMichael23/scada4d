from core.Core import CoreManager
from core.SCADAVars import SCADAVar
from core.Vars import *


async def initServerStart(core: CoreManager):
    await core.coreCreateServer()
    node = await core.coreAddNode("Room #1")
    return node


async def initCurrentTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "Current_Temp", valCurrentTemp, int64_t, core.getCoreModeRdHis())

    return SCADAVar(var)


async def initHiTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "Hi_Temp", valHiTemp, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initHiHiTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "HiHi_Temp", valHiHiTemp, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initLoTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "Lo_Temp", valLoTemp, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initLoLoTemp(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "LoLo_Temp", valLoLoTemp, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initIsServerHarmed(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "isServerHarmed", valIsServerHarmed, bool_t, core.getCoreModeRead())

    return SCADAVar(var)


async def initFailureProbability(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "FailureProbability", valFailureProbability, int64_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initRefrigerantActive(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "RefrigerantActive", valRefrigerantActive, bool_t, core.getCoreModeWrRd())

    return SCADAVar(var)


async def initIsOnCoolingWithServer(core: CoreManager, room) -> SCADAVar:
    var = await core.coreAddVariableToObject(
        room, "IsOnCoolingWithServer", valIsOnCoolingWithServer, bool_t, core.getCoreModeRead())

    return SCADAVar(var)
