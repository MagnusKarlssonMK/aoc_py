TEST_STRING = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

from aoc_py.y2017.day12 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "6"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "2"


# ----------- Edge cases ------------


def test_single_program() -> None:
    assert solve_parts("0 <-> 0") == ("1", "1")


# ----------- Both parts ------------


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("6", "-1")


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "2")


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("6", "2")
