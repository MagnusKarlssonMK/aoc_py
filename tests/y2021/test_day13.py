TEST_STRING_1 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

TEST_STRING_2 = """0,0
0,1
0,5
4,0

fold along x=3
fold along y=3"""

from aoc_py.y2021.day13 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "17"


def test_part1_2() -> None:
    """The folds have to be applied in the order they are given. Folding along y=3 first
    would merge the dot at 0,5 with the one at 0,1 straight away, leaving 3 rather than 4."""
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "4"


def test_part1_3() -> None:
    """Folding consumes the dots it is given, so a second run has to start again from the
    original dots."""
    p = InputData(TEST_STRING_1)
    assert p.fold_and_get_dots() == p.fold_and_get_dots() == 17


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "\n#####\n#...#\n#...#\n#...#\n#####\n.....\n.....\n"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "\n#.#\n#..\n...\n"
