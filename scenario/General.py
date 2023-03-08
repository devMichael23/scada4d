import asyncio

from core.Vars import *

from api.other.Logging import *
from api.controller.Harmed import *

from scenario.Common import *


async def sc_1():
    index = 0
    while True:
        try:
            apiLogDebug(index)
            index += 1
            await asyncio.sleep(1)
        except cancelledException_t:
            break


async def generalScenarioStart(scadaVars: scadaVars_t):
    isCoolingOnServer, scenario = await commonScenarioMenu()

    scTask = TaskManager(sc_1())

    lTask = TaskManager(
        controllerLoopHarmedServer(
            scTask, 40, scadaVars[idIsServerHarmed]
        )
    )

    while not await lTask.getTask():
        await asyncio.sleep(0)

    apiLogCritical(scTask.getMsg() + " " + str(isCoolingOnServer) + " " + str(scenario))