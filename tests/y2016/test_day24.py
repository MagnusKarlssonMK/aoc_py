TEST_STRING = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""

# A single number needs no travel at all.
TEST_STRING_SINGLE = """###
#0#
###"""

# Two disconnected number components: 0/1 and 2/3 can never all be visited.
TEST_STRING_ISOLATED = """#########
#0.1#2.3#
#########"""

from aoc_py.y2016.day24 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "14"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("14", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "20"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "20")


# ----------- Edge cases ------------


def test_single_number() -> None:
    p = InputData(TEST_STRING_SINGLE)
    assert p.get_shortest_path() == 0
    assert p.get_shortest_path(True) == 0


def test_unreachable_numbers() -> None:
    p = InputData(TEST_STRING_ISOLATED)
    assert p.get_shortest_path() == -1
    assert p.get_shortest_path(True) == -1


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("14", "20")
