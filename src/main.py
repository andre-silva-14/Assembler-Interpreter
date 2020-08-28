import commands
import signal
import sys

__author__ = "André Silva"
__license__ = "MIT"
__version__ = "1.0.2"
__status__ = "Development"
__extension__ = "lu"

COMMANDS = {
    'mov': commands.set_register,
    'inc': commands.increment_value,
    'dec': commands.decrement_value,
    'jnz': commands.jump_instruction,
    'help': commands.help,
    'quit': commands.quit_assembler,
}

REGISTER = {}


def main():
    if len(sys.argv) == 1:
        interactive()
    else:
        program = process_file(sys.argv[1])
        result = compiler(program)
        REGISTER.update(result)
        print(REGISTER)
        input("Press Enter to quit...")



def interactive():
    """
    Starts an interactive enviroment for the user
    to write commands and get instant feedback.
    """
    print(f"Welcome to Assembler Interpreter {__version__}. Run \"help\" for help.")
    # Create a Signal to support Ctrl+C to quit the program.
    signal.signal(signal.SIGINT, COMMANDS['quit'])
    while True:
        output = run_command(input(">> "))
        if output:
            try:
                REGISTER.update(output)
                print(REGISTER)
            except TypeError:
                # Commands that return indexes are meant to be used only on
                # the compiler and not on Interactive mode.
                print("CommandError: Used command is not supported on interactive mode")


def compiler(program: list):
    """
    Compiles a whole multiline program and returns the final result (current Register).
    :param program: The whole multiline commands separated with \n as a string list.
    :return: Returns the final program output.
    """
    REGISTER.clear()
    i = 0
    while i < len(program):
        command = program[i]
        output = run_command(command)
        if output:
            try:
                REGISTER.update(output)
                i += 1
            except TypeError:
                i += output
        else:
            i += 1

    return REGISTER


def run_command(command: str):
    """
    Runs individual commands and returns it's result.
    :param command: The whole command string of input.
    :return: Returns the command output.
    """
    args = command.split()[1:]
    command = command.split()[0]
    try:
        return COMMANDS[command](args, REGISTER)
    except KeyError:
        print(f"{command} is not recognized as an internal command. Run \"help\" for help.")
        return False


def process_file(filename: str):
    from helpers import get_file_extension
    try:
        if get_file_extension(filename) != __extension__:
            raise IOError
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"{filename} was not found in the current directory.")
        return sys.exit(0)
    except IOError:
        print(f"{filename} does not have the correct extension file type. Try example.{__extension__}")
        return sys.exit(0)


if __name__ == "__main__":
    main()
