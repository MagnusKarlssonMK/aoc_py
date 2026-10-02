TEST_STRING_1 = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

# A cave with a disconnected positive-flow valve: ZZ/YY cannot be reached from AA.
TEST_STRING_2 = """Valve AA has flow rate=0; tunnels lead to valve BB
Valve BB has flow rate=5; tunnels lead to valve AA
Valve ZZ has flow rate=9; tunnels lead to valve YY
Valve YY has flow rate=0; tunnels lead to valve ZZ"""

from aoc_py.y2022.day16 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1651"


def test_part1_2() -> None:
    # A valve reachable with exactly one minute left must still be opened (walk 1 + open 1 leaves 1).
    assert InputData(TEST_STRING_2).get_maxflow(3) == 5


def test_part1_3() -> None:
    # The disconnected valves ZZ/YY cannot be opened from AA.
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "140"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "1707"


def test_part2_2() -> None:
    # One agent may stay idle; an unopened mask must contribute 0.
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "120"
