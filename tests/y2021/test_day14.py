TEST_STRING_1 = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

TEST_STRING_2 = """ABAB

AA -> A
AB -> A
BA -> A
BB -> A"""

from aoc_py.y2021.day14 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1588"


def test_part1_2() -> None:
    """The template ABAB holds the pair AB twice, so the starting counts have to accumulate
    rather than overwrite. Spreading the two AB pairs over the template instead of adding them
    up gives 2045 rather than 3069."""
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "3069"


def test_part1_3() -> None:
    """Every call to run_steps advances the polymer a further 40 steps, so the starting pair
    counts have to be restored first."""
    p = InputData(TEST_STRING_1)
    assert p.run_steps() == p.run_steps() == (1588, 2188189693529)


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "2188189693529"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "3298534883325"
