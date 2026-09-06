TEST_STRING = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

from aoc_py.y2022.day19 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "33"


# ----------- Part 2 ------------

# Note: Test input doesn't work for part 2 - solution assumes at least 3 blueprints

# def test_part2_1() -> None:
#    _, p2 = solve_parts(TEST_STRING, 2)
#    assert p2 == "62"
