from aoc_py.y2021.day16 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("8A004A801A8002F478", 1)
    assert p1 == "16"


def test_part1_2() -> None:
    p1, _ = solve_parts("620080001611562C8802118E34", 1)
    assert p1 == "12"


def test_part1_3() -> None:
    p1, _ = solve_parts("C0015000016115A2E0802F182340", 1)
    assert p1 == "23"


def test_part1_4() -> None:
    p1, _ = solve_parts("A0016C880162017C3686B18A3D4780", 1)
    assert p1 == "31"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("C200B40A82", 2)
    assert p2 == "3"


def test_part2_2() -> None:
    _, p2 = solve_parts("04005AC33890", 2)
    assert p2 == "54"


def test_part2_3() -> None:
    _, p2 = solve_parts("880086C3E88112", 2)
    assert p2 == "7"


def test_part2_4() -> None:
    _, p2 = solve_parts("CE00C43D881120", 2)
    assert p2 == "9"


def test_part2_5() -> None:
    _, p2 = solve_parts("D8005AC2A8F0", 2)
    assert p2 == "1"


def test_part2_6() -> None:
    _, p2 = solve_parts("F600BC2D8F", 2)
    assert p2 == "0"


def test_part2_7() -> None:
    _, p2 = solve_parts("9C005AC2F8F0", 2)
    assert p2 == "0"


def test_part2_8() -> None:
    _, p2 = solve_parts("9C0141080250320F1802104A08", 2)
    assert p2 == "1"
