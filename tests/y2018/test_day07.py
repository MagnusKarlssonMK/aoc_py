TEST_STRING = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

from aoc_py.y2018.day07 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "CABDFE"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p = InputData(TEST_STRING)
    p2 = str(p.get_p2(1, 0))
    assert p2 == "15"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "253"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("CABDFE", "253")


def test_single_chain() -> None:
    p = InputData("Step A must be finished before step B can begin.")
    assert p.get_p1() == "AB"
    # A takes 0 and B takes 1 tick; each task also costs one tick to complete,
    # so with the sequential dependency the run ends at 3.
    assert p.get_p2(1, 0) == 3
