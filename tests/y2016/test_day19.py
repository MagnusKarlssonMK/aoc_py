from aoc_py.y2016.day19 import get_winning_elf, get_winning_elf_opposite

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1 = get_winning_elf(5)
    assert p1 == 3


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p2 = get_winning_elf_opposite(5)
    assert p2 == 2
