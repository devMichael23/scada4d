from core.Vars import *
from core.SCADAVars import *


async def controllerResetCurrentTemp(var: SCADAVar):
    await var.setValue(valCurrentTemp)


async def controllerResetHiTemp(var: SCADAVar):
    await var.setValue(valHiTemp)


async def controllerResetHiHiTemp(var: SCADAVar):
    await var.setValue(valHiHiTemp)


async def controllerResetLoTemp(var: SCADAVar):
    await var.setValue(valLoTemp)


async def controllerResetLoLoTemp(var: SCADAVar):
    await var.setValue(valLoLoTemp)


async def controllerResetIsServerHarmed(var: SCADAVar):
    await var.setValue(valIsServerHarmed)


async def controllerResetFailureProbability(var: SCADAVar):
    await var.setValue(valFailureProbability)


async def controllerResetRefrigerantActive(var: SCADAVar):
    await var.setValue(valRefrigerantActive)


async def controllerResetIsOnCoolingWithServer(var: SCADAVar):
    await var.setValue(idIsOnCoolingWithServer)


async def controllerResetAll(scadaVars: scadaVars_t):
    await controllerResetCurrentTemp(scadaVars[idCurrentTemp])
    await controllerResetHiTemp(scadaVars[idHiTemp])
    await controllerResetHiHiTemp(scadaVars[idHiHiTemp])
    await controllerResetLoTemp(scadaVars[idLoTemp])
    await controllerResetLoLoTemp(scadaVars[idLoLoTemp])
    await controllerResetIsServerHarmed(scadaVars[idIsServerHarmed])
    await controllerResetFailureProbability(scadaVars[idFailureProbability])
    await controllerResetRefrigerantActive(scadaVars[idRefrigerantActive])
    await controllerResetIsOnCoolingWithServer(scadaVars[idIsOnCoolingWithServer])

