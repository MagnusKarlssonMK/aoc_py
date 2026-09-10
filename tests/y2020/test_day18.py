TEST_STRING_1 = """1 + 2 * 3 + 4 * 5 + 6"""
TEST_STRING_2 = """1 + (2 * 3) + (4 * (5 + 6))"""
TEST_STRING_3 = """2 * 3 + (4 * 5)"""
TEST_STRING_4 = """5 + (8 * 3 + 9 + 3 * 4 * 3)"""
TEST_STRING_5 = """5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"""
TEST_STRING_6 = """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

from aoc_py.y2020.day18 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "71"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "51"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "26"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "437"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "12240"


def test_part1_6() -> None:
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "13632"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "231"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "51"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "46"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "1445"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "669060"


def test_part2_6() -> None:
    _, p2 = solve_parts(TEST_STRING_6, 2)
    assert p2 == "23340"
