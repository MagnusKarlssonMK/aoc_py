TEST_STRING = """ihgpwlah"""

from aoc_py.y2016.day17 import InputData, State, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "DDRRRD"


def test_part1_2() -> None:
    p1, _ = solve_parts("kglvqrro", 1)
    assert p1 == "DDUDRLRRUDRD"


def test_part1_3() -> None:
    p1, _ = solve_parts("ulqzkmiv", 1)
    assert p1 == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "370"


def test_part2_2() -> None:
    _, p2 = solve_parts("kglvqrro", 2)
    assert p2 == "492"


def test_part2_3() -> None:
    _, p2 = solve_parts("ulqzkmiv", 2)
    assert p2 == "830"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("DDRRRD", "370")


def test_get_paths() -> None:
    assert InputData(TEST_STRING).get_paths() == ("DDRRRD", 370)


# ----------- Neighbors ------------


def test_neighbors_skip_out_of_bounds() -> None:
    # md5("") starts with d41d: up (d) is open but off-grid, down (4) and left (1) are locked, right (d) is open.
    assert list(State(0, 0).get_neighbors("")) == [State(1, 0, "R")]


def test_neighbors_return_to_start() -> None:
    assert list(State(1, 0, "R").get_neighbors("")) == [State(0, 0, "RL")]
