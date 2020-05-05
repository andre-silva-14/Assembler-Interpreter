from main import simple_assembler


code0 = '''\
fasdfs
mov
inc
dec
dec
jnz
inc '''


code1 = '''\
mov a
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

simple_assembler(code0.splitlines()) # None
# simple_assembler(code1.splitlines())  # {'a': 1}
# simple_assembler(code2.splitlines()) # {'a': 409600, 'c': 409600, 'b': 409600}
