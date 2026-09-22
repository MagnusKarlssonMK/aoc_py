TEST_STRING = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""

# TODO: construct a test program that runs through all the optimizations and also considers the initial value of 'a' for each part.

from aoc_py.y2016.day23 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "3"
