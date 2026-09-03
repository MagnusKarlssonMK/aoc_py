TEST_STRING = """123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  """

from aoc_py.y2025.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "4277556"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "3263827"
