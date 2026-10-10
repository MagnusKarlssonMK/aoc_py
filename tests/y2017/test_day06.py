TEST_STRING = """0 2 7 0"""

from aoc_py.y2017.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "5"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("5", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "4"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "4")


# ----------- Edge cases ------------


def test_single_bank() -> None:
    # A single bank rebalances back to itself immediately.
    assert solve_parts("1") == ("1", "1")


def test_all_zero() -> None:
    assert solve_parts("0 0") == ("1", "1")


def test_wraparound() -> None:
    # The redistributed value exceeds the bank count, wrapping more than once.
    assert solve_parts("5 0 0") == ("4", "3")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("5", "4")
