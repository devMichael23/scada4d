import asyncio

from core.SCADAVars import SCADAVar
from core.Vars import *

from api.controller.Cooling import *
from api.controller.Temperature import *
from api.controller.Harmed import *

from api.other.Logging import *
from api.other.Checkers import *

from tasks.TaskManager import *


async def scenarioOne(scadaVars: scadaVars_t):
    try:
        apiLogInfo("Start increase temp")
        await controllerTemperatureIncreaseToHi(scadaVars, 2)
        apiLogWarning("Temperature is greater than Hi!")

        await controllerCoolingEnable(scadaVars)
        apiLogInfo("Cooling On")

        apiLogInfo("Start reduce temp")
        await controllerTemperatureReduceToLo(scadaVars, 2)
        apiLogWarning("Temperature is less than Lo!")

        await controllerCoolingDisable(scadaVars)
        apiLogInfo("Cooling Off")

        await asyncio.sleep(0)
        apiLogInfo("Scenario 1 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False


async def scenarioTwo(scadaVars: scadaVars_t):
    try:
        await controllerTemperatureIncreaseToHi(scadaVars, 2)
        apiLogWarning("Temperature is greater than Hi!")

        await controllerCoolingEnable(scadaVars)
        apiLogInfo("Cooling On")

        await controllerTemperatureIncreaseToHiHi(scadaVars, 2)
        apiLogWarning("Temperature is greater than HiHi!")

        await controllerTemperatureReduceToLo(scadaVars, 2)
        apiLogWarning("Temperature is less than Lo!")

        await controllerCoolingDisable(scadaVars)
        apiLogInfo("Cooling Off")

        await asyncio.sleep(0)
        apiLogInfo("Scenario 2 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False


async def scenarioThree(scadaVars: scadaVars_t):
    try:
        await controllerTemperatureIncreaseToHi(scadaVars, 2)
        apiLogWarning("Temperature is greater than Hi!")

        await controllerCoolingEnable(scadaVars)
        apiLogInfo("Cooling On")

        await controllerTemperatureIncreaseToHiHi(scadaVars, 2)
        apiLogWarning("Temperature is greater than HiHi!")

        await asyncio.sleep(timeWaitBeforeServerHarmed)
        apiLogWarning("Temperature does not decrease")

        await controllerSetServerHarmed(scadaVars)
        apiLogCritical(msgServerHarmed + " Because it overheated")

        await controllerCoolingDisable(scadaVars)

        await asyncio.sleep(0)
        apiLogInfo("Scenario 3 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False


async def scenarioFour(scadaVars: scadaVars_t):
    try:
        await controllerTemperatureIncreaseToHi(scadaVars, 2)
        apiLogWarning("Temperature is greater than Hi!")

        await controllerCoolingEnable(scadaVars)
        apiLogInfo("Cooling On")

        await controllerTemperatureReduceToLo(scadaVars, 2)
        apiLogWarning("Temperature is less than Lo!")

        await controllerCoolingDisable(scadaVars)
        apiLogInfo("Cooling Off")

        await controllerTemperatureReduceToLoLo(scadaVars, 2)
        apiLogWarning("Temperature is less than LoLo!")

        await controllerTemperatureIncreaseToHi(scadaVars, 2)
        apiLogWarning("Temperature is greater than Hi!")

        await asyncio.sleep(0)
        apiLogInfo("Scenario 4 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False


async def scenarioFive(scadaVars: scadaVars_t):
    try:
        await controllerTemperatureIncreaseToHi(scadaVars, 2)
        apiLogWarning("Temperature is greater than Hi!")

        await controllerCoolingEnable(scadaVars)
        apiLogInfo("Cooling On")

        await controllerTemperatureReduceToLo(scadaVars, 2)
        apiLogWarning("Temperature is less than Lo!")

        await controllerCoolingDisable(scadaVars)
        apiLogInfo("Cooling Off")

        await controllerTemperatureReduceToLoLo(scadaVars, 2)
        apiLogWarning("Temperature is less than LoLo!")

        await asyncio.sleep(timeWaitBeforeServerHarmed)
        apiLogWarning("Temperature does not rise")

        await controllerSetServerHarmed(scadaVars)
        apiLogCritical(msgServerHarmed + " Because it frozen")

        await controllerCoolingDisable(scadaVars)

        await asyncio.sleep(0)
        apiLogInfo("Scenario 5 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False


async def scenarioSix(scadaVars: scadaVars_t):
    try:
        await controllerCoolingEnable(scadaVars)
        apiLogInfo("Cooling On")

        await controllerTemperatureReduceToLo(scadaVars, 2)
        apiLogWarning("Temperature is less than Lo!")

        await controllerCoolingDisable(scadaVars)
        apiLogInfo("Cooling Off")

        await asyncio.sleep(0)
        apiLogInfo("Scenario 6 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False


async def scenarioSeven(scadaVars: scadaVars_t):
    try:
        await controllerCoolingEnable(scadaVars)
        apiLogInfo("Cooling On")

        await controllerTemperatureReduceToLo(scadaVars, 2)
        apiLogWarning("Temperature is less than Lo!")

        await controllerTemperatureReduceToLoLo(scadaVars, 2)
        apiLogWarning("Temperature is less than LoLo!")

        await controllerCoolingDisable(scadaVars)
        apiLogInfo("Cooling Off")

        await asyncio.sleep(0)
        apiLogInfo("Scenario 7 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False


async def scenarioEight(scadaVars: scadaVars_t):
    try:
        await controllerCoolingEnable(scadaVars)
        apiLogInfo("Cooling On")

        await controllerTemperatureReduceToLo(scadaVars, 2)
        apiLogWarning("Temperature is less than Lo!")

        await controllerTemperatureReduceToLoLo(scadaVars, 2)
        apiLogWarning("Temperature is less than LoLo!")

        await asyncio.sleep(timeWaitBeforeServerHarmed)
        apiLogWarning("Temperature does not rise")

        await controllerSetServerHarmed(scadaVars)
        apiLogCritical(msgServerHarmed + " Because it frozen")

        await controllerCoolingDisable(scadaVars)

        await asyncio.sleep(0)
        apiLogInfo("Scenario 8 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False