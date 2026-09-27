# Intcode programs for the painting robot: each cycle feeds the current panel color as input and
# emits a paint color and a turn direction (0=left, 1=right) before continuing.
TEST_STRING_1 = """3,0,104,1,104,1,3,0,104,1,104,1,3,0,104,1,104,1,99"""

TEST_STRING_2 = """3,0,104,1,104,1,3,0,104,1,104,1,3,0,104,1,104,1,3,0,104,1,104,1,3,0,104,1,104,1,99"""

TEST_STRING_3 = """3,0,104,1,104,1,3,0,104,1,104,1,3,0,104,0,104,0,3,0,104,1,104,0,3,0,104,1,104,0,99"""

from aoc_py.y2019.day11 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "3"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "4"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "5"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "\n##\n.#\n"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "\n##\n##\n"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "\n###\n..#\n"
