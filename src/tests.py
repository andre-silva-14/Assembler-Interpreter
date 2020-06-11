from main import compiler
import time


def main():
    for index, test in enumerate(TESTS):
        print(f"\n\nStarting Test {index + 1}...")

        program, expected_result = test
        assert run_test(program.splitlines(), expected_result)


def run_test(program: list, expected: dict):
    start = time.time()
    result = compiler(program)
    end = time.time()
    runtime = round((end - start)* 1000)

    if result == expected:
        print(f"Completed in {runtime} ms.")
        print("Test completed successfully!")
        return True
    else:
        print(f"Completed in {runtime} ms.")
        print("Test Failed!")
        return False


TESTS = [

    (
        '''\
        trigger error
        mov
        inc
        inc a
        dec
        jnz
        inc ''',
        {}
    ),

    (
        '''\
        mov a 5
        inc a
        dec a
        dec a
        jnz a -1
        inc a''',
        {'a': 1}
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
        {'a': 409600, 'c': 409600, 'b': 409600}
    ),
]

if __name__ == "__main__":
    main()
