from server.Imports import *


class SCADAVar:
    def __init__(self, variable):
        self.__variable = variable

    async def getValue(self):
        return await self.__variable.get_value()