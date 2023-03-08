from asyncua import ua


class ModeManager:
    def __init__(self):
        self.__read = [
            (ua.AttributeIds.AccessLevel, ua.AccessLevel.CurrentRead),
            (ua.AttributeIds.UserAccessLevel, ua.AccessLevel.CurrentRead)
        ]
        self.__write = [
            (ua.AttributeIds.AccessLevel, ua.AccessLevel.CurrentWrite),
            (ua.AttributeIds.UserAccessLevel, ua.AccessLevel.CurrentWrite)
        ]
        self.__history = [
            (ua.AttributeIds.AccessLevel, ua.AccessLevel.HistoryRead),
            (ua.AttributeIds.UserAccessLevel, ua.AccessLevel.HistoryRead)
        ]

    def read(self) -> list:
        return self.__read

    def write(self) -> list:
        return self.__write

    def history(self) -> list:
        return self.__history

    def wr(self) -> list:
        return self.read() + self.write()

    def wh(self) -> list:
        return self.write() + self.history()

    def rh(self) -> list:
        return self.read() + self.history()

    def wrh(self) -> list:
        return self.wr() + self.history()