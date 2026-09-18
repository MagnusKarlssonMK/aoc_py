TEST_STRING_1 = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""

TEST_STRING_2 = """The first floor contains a lithium generator and a lithium-compatible microchip.
The second floor contains a hydrogen generator and an elerium generator and a dilithium generator.
The third floor contains a hydrogen-compatible microchip and an elerium-compatible microchip and a dilithium-compatible microchip.
The fourth floor contains nothing relevant."""

from aoc_py.y2016.day11 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "11"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "25"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "49"
