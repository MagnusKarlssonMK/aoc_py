TEST_STRING_1 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

TEST_STRING_2 = """.....
.....
..S..
.....
....."""

from aoc_py.y2023.day21 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p = InputData(TEST_STRING_1)
    p1 = p.get_reachable(6)
    assert p1 == 16


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4056"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "4225"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    # TEST_STRING has rocks and no repeating geometry, so part 2's quadratic doesn't hold for it. A
    # rock-free grid has no effect from the grid repeating at all, so the gardener walks the infinite
    # plane where exactly (steps + 1) ** 2 tiles are reachable, making the quadratic exact.
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "702322240857769"
