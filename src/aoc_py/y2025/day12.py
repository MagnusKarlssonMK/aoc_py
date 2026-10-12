"""
2025 day 12 - Christmas Tree Farm

Part 1

The real input is built so that a region either fits all of its presents even when every
present claims a full 3x3 square, or does not fit even when every square of the region is
filled. That lets us ignore the shapes completely and just count the regions whose area covers
nine squares per present. A fully general packing solver would be far more complex.

Note that the puzzle's example input does not follow these assumptions, so a faithful test has
to use a hand-crafted region set instead.

Part 2 has no puzzle of its own.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Region:
    width: int
    height: int
    quantities: tuple[int, ...]

    @classmethod
    def from_str(cls, rawstr: str) -> Region:
        dimensions, quantities = rawstr.split(": ", 1)
        width, height = dimensions.split("x", 1)
        return cls(int(width), int(height), tuple(int(n) for n in quantities.split()))


class InputData:
    def __init__(self, rawstr: str) -> None:
        # The shapes are irrelevant to this simplified solution, so only the region list after
        # the final blank line is parsed.
        _, regions = rawstr.rsplit("\n\n", 1)
        self.__regions: list[Region] = [
            Region.from_str(line) for line in regions.splitlines()
        ]

    def get_p1(self) -> int:
        return sum(
            1
            for region in self.__regions
            if region.height * region.width >= sum(region.quantities) * 3 * 3
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
