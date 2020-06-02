import commands


COMMANDS = {
    'mov': commands.set_register,
    'inc': commands.increment_value,
    'dec': commands.decrease_value,
    'jnz': commands.jump_instruction,
    'help': commands.help,
    'quit': commands.quit_assembler,
}

REGISTER = {}


def run_command(command):
    args = command.split()[1:]
    command = command.split()[0]
    try:
        return COMMANDS[command](args, REGISTER)
    except KeyError:
        print(f"{command} is not recognized as an internal command. Run \"help\" for help.")
        return False


def simple_assembler(program):
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
    while True:
        output = run_command(input(">> "))
        if output:
            try:
                REGISTER.update(output)
                print(REGISTER)
            except TypeError:
                pass
