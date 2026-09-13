# Hand made custom made input to go through all operations for both parts
# (The example given in the problem description is not useful for a test run)
TEST_STRING = """15 -> x
22 -> y
1 -> b
x AND y -> c
c OR b -> d
d RSHIFT 1 -> e
e LSHIFT 1 -> f
NOT f -> a"""

from aoc_py.y2015.day07 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "65529"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "1"
