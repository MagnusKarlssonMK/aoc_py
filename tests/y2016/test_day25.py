TEST_STRING = """cpy a d
cpy 2 c
cpy 3 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy 5 b
inc d
dec b
jnz b -2
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21"""

from aoc_py.y2016.day25 import solve_parts

# ----------- Part 1 ------------

# The program transmits the LSB-first bits of a + 11 repeatedly. The smallest a for
# which that stream is an endless 0,1,0,1,... is a = 42 - 11 = 31 (42 = 0b101010).


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "31"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "-"
