TEST_STRING_1 = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

TEST_STRING_2 = """1234
5678"""

from aoc_py.y2021.day15 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "40"


def test_part1_2() -> None:
    """The cave is 2 deep and 4 wide, so Part 2 has to wrap the rows every len(grid) and the
    columns every len(grid[0]). The two line counts are equal on the square first example, so
    wrapping the columns on the row count instead is invisible there and gives 20 rather than 17
    here."""
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "17"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "315"


def test_part2_2() -> None:
    """Wrapping the rows on the column count rather than the row count leaves Part 1 at 17 and
    only shows up here, dropping the answer to 95."""
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "96"
