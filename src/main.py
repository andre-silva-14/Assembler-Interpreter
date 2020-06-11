import commands


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
    """
    Starts an interactive enviroment for the user
    to write commands and get instant feedback.
    """
    while True:
        output = run_command(input(">> "))
        if output:
            try:
                REGISTER.update(output)
                print(REGISTER)
            except TypeError:
                # Commands that return indexes are meant to be used on compiler
                # scripts so they will be ignored in interactive mode.
                pass


def run_command(command):
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


def compiler(program):
    """
    Compiles a whole multiline program and returns the final result.
    :param program: The whole multiline commands separated with \n as a single string.
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


if __name__ == "__main__":
    main()
