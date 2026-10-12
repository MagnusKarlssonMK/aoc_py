TEST_STRING_1 = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)

TEST_STRING_2 = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)

from aoc_py.y2024.day03 import calculate, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "161"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "48"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_2) == ("161", "48")


# ----------- Parser guards ------------


def test_calculate() -> None:
    assert calculate("mul(2,4)") == 8
    assert calculate("mul(2,4,5)") == 0
    assert calculate("mul(12,3") == 0
    assert calculate("mul(32,64]") == 0
    assert calculate("mul(a,4)") == 0
