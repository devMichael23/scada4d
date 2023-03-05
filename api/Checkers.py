def isInt(var) -> bool:
    try:
        int(var)
        return True
    except ValueError:
        return False