TEST_STRING = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

from aoc_py.y2020.day21 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "5"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "mxmxvkd,sqjhc,fvjkl"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("5", "mxmxvkd,sqjhc,fvjkl")


def test_parts_are_order_independent() -> None:
    p = InputData(TEST_STRING)
    assert (p.get_p2(), p.get_p1()) == ("mxmxvkd,sqjhc,fvjkl", 5)
