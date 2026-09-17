# Player always wins
TEST_STRING_1 = """Hit Points: 1
Damage: 0
Armor: 0"""

# Invincible boss
TEST_STRING_2 = """Hit Points: 1000
Damage: 100
Armor: 100"""

from aoc_py.y2015.day21 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "8"


def test_part1_2() -> None:
    # No solution exists, boss always wins
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    # No solution exists, player always wins
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "-1"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "356"
