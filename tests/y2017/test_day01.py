from aoc_py.y2017.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("1122", 1)
    assert p1 == "3"


def test_part1_2() -> None:
    p1, _ = solve_parts("1111", 1)
    assert p1 == "4"


def test_part1_3() -> None:
    p1, _ = solve_parts("1234", 1)
    assert p1 == "0"


def test_part1_4() -> None:
    p1, _ = solve_parts("91212129", 1)
    assert p1 == "9"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("1212", 2)
    assert p2 == "6"


def test_part2_2() -> None:
    _, p2 = solve_parts("1221", 2)
    assert p2 == "0"


def test_part2_3() -> None:
    _, p2 = solve_parts("123425", 2)
    assert p2 == "4"


def test_part2_4() -> None:
    _, p2 = solve_parts("123123", 2)
    assert p2 == "12"


def test_part2_5() -> None:
    _, p2 = solve_parts("12131415", 2)
    assert p2 == "4"
