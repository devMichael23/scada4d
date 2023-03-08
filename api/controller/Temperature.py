import asyncio

from core.SCADAVars import SCADAVar
from core.Vars import scadaVars_t


async def __changeTemperature(temperature: SCADAVar,
                              value,
                              limitValue,
                              code: str):
    match code:
        case '-':
            while value >= limitValue:
                value -= 1
                await temperature.setValue(value)
                await asyncio.sleep(1)
        case '+':
            while value <= limitValue:
                value += 1
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


async def controllerTemperatureReduceToLo(serverValues: scadaVars_t):
    await controllerTemperatureReduce(
        serverValues[idCurrentTemp],
        await serverValues[idLoTemp].getValue()
    )


async def controllerTemperatureReduceToLoLo(serverValues: scadaVars_t):
    await controllerTemperatureReduce(
        serverValues[idCurrentTemp],
        await serverValues[idLoLoTemp].getValue()
    )


async def controllerTemperatureIncreaseToHi(serverValues: scadaVars_t):
    await controllerTemperatureIncrease(
        serverValues[idCurrentTemp],
        await serverValues[idHiTemp].getValue()
    )


async def controllerTemperatureIncreaseToHiHi(serverValues: scadaVars_t):
    await controllerTemperatureIncrease(
        serverValues[idCurrentTemp],
        await serverValues[idHiHiTemp].getValue()
    )