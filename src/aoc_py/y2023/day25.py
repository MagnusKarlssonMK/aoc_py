"""
2023 day 25 - Snowverload

Builds an undirected graph of the wires and finds a minimum edge cut of 3 between two nodes. The cut is found by
max flow (Edmonds-Karp): repeatedly locate an augmenting path with a BFS and push flow along it, until no path
remains. Whatever is still reachable from the source in the residual graph is one side of the cut, and the answer
is the product of the sizes of the two sides.
"""

import math
from collections import deque
from typing import Final

WIRES_TO_CUT: Final = 3


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__wires: dict[str, set[str]] = {}
        for line in rawstr.splitlines():
            name, others = [part.strip() for part in line.split(": ")]
            for other in others.split():
                self.__wires.setdefault(name, set()).add(other)
                self.__wires.setdefault(other, set()).add(name)

    def __min_cut(self, source: str, sink: str) -> tuple[int, set[str]]:
        """Finds a minimum edge cut between the source and the sink by max flow, and returns the value of the
        cut together with the set of nodes on the source's side of it."""
        nodes = list(self.__wires)
        index = {node: i for i, node in enumerate(nodes)}
        # Each wire becomes a pair of arcs that are each other's reverse, both starting with capacity 1, which is
        # how an undirected unit capacity edge is modelled. The reverse of arc i is therefore always i ^ 1.
        heads: list[list[int]] = [[] for _ in nodes]
        targets: list[int] = []
        residual: list[int] = []

        def add_arc(first: int, second: int) -> None:
            targets.extend((second, first))
            residual.extend((1, 1))
            heads[first].append(len(targets) - 2)
            heads[second].append(len(targets) - 1)

        for name, others in self.__wires.items():
            for other in others:
                if index[name] < index[other]:
                    add_arc(index[name], index[other])

        start, end = index[source], index[sink]
        value = 0
        while True:
            via: list[int] = [-1] * len(nodes)
            via[start] = -2
            queue = deque([start])
            while queue and via[end] == -1:
                node = queue.popleft()
                for arc in heads[node]:
                    nxt = targets[arc]
                    if residual[arc] > 0 and via[nxt] == -1:
                        via[nxt] = arc
                        queue.append(nxt)
            if via[end] == -1:
                break
            value += 1
            node = end
            while node != start:
                arc = via[node]
                residual[arc] -= 1
                residual[arc ^ 1] += 1
                node = targets[arc ^ 1]

        # Whatever the last BFS reached is exactly one side of the minimum cut.
        side = {node for i, node in enumerate(nodes) if via[i] != -1}
        return value, side

    def get_p1(self) -> int:
        result = -1
        source = next(iter(self.__wires))
        for sink in self.__wires:
            if source != sink:
                value, side = self.__min_cut(source, sink)
                if value == WIRES_TO_CUT:
                    result = math.prod((len(side), len(self.__wires) - len(side)))
                    break
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
