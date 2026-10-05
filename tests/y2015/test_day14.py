TEST_STRING_1 = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

# Three reindeer, so this is read as a real race and scored over 2503 seconds rather than the worked
# example's 1000. Comet and Dancer above are level only once, at second 521, whereas A and B here are
# level often enough to give part 2's tie handling something to do.
#
# A comes first deliberately. A and B share the lead at 29 of the 2503 seconds, and A is the one who
# wins on points, so loosening the lead test to >= would let B take those 29 points off A and drop the
# answer to 2335. With A listed last the same loosening only costs B points, which nobody reports.
TEST_STRING_2 = """A can fly 7 km/s for 20 seconds, but then must rest for 3 seconds.
B can fly 20 km/s for 3 seconds, but then must rest for 7 seconds.
C can fly 10 km/s for 5 seconds, but then must rest for 5 seconds."""

TEST_STRING_3 = ""

from aoc_py.y2015.day14 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1120"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "15253"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "689"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "2364"


# ----------- Both parts at once ------------


# Every other test here asks for one part at a time. This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "1120"
    assert p2 == "689"


# No reindeer at all, so there is no distance to compare and no score to award.
def test_both_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_3)
    assert p1 == "-1"
    assert p2 == "-1"
