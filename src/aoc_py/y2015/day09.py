"""
2015 day 9 - All in a Single Night

Treat each city as a node and each line as an undirected edge, then score every ordering of the cities by the sum of
the distances along it. Part 1 is the cheapest such ordering and part 2 the dearest, so a single pass over all of them
yields both answers at once.

Distances are recorded in both directions, which makes the graph symmetric and means an ordering and its reverse always
score the same. That lets the search keep just one of each such pair, which is where the speed comes from: it halves
the work without being able to change either answer, since the pair it discards is worth precisely what it kept. The
fact that the cities live in a set therefore cannot make the result depend on iteration order either.

An ordering is only scored if every consecutive pair has a distance on record. Where one is missing the ordering is
skipped outright rather than counted as a zero-length leg, since a leg nobody measured is not a free hop. The puzzle
guarantees a complete graph, so both answers come from real distances; the -1 is only reachable by input the puzzle
excludes, such as two disconnected pairs of cities.
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
        if not route_lengths:
            # No ordering visits every city, which needs the city graph to be disconnected or to have too many
            # leaves for a single hub. The puzzle guarantees a complete graph, so nothing valid reaches this.
            return -1, -1
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
