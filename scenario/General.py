import asyncio

from imports.General import *
from scenario.Common import *
import time


async def sc_1():
    index = 0
    while True:
        try:
            print(index)
            index += 1
            await asyncio.sleep(1)
        except cancelledException_t:
            break


async def generalScenarioStart():
    isCoolingOnServer, scenario = await commonScenarioMenu()

    scTask = TaskManager(sc_1())
    lTask = TaskManager(controllerLoopHarmedServer(scTask, 10))

    while not await lTask.getTask():
        await asyncio.sleep(0)

    print(scTask.getMsg(), isCoolingOnServer, scenario)