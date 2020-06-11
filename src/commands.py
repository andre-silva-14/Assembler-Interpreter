from exceptions import (ArgumentCountException, ArgumentTypeException,
                        UninitializedRegisterException)


def set_register(args: list, register_copy: dict):
    """
    "mov x y" - Copies y (either a constant value or the content of a register) into register x.
    Register names are alphabetical (letters only). Constants are always integers (positive or negative).
    :param args: Array of arguments passed into this command.
    :param register_copy: Dict with all Initialized registers.
    :return: False if errors are found. Dictionary with created/changed registers and it's values otherwise.
    """
    args_count = 2
    name = "SetRegister"

    if ArgumentCountException(name, len(args), args_count):
        return False

    register, value = args
    # Int is silenced in case user wants to assign a variable to another variable,
    # in that case we do not want the error message to show up.
    if ArgumentTypeException(name, (register, 'alpha'), (value, 'int'), silence=['int',]):
        try:
            value = register_copy[value]
        except KeyError:
            ArgumentTypeException(name, (value, 'int'))
            return False

    return {register: int(value)}


def increment_value(args: list, register_copy: dict):
    """
    "inc x" - Increases the content of the register x by one.
    :param args: Array of arguments passed into this command.
    :param register_copy: Dict with all Initialized registers.
    :return: False if errors are found. Dictionary with created/changed registers and it's values otherwise.
    """
    args_count = 1
    name = "IncrementValue"

    if ArgumentCountException(name, len(args), args_count):
        return False

    register = args[0]
    if UninitializedRegisterException(name, register_copy, register):
        return False

    return {register: register_copy[register] + 1}


def decrement_value(args: list, register_copy: dict):
    """
    "dec x" - Decrements the content of the register x by one.
    :param args: Array of arguments passed into this command.
    :param register_copy: Dict with all Initialized registers.
    :return: False if errors are found. Dictionary with created/changed registers and it's values otherwise.
    """
    args_count = 1
    name = "DecrementValue"

    if ArgumentCountException(name, len(args), args_count):
        return False

    register = args[0]
    if UninitializedRegisterException(name, register_copy, register):
        return False

    return {register: register_copy[register] - 1}


def jump_instruction(args: list, register_copy: dict):
    """
    "jnz x y" - Jumps to an instruction y steps away (positive means forward, negative means backward),
    but only if x (a constant or a register) is not zero
    :param args: Array of arguments passed into this command.
    :param register_copy: Dict with all Initialized registers.
    :return: False if errors are found. Integer with jumps value otherwise.
    """
    args_count = 2
    name = "JumpInstruction"

    if ArgumentCountException(name, len(args), args_count):
        return False

    register, value = args
    if ArgumentTypeException(name, (register, 'alpha'), (value, 'int'), silence=['alpha']):
        try:
            register = int(register)
        except ValueError:
            ArgumentTypeException(name, (register, 'alpha'))
            return False

    elif UninitializedRegisterException(name, register_copy, register):
        return False
    else:
        register = register_copy[register]

    return int(value) if register != 0 else False


def help(args: list, register_copy: dict):
    """
    Help function to guide user.
    :return: List of available commands.
    """
    commands = {
        'mov': "Create a variable. I.e. mov a 5",
        'inc': "Increment variable by 1. I.e. inc a",
        'dec': "Decrement variable by 1. I.e. dec a",
        'jnz': "Jump a specific amount of steps forwards or backwards inside a multi-command call until \
the defined variable is 0. I.e. jnz a -2",
        'quit': "Quit the assembler."
    }

    for command in commands:
        print(f"- {command} : {commands[command]}")


def quit_assembler(args: list, register_copy: dict):
    """
    Quits the program.
    :return: None
    """
    quit()
