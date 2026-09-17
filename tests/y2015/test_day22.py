TEST_STRING_1 = """Hit Points: 13
Damage: 8"""

# Custom made test vectors:
TEST_STRING_2 = """Hit Points: 14
Damage: 8"""

TEST_STRING_3 = """Hit Points: 4
Damage: 1"""

TEST_STRING_4 = """Hit Points: 8
Damage: 1"""

from aoc_py.y2015.day22 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    # Need custom player stats for part 1
    p = InputData(TEST_STRING_1, 10, 250)
    p1 = p.get_cheapest_win()
    assert p1 == 226


def test_part1_2() -> None:
    # Need custom player stats for part 1
    p = InputData(TEST_STRING_2, 10, 250)
    p1 = p.get_cheapest_win()
    assert p1 == 641


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_3)
    assert p2 == "53"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_4)
    assert p2 == "106"
