import asyncio

from core.Vars import *

from api.other.Logging import *
from api.controller.Harmed import *

from scenario.Common import *


def serverHarmedFunc(task: asyncio.Task):
    result = task.result()
    apiLogCritical(result.getMsg())


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

    lTask.addCallBack(serverHarmedFunc)