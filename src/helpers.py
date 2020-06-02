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


def isinitialized(register: str, register_copy: dict) -> bool:
    """
    Check if a given register is already initialized.
    :param register: Register to check.
    :param register_copy: Dictionary of existing registers.
    :return: True if register is already initialized.
    """
    try:
        register_copy[register]
        return True
    except KeyError:
        return False
