from aoc_py.y2016.day16 import InputData


def test_1() -> None:
    p = InputData("110010110100")
    p1 = p.get_checksum(12)
    assert p1 == "100"


def test_2() -> None:
    p = InputData("10000")
    p1 = p.get_checksum(20)
    assert p1 == "01100"
