TEST_STRING_1 = """H => HO
H => OH
O => HH

HOH"""

TEST_STRING_2 = """H => HO
H => OH
O => HH

HOHOHO"""

TEST_STRING_3 = """e => H
e => O
H => HO
H => OH
O => HH

HOH"""

TEST_STRING_4 = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO"""

from aoc_py.y2015.day19 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "7"


# ----------- Part 2 ------------

# Examples don't follow the assumptions that can be made with real input for part 2

# def test_part2_1() -> None:
#    _, p2 = solve_parts(TEST_STRING_3, 2)
#    assert p2 == "3"


# def test_part2_2() -> None:
#    _, p2 = solve_parts(TEST_STRING_4, 2)
#    assert p2 == "6"
