from imports.General import *

manager = mng()


async def main():
    room = await serverInitStart(manager)

    currentTemp = await initCurrentTemp(manager, room)
    hiTemp = await initHiTemp(manager, room)
    hiHiTemp = await initHiHiTemp(manager, room)
    loTemp = await initLoTemp(manager, room)
    loLoTemp = await initLoLoTemp(manager, room)
    isServerHarmed = await initIsServerHarmed(manager, room)
    failureProbability = await initFailureProbability(manager, room)
    refrigerantActive = await initRefrigerantActive(manager, room)
    isOnCoolingWithServer = await initIsOnCoolingWithServer(manager, room)

    serverValues = {
        "manager": manager,
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

    await manager.startHistoryOfVar([currentTemp.getVar()])

    await manager.server.start()

    await startScenario()

    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
    manager.server.stop()
