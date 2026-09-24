"""
2018 day 6 - Chronal Coordinates

Key point here is that the min and max values in each direction forms a "frame", and any location outside that will
extend to infinity. I.e. any coordinate having a location as 'closest' on or outside that area will have an infinite
area.
"""

from collections.abc import Generator

from aoc_py.util.point import Point


class InputData:
    def __init__(self, s: str) -> None:
        self.__points = [Point.from_str(line) for line in s.splitlines()]
        self.__x_range = range(self.__points[0].x, self.__points[0].x + 1)
        self.__y_range = range(self.__points[0].y, self.__points[0].y + 1)
        for c in self.__points:
            self.__x_range = range(
                min(c.x, self.__x_range.start), max(c.x + 1, self.__x_range.stop)
            )
            self.__y_range = range(
                min(c.y, self.__y_range.start), max(c.y + 1, self.__y_range.stop)
            )

    def __get_locations(self) -> Generator[Point]:
        for x in self.__x_range:
            for y in self.__y_range:
                yield Point(x, y)

    def get_p1(self) -> int:
        areas: dict[Point, set[Point]] = {}
        # Find areas for each coordinate, i.e. coordinates that have the closest manhattan distance to only that coord
        for loc in self.__get_locations():
            distances = sorted(
                [(loc.manhattan(c), i) for i, c in enumerate(self.__points)],
                key=lambda x: x[0],
            )
            if len(distances) == 1 or distances[0][0] < distances[1][0]:
                if self.__points[distances[0][1]] not in areas:
                    areas[self.__points[distances[0][1]]] = set()
                areas[self.__points[distances[0][1]]].add(loc)
        # Remove the coords that have infinite areas, i.e. are located on the range border
        infinite_areas: set[Point] = set()
        for a, val in areas.items():
            for c in val:
                if any(
                    [
                        c.x == self.__x_range.start,
                        c.x == self.__x_range.stop - 1,
                        c.y == self.__y_range.start,
                        c.y == self.__y_range.stop - 1,
                    ]
                ):
                    infinite_areas.add(a)
                    break
        for i in infinite_areas:
            areas.pop(i)
        return max(len(areas[a]) for a in areas)

    def get_p2(self, max_total_distance: int = 10_000) -> int:
        # For each location, find the total distance to all coordinates and see if it is smaller than max
        return sum(
            [
                1
                for loc in self.__get_locations()
                if sum([loc.manhattan(c) for c in self.__points]) < max_total_distance
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
