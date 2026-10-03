# A mixed string that ends at floor 1 and never reaches the basement, so part 2 has no answer.
TEST_STRING_1 = """(())()()((((()(()())(((((())))())))())())"""

# The official part 2 examples.
TEST_STRING_2 = """)"""

TEST_STRING_3 = """()())"""

# An official part 1 example that dips below the basement twice, so part 2 must report the first time.
TEST_STRING_4 = """))("""

from aoc_py.y2015.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-1"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "-1"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "-1"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "1"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "5"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "1"
