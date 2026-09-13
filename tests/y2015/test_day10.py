from aoc_py.y2015.day10 import InputData

# No specific day1 / day2 tests here, just run one round for each input.
# It would be far too slow to run the full 40/50 rounds in testing, and it
# would anyway just the same code being run multiple times.


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
