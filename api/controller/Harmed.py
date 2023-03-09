import asyncio

from core.SCADAVars import SCADAVar
from core.Vars import true_t

from tasks.TaskManager import *

from api.other.Checkers import *
from api.other.Logging import *


async def controllerSetServerHarmed(serverHarmedVar: SCADAVar):
    await serverHarmedVar.setValue(true_t)


async def controllerLoopHarmedServer(task: TaskManager, probability: int, serverHarmedVar: SCADAVar):
    try:
        while not checkIsServerHarmedWithProbability(probability):
            apiLogInfo("Server not harmed with " + str(probability) + "%")
            await asyncio.sleep(10)
        await task.cancel(msgServerHarmed)
        await serverHarmedVar.setValue(true_t)
        return True
    except cancelledException_t:
        return False
