from aoc_py.y2018.day14 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("9", 1)
    assert p1 == "5158916779"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("51589", 2)
    assert p2 == "9"


def test_part2_two_recipe() -> None:
    # The first generation appends "10", so the target 1 is found one position
    # before the end (the "two new recipes" check).
    _, p2 = solve_parts("1", 2)
    assert p2 == "2"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts("2018") == ("5941429882", "86764")
