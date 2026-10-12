TEST_STRING = """2333133121414131402"""

# Even-length disk map: the final entry is trailing free space (exercises the
# "last index is odd" branch that trims right_idx before the scan).
TEST_STRING_2 = """1234"""

from aoc_py.y2024.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "1928"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "2858"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("1928", "2858")


def test_both_parts_even_length() -> None:
    assert solve_parts(TEST_STRING_2) == ("6", "12")
