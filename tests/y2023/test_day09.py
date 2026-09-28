TEST_STRING_1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# A single arithmetic row, where the two parts extend the history in opposite directions: 6 comes after the 5, and
# 0 comes before the 1.
TEST_STRING_2 = "1 2 3 4 5"

# A flat history has no differences left to add, so it contributes nothing to either answer.
TEST_STRING_3 = "0 0 0"

from aoc_py.y2023.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "114"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "6"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "0"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "2"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "0"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "0"
