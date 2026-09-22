TEST_STRING_1 = """5 1 9 5
7 5 3
2 4 6 8"""

TEST_STRING_2 = """5 9 2 8
9 4 7 3
3 8 6 5"""

from aoc_py.y2017.day02 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "18"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "9"
