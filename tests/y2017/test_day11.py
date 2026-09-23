from aoc_py.y2017.day11 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("ne,ne,ne", 1)
    assert p1 == "3"


def test_part1_2() -> None:
    p1, _ = solve_parts("ne,ne,sw,sw", 1)
    assert p1 == "0"


def test_part1_3() -> None:
    p1, _ = solve_parts("ne,ne,s,s", 1)
    assert p1 == "2"


def test_part1_4() -> None:
    p1, _ = solve_parts("se,sw,se,sw,sw", 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("ne,ne,ne", 2)
    assert p2 == "3"


def test_part2_2() -> None:
    _, p2 = solve_parts("ne,ne,sw,sw", 2)
    assert p2 == "2"


def test_part2_3() -> None:
    _, p2 = solve_parts("ne,ne,s,s", 2)
    assert p2 == "2"


def test_part2_4() -> None:
    _, p2 = solve_parts("se,sw,se,sw,sw", 2)
    assert p2 == "3"
