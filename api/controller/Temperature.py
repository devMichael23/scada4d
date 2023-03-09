import asyncio

from core.SCADAVars import SCADAVar
from core.Vars import *

from api.other.Logging import *


async def __changeTemperature(temperature: SCADAVar,
                              value,
                              limitValue,
                              code: str):
    match code:
        case '-':
            while value >= limitValue:
                value -= 1
                apiLogDebug("new temp = " + str(value))
                await temperature.setValue(value)
                await asyncio.sleep(1)
        case '+':
            while value <= limitValue:
                value += 1
                apiLogDebug("new temp = " + str(value))
                await temperature.setValue(value)
                await asyncio.sleep(1)


async def controllerTemperatureIncrease(temperature: SCADAVar, limitValue):
    await __changeTemperature(temperature,
                              await temperature.getValue(),
                              limitValue,
                              code='+')


async def controllerTemperatureReduce(temperature: SCADAVar, limitValue):
    await __changeTemperature(temperature,
                              await temperature.getValue(),
                              limitValue,
                              code='-')


async def controllerTemperatureReduceToLo(serverValues: scadaVars_t, value=0):
    await controllerTemperatureReduce(
        serverValues[idCurrentTemp],
        await serverValues[idLoTemp].getValue() - value
    )


async def controllerTemperatureReduceToLoLo(serverValues: scadaVars_t, value=0):
    await controllerTemperatureReduce(
        serverValues[idCurrentTemp],
        await serverValues[idLoLoTemp].getValue() - value
    )


async def controllerTemperatureIncreaseToHi(serverValues: scadaVars_t, value=0):
    await controllerTemperatureIncrease(
        serverValues[idCurrentTemp],
        await serverValues[idHiTemp].getValue() + value
    )


async def controllerTemperatureIncreaseToHiHi(serverValues: scadaVars_t, value=0):
    await controllerTemperatureIncrease(
        serverValues[idCurrentTemp],
        await serverValues[idHiHiTemp].getValue() + value
    )