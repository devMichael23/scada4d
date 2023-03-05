from imports.General import *
import time


async def startLoopHarmedServer(task: TaskManager, probability: int):
    while not isServerHarmedWithProbability(probability):
        print("No")
        await asyncio.sleep(10)
    task.cancelTask(serverHarmedMsg_t)
    return True