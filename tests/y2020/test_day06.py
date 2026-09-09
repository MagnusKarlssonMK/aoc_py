TEST_STRING_1 = """abcx
abcy
abcz"""

TEST_STRING_2 = """abc

a
b
c

ab
ac

a
a
a
a

b"""

from aoc_py.y2020.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "6"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "11"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "6"
