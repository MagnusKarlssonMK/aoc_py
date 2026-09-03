"""
2023 day 5 - If You Give A Seed A Fertilizer

No need to actually make any dict of the different conversion layers, just put them all in an array
in the order of parsing it and process them one by one.
"""

from collections.abc import Generator
from dataclasses import dataclass


@dataclass(frozen=True)
class Mapfilter:
    mask: range
    offset: int


class Map:
    def __init__(self, mapinput: list[str]) -> None:
        self.__filterlist: list[Mapfilter] = []
        for line in mapinput[1:]:
            dest_start, source_start, size = map(int, line.split())
            self.__filterlist.append(
                Mapfilter(
                    range(source_start, source_start + size), dest_start - source_start
                )
            )

    def map_number(self, nbr: int) -> int:
        for mapfilter in self.__filterlist:
            if nbr in mapfilter.mask:
                return nbr + mapfilter.offset
        return nbr

    def map_range(self, i: range) -> Generator[range]:
        for f in self.__filterlist:
            if f.mask.start < i.stop and f.mask.stop > i.start:  # At least some overlap
                if (
                    f.mask.start <= i.start and i.stop <= f.mask.stop
                ):  # Filter completely covers input range
                    yield range(i.start + f.offset, i.stop + f.offset)
                    return
                if (
                    i.start < f.mask.start and f.mask.stop < i.stop
                ):  # Input range sticks out on both sides
                    yield from self.map_range(range(i.start, f.mask.start))
                    yield range(f.mask.start + f.offset, f.mask.stop + f.offset)
                    yield from self.map_range(range(f.mask.stop, i.stop))
                    return
                if (
                    f.mask.start <= i.start and f.mask.stop < i.stop
                ):  # Input range sticks out only above
                    yield range(i.start + f.offset, f.mask.stop + f.offset)
                    yield from self.map_range(range(f.mask.stop, i.stop))
                    return
                if (
                    i.start < f.mask.start and i.stop <= f.mask.stop
                ):  # Input range sticks out only below
                    yield from self.map_range(range(i.start, f.mask.start))
                    yield range(f.mask.start + f.offset, i.stop + f.offset)
                    return
            # else - no overlap, try next filter
        yield i


class InputData:
    def __init__(self, rawstr: str) -> None:
        blocks = rawstr.split("\n\n")
        self.__seeds: list[int] = [int(seed) for seed in blocks[0].split()[1:]]
        self.__maps = [m for m in [Map(block.splitlines()) for block in blocks[1:]]]

    def get_p1(self) -> int:
        currentseeds = list(self.__seeds)
        for layer in self.__maps:
            currentseeds = [layer.map_number(seed) for seed in currentseeds]
        return min(currentseeds)

    def get_p2(self) -> int:
        seedranges: list[range] = [
            range(self.__seeds[idx], self.__seeds[idx] + self.__seeds[idx + 1])
            for idx in range(0, len(self.__seeds), 2)
        ]
        for layer in self.__maps:
            seedranges = [
                newrange for s in seedranges for newrange in layer.map_range(s)
            ]

        return min([r.start for r in seedranges])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
