TEST_STRING = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

from aoc_py.y2022.day12 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "31"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "29"
