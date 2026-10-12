TEST_STRING_1 = """0 1 10 99 999"""
TEST_STRING_2 = """125 17"""

from aoc_py.y2024.day11 import InputData, blink, solve_parts

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


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_2) == ("55312", "65601038650482")


def test_blink_large_digit_count() -> None:
    # 999999999999999 has 15 digits and must be multiplied; a log10-based digit
    # count rounds it up to 16 and would wrongly split it.
    assert blink({999999999999999: 1}) == {2023999999999997976: 1}
