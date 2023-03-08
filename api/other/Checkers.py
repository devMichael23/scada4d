from random import randint


def checkIsInt(var) -> bool:
    try:
        int(var)
        return True
    except ValueError:
        return False


def checkIsServerHarmedWithProbability(probability: int) -> bool:
    return randint(0, 100) <= probability