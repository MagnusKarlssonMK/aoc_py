from aoc_py.y2020.day15 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("0,3,6", 1)
    assert p1 == "436"


def test_part1_2() -> None:
    p1, _ = solve_parts("1,3,2", 1)
    assert p1 == "1"


def test_part1_3() -> None:
    p1, _ = solve_parts("2,1,3", 1)
    assert p1 == "10"


def test_part1_4() -> None:
    p1, _ = solve_parts("1,2,3", 1)
    assert p1 == "27"


def test_part1_5() -> None:
    p1, _ = solve_parts("2,3,1", 1)
    assert p1 == "78"


def test_part1_6() -> None:
    p1, _ = solve_parts("3,2,1", 1)
    assert p1 == "438"


def test_part1_7() -> None:
    p1, _ = solve_parts("3,1,2", 1)
    assert p1 == "1836"


# ----------- Part 2 ------------

# Skip testing of part 2 since it is so slow, and anyway just running the same
# function as in part 1 but with a lot more iterations.

# def test_part2_1() -> None:
#    _, p2 = solve_parts("1", 2)
#    assert p2 == "1"
