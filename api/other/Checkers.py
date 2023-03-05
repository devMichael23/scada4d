from random import randint


def isInt(var) -> bool:
    try:
        int(var)
        return True
    except ValueError:
        return False


def isServerHarmedWithProbability(probability: int) -> bool:
    return randint(0, 100) <= probability