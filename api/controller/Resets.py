from core.Vars import *
from core.SCADAVars import *


async def controllerResetCurrentTemp(var: SCADAVar):
    await var.setValue(valCurrentTemp)


async def controllerResetIsServerHarmed(var: SCADAVar):
    await var.setValue(valIsServerHarmed)


async def controllerResetRefrigerantActive(var: SCADAVar):
    await var.setValue(valRefrigerantActive)


async def controllerResetAll(scadaVars: scadaVars_t):
    await controllerResetCurrentTemp(scadaVars[idCurrentTemp])
    await controllerResetIsServerHarmed(scadaVars[idIsServerHarmed])
    await controllerResetRefrigerantActive(scadaVars[idRefrigerantActive])
