# The puzzle's own example: a complete triangle, and the first place the two answers part company.
TEST_STRING_1 = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

# Four cities with A-C and B-D unrecorded, which is the case the real input never reaches since its graph is complete.
# Four of the twelve orderings survive, and the two cheapest orderings break on the first leg and on a later one:
#
#   A -> B -> C -> D  = 1 + 2 + 3 = 6      C -> B -> A -> D = 2 + 1 + 4 = 7
#   B -> A -> D -> C  = 1 + 4 + 3 = 8      A -> D -> C -> B = 4 + 3 + 2 = 9
#
# Anything needing A-C or B-D is skipped rather than scored as if that leg were free, which is the whole point: treating
# the missing legs as zero would drop the answer to something far below 6.
TEST_STRING_2 = """A to B = 1
B to C = 2
C to D = 3
A to D = 4"""

# Two disconnected pairs, so no ordering visits all four cities and there is no answer to give. Out of spec, but it is
# what keeps the guard in the solver honest.
TEST_STRING_3 = """A to B = 1
C to D = 2"""

from aoc_py.y2015.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "605"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "6"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "982"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "9"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "-1"
