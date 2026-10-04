TEST_STRING_1 = """abcdef"""

TEST_STRING_2 = """pqrstuv"""

# Not a puzzle example, but a key chosen because both of its answers are small enough to hash quickly. Six zeroes
# would otherwise need around 16 million hashes on average, which is far too slow for a unit test: the part 2 answers
# for TEST_STRING_1 and TEST_STRING_2 alone are 6742839 and 5714438, which is seconds of hashing apiece. The two
# answers deliberately differ, which is what proves part 2 really asks for six zeroes rather than reusing part 1's
# five.
TEST_STRING_3 = """aaae"""

from aoc_py.y2015.day04 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "609043"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "1048970"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "589086"


# ----------- Part 2 ------------


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "808543"
