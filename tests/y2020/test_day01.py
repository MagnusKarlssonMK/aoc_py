TEST_STRING = """1721
979
366
299
675
1456"""

from aoc_py.y2020.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "514579"


def test_part1_2() -> None:
    # Testing input with no solution for code coverage
    p1, _ = solve_parts("", 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "241861950"


def test_part2_2() -> None:
    # Testing input with no solution for code coverage
    _, p2 = solve_parts("", 2)
    assert p2 == "-1"
