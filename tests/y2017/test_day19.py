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

# The first example again, but with real trailing spaces (instead of the boundary dots
# used above). The trailing whitespace has been automatically removed by editor,
# so this is to test that the solver can handle that.

TEST_STRING_WITH_TRAILING_SPACES = """     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+ """

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


def test_stripped_trailing_spaces() -> None:
    """Trailing whitespace is routinely stripped from input files, which makes the
    rows ragged. The grid has to be padded to the widest row before it is parsed."""
    stripped = "\n".join(
        line.rstrip() for line in TEST_STRING_WITH_TRAILING_SPACES.splitlines()
    )
    assert solve_parts(stripped) == ("ABCDEF", "38")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("ABCDEF", "38")
