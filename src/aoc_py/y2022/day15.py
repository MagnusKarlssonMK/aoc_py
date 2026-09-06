"""
2022 day 15 - Beacon Exclusion Zone
"""

from collections.abc import Generator

from aoc_py.util.point import Point


def mergeintervals(intervallist: list[list[int]]) -> Generator[list[int]]:
    intervallist.sort()
    intqueue = [intervallist[0]]
    for i in intervallist[1:]:
        if intqueue[-1][0] <= i[0] <= intqueue[-1][-1]:
            intqueue[-1][-1] = max(intqueue[-1][-1], i[-1])
        else:
            intqueue.append(i)

    for i in range(len(intqueue)):
        yield intqueue[i]


class Sensor:
    def __init__(self, s: str) -> None:
        left, right = s.split(": ")
        pos_left, pos_right = left.split(", y=")
        _, pos_left = pos_left.split("=")
        self.position: Point = Point(int(pos_left), int(pos_right))
        b_left, b_right = right.split(", y=")
        _, b_left = b_left.split("=")
        self.beacon: Point = Point(int(b_left), int(b_right))
        self.range: int = self.position.manhattan(self.beacon)

    def is_inrange(self, position: Point) -> bool:
        return self.range >= self.position.manhattan(position)


class InputData:
    def __init__(self, s: str):
        self.sensors: list[Sensor] = [Sensor(line) for line in s.splitlines()]

    def get_coverage(self, row: int) -> int:
        p1_rangelist: list[list[int]] = []  # Start, stop
        for sensor in self.sensors:
            if (x_at_y := sensor.range - abs(row - sensor.position.y)) > 0:
                p1_rangelist.append(
                    [sensor.position.x - x_at_y, sensor.position.x + x_at_y]
                )
        # Merge overlapping ranges
        filtered_rangelist: list[list[int]] = [r for r in mergeintervals(p1_rangelist)]
        # Total number of tiles covered:
        totalcount = sum([1 + x[1] - x[0] for x in filtered_rangelist])
        # Subtract 1 for every beacon inside those ranges
        for beacon in list(
            filter(lambda x: x.y == row, {s.beacon for s in self.sensors})
        ):
            for r in filtered_rangelist:
                if r[0] <= beacon.x <= r[1]:
                    totalcount -= 1
                    break
        return totalcount

    def get_darkpointfreq(self, maxsize: int) -> int:
        lines: dict[tuple[int, int], int] = {}
        for sensor in self.sensors:
            # Create 4 lines representing the outsides of the sensor's area, y = ax + b, a = [1, -1]
            # Tuple values (a, b)
            upper_left = (1, sensor.position.y - sensor.range - 1 - sensor.position.x)
            upper_right = (-1, sensor.position.y - sensor.range - 1 + sensor.position.x)
            lower_left = (-1, sensor.position.y + sensor.range + 1 + sensor.position.x)
            lower_right = (1, sensor.position.y + sensor.range + 1 - sensor.position.x)
            for line in (upper_left, upper_right, lower_left, lower_right):
                if line in lines:
                    lines[line] += 1
                else:
                    lines[line] = 1
        # Filter out and keep only the lines that appear at least twice
        ascending: list[int] = []
        descending: list[int] = []
        for line, nbr in lines.items():
            if nbr > 1:
                if line[0] == 1:
                    ascending.append(line[1])
                else:
                    descending.append(line[1])

        positions: list[Point] = []
        for asc_b in ascending:
            for des_b in descending:
                x = (des_b - asc_b) // 2
                positions.append(Point(x, x + asc_b))

        for p in positions:
            if (
                0 <= p.x <= maxsize
                and 0 <= p.y <= maxsize
                and self.__is_positiondark(p)
            ):
                return p.x * 4000000 + p.y
        return -1

    def __is_positiondark(self, position: Point) -> bool:
        for sensor in self.sensors:
            if sensor.is_inrange(position):
                return False
        return True


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_coverage(2000000))
    if part in (None, 2):
        p2 = str(p.get_darkpointfreq(4000000))

    return p1, p2
