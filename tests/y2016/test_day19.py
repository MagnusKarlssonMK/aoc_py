TEST_STRING = """5"""

from aoc_py.y2016.day19 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


def test_part1_known_values() -> None:
    expected = {1: 1, 2: 1, 3: 3, 4: 1, 5: 3, 6: 5, 7: 7, 8: 1, 9: 3, 10: 5}
    for n, winner in expected.items():
        assert InputData(str(n)).get_p1() == winner


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "2"


def test_part2_known_values() -> None:
    expected = {
        1: 1,
        2: 1,
        3: 3,
        4: 1,
        5: 2,
        6: 3,
        7: 5,
        8: 7,
        9: 9,
        10: 1,
        19: 11,
        27: 27,
    }
    for n, winner in expected.items():
        assert InputData(str(n)).get_p2() == winner


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("3", "2")
