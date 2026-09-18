TEST_STRING = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

from aoc_py.y2016.day12 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "42"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "42"
