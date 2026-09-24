TEST_STRING = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""

from aoc_py.y2018.day08 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "138"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "66"
