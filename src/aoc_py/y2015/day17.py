"""
2015 day 17 - No Such Thing as Too Much

Part 1 wants the number of ways to pick containers that come to exactly 150 litres, and part 2 wants
that number restricted to the picks that use the fewest containers. Both questions are answered from
the same set of matches, so the scan enumerates every combination of one container up to all of them
and records the size of each one that lands on the target. Part 1 is the length of that list and part
2 is how often its smallest entry appears.
"""

from itertools import combinations


class InputData:
    def __init__(self, s: str) -> None:
        self.__containers = [int(n) for n in s.splitlines()]
        self.__matching: list[int] | None = None
        # For handling different target amount for the smaller test input:
        self.__target_amount: int = 150 if sum(self.__containers) >= 150 else 25

    def __matching_sizes(self) -> list[int]:
        """The size of every combination of containers that sums to the target."""
        if self.__matching is None:
            sizes: list[int] = []
            for comb_count in range(1, len(self.__containers) + 1):
                for c in combinations(self.__containers, comb_count):
                    if sum(c) == self.__target_amount:
                        sizes.append(len(c))
            self.__matching = sizes
        return self.__matching

    def get_p1(self) -> int:
        sizes = self.__matching_sizes()
        # An empty list means no combination reaches the target, leaving us with no solution
        return len(sizes) if sizes else -1

    def get_p2(self) -> int:
        sizes = self.__matching_sizes()
        # An empty list means no combination reaches the target, leaving us with no solution
        return sizes.count(min(sizes)) if sizes else -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
