TEST_STRING = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

from aoc_py.y2023.day15 import solve_parts

# ----------- Part 1 ------------

def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "1320"


# ----------- Part 2 ------------

def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "145"
