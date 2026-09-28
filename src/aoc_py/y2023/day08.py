"""
2023 day 8 - Haunted Wasteland

Stores the node input in a dict in a class, which provides methods to calculate the corresponding answers to Part 1
and Part 2, with the sequence as input. Uses LCM from the math module to calculate the value for part 2.
Every node whose name ends in A walks in a cycle of its own until a node ending in Z is reached, and the number of
steps that walk needs is the length of that cycle, so part 2 wants the first step count that is a multiple of
every cycle length, which is their least common multiple. Part 1 is the same walk with a single start, from AAA
to ZZZ.
"""

from math import lcm


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__nodes: dict[str, dict[str, str]] = {}
        self.__sequence, lines = rawstr.split("\n\n")
        for line in lines.splitlines():
            name, targets = line.split(" = (")
            left, right = targets.removesuffix(")").split(", ")
            self.__nodes[name] = {"L": left, "R": right}

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
        startpoints = [node for node in self.__nodes if node[-1] == "A"]
        return lcm(*[self.__steps_to_z(startpoint) for startpoint in startpoints])

    def __steps_to_z(self, startpoint: str) -> int:
        location = startpoint
        stepcount = 0
        while location[-1] != "Z":
            location = self.__nodes[location][
                self.__sequence[stepcount % len(self.__sequence)]
            ]
            stepcount += 1
        return stepcount


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
