TEST_STRING_1 = """16,1,2,0,4,2,7,1,2,14"""

TEST_STRING_2 = """0,1,2,3,4,5,7"""

from aoc_py.y2021.day07 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "37"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "13"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "168"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "24"
