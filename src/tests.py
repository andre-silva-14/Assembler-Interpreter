from main import compiler, process_file
from helpers import get_runtime, build_test_path


def main():
    for index, test in enumerate(TESTS):
        print(f"\n\nStarting Test {index + 1}...")

        program, expected_result, time_limit = test
        assert run_test(process_file(program), expected_result, time_limit)


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
        build_test_path('test_1.lu'),
        {},
        2
    ),

    (
        build_test_path('test_2.lu'),
        {'a': 1},
        1
    ),

    (
        build_test_path('test_3.lu'),
        {'a': 409600, 'c': 409600, 'b': 409600},
        2000
    ),
]

if __name__ == "__main__":
    main()
