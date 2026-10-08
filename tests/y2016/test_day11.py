TEST_STRING_1 = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""

TEST_STRING_2 = """The first floor contains a lithium generator and a lithium-compatible microchip.
The second floor contains a hydrogen generator and an elerium generator and a dilithium generator.
The third floor contains a hydrogen-compatible microchip and an elerium-compatible microchip and a dilithium-compatible microchip.
The fourth floor contains nothing relevant."""

# No items on the elevator's starting floor: the elevator can never move, so a minimal BFS exhausts the
# state space and proves the puzzle is unsolvable. The ", and " separators match the real-input item
# listing style.
TEST_STRING_3 = """The first floor contains nothing relevant.
The second floor contains a hydrogen generator, and a lithium generator.
The third floor contains a hydrogen-compatible microchip, and a lithium-compatible microchip.
The fourth floor contains nothing relevant."""

# Real-input item listings join a multi-item floor list with ", and " for the final item. This layout
# pins that form: dropping the item before ", and " (a parse-level error) would change the answer.
TEST_STRING_4 = """The first floor contains a hydrogen-compatible microchip.
The second floor contains a hydrogen generator, and a lithium generator.
The third floor contains nothing relevant."""

# A generator and a microchip of different items must not ride the elevator together. In this crossed
# layout such a "mixed" trip (hydrogen generator with the lithium chip from the first floor) would be
# the shortcut, so the guard is load-bearing here.
TEST_STRING_5 = """The first floor contains a hydrogen generator and a lithium-compatible microchip.
The second floor contains a hydrogen-compatible microchip and a lithium generator.
The third floor contains nothing relevant."""

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


# ----------- Edge cases ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_2) == ("25", "49")


def test_unsolvable_start() -> None:
    # The elevator starts on the first floor with nothing to move, so the puzzle is unsolvable.
    # Part 1 pins the -1 sentinel; part 2 is solvable (it injects two items on the first floor),
    # so only part 1 is asserted.
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "-1"


def test_comma_and_separator() -> None:
    # The ", and " item listing keeps the final item on the floor; both items must be parsed.
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "6"


def test_no_mixed_pair_trips() -> None:
    # A generator and a microchip of different items are not allowed on the elevator together.
    # Allowing the shortcut mixed trip drops the answer from 8 to 6.
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "8"
