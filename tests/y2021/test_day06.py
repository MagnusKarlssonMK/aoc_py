TEST_STRING_1 = """3,4,3,1,2"""

from aoc_py.y2021.day06 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "5934"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "26984457539"


def test_part2_2() -> None:
    """get_answers makes a copy of the buckets, so one instance gives the same answer on repeated calls."""
    p = InputData(TEST_STRING_1)
    assert p.get_answers() == (5934, 26984457539)
    assert p.get_answers() == (5934, 26984457539)
