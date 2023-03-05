from imports.General import *


cancelledException_t = asyncio.CancelledError


class TaskManager:
    def __init__(self, task):
        self.__loop = asyncio.get_event_loop()
        self.__task = self.__loop.create_task(task)
        self.__msg = msgNotSetMsg_t

    def cancelTask(self, msg):
        self.__task.cancel()
        self.__msg = msg

    def doneTask(self, msg):
        self.__task.done()
        self.__msg = msg

    def isTaskCanceled(self):
        return self.__task.cancelled()

    def getTask(self):
        return self.__task

    def getMsg(self):
        return self.__msg