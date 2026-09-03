TEST_STRING_1 = """0 1 10 99 999"""
TEST_STRING_2 = """125 17"""

from aoc_py.y2024.day11 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p = InputData(TEST_STRING_1)
    p1, _ = p.get_stone_count(1, 2)
    assert p1 == 7


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p = InputData(TEST_STRING_2)
    p1, p2 = p.get_stone_count(6, 25)
    assert p1 == 22
    assert p2 == 55312


# Running the test with the entire solver for coverage
def test_part2_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_2)
    assert p1 == "55312"
    assert p2 == "65601038650482"
