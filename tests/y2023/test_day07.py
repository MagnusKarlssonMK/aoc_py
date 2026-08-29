TEST_STRING = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

from aoc_py.y2023.day07 import solve_parts

# ----------- Part 1 ------------

def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "6440"


# ----------- Part 2 ------------

def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "5905"
