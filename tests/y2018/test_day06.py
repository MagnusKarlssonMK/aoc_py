TEST_STRING = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

from aoc_py.y2018.day06 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "17"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p = InputData(TEST_STRING)
    p2 = str(p.get_p2(32))
    assert p2 == "16"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "72"
