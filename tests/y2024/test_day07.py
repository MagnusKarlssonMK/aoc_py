TEST_STRING = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# One equation solvable only through a concatenation hanging off an addition
# (1 + 1 || 5 = 25) and one where the running total must overshoot and be pruned.
TEST_STRING_2 = """25: 1 1 5
20: 10 3 3"""

from aoc_py.y2024.day07 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3749"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "11387"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("3749", "11387")


def test_both_parts_2() -> None:
    assert solve_parts(TEST_STRING_2) == ("0", "25")
