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

    if not ArgumentCountException(name, len(args), args_count):
        return False

    register = args[0]
    value = args[1]
    if not ArgumentTypeException(name, (register, 'alpha'), (value, 'int')):
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

    if not ArgumentCountException(name, len(args), args_count):
        return False

    register = args[0]
    if not UninitializedRegisterException(name, register_copy, register):
        return False

    return {register: register_copy[register] + 1}


def decrease_value(args, register_copy: dict):
    """
    "dec x" - Decreases the content of the register x by one.
    :param args: Array of arguments passed into this command.
    :param register_copy: Dict with all Initialized registers.
    :return: False if errors are found. Dictionary with created/changed registers and it's values otherwise.
    """
    args_count = 1
    name = "DecrementValue"
    if not ArgumentCountException(name, len(args), args_count):
        return False

    register = args[0]
    if not UninitializedRegisterException(name, register_copy, register):
        return False

    return {register: register_copy[register] - 1}


def jump_instruction(args, register_copy: dict):
    args_count = 2
    name = "JumpInstruction"
    if not ArgumentCountException(name, len(args), args_count):
        return False
