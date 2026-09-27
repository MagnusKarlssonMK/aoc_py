"""
2023 day 5 - If You Give A Seed A Fertilizer

Each layer is a list of mappings, one per line, giving the start of a destination range, the start of the matching
source range and the length of both, and the layers are applied in the order they are parsed.
A value that a mapping covers is shifted by the offset of that mapping and never reaches the mappings after it,
while a value that no mapping covers is passed on unchanged.
Mapping a range instead splits it: a mapping covering part of the range shifts the covered fragment and hands the
fragments before and after it to the remaining mappings of the layer.
Part 1 maps the seeds one by one, and part 2 maps the seed ranges, and both answers are the lowest value left.
"""

from collections.abc import Generator
from dataclasses import dataclass


@dataclass(frozen=True)
class MapFilter:
    source: range
    offset: int


class Map:
    def __init__(self, block: str) -> None:
        self.__filterlist: list[MapFilter] = []
        for line in block.splitlines()[1:]:
            dest_start, source_start, size = map(int, line.split())
            self.__filterlist.append(
                MapFilter(
                    range(source_start, source_start + size), dest_start - source_start
                )
            )

    def map_number(self, nbr: int) -> int:
        for mapfilter in self.__filterlist:
            if nbr in mapfilter.source:
                return nbr + mapfilter.offset
        return nbr

    def map_range(self, i: range) -> Generator[range]:
        for f in self.__filterlist:
            if (
                f.source.start < i.stop and f.source.stop > i.start
            ):  # At least some overlap
                if (
                    f.source.start <= i.start and i.stop <= f.source.stop
                ):  # Filter completely covers input range
                    yield range(i.start + f.offset, i.stop + f.offset)
                    return
                if (
                    i.start < f.source.start and f.source.stop < i.stop
                ):  # Input range sticks out on both sides
                    yield from self.map_range(range(i.start, f.source.start))
                    yield range(f.source.start + f.offset, f.source.stop + f.offset)
                    yield from self.map_range(range(f.source.stop, i.stop))
                    return
                if (
                    f.source.start <= i.start and f.source.stop < i.stop
                ):  # Input range sticks out only above
                    yield range(i.start + f.offset, f.source.stop + f.offset)
                    yield from self.map_range(range(f.source.stop, i.stop))
                    return
                if (
                    i.start < f.source.start and i.stop <= f.source.stop
                ):  # Input range sticks out only below
                    yield from self.map_range(range(i.start, f.source.start))
                    yield range(f.source.start + f.offset, i.stop + f.offset)
                    return
            # else - no overlap, try next filter
        yield i


class InputData:
    def __init__(self, rawstr: str) -> None:
        blocks = rawstr.split("\n\n")
        self.__seeds: list[int] = [int(seed) for seed in blocks[0].split()[1:]]
        self.__maps: list[Map] = [Map(block) for block in blocks[1:]]

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
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
