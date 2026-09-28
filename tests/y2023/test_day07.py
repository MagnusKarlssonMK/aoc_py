TEST_STRING = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# The four hand types that the official example has no hand of.
TEST_STRING_2 = """AAAAA 1
AAAAK 1
AAAKK 1
23456 1"""

# The joker cases: a hand of nothing but jokers, five of a kind made by merging, and a full house made by merging.
TEST_STRING_3 = """JJJJJ 1
JJJAA 10
AAJKK 100"""

from aoc_py.y2023.day07 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "6440"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "10"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "123"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "5905"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "10"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "132"
