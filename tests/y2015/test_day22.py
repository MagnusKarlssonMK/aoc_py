TEST_STRING_1 = """Hit Points: 13
Damage: 8"""

# Custom made test vectors:
TEST_STRING_2 = """Hit Points: 14
Damage: 8"""

TEST_STRING_3 = """Hit Points: 4
Damage: 1"""

TEST_STRING_4 = """Hit Points: 8
Damage: 1"""

# Poison lasts six turns rather than any other number of them, which only shows up as an answer
# difference against a boss that outlives five ticks.
TEST_STRING_5 = """Hit Points: 35
Damage: 1"""

# A boss that hits softly enough that drain's damage and shield's armour matter, and that is
# beaten the expensive way round, so recharge's amount and duration matter too.
TEST_STRING_6 = """Hit Points: 60
Damage: 6"""

# Shield's seven points of armour matter only once the boss hits hard enough to be slowed by it.
TEST_STRING_7 = """Hit Points: 60
Damage: 7"""

TEST_STRING_8 = """Hit Points: 60
Damage: 10"""

# Unwinnable in hard mode at the default 50 hit points and 500 mana, so part 2 has no answer.
TEST_STRING_9 = """Hit Points: 72
Damage: 10"""

# The shape of the real input.
TEST_STRING_10 = """Hit Points: 55
Damage: 8"""

# Recharge restores 101 mana a turn, and at 300 starting mana that exact figure decides whether
# the wizard can afford its next spell. None of the other inputs tell 101 from 100.
TEST_STRING_11 = """Hit Points: 50
Damage: 10"""

# Dropped the rule that an effect spell cannot be cast while its own effect is still running and
# this search runs off indefinitely, because recharge can be recast for unbounded mana.
TEST_STRING_12 = """Hit Points: 25
Damage: 8"""

from aoc_py.y2015.day22 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    # Need custom player stats for part 1
    p = InputData(TEST_STRING_1, 10, 250)
    p1 = p.get_cheapest_win()
    assert p1 == 226


def test_part1_2() -> None:
    # Need custom player stats for part 1
    p = InputData(TEST_STRING_2, 10, 250)
    p1 = p.get_cheapest_win()
    assert p1 == 641


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "438"


def test_part1_6() -> None:
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "893"


def test_part1_8() -> None:
    p1, _ = solve_parts(TEST_STRING_8, 1)
    assert p1 == "1309"


def test_part1_10() -> None:
    p1, _ = solve_parts(TEST_STRING_10, 1)
    assert p1 == "953"


def test_part1_12() -> None:
    p1, _ = solve_parts(TEST_STRING_12, 1)
    assert p1 == "279"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_3)
    assert p2 == "53"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_4)
    assert p2 == "106"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "438"


def test_part2_6() -> None:
    _, p2 = solve_parts(TEST_STRING_6, 2)
    assert p2 == "1249"


def test_part2_6_custom_stats() -> None:
    # Need custom player stats: at 30 hit points the wizard only survives shield for its full
    # duration, so the number of turns shield lasts is visible in the answer.
    p = InputData(TEST_STRING_6, 30, 400)
    p2 = p.get_cheapest_win(True)
    assert p2 == 1671


def test_part2_7() -> None:
    _, p2 = solve_parts(TEST_STRING_7, 2)
    assert p2 == "1249"


def test_part2_7_custom_stats() -> None:
    # Need custom player stats: at 30 hit points drain's two points of healing is the difference
    # between surviving the boss's turn and not.
    p = InputData(TEST_STRING_7, 30, 400)
    p2 = p.get_cheapest_win(True)
    assert p2 == 1764


def test_part2_8() -> None:
    _, p2 = solve_parts(TEST_STRING_8, 2)
    assert p2 == "1442"


def test_part2_9() -> None:
    # No winning plan exists
    _, p2 = solve_parts(TEST_STRING_9, 2)
    assert p2 == "-1"


def test_part2_10() -> None:
    _, p2 = solve_parts(TEST_STRING_10, 2)
    assert p2 == "1289"


def test_part2_11_custom_stats() -> None:
    # Need custom player stats: 300 mana is tight enough that recharge's exact amount decides
    # which spells come within reach.
    p = InputData(TEST_STRING_11, 50, 300)
    p2 = p.get_cheapest_win(True)
    assert p2 == 1309


# ----------- Unwinnable without custom stats ------------


# With no mana at all there is no spell to cast, so the search has nothing to try and the wizard
# can never win. That is the only way to reach the sentinel through solve_parts' fixed 50/500.
def test_no_mana() -> None:
    p = InputData(TEST_STRING_10, 50, 0)
    assert p.get_cheapest_win() == -1
    assert p.get_cheapest_win(True) == -1


# ----------- Both parts at once ------------


# This is the shape the runner itself uses.
def test_both_10() -> None:
    p1, p2 = solve_parts(TEST_STRING_10)
    assert p1 == "953"
    assert p2 == "1289"


def test_both_9() -> None:
    p1, p2 = solve_parts(TEST_STRING_9)
    assert p1 == "1824"
    assert p2 == "-1"
