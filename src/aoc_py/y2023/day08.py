"""
2023 day 8 - Haunted Wasteland

Stores the node input in a dict in a class, which provides methods to calculate the corresponding answers to Part 1
and Part 2, with the sequence as input. Uses LCM from the math module to calculate the value for part 2.
"""

from math import lcm


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__nodes: dict[str, dict[str, str]] = {}
        self.__sequence, lines = rawstr.split("\n\n")
        for line in lines.splitlines():
            parts = line.split(" = (")
            a = parts[0]
            parts = parts[1].split(", ")
            b = parts[0]
            c = parts[1].strip(")")
            self.__nodes[a] = {"L": b, "R": c}

    def get_p1(self) -> int:
        location = "AAA"
        stepcount = 0
        while location != "ZZZ":
            location = self.__nodes[location][
                self.__sequence[stepcount % len(self.__sequence)]
            ]
            stepcount += 1
        return stepcount

    def get_p2(self) -> int:
        location = [node for node in self.__nodes if node[-1] == "A"]
        cycles: list[int] = []
        for startpoint in location:
            stepcount = 0
            currentloc = startpoint
            while currentloc[-1] != "Z":
                currentloc = self.__nodes[currentloc][
                    self.__sequence[stepcount % len(self.__sequence)]
                ]
                stepcount += 1
            cycles.append(stepcount)
        return lcm(*cycles)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
