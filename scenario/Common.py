from api.Imports import *
from api.Vars import *
from api.SCADAVars import SCADAVar
from api.Checkers import *


def __showScenarios():
    print("==Menu==")
    print("Select № of scenario")
    print("========")
    print("? - Show this page again")
    print("0 - Reset params")
    print()

    print("№1 - Temp > Hi; Cooling On; Temp < Lo; Cooling Off")
    print("№2 - Temp > Hi; Cooling On; Temp > HiHi; Temp < Lo; Cooling Off")
    print("№3 - Temp > Hi; Cooling On; Temp > HiHi; Server Harmed")
    print("№4 - Temp > Hi; Cooling not On; Temp > HiHi; Server Harmed")

    print("№5 - Temp > Hi; Cooling On; Temp < Lo; Cooling not Off; Temp < LoLo; Cooling Off")
    print("№6 - Temp > Hi; Cooling On; Temp < Lo; Cooling not Off; Temp < LoLo; Server Harmed")
    print()

    print("№7 - Temp = normal; Cooling On; Temp < Lo; Cooling Off; (Only CC on server)")
    print("№8 - Temp = normal; Cooling On; Temp < Lo; Cooling not Off; Temp < LoLo; Cooling Off; (Only CC on server)")
    print("№9 - Temp = normal; Cooling On; Temp < Lo; Cooling not Off; Temp < LoLo; Server Harmed; (Only CC on server)")


def __checkIntChoice(bool_var: bool, int_var: int) -> bool:
    if 0 <= int(int_var) < 10:
        if (not bool_var) and (int(int_var) >= 7):
            print("Error. CC not on Server Side, but this scenario can start only if CC on Server Side. Try Again")
            return False
        else:
            return True
    else:
        print("Error. Try again")
        return False


def __getIsCoolingOnServer() -> bool:
    print("Is Cooling Control on server side? (Y/N)")
    while True:
        print()
        choice = input("> ")
        match choice:
            case 'Y':
                print()
                return True
            case 'N':
                print()
                return False
            case _:
                print("Error. Try again")


def __getScenario(isCoolingOnServerVar: bool) -> int:
    __showScenarios()
    while True:
        print()
        choice = input("> ")

        if isInt(choice):
            if __checkIntChoice(isCoolingOnServerVar, int(choice)):
                return int(choice)
        else:
            match choice:
                case '?':
                    print()
                    __showScenarios()
                case _:
                    print("Error. Try again")


def showMenu() -> (bool, int):
    isCoolingOnServerVar = __getIsCoolingOnServer()
    scenarioVar = __getScenario(isCoolingOnServerVar)

    return isCoolingOnServerVar, scenarioVar