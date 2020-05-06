from helpers import isint, isinitialized


def ArgumentCountException(function: str, args: int, count: int) -> bool:
    """
    Checks if the correct number of arguments were given to a specific command.
    :param function: The display name given to the function making the call.
    :param args: The number of arguments passed into the command.
    :param count: The expected number of arguments for this command.
    :return: Returns a boolean as a result of the count lookup.
    """
    name = "ArgumentCountException"
    if args != count:
        print(f'{function} {name}: Incorrect Number of Arguments. Expected {count}, got {args}.')
        return False
    return True


def ArgumentTypeException(function: str, *args: tuple) -> bool:
    """
    Checks if the given arguments were given with the correct data types.
    :param function: The display name given to the function making the call.
    :param args: One or more tuples, each should contain a variable and an expected type as string.
    I.e. (variable, 'int')
    :return: Returns a boolean as a result of the type check lookup.
    """
    name = "ArgumentTypeException"
    supported_data_types = {
        'int': isint,
        'alpha': str.isalpha,
    }

    for arg in args:
        try:
            if not supported_data_types[arg[1]](arg[0]):
                print(f'{function} {name}: Provided data type for {arg[0]} is incorrect, expected {arg[1]}.')
                return False
        except KeyError:
            print(f'{function} {name}: Internal error, expected data type is not supported.')
            return False

    return True


def UninitializedRegisterException(function: str, register_dict: dict, *args: str) -> bool:
    """
    Checks if the given registers are initialized.
    :param function: The display name given to the function making the call.
    :param register_dict: The global Register Dict with all current initialized registers.
    :param args: One or more registers to check.
    :return: Returns a boolean as a result initialization lookup.
    """
    name = UninitializedRegisterException.__name__

    for register in args:
        if not isinitialized(register, register_dict):
            print(f'{function} {name}: Register {register} is not initialized.')
            return False

    return True
