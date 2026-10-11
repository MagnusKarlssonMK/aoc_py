TEST_STRING = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""

# Two disjoint chains starting at 0. The stronger one is found after the weaker one of the same (maximal) length,
# forcing the strength tie-break when tracking the longest bridge.
TEST_STRING_TIE = """0/5
5/6
6/7
0/1
1/2
2/3"""

# A component with the zero connector on the right side.
TEST_STRING_RIGHT_ZERO = """3/0"""

from aoc_py.y2017.day24 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "31"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "19"


# ----------- Edge cases ------------


def test_tie_break() -> None:
    assert solve_parts(TEST_STRING_TIE) == ("29", "29")


def test_right_zero() -> None:
    assert solve_parts(TEST_STRING_RIGHT_ZERO) == ("3", "3")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("31", "19")
