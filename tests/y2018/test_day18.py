TEST_STRING = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

from aoc_py.y2018.day18 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "1147"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "0"


# ----------- Both parts ------------


def test_both_parts() -> None:
    # The example's 1-billion-minute cycle lands on a zero-value state.
    assert solve_parts(TEST_STRING) == ("1147", "0")


def test_all_open() -> None:
    # Open cells never grow anything: the value stays 0 and the grid already
    # cycles after one minute (the cycle is found before P1_TIME elapses).
    assert solve_parts("...\n...\n...") == ("0", "0")
