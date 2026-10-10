from aoc_py.y2017.day10 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p = InputData("3,4,1,5")
    p1 = p.get_p1(5)
    assert p1 == 12


def test_part1_solve_parts() -> None:
    # solve_parts runs with the default 256-element buffer (not the 5 from the
    # official example), so the product differs from test_part1_1.
    assert solve_parts("3,4,1,5", 1) == ("2", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("", 2)
    assert p2 == "a2582a3a0e66e6e86e3812dcb672a272"


def test_part2_2() -> None:
    _, p2 = solve_parts("AoC 2017", 2)
    assert p2 == "33efeb34ea91902bb2f59c9920caa6cd"


def test_part2_3() -> None:
    _, p2 = solve_parts("1,2,3", 2)
    assert p2 == "3efbe78a8d82f29979031a4aa0b16a9d"


def test_part2_4() -> None:
    _, p2 = solve_parts("1,2,4", 2)
    assert p2 == "63960835bcdc130f0b66d7ff4f6a5a8e"


def test_part2_solve_parts() -> None:
    assert solve_parts("1,2,3", 2) == ("-1", "3efbe78a8d82f29979031a4aa0b16a9d")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts("3,4,1,5") == ("2", "4a19451b02fb05416d73aea0ec8c00c0")
