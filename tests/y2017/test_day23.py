TEST_STRING = """set b 8
set c 13
mul a 2
jnz a 1
sub a 1
set d 1
mul b c
mul d 3
sub b 92
set a b
jnz a 2
mul a b
jnz e 3
jnz 0 2
jnz 1 2
sub h 5
set h 7"""

from aoc_py.y2017.day23 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "1"
