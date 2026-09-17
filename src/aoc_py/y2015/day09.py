"""
2015 day 9 - All in a Single Night

Generate all permutations of and find the one yielding the shortest total distance covering all nodes. I.e. basically
a brute force approach, which works decently fast due to the somewhat limited number of nodes.
"""

from itertools import permutations


class InputData:
    def __init__(self, s: str) -> None:
        self.__distances: dict[tuple[str, str], int] = {}
        self.__cities: set[str] = set()
        for line in s.splitlines():
            city1, _, city2, _, distance = line.split()
            self.__distances[(city1, city2)] = int(distance)
            self.__distances[(city2, city1)] = int(distance)
            self.__cities.add(city1)
            self.__cities.add(city2)

    def get_route_lengths(self) -> tuple[int, int]:
        route_lengths: list[int] = []
        for route in permutations(self.__cities):
            if (
                route[0] < route[-1]
            ):  # To avoid re-calculating the same route twice in both directions
                new_len = 0
                for i in range(len(route) - 1):
                    if (
                        route[i],
                        route[i + 1],
                    ) in self.__distances:  # Just in case distance data is missing
                        new_len += self.__distances[(route[i], route[i + 1])]
                    else:
                        break
                else:
                    route_lengths.append(new_len)
        return min(route_lengths), max(route_lengths)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_route_lengths()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
