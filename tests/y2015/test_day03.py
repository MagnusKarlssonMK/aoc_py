TEST_STRING_1 = """>"""

TEST_STRING_2 = """^>v<"""

TEST_STRING_3 = """^v"""

TEST_STRING_4 = """^v^v^v^v^v"""

# Not an official example. Mixing both axes in one string is what pins which arrow belongs to which direction:
# every other input is symmetric under swapping any single arrow for another, so it passes even if the arrow
# to direction map is wrong.
TEST_STRING_5 = """^>v<^"""

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


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "2"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "4"


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


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "2"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "3"
