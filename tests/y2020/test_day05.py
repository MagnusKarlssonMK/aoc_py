TEST_STRING_1 = """BFFFBBFRRR"""

TEST_STRING_2 = """FFFBBBFRRR"""

TEST_STRING_3 = """BBFFBBFRLL"""

TEST_STRING_4 = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

TEST_STRING_5 = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
BBFFBBFRRL"""

from aoc_py.y2020.day05 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "567"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "119"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "820"


# ----------- Part 2 ------------
# No test vector given for part 2, just constructing one non-working combination
# from part 1 for code coverage, and then one with a small modification to make
# it working.


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "-1"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "821"
