TEST_STRING = """1
2
3
4
5
7
8
9
10
11"""

# Custom made test vectors:

# The example above only ever holds combinations whose remainder divides as well. This one contains
# a cheaper combination that does not: 3 7 10 reaches the group total of 20 first, but 4 4 6 8 9 9
# is left over and no subset of that sums to 20, so no partition holds that group. Accepting it
# anyway answers 210, where 216, from 3 8 9, is the only correct answer at that size.
TEST_STRING_2 = """3
4
4
6
7
8
9
9
10"""

# Three weights for three groups, so the first group is one weight and is as large a first group as
# can be asked for. Skipping that size leaves nothing at all to try.
TEST_STRING_3 = """5
5
5"""

# Totals ten against three groups, so there is no group size to search for in the first place.
TEST_STRING_4 = """1
2
3
4"""

# Totals forty-two against three groups, so the group size is fourteen, and the one combination
# reaching it leaves 3 7 8 10 behind, which splits into nothing of the sort.
TEST_STRING_5 = """3
5
7
8
9
10"""

# Six weighs more than the group size of four, so it can never sit in a group, and every
# combination leaving it out fails to fill the remaining groups.
TEST_STRING_6 = """2
2
2
6"""

# Nothing at all.
TEST_STRING_7 = ""

# Nothing but zero, so the first combination reaching the group total of zero takes every weight
# and leaves an empty pool behind.
TEST_STRING_8 = """0"""

# Two pairs reach the group total of twenty here and both leave a remainder that divides, but
# combinations walks 10 10 before it walks 1 19, so settling for whatever turns up first answers
# 100 where the cheapest of them is 19.
TEST_STRING_9 = """10
10
1
19
10
10"""

from aoc_py.y2015.day24 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "99"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "216"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "5"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "-1"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "-1"


def test_part1_6() -> None:
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "-1"


def test_part1_7() -> None:
    p1, _ = solve_parts(TEST_STRING_9, 1)
    assert p1 == "19"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "44"


# TEST_STRING_2 divides three ways but not four, so part 2 has no answer at all even though part 1
# does.
def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "-1"


# ----------- Both parts at once ------------


def test_no_weights() -> None:
    assert solve_parts(TEST_STRING_7) == ("-1", "-1")


def test_only_zero() -> None:
    assert solve_parts(TEST_STRING_8) == ("-1", "-1")
