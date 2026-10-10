TEST_STRING = """0
3
0
1
-3"""

from aoc_py.y2017.day05 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "5"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("5", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "10"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "10")


# ----------- Edge cases ------------


def test_minimal_divergence() -> None:
    # Smallest input where the parts differ: a cell climbs from 2 to 3, tripping the ">= 3" rule.
    assert solve_parts("2\n-1\n-2\n-2") == ("6", "13")


def test_single_step_out() -> None:
    assert solve_parts("-1") == ("1", "1")


def test_empty_input() -> None:
    assert solve_parts("") == ("0", "0")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("5", "10")
