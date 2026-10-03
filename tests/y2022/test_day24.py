TEST_STRING_1 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

# The puzzle description's blizzard-movement illustration, with independently calculated expected answer.
# (Anwer not given in description text).
TEST_STRING_2 = """#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#"""

# A map where slipping along the top wall row would shorten the crossing, pinning that only the interior and the two
# openings are walkable. The expected 7 / 22 were verified with an independent BFS.
TEST_STRING_3 = """###.#
#.>.#
#>..#
#.^.#
#.###"""

from aoc_py.y2022.day24 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "18"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "10"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "7"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "54"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "30"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "22"
