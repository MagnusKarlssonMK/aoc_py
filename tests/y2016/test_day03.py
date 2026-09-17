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


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "6"
