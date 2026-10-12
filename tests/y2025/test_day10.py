TEST_STRING = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

EXTRA_1 = "[##..##..] (0,1,3,4,5,6) (2,4,6) (1,5,6,7) (0,4,5) (3,6) (1,2,3,5,6) (0,2,4,5,6,7) {31,34,131,26,148,48,168,25}"
EXTRA_2 = "[.##...#.] (4,5) (0,1,2,3,7) (0,1,2,3,6) (0,1,2,4,6,7) (3,4,7) (0,3,6,7) {64,50,50,174,163,15,50,176}"
EXTRA_3 = "[.##..] (1,2) (0,2,3,4) (0,1,3,4) {17,20,19,17,17}"
EXTRA_4 = "[###] (0,1) (0,2) (1,2) {2,2,2}"

from aoc_py.y2025.day10 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "7"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "33"


def test_part2_extras_1() -> None:
    _, p2 = solve_parts(EXTRA_1, 2)
    assert p2 == "171"


def test_part2_extras_2() -> None:
    _, p2 = solve_parts(EXTRA_2, 2)
    assert p2 == "208"


def test_part2_extras_3() -> None:
    _, p2 = solve_parts(EXTRA_3, 2)
    assert p2 == "28"


def test_part2_extras_4() -> None:
    _, p2 = solve_parts(EXTRA_4, 2)
    assert p2 == "3"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("7", "33")
