TEST_STRING = """flqrgnkx"""

from aoc_py.y2017.day14 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "8108"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "1242"


# ----------- Edge cases ------------


def test_single_char_key() -> None:
    # Still a full 128-row disk, but a minimal key string.
    assert solve_parts("0") == ("8264", "1101")


# ----------- Both parts ------------


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("8108", "-1")


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "1242")


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("8108", "1242")
