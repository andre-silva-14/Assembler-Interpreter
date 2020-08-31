# Lupey

Lupey is an assembler interpreter built with python which compiles custom commands. With Lupey you can create your own scripts and then compile them or run commands in real-time on the interactive mode.
The main focus in this project at the moment is a robust and clean structure that seamlessly interacts with it's different modules in order to prevent scalling issues for future functionality.

## Getting Started...

Clone the project and run main to initialize the *interactive mode*:

    $ git clone https://github.com/andre-silva-14/lupey.git
    $ cd lupey/src
    $ python main.py

Alternatively, create your own script on a *.lu* file as the example bellow:

```bash
# example.lu
set run 100
set base 2000
inc base
dec run
jnz run -2
```

And then run `python main.py example.lu` to execute the script.

## Commands
A list of the supported commands so far:

- `set x y` - copies `y` (either a constant value or the content of a register) into register `x`.

- `inc x` - increases the content of the register `x` by one.

- `dec x` - decreases the content of the register `x` by one.

- `jnz x y` - jumps to an instruction `y` steps away (positive means forward, negative means backward), but only if `x` (a constant or a register) is not zero. *Not supported on interactive mode*.

- `help x` - will display help documentation. `x` is optional and can be a command or multiple commands. If no `x` is given
`help` will display documentation for all existing commands.

- `quit` or `Ctrl+C` will stop/quit the program.

## How to contribute

If you would like to contribute to the project you are more than welcome to do so:

- Fork the repository and clone your own fork.
- Create a new branch for your feature update:
 `git checkout -b featureUpdate`
- Code and commit your changes: `git commit -m "Feature Update"`
- Push to GitHub: `git push origin featureUpdate`
- Submit your changes for review by opening a pull request with a description about your update.

## Licence

This project is under the MIT license. See [LICENSE](LICENSE) for more details.
