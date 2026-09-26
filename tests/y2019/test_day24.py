TEST_STRING_1 = """....#
#..#.
#..##
..#..
#...."""

from aoc_py.y2019.day24 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "2129920"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p = InputData(TEST_STRING_1)
    p2 = str(p.get_p2(10))
    assert p2 == "99"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "1922"
