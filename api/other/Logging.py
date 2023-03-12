from logs.LoggerManager import *


__apiLoggerManager = LoggerManager(levelLogAll_t)

msgServerHarmed = "Server is harmed!"
msgTaskNoCancel = "Task not canceled"
msgTaskNotWorkWithoutScenario = "This task dont work without scenario"
msgNotSet = "Msg is not set"


def apiLogInfo(msg):
    __apiLoggerManager.log(msg, levelLogInfo_t)


def apiLogDebug(msg):
    __apiLoggerManager.log(msg, levelLogDebug_t)


def apiLogWarning(msg):
    __apiLoggerManager.log(msg, levelLogWarning_t)


def apiLogError(msg):
    __apiLoggerManager.log(msg, levelLogError_t)


def apiLogCritical(msg):
    __apiLoggerManager.log(msg, levelLogCritical_t)