TEST_STRING_1 = """ADVENT"""
TEST_STRING_2 = """A(1x5)BC"""
TEST_STRING_3 = """(3x3)XYZ"""
TEST_STRING_4 = """A(2x2)BCD(2x2)EFG"""
TEST_STRING_5 = """(6x1)(1x3)A"""
TEST_STRING_6 = """X(8x2)(3x3)ABCY"""
TEST_STRING_7 = """(27x12)(20x12)(13x14)(7x10)(1x12)A"""
TEST_STRING_8 = """(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"""

from aoc_py.y2016.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "6"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "7"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "9"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "11"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "6"


def test_part1_6() -> None:
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "18"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "9"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_6, 2)
    assert p2 == "20"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_7, 2)
    assert p2 == "241920"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_8, 2)
    assert p2 == "445"
