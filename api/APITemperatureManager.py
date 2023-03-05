from api.APIImports import *


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


async def increaseTemperature(temperature: SCADAVar, limitValue):
    await __changeTemperature(temperature,
                              await temperature.getValue(),
                              limitValue,
                              code='+')


async def reduceTemperature(temperature: SCADAVar, limitValue):
    await __changeTemperature(temperature,
                              await temperature.getValue(),
                              limitValue,
                              code='-')


async def increaseTemperatureToLo(serverValues: serverValues_t):
    await reduceTemperature(
        serverValues[currentTemp_d],
        await serverValues[loTemp_d].getValue()
    )


async def increaseTemperatureToLoLo(serverValues: serverValues_t):
    await reduceTemperature(
        serverValues[currentTemp_d],
        await serverValues[loLoTemp_d].getValue()
    )


async def increaseTemperatureToHi(serverValues: serverValues_t):
    await reduceTemperature(
        serverValues[currentTemp_d],
        await serverValues[hiTemp_d].getValue()
    )


async def increaseTemperatureToHiHi(serverValues: serverValues_t):
    await reduceTemperature(
        serverValues[currentTemp_d],
        await serverValues[hiHiTemp_d].getValue()
    )