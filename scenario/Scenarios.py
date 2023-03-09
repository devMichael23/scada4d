import asyncio

from core.SCADAVars import SCADAVar
from core.Vars import *

from api.controller.Cooling import *
from api.controller.Temperature import *

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
        apiLogInfo("CoolingOff")

        await asyncio.sleep(0)
        apiLogInfo("Scenario 1 done success")

        return True
    except cancelledException_t:
        apiLogCritical(msgServerHarmed)
        return False