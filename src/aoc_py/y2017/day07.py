"""
2017 day 7 - Recursive Circus

Part 1

Store the program tree in a dict, with each node containig its weight, leafs and parent. The node without a parent
is the answer.

Part 2

Make a recursive weight calculation of the tree, where each program checks the weight of its leafs (if any),
and calculates and reports the required correction if discovered.
"""

from dataclasses import dataclass


@dataclass
class Program:
    weight: int
    leafs: set[str]
    parent: str = ""


class InputData:
    def __init__(self, s: str) -> None:
        self.__programs: dict[str, Program] = {}
        self.__root: str = ""
        for line in s.splitlines():
            tokens = line.split()
            leafs = {w.strip(",") for w in tokens[3:]}
            self.__programs[tokens[0]] = Program(
                int(tokens[1].strip("(").strip(")")), leafs
            )
        for p, item in self.__programs.items():
            for leaf in item.leafs:
                self.__programs[leaf].parent = p
        for p in self.__programs:
            if self.__programs[p].parent == "":
                self.__root = p

    def get_p1(self) -> str:
        return self.__root

    def get_p2(self) -> int:
        _, c = self.__get_weight_and_correction(self.__root)
        return c

    def __get_weight_and_correction(self, program: str) -> tuple[int, int]:
        leafweights = {}
        leafcorrections = []
        if not self.__programs[program].leafs:
            # Node without leafs
            return self.__programs[program].weight, 0

        for leaf in self.__programs[program].leafs:
            w, c = self.__get_weight_and_correction(leaf)
            if w not in leafweights:
                leafweights[w] = [leaf]
            else:
                leafweights[w].append(leaf)
            leafcorrections.append(c)

        if (corr := sum(leafcorrections)) > 0:
            # A node further down the tree has reported a correction, just propagate upwards
            return (
                self.__programs[program].weight
                + (sum(leafweights) * sum([len(v) for v in leafweights.values()])),
                corr,
            )
        elif len(leafweights) > 1:
            # These leafs are not balanced; figure out which one is bad and calculate the required correction
            correctweight = -1
            badweight = -1
            badnode = ""
            for w, val in leafweights.items():
                if len(val) > 1:
                    correctweight = w
                else:
                    badweight = w
                    badnode = val[0]
            return (
                self.__programs[program].weight
                + (correctweight * sum([len(v) for v in leafweights.values()])),
                correctweight - (badweight - self.__programs[badnode].weight),
            )
        # else - all leafs have reported the same weight and are thus balanced
        return self.__programs[program].weight + (
            sum(leafweights) * sum([len(v) for v in leafweights.values()])
        ), 0


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
