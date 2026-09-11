TEST_STRING_1 = """>"""

TEST_STRING_2 = """^>v<"""

TEST_STRING_3 = """^v"""

TEST_STRING_4 = """^v^v^v^v^v"""

from aoc_py.y2015.day03 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "2"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "4"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "3"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "3"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "11"
