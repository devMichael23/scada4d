from asyncua import Server, ua
from asyncua.server.history_sql import HistorySQLite
from datetime import timedelta
import asyncio

from core.Vars import *
from core.Logger import *
from core.Modes import ModeManager


class CoreManager:
    def __init__(self, host, name):
        self.__ID = 0
        self.__host = host
        self.__name = name
        self.__coreNodes = dict()
        self.__coreServer = Server(iserver=None)
        self.__modes = ModeManager()

    async def coreCreateServer(self):
        self.__coreServer.iserver.history_manager.set_storage(
            HistorySQLite("core/database/server_room.sql")
        )

        await self.__coreServer.init()
        await self.__coreServer.nodes.server.delete()

        self.__coreServer.set_security_policy(varNoSecurity)
        self.__coreServer.set_endpoint(self.__host)
        self.__coreServer.set_server_name(self.__name)

        self.__ID = await self.__coreServer.register_namespace(
            'http://{0}'.format(str(self.__name).replace(' ', '_'))
        )

        self.__coreServer.default_timeout = 3600000

    async def coreAddNode(self, node):
        self.__coreNodes[node] = await \
            self.__coreServer.get_objects_node().add_object(self.__ID, node)

        await self.__coreNodes[node].set_attr_bit(
            varEventNotifier, varSubscribeToEvents
        )

        return self.__coreNodes[node]

    async def coreAddVariableToObject(self, objectRef, varName, varValue, varType, attributesBits=None):
        if attributesBits is None:
            attributesBits = []

        variable = await objectRef.add_variable(
            self.__ID, varName, ua.Variant(varValue, varType)
        )

        for attr, bit in attributesBits:
            await variable.set_attr_bit(attr, bit)

        return variable

    async def coreStartHistoryOfVar(self, listOfVariables):
        for variable in listOfVariables:
            await self.__coreServer.historize_node_data_change(
                variable, period=timedelta(minutes=1), count=100
            )

    def getCoreServer(self):
        return self.__coreServer

    def getCoreModeWrite(self):
        return self.__modes.write()

    def getCoreModeRead(self):
        return self.__modes.read()

    def getCoreModeHistory(self):
        return self.__modes.history()

    def getCoreModeWrRd(self):
        return self.__modes.wr()

    def getCoreModeWrHis(self):
        return self.__modes.wh()

    def getCoreModeRdHis(self):
        return self.__modes.rh()

    def getCoreModeWrRdHis(self):
        return self.__modes.wrh()