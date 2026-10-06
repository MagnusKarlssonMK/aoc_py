TEST_STRING = """To continue, please consult the code grid in the manual.  Enter the code at row 2, column 1."""

TEST_STRING_START = """To continue, please consult the code grid in the manual.  Enter the code at row 1, column 1."""

TEST_STRING_LARGE = """Enter the code at row 4000, column 4000."""

from aoc_py.y2015.day25 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "31916031"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_START, 1)
    assert p1 == "20151125"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_LARGE, 1)
    assert p1 == "28241514"


# ----------- Both parts ------------


def test_both_parts() -> None:
    p1, p2 = solve_parts(TEST_STRING)
    assert (p1, p2) == ("31916031", "-")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "-"
