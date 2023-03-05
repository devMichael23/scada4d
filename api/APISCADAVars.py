from api.APIImports import *


class SCADAVar:
    def __init__(self, variable):
        self.__variable = variable

    async def getValue(self):
        return await self.__variable.get_value()

    def getVar(self):
        return self.__variable

    async def setValue(self, value):
        await self.__variable.set_value(value)