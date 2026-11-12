TEST_OFFICIAL_1 = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

# Four three-bit numbers with an even split at bit 1, so the tie-breaking direction decides both answers.
TEST_CUSTOM_1 = """010
110
101
100"""

# Two equal numbers never reduces down to a single number, so no solution is possible for part 2.
TEST_CUSTOM_2 = """011
011"""

from aoc_py.y2021.day03 import solve_parts

# ----------- Part 1 ------------


def test_part1_official_1() -> None:
    p1, _ = solve_parts(TEST_OFFICIAL_1, 1)
    assert p1 == "198"


def test_part1_custom_1() -> None:
    p1, _ = solve_parts(TEST_CUSTOM_1, 1)
    assert p1 == "6"


# ----------- Part 2 ------------


def test_part2_official_1() -> None:
    _, p2 = solve_parts(TEST_OFFICIAL_1, 2)
    assert p2 == "230"


def test_part2_custom_1() -> None:
    _, p2 = solve_parts(TEST_CUSTOM_1, 2)
    assert p2 == "10"


def test_part2_custom_2() -> None:
    _, p2 = solve_parts(TEST_CUSTOM_2, 2)
    assert p2 == "-1"
