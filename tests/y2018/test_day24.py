TEST_STRING = """Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""

# The only damage the infection can do is immune, and the immune system's blows are
# sub-lethal, so the fight deadlocks until the boost gets big enough to one-shot it.
DEADLOCK_STRING = """Immune System:
1 units each with 10 hit points (immune to cold) with an attack that does 1 bludgeoning damage at initiative 1

Infection:
1 units each with 10 hit points with an attack that does 1 cold damage at initiative 2"""

# The immune system wins without any boost, so parts 1 and 2 give the same units.
ALREADY_WINS_STRING = """Immune System:
10 units each with 10 hit points with an attack that does 10 bludgeoning damage at initiative 1

Infection:
1 units each with 10 hit points with an attack that does 1 cold damage at initiative 2"""

from aoc_py.y2018.day24 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "5216"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "51"


def test_immune_and_deadlock() -> None:
    assert solve_parts(DEADLOCK_STRING) == ("-1", "1")


def test_already_wins_without_boost() -> None:
    assert solve_parts(ALREADY_WINS_STRING) == ("10", "10")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("5216", "51")
