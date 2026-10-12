from aoc_py.y2024.day22 import solve_parts

TEST_STRING_1 = """1
10
100
2024"""

TEST_STRING_2 = """1
2
3
2024"""

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "37327623"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "23"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_2) == ("37990510", "23")
