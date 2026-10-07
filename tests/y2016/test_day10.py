TEST_STRING = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

TEST_STRING_2 = """value 61 goes to bot 4
value 17 goes to bot 4
value 1 goes to bot 0
value 2 goes to bot 0
value 3 goes to bot 1
value 4 goes to bot 1
value 5 goes to bot 2
value 6 goes to bot 3
bot 4 gives low to output 0 and high to output 1
bot 0 gives low to output 2 and high to output 3
bot 1 gives low to output 4 and high to output 5
bot 2 gives low to output 6 and high to output 7
bot 3 gives low to output 8 and high to output 9"""

TEST_STRING_3 = """value 1 goes to bot 0
value 2 goes to bot 0
value 4 goes to bot 1
value 3 goes to bot 1
value 6 goes to bot 2
value 5 goes to bot 2
bot 1 gives low to bot 0 and high to output 0
bot 2 gives low to bot 0 and high to output 2
bot 0 gives low to output 1 and high to output 0"""

from aoc_py.y2016.day10 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "30"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("2", "30")


def test_61_17_targets() -> None:
    # Eight value lines select the real-input target pair; bot 4 compares 17 and 61,
    # and the part 2 product is 17 * 61 * 1.
    assert solve_parts(TEST_STRING_2) == ("4", "1037")


def test_multiple_rounds() -> None:
    # Bot 0 acts twice (chips arrive in two rounds) and output 0 collects three chips;
    # no bot compares 5 and 2, so part 1 stays at the not-found sentinel.
    assert solve_parts(TEST_STRING_3) == ("-1", "12")


TEST_STRING_4 = """value 1 goes to bot 0
value 3 goes to bot 0
value 4 goes to bot 1
value 2 goes to bot 1
value 6 goes to bot 2
value 5 goes to bot 2
bot 0 gives low to output 0 and high to output 5
bot 1 gives low to bot 0 and high to output 1
bot 2 gives low to bot 0 and high to output 2"""


def test_second_round_compare() -> None:
    # Bot 0 compares {1, 3} first, then the second round of chips {2, 5} -- the answer depends
    # on its slots being cleared after the first act. Product is 1 * 4 * 6.
    assert solve_parts(TEST_STRING_4) == ("0", "24")
