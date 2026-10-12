TEST_STRING_1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

TEST_STRING_2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

# Single small mask (only two floating bits) that is cheap enough to run both parts on.
TEST_STRING_BOTH = """mask = 000000000000000000000000000000X1001X
mem[42] = 100"""

from aoc_py.y2020.day14 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "165"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "208"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_BOTH) == ("50", "400")
