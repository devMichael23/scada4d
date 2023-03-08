from imports.General import *


cancelledException_t = asyncio.CancelledError


class TaskManager:
    def __init__(self, task):
        self.__loop = asyncio.get_event_loop()
        self.__task = self.__loop.create_task(task)
        self.__msg = msgNotSetMsg_t

    async def cancel(self, msg):
        self.__task.cancel()
        self.__msg = msg

    async def done(self, msg):
        self.__task.done()
        self.__msg = msg

    def isCanceled(self):
        return self.__task.cancelled()

    def getTask(self):
        return self.__task

    def getMsg(self):
        return self.__msg