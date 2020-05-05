def check_arg_count(function: str, args: int, count: int) -> bool:
    """
    Checks if the correct number of arguments were given to a specific command.
    :param function: The display name given to the function making the call.
    :param args: The number of arguments passed into the command.
    :param count: The expected number of arguments for this command.
    :return: Returns a boolean as a result of the count lookup.
    """
    name = "ArgumentError"
    if args != count:
        print(f'{function} {name}: Incorrect Number of Arguments. Expected {count}, got {args}.')
        return False
    return True
