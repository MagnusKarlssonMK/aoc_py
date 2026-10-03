TEST_STRING_1 = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

# Four blueprints; part 2 must only use the first three.
TEST_STRING_2 = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
Blueprint 3: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 6 clay. Each geode robot costs 2 ore and 3 obsidian.
Blueprint 4: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 5 clay. Each geode robot costs 3 ore and 2 obsidian."""

# The first three blueprints of TEST_STRING_2.
TEST_STRING_3 = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
Blueprint 3: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 6 clay. Each geode robot costs 2 ore and 3 obsidian."""

# A single blueprint where the final minutes of an already-built geode robot must still be counted.
TEST_STRING_4 = "Blueprint 1: Each ore robot costs 6 ore. Each clay robot costs 6 ore. Each obsidian robot costs 3 ore and 4 clay. Each geode robot costs 3 ore and 4 obsidian."

from aoc_py.y2022.day19 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "33"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "14"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "3472"


def test_part2_2() -> None:
    # Part 2 multiplies the first three blueprints; any further blueprints are ignored.
    assert InputData(TEST_STRING_3).get_p2(20) == 84
    assert InputData(TEST_STRING_2).get_p2(20) == 84
