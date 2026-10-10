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


def test_part1_solve_parts() -> None:
    assert solve_parts("23", 1) == ("2", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("750", 2)
    assert p2 == "806"


def test_part2_solve_parts() -> None:
    assert solve_parts("750", 2) == ("-1", "806")


# ----------- Edge cases ------------


def test_smallest_input() -> None:
    # Both loops are skipped entirely for the center.
    assert solve_parts("1") == ("0", "1")


def test_part2_value_equals_target() -> None:
    # Part 2 exits on value == target (the "while value < target" boundary), returning 23 not the next larger cell.
    assert solve_parts("23") == ("2", "23")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts("1024") == ("31", "1968")
