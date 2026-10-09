TEST_STRING = """10"""

from aoc_py.util.point import Point
from aoc_py.y2016.day13 import InputData, get_neighbors, is_open, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p = InputData(TEST_STRING)
    p1 = p.get_shortest_path(Point(7, 4))
    assert p1 == 11


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p = InputData(TEST_STRING)
    assert p.get_reachable_count(50) == 151


# ----------- Both parts ------------


def test_both_parts() -> None:
    # Part 1 uses the real puzzle target (31, 39), which is unreachable for the example
    # favorite number 10, so the shortest-path search reports -1.
    assert solve_parts(TEST_STRING) == ("-1", "151")


def test_part1_solve_parts() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "-1"


def test_part2_solve_parts() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "151"


# ----------- Neighbors / formula ------------


def test_neighbors_start() -> None:
    # From (1, 1): right (2, 1) and up (1, 0) are walls, left (0, 1) and down (1, 2) are open.
    assert set(get_neighbors(Point(1, 1), 10)) == {Point(0, 1), Point(1, 2)}


def test_negative_coordinates_excluded() -> None:
    # (0, 0) is open, but its left/up neighbours are negative and must not be yielded.
    neighbors = list(get_neighbors(Point(0, 0), 10))
    assert neighbors == [Point(0, 1)]
    assert all(p.x >= 0 and p.y >= 0 for p in neighbors)


def test_example_maze_rows() -> None:
    # The corner of the building from the puzzle statement, favorite number 10.
    expected = [
        ".#.####.##",
        "..#..#...#",
        "#....##...",
        "###.#.###.",
        ".##..#..#.",
        "..##....#.",
        "#...##.###",
    ]
    for y, row in enumerate(expected):
        assert "".join("." if is_open(x, y, 10) else "#" for x in range(10)) == row
