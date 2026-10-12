from aoc_py.y2024.day24 import solve_parts

TEST_STRING_1 = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

TEST_STRING_2 = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

# A complete 4-bit ripple carry adder (x00..x03 + y00..y03 -> z00..z04) with the
# outputs of (a1, d1), (z01, a3) and (z04, z02) crossed, exercising every rule
# used to spot the swapped wires.
TEST_STRING_3 = """x00: 0
x01: 0
x02: 0
x03: 0
y00: 0
y01: 0
y02: 0
y03: 0

x00 XOR y00 -> z00
x00 AND y00 -> c0
x01 XOR y01 -> d1
a1 XOR c0 -> a3
x01 AND y01 -> a1
a1 AND c0 -> e1
d1 OR e1 -> c1
x02 XOR y02 -> a2
a2 XOR c1 -> z04
x02 AND y02 -> d2
a2 AND c1 -> e2
d2 OR e2 -> c2
x03 XOR y03 -> z01
a3 XOR c2 -> z03
x03 AND y03 -> d3
a3 AND c2 -> e3
d3 OR e3 -> z02"""

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "2024"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "a1,a3,d1,z01,z02"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_1) == ("4", "z01")
