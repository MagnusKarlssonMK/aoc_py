# Note: the test input needs to be adjusted to add an escape backslash before every backslash character
TEST_STRING_1 = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

# A grid with no bouncers at all, so every beam runs straight to the far edge.
TEST_STRING_2 = """...
...
..."""

# A vertical splitter reached by a horizontal beam, which then splits upwards and downwards.
TEST_STRING_3 = """..|
...
..."""

# A horizontal splitter reached by a horizontal beam, which then carries straight on.
TEST_STRING_4 = """.-.
...
..."""

# A single row, so the grid has no vertical extent at all.
TEST_STRING_5 = """..."""

from aoc_py.y2023.day16 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "46"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "3"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "5"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "3"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "51"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "3"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "5"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "5"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "3"
