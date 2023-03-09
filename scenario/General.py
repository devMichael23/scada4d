import asyncio

from core.Vars import *

from api.other.Logging import *
from api.controller.Harmed import *

from scenario.Common import *


def serverHarmedFunc(task: asyncio.Task):
    result = task.result()
    apiLogCritical(result.getMsg())


async def sc_1(scadaVars: scadaVars_t):
    index = 0
    while True:
        try:
            apiLogDebug(index)
            index += 1
            await asyncio.sleep(1)
        except cancelledException_t:
            return scadaVars


async def generalScenarioStart(scadaVars: scadaVars_t):
    isCoolingOnServer, scenario = await commonScenarioMenu()
    while scenario != 'x':
        scTask = TaskManager(sc_1(scadaVars))

        lTask = TaskManager(
            controllerLoopHarmedServer(
                scTask, 40, scadaVars[idIsServerHarmed]
            )
        )
        lTask.addCallBack(serverHarmedFunc)

        await lTask.getTask()

        isCoolingOnServer, scenario = await commonScenarioMenu()

    exit(0)