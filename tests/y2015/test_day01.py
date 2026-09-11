TEST_STRING = """(())()()((((()(()())(((((())))())))())())"""

from aoc_py.y2015.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(")", 2)
    assert p2 == "1"


def test_part2_2() -> None:
    _, p2 = solve_parts("()())", 2)
    assert p2 == "5"
