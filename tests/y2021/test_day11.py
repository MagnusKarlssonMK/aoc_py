TEST_STRING_1 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

TEST_STRING_2 = """567
789
123"""

from aoc_py.y2021.day11 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1656"


def test_part1_2() -> None:
    """This grid flashes as a whole on step 61, so part 1 has to keep simulating to
    step 100 rather than stopping at the first full flash."""
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "110"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "195"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "61"


def test_part2_3() -> None:
    """The run must be repeatable, so calling get_flashcounts twice on one object
    has to give the same answer both times."""
    p = InputData(TEST_STRING_2)
    assert p.get_flashcounts() == p.get_flashcounts() == (110, 61)
