"""
2020 day 10 - Adapter Array

Part 1

Sort the parsed input, add 0 at the start and max+3 at the end, then simply make a counter object to put the
value differences into.

Part 2

Create an adjacency list / DAG out of the possible other adapters that one adapter can connect to, then apply a
memoized DFS to count the number of paths.
"""

from collections import Counter


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__ratings: list[int] = sorted(map(int, rawstr.splitlines()))
        self.__ratings.append(self.__ratings[-1] + 3)
        self.__ratings.insert(0, 0)

    def get_p1(self) -> int:
        diff: Counter[int] = Counter()
        for i in range(len(self.__ratings) - 1):
            diff[self.__ratings[i + 1] - self.__ratings[i]] += 1
        return diff[1] * diff[3]

    def get_p2(self) -> int:
        adj: dict[int, list[int]] = {}
        for i in range(len(self.__ratings) - 1):
            adj[self.__ratings[i]] = []
            for j in range(i + 1, i + 4):
                if (
                    j >= len(self.__ratings)
                    or self.__ratings[j] - self.__ratings[i] > 3
                ):
                    break
                else:
                    adj[self.__ratings[i]].append(self.__ratings[j])
        start = self.__ratings[0]
        return pathcount(adj, start, {})


def pathcount(dag: dict[int, list[int]], vertex: int, memo: dict[int, int]) -> int:
    if vertex in memo:
        return memo[vertex]
    elif vertex in dag:
        memo[vertex] = sum([pathcount(dag, x, memo) for x in dag[vertex]])
        return memo[vertex]
    else:
        return 1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
