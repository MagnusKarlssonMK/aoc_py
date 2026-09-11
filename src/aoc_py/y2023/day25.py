"""
2023 day 25 - Snowverload

Uses the 'minimum cut' function from nx module to determine the answer.
(Saving it for a rainy day to figure out how this actually works.)
"""

import math

import networkx as nx


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__graph = nx.Graph()
        for line in rawstr.splitlines():
            left, right = [part.strip() for part in line.split(": ")]
            self.__graph.add_node(left)
            [self.__graph.add_edge(left, r, capacity=1.0) for r in right.split()]

    def get_p1(self) -> int:
        result = -1
        left = next(iter(self.__graph.nodes))
        for right in self.__graph.nodes:
            if left != right:
                cut_val, partitions = nx.minimum_cut(self.__graph, left, right)
                if cut_val == 3:
                    result = math.prod(len(p) for p in partitions)
                    break
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
