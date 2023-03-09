from core.Vars import *
from core.SCADAVars import *


async def __controllerCoolingChange(refrigerantActive: SCADAVar,
                                    isCoolingOnServer: bool,
                                    value):
    if isCoolingOnServer:
        await refrigerantActive.setValue(value)
    else:
        return await refrigerantActive.getValue()


async def controllerCoolingEnable(scadaVars: scadaVars_t):
    await __controllerCoolingChange(scadaVars[idRefrigerantActive],
                                    await scadaVars[idIsOnCoolingWithServer].getValue(),
                                    true_t)


async def controllerCoolingDisable(scadaVars: scadaVars_t):
    await __controllerCoolingChange(scadaVars[idRefrigerantActive],
                                    await scadaVars[idIsOnCoolingWithServer].getValue(),
                                    false_t)