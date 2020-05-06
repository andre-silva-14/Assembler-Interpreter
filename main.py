import commands


COMMANDS = {
    'mov': commands.set_register,
    'inc': commands.increment_value,
    'dec': commands.decrease_value,
    'jnz': commands.jump_instruction
}

REGISTER = {}


def run_command(command):
    args = command.split()[1:]
    command = command.split()[0]
    register_copy = REGISTER
    try:
        return COMMANDS[command](args, register_copy)
    except KeyError:
        print(f"{command} is not recognized as an internal command. Run \"help\" for help.")
        return False


def simple_assembler(program):
    i = 0
    while i < len(program):
        command = program[i]
        output = run_command(command)
        if output:
            try:
                REGISTER.update(output)
                i += 1
            except ValueError:
                i += output
        else:
            i += 1

    return REGISTER


if __name__ == "__main__":
    while True:
        output = run_command(input(">> "))
        if output:
            REGISTER.update(output)
            print(REGISTER)
