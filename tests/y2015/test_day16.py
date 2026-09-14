TEST_STRING = """Sue 1: goldfish: 5, cars: 2, children: 3
Sue 2: cats: 8, trees: 4, pomeranians: 2
Sue 3: akitas: 1, vizslas: 2, goldfish: 10"""


from aoc_py.y2015.day16 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "2"
