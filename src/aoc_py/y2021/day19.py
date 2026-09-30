"""
2021 day 19 - Beacon Scanner

Scanner 0 is taken as the origin and every other scanner is aligned to the ones already placed, one at a time.
Instead of trying all 24 orientations, each output axis is resolved on its own: the sign and direction for which
the most beacon pairs agree on a single difference fix that axis, and NBR_OF_BEACONS agreeing pairs are what a
scanner must reach before it is accepted. Part 2 asks for the greatest distance between any two scanners, and
the anchor is one of them, so the origin goes into the offset list before anything has been aligned.
"""

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from typing import Final

NBR_OF_BEACONS: Final = 12


@dataclass(frozen=True)
class Point3d:
    x: int
    y: int
    z: int

    def get_manhattan(self, other: Point3d) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def get_values(self) -> tuple[int, int, int]:
        return self.x, self.y, self.z


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__scanners: dict[int, set[Point3d]] = {}
        for i, block in enumerate(rawstr.split("\n\n")):
            self.__scanners[i] = {
                Point3d(*map(int, line.split(","))) for line in block.splitlines()[1:]
            }
        self.__offsets: list[Point3d] = [Point3d(0, 0, 0)]
        self.__mapcreated: bool = False

    def __create_map(self) -> None:
        if self.__mapcreated:
            return
        self.__mapcreated = True
        aligned = [0]
        queue = [s for s in self.__scanners if s not in aligned]

        while queue:
            for a in aligned:
                offset_list: list[int] = []
                rotation: list[tuple[int, int]] = []
                found = -1
                for u in queue:
                    for base_i in range(3):
                        for sign, direction in [
                            (1, 0),
                            (-1, 0),
                            (1, 1),
                            (-1, 1),
                            (1, 2),
                            (-1, 2),
                        ]:
                            delta = [
                                b0.get_values()[base_i]
                                - sign * b1.get_values()[direction]
                                for b1 in self.__scanners[u]
                                for b0 in self.__scanners[a]
                            ]
                            offset, matches = Counter(delta).most_common()[0]
                            if matches >= NBR_OF_BEACONS:
                                offset_list.append(offset)
                                rotation.append((sign, direction))
                    if len(offset_list) > 0:
                        found = u
                        break
                if found >= 0:
                    queue.remove(found)
                    aligned.append(found)
                    self.__offsets.append(Point3d(*offset_list))
                    scanner_aligned = [
                        [x, y, z]
                        for x, y, z in [b.get_values() for b in self.__scanners[found]]
                    ]
                    scanner_aligned = [
                        [
                            rotation[0][0] * xyz[rotation[0][1]],
                            rotation[1][0] * xyz[rotation[1][1]],
                            rotation[2][0] * xyz[rotation[2][1]],
                        ]
                        for xyz in scanner_aligned
                    ]
                    scanner_aligned = [
                        Point3d(
                            x + offset_list[0], y + offset_list[1], z + offset_list[2]
                        )
                        for x, y, z in scanner_aligned
                    ]
                    self.__scanners[found] = set(scanner_aligned)

    def get_p1(self) -> int:
        self.__create_map()
        return len({b for s in self.__scanners for b in self.__scanners[s]})

    def get_p2(self) -> int:
        self.__create_map()
        return max(
            [
                self.__offsets[i].get_manhattan(self.__offsets[j])
                for i, j in combinations(range(len(self.__offsets)), 2)
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
