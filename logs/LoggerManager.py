from core.Vars import *


class LoggerManager:
    def __init__(self, level):
        self.__levels = {
            "info": levelLogInfo_t,
            "debug": levelLogDebug_t,
            "warning": levelLogWarning_t,
            "error": levelLogError_t,
            "critical": levelLogCritical_t
        }
        self.__level = level

    def __getKey(self, value) -> str:
        for key, vals in self.__levels.items():
            if vals == value:
                return key

    def addLevel(self, name: str, level: int):
        for key, vals in self.__levels.items():
            if vals == level:
                return
        self.__levels[name] = level

    def log(self, msg, level: int):
        if self.__level >= level:
            print("[" + self.__getKey(level) + "] "
                  + str(msg))