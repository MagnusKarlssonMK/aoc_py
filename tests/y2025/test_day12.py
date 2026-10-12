from aoc_py.y2025.day12 import solve_parts

TEST_STRING_1 = """0:
.#.
#.#
.#.

1:
##.
.##
###

3x3: 1 0 0
2x2: 5 5 5 5 5
4x3: 0 0 0 0 1"""

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "-"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_1) == ("2", "-")
