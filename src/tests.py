from main import compiler
from helpers import get_runtime


def main():
    for index, test in enumerate(TESTS):
        print(f"\n\nStarting Test {index + 1}...")

        program, expected_result, time_limit = test
        assert run_test(program.splitlines(), expected_result, time_limit)


def run_test(program: list, expected: dict, time_limit: int):
    print(f"Expected results: {expected}")
    print(f"Maximum time limit: {f'{time_limit} ms' if time_limit else 'Infinite'}")

    result, runtime = get_runtime(compiler, program)
    print(f"Actual results: {result}")
    print(f"Completed in {runtime} ms.")

    if result == expected and runtime <= time_limit:
        print("\nTest successfully completed!")
        return True
    else:
        print("\nTest Failed!")
        return False


TESTS = [
    # ( Test(str), Expected(dict), Limit Time(int // ms))
    (
        '''\
        trigger error
        mov
        inc
        inc a
        dec
        jnz
        inc ''',
        {},
        2
    ),

    (
        '''\
        mov a 5
        inc a
        dec a
        dec a
        jnz a -1
        inc a''',
        {'a': 1},
        1
    ),

    (
        '''\
        mov c 12
        mov b 0
        mov a 200
        dec a
        inc b
        jnz a -2
        dec c
        mov a b
        jnz c -5
        jnz 0 1
        mov c a''',
        {'a': 409600, 'c': 409600, 'b': 409600},
        2000
    ),
]

if __name__ == "__main__":
    main()
