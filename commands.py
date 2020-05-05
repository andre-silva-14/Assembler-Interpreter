from exceptions import ArgumentCountException, ArgumentTypeException


def set_register(args):
    """
    "mov x y" Copies y (either a constant value or the content of a register) into register x.
    Register names are alphabetical (letters only). Constants are always integers (positive or negative).
    :param args: Array of arguments passed into this command.
    :return: False if errors are found. Dictionary with created/changed registers and it's values.
    """
    args_count = 2
    name = "SetRegister"

    if not ArgumentCountException(name, len(args), args_count):
        return False

    register = args[0]
    value = args[1]
    if not ArgumentTypeException(name, (register, 'alpha'), (value, 'int')):
        return False

    return {register: value}


def increment_value(args):
    args_count = 1
    if not ArgumentCountException("IncrementValue", len(args), args_count):
        return False


def decrease_value(args):
    args_count = 1
    if not ArgumentCountException("DecrementValue", len(args), args_count):
        return False


def jump_instruction(args):
    args_count = 2
    if not ArgumentCountException("JumpInstruction", len(args), args_count):
        return False
