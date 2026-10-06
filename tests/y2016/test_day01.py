from aoc_py.y2016.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("R2, L3", 1)
    assert p1 == "5"


def test_part1_2() -> None:
    p1, _ = solve_parts("R2, R2, R2", 1)
    assert p1 == "2"


def test_part1_3() -> None:
    p1, _ = solve_parts("R5, L5, R5, R3", 1)
    assert p1 == "12"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("R8, R4, R4, R8", 2)
    assert p2 == "4"


def test_part2_2() -> None:
    _, p2 = solve_parts("R1, L1, L1, L1, R3", 2)
    assert p2 == "0"


def test_part2_3() -> None:
    _, p2 = solve_parts("R2, L3", 2)
    assert p2 == "-1"


def test_part2_4() -> None:
    _, p2 = solve_parts("L1, L1, R1, R1, R1", 2)
    assert p2 == "1"


# ----------- Both parts ------------


def test_both_parts() -> None:
    p1, p2 = solve_parts("R8, R4, R4, R8")
    assert (p1, p2) == ("8", "4")
