TEST_STRING_1 = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
TEST_STRING_2 = """>><>>><<<<<<>>><"""

from aoc_py.y2022.day17 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "3068"


def test_part1_2() -> None:
    # A short drop must not trip the part-2 cycle detection (covers the non-cycle return).
    assert InputData(TEST_STRING_2).drop_rocks(50) == 64


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "1514285714288"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "1314285714284"
