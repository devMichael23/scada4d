from imports.General import *
import time


async def controllerLoopHarmedServer(task: TaskManager, probability: int):
    while not checkIsServerHarmedWithProbability(probability):
        print("No")
        await asyncio.sleep(10)
    await task.cancel(msgServerHarmed)
    return True