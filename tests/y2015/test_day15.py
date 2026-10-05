TEST_STRING_1 = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

# Every ingredient here is worth a single calorie, so the most calories any 100-teaspoon split can
# reach is 100 and part 2 has no recipe to maximise over. That makes 0 the answer, and it is the only
# score these ingredients can produce.
TEST_STRING_2 = """Sugar: capacity 1, durability 1, flavor 1, texture 1, calories 1
Spice: capacity 1, durability 1, flavor 1, texture 1, calories 1"""

# Four ingredients, which is the shape the real input uses. The search runs 176,851 leaves here rather
# than the 101 that TEST_STRING_1 costs, so each call takes about a third of a second.
TEST_STRING_3 = """Vran: capacity -1, durability 2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability -2, flavor 3, texture 5, calories 3
Nutmeg: capacity 3, durability 5, flavor -1, texture 7, calories 4
Sugar: capacity 4, durability 4, flavor 4, texture 4, calories 10"""

# Vran beats Cinnamon on every property, so the best split is all 100 teaspoons of Vran and none of
# anything else. That is the split where the first ingredient takes the whole bowl, which is the one a
# quantity loop that stopped one short would never reach.
TEST_STRING_4 = """Vran: capacity 10, durability 10, flavor 10, texture 10, calories 6
Cinnamon: capacity 1, durability 1, flavor 1, texture 1, calories 1"""

# Both ingredients are negative on flavour, so flavour comes out at -400 for every split and clamps
# to zero, which zeroes the whole product. Part 1 is therefore 0 rather than a clamp that quietly
# becomes 1 and hands back a positive score for a recipe that is worthless.
TEST_STRING_5 = """Bitter: capacity 5, durability 5, flavor -4, texture 5, calories 6
Sour: capacity 5, durability 5, flavor -4, texture 5, calories 4"""

TEST_STRING_6 = ""

from aoc_py.y2015.day15 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "62842880"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "100000000"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "25600000000"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "1000000000000"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "0"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "57600000"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "0"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "5794095600"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "452121760000"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "0"


# ----------- Both parts at once ------------


# Every other test here asks for one part at a time. This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "62842880"
    assert p2 == "57600000"


# No ingredients at all, so there is no recipe to score.
def test_both_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_6)
    assert p1 == "-1"
    assert p2 == "-1"
