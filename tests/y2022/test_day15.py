# The official test example input
TEST_STRING_1 = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

# Built so solve_parts' own row and window are reachable. The two left sensors share
# both of their upper edges, so part 2's dark point is their shared corner at
# (0, 1999998), which sits on the window's x = 0 boundary. The far sensor is the only
# one whose reach runs out exactly at row 2000000, so it pins the single boundary tile
# part 1 used to drop, and it lands far enough away to force the disjoint-interval
# branch of the merge.
TEST_STRING_2 = """Sensor at x=0, y=2000000: closest beacon is at x=1, y=2000000
Sensor at x=0, y=2000001: closest beacon is at x=0, y=2000003
Sensor at x=3999999, y=2000001: closest beacon is at x=3999998, y=2000001"""

from aoc_py.y2022.day15 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1 = InputData(TEST_STRING_1).get_coverage(10)
    assert p1 == 26


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p2 = InputData(TEST_STRING_1).get_dark_point_freq(20)
    assert p2 == 56000011


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "1999998"


def test_part2_3() -> None:
    # The same example one column too narrow: its dark point is at x = 14, so nothing
    # qualifies and the window holds no missing beacon.
    p2 = InputData(TEST_STRING_1).get_dark_point_freq(13)
    assert p2 == -1
