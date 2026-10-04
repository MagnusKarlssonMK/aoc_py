TEST_STRING_1 = """2x3x4"""

TEST_STRING_2 = """1x1x10"""

# The same present as TEST_STRING_1 with its dimensions in descending order, so it only gives the right answer if the
# dimensions get sorted.
TEST_STRING_3 = """4x3x2"""

# Two presents, so the per-present answers have to be accumulated rather than taken from the last one.
TEST_STRING_4 = """3x4x5
2x2x3"""

from aoc_py.y2015.day02 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "58"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "43"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "58"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "142"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "34"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "14"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "34"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "94"
