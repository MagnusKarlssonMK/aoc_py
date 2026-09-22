from aoc_py.y2017.day03 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("1", 1)
    assert p1 == "0"


def test_part1_2() -> None:
    p1, _ = solve_parts("12", 1)
    assert p1 == "3"


def test_part1_3() -> None:
    p1, _ = solve_parts("23", 1)
    assert p1 == "2"


def test_part1_4() -> None:
    p1, _ = solve_parts("1024", 1)
    assert p1 == "31"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("750", 2)
    assert p2 == "806"
