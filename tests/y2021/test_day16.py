from aoc_py.y2021.day16 import InputData, solve_parts

# A hand built transmission: v1 SUM count=3 { v2 GT count=2 {LIT 10, LIT 10},
# v3 LT count=2 {LIT 5, LIT 5}, v0 LIT 7 }. None of the official examples compare two equal
# operands, and that is the only case where GT/LT differ from their non strict counterparts.
TEST_STRING_2 = "2200D5802114229E80210A214438"

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


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "6"


def test_part1_6() -> None:
    """decodestream() accumulates into versionsum, so a second call on the same object has to
    start counting from zero again or the version sum doubles."""
    decoder = InputData("8A004A801A8002F478")
    _ = decoder.decodestream()
    first = decoder.versionsum
    _ = decoder.decodestream()
    assert decoder.versionsum == first == 16


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


def test_part2_9() -> None:
    """Both comparisons here are on equal operands, so they have to be strict. Treating them as
    >= and <= makes one of the two come out as 1 and the part 2 total 8 rather than 7."""
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "7"
