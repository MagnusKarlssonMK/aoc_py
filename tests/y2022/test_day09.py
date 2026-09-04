TEST_STRING_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

TEST_STRING_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

from aoc_py.y2022.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "13"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "1"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "36"
