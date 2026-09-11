TEST_STRING_1 = """abcdef"""

TEST_STRING_2 = """pqrstuv"""

from aoc_py.y2015.day04 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "609043"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "1048970"


# ----------- Part 2 ------------

# No test vectors given for part 2, and it's too slow for unit testing anyway.
# Plus it's really the same code as in part 1 anyway.
