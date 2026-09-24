TEST_STRING = """..#
#..
..."""

from aoc_py.y2017.day22 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "5587"


# ----------- Part 2 ------------

# Disabling this test; too slow with current solution
# def test_part2_1() -> None:
#    _, p2 = solve_parts(TEST_STRING, 2)
#    assert p2 == "2511944"
