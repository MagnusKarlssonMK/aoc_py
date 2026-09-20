from aoc_py.y2016.day18 import InputData


def test_1() -> None:
    p = InputData("..^^.")
    p1 = p.get_safetile_count(3)
    assert p1 == 6


def test_2() -> None:
    p = InputData(".^^.^.^^^^")
    p1 = p.get_safetile_count(10)
    assert p1 == 38
