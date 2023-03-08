from imports.General import *
import time


async def controllerLoopHarmedServer(task: TaskManager, probability: int, serverHarmedVar: SCADAVar):
    while not checkIsServerHarmedWithProbability(probability):
        print("No")
        await asyncio.sleep(10)
    await task.cancel(msgServerHarmed)
    await serverHarmedVar.setValue(true_t)
    return True