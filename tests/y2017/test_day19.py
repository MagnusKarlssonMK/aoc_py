TEST_STRING = """.     |          .
.     |  +--+    .
.     A  |  C    .
. F---|----E|--+ .
.     |  |  |  D .
.     +B-+  +--+ .
.                ."""

# Minimal grid: a single vertical run with no turns.
TEST_STRING_STRAIGHT = """ |
 A
  """

# One turn to the left/east branch: the packet goes down, hits '+' and turns.
TEST_STRING_TURN = """   |  
 B-+  
      """

from aoc_py.y2017.day19 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "ABCDEF"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "38"


# ----------- Edge cases ------------


def test_straight_grid() -> None:
    assert solve_parts(TEST_STRING_STRAIGHT) == ("A", "2")


def test_single_turn() -> None:
    assert solve_parts(TEST_STRING_TURN) == ("B", "4")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("ABCDEF", "38")
