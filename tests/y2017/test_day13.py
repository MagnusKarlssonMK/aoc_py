TEST_STRING = """0: 3
1: 2
4: 4
6: 4"""

from aoc_py.y2017.day13 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "24"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "10"


# ----------- Edge cases ------------


def test_single_scanner() -> None:
    # Caught at time 0 (severity 0 * 4 = 0); the first safe delay is 1.
    assert solve_parts("0: 4") == ("0", "1")


def test_two_scanners() -> None:
    assert solve_parts("0: 2\n1: 3") == ("0", "1")


# ----------- Both parts ------------


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("24", "-1")


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "10")


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("24", "10")
