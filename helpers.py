def isint(val: int) -> bool:
    """
    Check if a given input can be converted to an Integer.
    :param val: Input to check.
    :return: True if value can be converted to an Integer.
    """
    try:
        int(val)
        return True
    except ValueError:
        return False
