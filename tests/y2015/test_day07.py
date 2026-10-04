# Hand made custom made input to go through all operations for both parts
# (The example given in the problem description is not useful for a test run)
TEST_STRING_1 = """15 -> x
22 -> y
1 -> b
x AND y -> c
c OR b -> d
d RSHIFT 1 -> e
e LSHIFT 1 -> f
NOT f -> a"""

# Every shift in TEST_STRING_1 lands inside 16 bits already, so the mask on the left shift there changes nothing and
# can be dropped without any test noticing. This one overflows: 300 shifted left by 8 is 76800, which has to wrap
# around to 11264.
TEST_STRING_2 = """300 -> x
x LSHIFT 8 -> a"""

# A literal as the first operand rather than the second, which is the shape the real input uses for its sixteen
# '1 AND cx' instructions. The final gate shifts one wire by another, and the two have to differ in value, since a
# shift is the one operation here whose operand order actually matters: with d at 1 it would come out the same either
# way round. Driving a from b also makes the two parts differ, so this covers overriding b reaching a wire other than
# the final one.
TEST_STRING_3 = """1 -> b
3 -> d
7 -> x
1 AND x -> c
d LSHIFT b -> a"""

from aoc_py.y2015.day07 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "65529"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "11264"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "6"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "1"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "11264"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "192"


# ----------- Both parts ------------

# Passing no part computes both. Worth pinning here more than usual, because the two answers share a single
# evaluation that reseeds its own memo between them, so there is no part-by-part filtering to fall back on.


def test_both_1() -> None:
    assert solve_parts(TEST_STRING_1) == ("65529", "1")
