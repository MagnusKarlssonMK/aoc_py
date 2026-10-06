TEST_STRING = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""

from aoc_py.y2016.day03 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


def test_part1_2() -> None:
    p1, _ = solve_parts("9 1 1", 1)
    assert p1 == "0"


def test_part1_3() -> None:
    p1, _ = solve_parts("5 5 10", 1)
    assert p1 == "0"


def test_part1_4() -> None:
    p1, _ = solve_parts("883  357  185\n572   189 424\n842 206 272\n", 1)
    assert p1 == "1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "6"


def test_part2_2() -> None:
    _, p2 = solve_parts("100 1 1\n100 2 2\n100 3 3", 2)
    assert p2 == "1"


# ----------- Both parts ------------


def test_both_parts() -> None:
    p1, p2 = solve_parts(TEST_STRING)
    assert (p1, p2) == ("3", "6")
