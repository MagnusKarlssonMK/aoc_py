from aoc_py.y2015.day10 import InputData, solve_parts


def test_part1_1() -> None:
    test_input = InputData("1")
    assert test_input.get_generated_length(1) == 2


def test_part1_2() -> None:
    test_input = InputData("11")
    assert test_input.get_generated_length(1) == 2


def test_part1_3() -> None:
    test_input = InputData("21")
    assert test_input.get_generated_length(1) == 4


def test_part1_4() -> None:
    test_input = InputData("1211")
    assert test_input.get_generated_length(1) == 6


def test_part1_5() -> None:
    test_input = InputData("111221")
    assert test_input.get_generated_length(1) == 6


# One run of two equal digits is a fixed point: every round emits the same thing, so both parts answer 2 however many
# rounds they run. Cheap enough to sit in the suite, and it still drives solve_parts end to end.
def test_part1_6() -> None:
    p1, _ = solve_parts("22", 1)
    assert p1 == "2"


def test_part2_6() -> None:
    _, p2 = solve_parts("22", 2)
    assert p2 == "2"


# The only input that tells the two parts apart. Every other starting point cheap enough for a test is either a fixed
# point or too short for 40 and 50 rounds to have diverged, so without this the round counts themselves are unpinned.
def test_part1_7() -> None:
    p1, _ = solve_parts("1", 1)
    assert p1 == "82350"


def test_part2_7() -> None:
    _, p2 = solve_parts("1", 2)
    assert p2 == "1166642"
