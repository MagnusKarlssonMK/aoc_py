from aoc_py.y2019.day16 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("80871224585914546619083218645595", 1)
    assert p1 == "24176176"


def test_part1_2() -> None:
    p1, _ = solve_parts("19617804207202209144916044189917", 1)
    assert p1 == "73745418"


def test_part1_3() -> None:
    p1, _ = solve_parts("69317163492948606335995924319873", 1)
    assert p1 == "52432133"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("03036732577212944063491565474664", 2)
    assert p2 == "84462026"


def test_part2_2() -> None:
    _, p2 = solve_parts("02935109699940807407585447034323", 2)
    assert p2 == "78725270"


def test_part2_3() -> None:
    _, p2 = solve_parts("03081770884921959731165446850517", 2)
    assert p2 == "53553731"
