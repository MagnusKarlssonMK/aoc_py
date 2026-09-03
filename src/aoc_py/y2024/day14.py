"""
2024 day 14 - Restroom Redoubt

Part 1

No need to run the simulation for 100 steps, just directly calculate the positions.

Part 2

Run the simulation until all robots are in unique positions with no overlap.
"""

from math import prod


class Robot:
    def __init__(self, rawstr: str) -> None:
        left, right = rawstr.split()
        left_x, left_y = left.split(",")
        right_x, right_y = right.split(",")
        self.pos: tuple[int, int] = int(left_x.strip("p=")), int(left_y)
        self.vel: tuple[int, int] = int(right_x.strip("v=")), int(right_y)


class InputData:
    def __init__(self, rawstr: str, x_max: int, y_max: int) -> None:
        self.__robots = [Robot(r) for r in rawstr.splitlines()]
        self.__x_max = x_max
        self.__y_max = y_max

    def get_p1(self) -> int:
        middle_x = (self.__x_max - 1) // 2
        middle_y = (self.__y_max - 1) // 2
        quadrants = [0, 0, 0, 0]
        for r in self.__robots:
            x_100 = (r.pos[0] + 100 * r.vel[0]) % self.__x_max
            y_100 = (r.pos[1] + 100 * r.vel[1]) % self.__y_max
            if x_100 != middle_x and y_100 != middle_y:
                quadrants[x_100 // (middle_x + 1) + 2 * (y_100 // (middle_y + 1))] += 1
        return prod(quadrants)

    def get_p2(self) -> int:
        points: set[tuple[int, int]] = set()
        time = 0
        overlap = True
        while overlap:
            time += 1
            overlap = False
            for r in self.__robots:
                newpoint_x = (r.pos[0] + time * r.vel[0]) % self.__x_max
                newpoint_y = (r.pos[1] + time * r.vel[1]) % self.__y_max
                if (newpoint_x, newpoint_y) in points:
                    overlap = True
                    break
                else:
                    points.add((newpoint_x, newpoint_y))
            points.clear()
        return time


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata, 101, 103)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
