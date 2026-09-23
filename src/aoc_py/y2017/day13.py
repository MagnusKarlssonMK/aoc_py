"""
2017 day 13 - Packet Scanners
"""

from math import lcm


class Scanner:
    depth: int
    range: int
    cycle: int

    def __init__(self, s: str) -> None:
        left, right = s.split(": ")
        self.depth = int(left)
        self.range = int(right)
        self.cycle = 2 * (self.range - 1)

    def get_severity(self) -> int:
        return self.depth * self.range


class InputData:
    def __init__(self, s: str) -> None:
        self.__scanners = [Scanner(line) for line in s.splitlines()]

    def get_p1(self) -> int:
        return sum(s.get_severity() for s in self.__scanners if s.depth % s.cycle == 0)

    def get_p2(self) -> int:
        current_lcm = 1
        delays = [1]
        for s in self.__scanners:
            new_lcm = lcm(current_lcm, s.cycle)
            new_delays = []
            for extra in range(0, new_lcm, current_lcm):
                for delay in delays:
                    if (delay + extra + s.depth) % s.cycle != 0:
                        new_delays.append(delay + extra)
            current_lcm = new_lcm
            delays = new_delays
        return delays[0]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
