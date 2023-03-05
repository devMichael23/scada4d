from imports.General import *


class ServerManager:
    def __init__(self):
        self.ID = 0
        self.nodes = dict()
        self.folders = dict()
        self.methods = dict()
        self.server = Server(iserver=None)

    async def createServer(self, host, serverName):
        logging.basicConfig(level=logging.CRITICAL)

        self.server.iserver.history_manager.set_storage(
            HistorySQLite("server/database/server_room.sql")
        )

        await self.server.init()
        await self.server.nodes.server.delete()
        self.server.set_security_policy(NoSecurity)
        self.server.set_endpoint(host)
        self.server.set_server_name(serverName)

        self.ID = await self.server.register_namespace(
            'http://{0}'.format(str(serverName).replace(' ', '_')))

        self.server.default_timeout = 3600000

    async def addNode(self, node):
        self.nodes[node] = await \
            self.server.get_objects_node().add_object(self.ID, node)

        await self.nodes[node].set_attr_bit(
            EventNotifier, SubscribeToEvents)

        return self.nodes[node]

    async def addVariableToObject(self, objectRef, varName, varValue, varType, attributesBits=None):
        if attributesBits is None:
            attributesBits = []

        variable = await objectRef.add_variable(
            self.ID, varName, ua.Variant(varValue, varType))

        for attr, bit in attributesBits:
            await variable.set_attr_bit(attr, bit)

        return variable

    async def startHistoryOfVar(self, listOfVariables):
        for variable in listOfVariables:
            await self.server.historize_node_data_change(
                variable, period=timedelta(minutes=1), count=100
            )