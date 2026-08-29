from collections import defaultdict
from math import log10


def blink(stones: dict[int, int]) -> dict[int, int]:
    newstones: dict[int, int] = defaultdict(int)
    for stone, amount in stones.items():
        if stone == 0:
            newstones[1] += amount
        else:
            if int(digits := 1 + log10(stone)) % 2 == 0:
                power = int(10**(digits // 2))
                newstones[stone // power] += amount
                newstones[stone % power] += amount
            else:
                newstones[stone * 2024] += amount
    return newstones


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__stones = [int(n) for n in rawstr.split()]

    def get_stone_count(self, blinks1: int, blinks2: int) -> tuple[int, int]:
        results: list[int] = []
        blink_counter = 0
        stones: dict[int, int] = {s: 1 for s in self.__stones}
        while len(results) < 2:
            blink_counter += 1
            stones = blink(stones)
            if blink_counter in (blinks1, blinks2):
                results.append(sum(stones.values()))
        return results[0], results[1]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        part1, part2 = p.get_stone_count(25, 75)
        if part in (None, 1):
            p1 = str(part1)
        if part in (None, 2):
            p2 = str(part2)

        return p1, p2
