TEST_STRING = """10"""

from aoc_py.util.point import Point
from aoc_py.y2016.day13 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p = InputData(TEST_STRING)
    p1 = p.get_count(Point(7, 4), 0)
    assert p1 == 11


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "151"
