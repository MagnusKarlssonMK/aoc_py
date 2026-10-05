TEST_STRING_1 = """Sue 1: goldfish: 5, cars: 2, children: 3
Sue 2: cats: 8, trees: 4, pomeranians: 2
Sue 3: akitas: 1, vizslas: 2, goldfish: 10"""

# The example above only ever mentions six of the ten items, so samoyeds, akitas, vizslas and
# perfumes are never asked about. This one mentions all ten. The first Sue has every item at exactly
# the ticker-tape amount, which satisfies part 1 but not part 2, since cats has to be greater than 7
# rather than equal to it. The second Sue has the four items part 2 cares about moved off their
# targets and everything else untouched, so it satisfies part 2 but not part 1.
TEST_STRING_2 = """Sue 1: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1
Sue 2: children: 3, cats: 8, samoyeds: 2, pomeranians: 2, akitas: 0, vizslas: 0, goldfish: 4, trees: 4, cars: 2, perfumes: 1"""

# Nothing here can match either part. Part 1 wants cats at exactly 7 and this has 9; part 2 wants
# more than 7, which 9 would satisfy, so the items are picked to be wrong under both rules instead.
TEST_STRING_3 = """Sue 1: children: 9
Sue 2: cars: 9"""

# Every Sue here lists more than one item, and part 1 and part 2 disagree about which ones. Sue 1 is
# half right for part 1 and Sue 2 is half right for part 2, so neither of them is a match even though
# an "any item agrees" reading would accept both. Sue 3 is the first that satisfies part 1 outright and
# Sue 4 the first that satisfies part 2, and each has an identical twin further down so that stopping
# at the first match is distinguishable from reporting the last one found.
TEST_STRING_4 = """Sue 1: cats: 7, children: 9
Sue 2: trees: 4, cars: 9
Sue 3: cats: 7
Sue 4: children: 3, trees: 4
Sue 5: cats: 7
Sue 6: children: 3, trees: 4"""

TEST_STRING_5 = ""

from aoc_py.y2015.day16 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "1"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "-1"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "2"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "2"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "-1"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "4"


# ----------- Both parts at once ------------


# Every other test here asks for one part at a time. This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "1"
    assert p2 == "2"


# No Sues at all, so there is nobody to match.
def test_both_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_5)
    assert p1 == "-1"
    assert p2 == "-1"
