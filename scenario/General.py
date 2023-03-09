import asyncio

from core.Vars import *

from api.other.Logging import *
from api.controller.Harmed import *
from api.controller.Resets import *

from scenario.Common import *
from scenario.Scenarios import *

scenarios_d = {
    1: scenarioOne,
    2: scenarioTwo,
    3: scenarioThree,
    4: scenarioFour,
    5: scenarioFive,
    6: scenarioSix,
    7: scenarioSeven,
    8: scenarioEight
}


async def scenarioGeneralStart(scadaVars: scadaVars_t):
    isCoolingOnServer, scenario = await scenarioCommonMenu()

    while True:
        if scenario == 0:
            await controllerResetAll(scadaVars)
        else:
            if isCoolingOnServer:
                await scadaVars[idIsOnCoolingWithServer].setValue(true_t)
            else:
                await scadaVars[idIsOnCoolingWithServer].setValue(false_t)

            scTask = TaskManager(
                scenarios_d[scenario](scadaVars))

            lTask = TaskManager(
                controllerLoopHarmedServer(
                    scTask,
                    await scadaVars[idFailureProbability].getValue(),
                    scadaVars[idIsServerHarmed]
                )
            )

            await scTask.getTask()
            await lTask.cancel()

        isCoolingOnServer, scenario = await scenarioCommonMenu()
