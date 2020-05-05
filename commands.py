from exceptions import check_arg_count
from helpers import isint


def set_register(args):
    args_count = 2
    if not check_arg_count("SetRegister", len(args), args_count):
        return False


def increment_value(args):
    args_count = 1
    if not check_arg_count("IncrementValue", len(args), args_count):
        return False


def decrease_value(args):
    args_count = 1
    if not check_arg_count("DecrementValue", len(args), args_count):
        return False


def jump_instruction(args):
    args_count = 2
    if not check_arg_count("JumpInstruction", len(args), args_count):
        return False
