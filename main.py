import asyncio
import logging

from api.init.Server import *
from api.other.Logging import *

from tasks.TaskManager import *

from scenario.General import *


core = CoreManager("opc.tcp://0.0.0.0:1984/", "Server Room")


async def main():
    logging.basicConfig(level=logging.CRITICAL)

    room = await initServerStart(core)

    currentTemp = await initCurrentTemp(core, room)
    hiTemp = await initHiTemp(core, room)
    hiHiTemp = await initHiHiTemp(core, room)
    loTemp = await initLoTemp(core, room)
    loLoTemp = await initLoLoTemp(core, room)
    isServerHarmed = await initIsServerHarmed(core, room)
    failureProbability = await initFailureProbability(core, room)
    refrigerantActive = await initRefrigerantActive(core, room)
    isOnCoolingWithServer = await initIsOnCoolingWithServer(core, room)

    scadaVars = {
        "core": core,
        "currentTemp": currentTemp,
        "hiTemp": hiTemp,
        "hiHiTemp": hiHiTemp,
        "loTemp": loTemp,
        "loLoTemp": loLoTemp,
        "isServerHarmed": isServerHarmed,
        "failureProbability": failureProbability,
        "refrigerantActive": refrigerantActive,
        "isOnCoolingWithServer": isOnCoolingWithServer,
    }

    await core.coreStartHistoryOfVar([currentTemp.getVar()])

    await core.getCoreServer().start()

    await scenarioGeneralStart(scadaVars)

    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
    core.getCoreServer().stop()
