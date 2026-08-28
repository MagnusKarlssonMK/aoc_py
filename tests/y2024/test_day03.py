from aoc_py.y2024.day03 import solve_parts

# ----------- Part 1 ------------

def test_part1_1() -> None:
    p1, _ = solve_parts("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 1)
    assert p1 == "161"


# ----------- Part 2 ------------

def test_part2_1() -> None:
    _, p2 = solve_parts("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 2)
    assert p2 == "48"
