TEST_STRING = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

# A small game whose recursive play repeats a deck configuration, triggering the loop rule.
LOOP_TEST_STRING = """Player 1:
1
2
4
7

Player 2:
3
5
8
6
"""

from aoc_py.y2020.day22 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "306"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "291"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("306", "291")


def test_parts_are_order_independent() -> None:
    p = InputData(TEST_STRING)
    assert (p.get_p2(), p.get_p1()) == (291, 306)


# ----------- Loop detection ------------


def test_loop_detection() -> None:
    assert solve_parts(LOOP_TEST_STRING) == ("175", "179")
