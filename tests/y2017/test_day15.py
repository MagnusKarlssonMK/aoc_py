TEST_STRING = """Generator A starts with 65
Generator B starts with 8921"""

# Both generators start at 1: no matches among the first 10,000 raw pairs,
# but the multiple-filtered streams match once.
TEST_STRING_BOTH_ONE = """Generator A starts with 1
Generator B starts with 1"""

from aoc_py.y2017.day15 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1, pairs=(10_000, 10_000))
    assert p1 == "1"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1, pairs=(10_000, 10_000)) == ("1", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2, pairs=(10_000, 10_000))
    assert p2 == "2"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2, pairs=(10_000, 10_000)) == ("-1", "2")


# ----------- Edge cases ------------


def test_p2_filters_independently() -> None:
    assert solve_parts(TEST_STRING_BOTH_ONE, pairs=(10_000, 10_000)) == ("0", "1")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING, pairs=(10_000, 10_000)) == ("1", "2")
