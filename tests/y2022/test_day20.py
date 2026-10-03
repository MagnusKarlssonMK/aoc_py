TEST_STRING_1 = """1
2
-3
3
-2
0
4"""

# Repeated values (three 2s), a magnitude larger than the list (7 > n-1) and negatives.
TEST_STRING_2 = """2
2
2
-5
0
7
-1"""

from aoc_py.y2022.day20 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "3"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "6"


def test_part1_3() -> None:
    # Part 2's rescaling must not disturb part 1: asking for part 1 afterwards must still be correct.
    data = InputData(TEST_STRING_1)
    assert data.get_p2() == 1623178306
    assert data.get_p1() == 3


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "1623178306"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "2434767459"
