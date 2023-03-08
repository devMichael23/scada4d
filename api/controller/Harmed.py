import asyncio

from core.SCADAVars import SCADAVar
from core.Vars import true_t

from tasks.TaskManager import *

from api.other.Checkers import *
from api.other.Logging import *


async def controllerLoopHarmedServer(task: TaskManager, probability: int, serverHarmedVar: SCADAVar):
    while not checkIsServerHarmedWithProbability(probability):
        apiLogInfo("No")
        await asyncio.sleep(10)
    await task.cancel(msgServerHarmed)
    await serverHarmedVar.setValue(true_t)
    return True