import commands


COMMANDS = {
    'mov': commands.set_register,
    'inc': commands.increment_value,
    'dec': commands.decrease_value,
    'jnz': commands.jump_instruction
}


def run_command(command):
    args = command.split()[1:]
    command = command.split()[0]
    try:
        return COMMANDS[command](args)
    except KeyError:
        print(f"{command} is not recognized as an internal command. Run \"help\" for help.")
        return False


def simple_assembler(program):
    register = {}

    for command in program:
        output = run_command(command)
        if output:
            register.update(output)

    return register
