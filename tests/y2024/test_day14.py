TEST_STRING = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

from aoc_py.y2024.day14 import InputData, solve_parts

# ----------- Part 1 ------------

def test_part1_1() -> None:
    p = InputData(TEST_STRING, 11, 7)
    p1 = p.get_p1()
    assert p1 == 12


# ----------- Part 2 ------------

def test_part2_1() -> None:
    p = InputData(TEST_STRING, 11, 7)
    p1 = p.get_p2()
    assert p1 == 1

def test_part2_2() -> None:
    p1, p2 = solve_parts(TEST_STRING)
    assert p1 == "21"
    assert p2 == "1"
