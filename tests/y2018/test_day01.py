from aoc_py.y2018.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("+1\n-2\n+3\n+1", 1)
    assert p1 == "3"


def test_part1_2() -> None:
    p1, _ = solve_parts("+1\n+1\n+1", 1)
    assert p1 == "3"


def test_part1_3() -> None:
    p1, _ = solve_parts("+1\n+1\n-2", 1)
    assert p1 == "0"


def test_part1_4() -> None:
    p1, _ = solve_parts("-1\n-2\n-3", 1)
    assert p1 == "-6"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("+1\n-2\n+3\n+1", 2)
    assert p2 == "2"


def test_part2_2() -> None:
    _, p2 = solve_parts("+1\n-1", 2)
    assert p2 == "0"


def test_part2_3() -> None:
    _, p2 = solve_parts("+3\n+3\n+4\n-2\n-4", 2)
    assert p2 == "10"


def test_part2_4() -> None:
    _, p2 = solve_parts("-6\n+3\n+8\n+5\n-6", 2)
    assert p2 == "5"


def test_part2_5() -> None:
    _, p2 = solve_parts("+7\n+7\n-2\n-7\n-4", 2)
    assert p2 == "14"
