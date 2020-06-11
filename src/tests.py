from main import compiler


def main():
    print("Starting Test 1...")
    assert test(compiler(code0.splitlines()), {})

    print("\n\nStarting Test 2...")
    assert test(compiler(code1.splitlines()), {'a': 1})

    print("\n\nStarting Test 3...")
    assert test(compiler(code2.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})


def test(result: dict, expected: dict):
    if result == expected:
        print("Test completed successfully!")
        return True
    else:
        print("Test Failed!")
        return False


code0 = '''\
fasdfs
mov
inc
inc a
dec
jnz
inc '''


code1 = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''


code2 = '''\
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
mov c a'''


if __name__ == "__main__":
    main()
