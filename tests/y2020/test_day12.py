TEST_STRING = """F10
N3
F7
R90
F11"""

# Turns left and then moves, exercising the rotate_left path.
TEST_STRING_2 = """L90
F1"""

from aoc_py.y2020.day12 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "25"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "286"


# ----------- Both parts ------------


def test_left_rotation() -> None:
    assert solve_parts(TEST_STRING_2) == ("1", "11")


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("25", "286")
