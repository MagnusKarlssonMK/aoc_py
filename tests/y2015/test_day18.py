TEST_STRING_1 = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""

# Four R-pentominoes, the classic pattern that keeps changing for well over a thousand
# generations. It is here for its longevity rather than its looks: a small grid settles into a still
# life after three or four generations, so a test input of this size gives the same answer at 4 steps
# as at 100 and cannot tell the two apart. This one is still churning at 100, so the step count
# actually matters. It also has 20 lit cells, which is what pushes it onto the real 100-step count
# rather than the short one the example above uses.
TEST_STRING_2 = """.........
..#...#..
.##..##..
.##..##..
.........
..#...#..
.##..##..
.##..##..
........."""

# A pulsar, with a ring of dead cells around it so its expanding phases are not clipped by the edge
# of the grid. Being an oscillator it never settles down, and because its population swings between
# phases it pins the step count exactly: 99 steps gives 48 lit cells where 100 gives 56. The
# pentominoes above cannot do that, since by generation 99 they have burned out to a fixed point.
TEST_STRING_3 = """...............
...###...###...
...............
.#....#.#....#.
.#....#.#....#.
.#....#.#....#.
...###...###...
...............
...###...###...
.#....#.#....#.
.#....#.#....#.
.#....#.#....#.
...............
...###...###...
..............."""

# The same four pentominoes with one cell removed, so there are 19 lit cells: one below the cutoff
# that selects the short step count. Without an input sitting exactly on that boundary, nothing here
# would notice the cutoff being moved.
TEST_STRING_4 = """.........
..#...#..
.##...#..
.##..##..
.........
..#...#..
.##..##..
.##..##..
........."""

from aoc_py.y2015.day18 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "6"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "56"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "14"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    # Note: only run 4 steps like in part 1 to keep it simple
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "14"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "4"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "60"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "29"


# ----------- Both parts at once ------------


# Every other test here asks for one part at a time. This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "4"
    assert p2 == "14"


def test_both_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_2)
    assert p1 == "6"
    assert p2 == "4"
