TEST_STRING_1 = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

# Every pair gets on badly, so the best seating around this table is negative. 0 is not a total any seating can reach,
# which is what makes this the case the accumulator must not be seeded with.
TEST_STRING_2 = """A would lose 1 happiness units by sitting next to B.
A would lose 1 happiness units by sitting next to C.
B would lose 1 happiness units by sitting next to A.
B would lose 1 happiness units by sitting next to C.
C would lose 1 happiness units by sitting next to A.
C would lose 1 happiness units by sitting next to B."""

TEST_STRING_3 = """A would gain 5 happiness units by sitting next to B.
A would gain 5 happiness units by sitting next to C.
B would gain 5 happiness units by sitting next to A.
B would gain 5 happiness units by sitting next to C.
C would gain 5 happiness units by sitting next to A.
C would gain 5 happiness units by sitting next to B."""

TEST_STRING_4 = ""

from aoc_py.y2015.day13 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "330"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-6"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "30"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "286"
    # Note - The answer 286 is not given by the description for part 2, but calculated with the solution


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "-4"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "20"


# ----------- Both parts at once ------------


# Every other test here asks for one part at a time. This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "330"
    assert p2 == "286"


# No guests at all, so there is no table to seat and no total to maximise.
def test_both_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_4)
    assert p1 == "-1"
    assert p2 == "-1"
