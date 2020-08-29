from main import compiler, process_file
from helpers import get_runtime, build_test_path


def main():
    for index, test in enumerate(TESTS):
        print(f"\n\nStarting Test {index + 1}...")

        program, result, timeout = test.values()
        assert run_test(process_file(program), result, timeout)


def run_test(program: list, expected: dict, timeout: int):
    print(f"Expected results: {expected}")
    print(f"Maximum time limit: {f'{timeout} ms' if timeout else 'Infinite'}")

    result, runtime = get_runtime(compiler, program)
    print(f"Actual results: {result}")
    print(f"Completed in {runtime} ms.")

    if result == expected and runtime <= timeout:
        print("\nTest successfully completed!")
        return True
    else:
        print("\nTest Failed!")
        return False


TESTS = [
    # Timeout (ms)
    {
        'test': build_test_path('test_1.lu'),
        'result': {},
        'timeout': 2
    },

    {
        'test': build_test_path('test_2.lu'),
        'result': {'a': 1},
        'timeout': 1
    },

    {
        'test': build_test_path('test_3.lu'),
        'result': {'a': 409600, 'c': 409600, 'b': 409600},
        'timeout': 4500
    },
]

if __name__ == "__main__":
    main()
