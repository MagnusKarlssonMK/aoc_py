"""
2022 day 16 - Proboscidea Volcanium

Stores parsed data in a graph, and generates a trimmed variant of it with only the rooms containing a valve
with Floyd-Warshall algorithm.
Then finds the answer with a recursive search using bitmaps.
"""

from itertools import permutations


class InputData:
    def __init__(self, rawstr: str) -> None:
        adjlist: dict[str, list[str]] = {}
        self.__valves: dict[str, int] = {}
        for line in rawstr.splitlines():
            left, right = line.split("; ")
            left, flow_rate = left.split("=")
            flow_rate = int(flow_rate)
            from_valve = left.split()[1]
            if "valves" in right:
                _, right = right.split("valves ")
            else:
                _, right = right.split("valve ")
            to_valves = right.split(", ")
            adjlist[from_valve] = to_valves
            if flow_rate > 0:
                self.__valves[from_valve] = flow_rate
        self.__start = "AA"
        self.__valve_indicies = {valve: 1 << i for i, valve in enumerate(self.__valves)}
        # Create a trimmed version of the adj list with Floyd-Warshall, keep only the nodes with non-zero valves
        self.__distances: dict[tuple[str, str], int] = {}
        for valve, lead_to in adjlist.items():
            for tunnel_to in adjlist:
                if tunnel_to in lead_to:
                    self.__distances[(valve, tunnel_to)] = 1
                else:
                    self.__distances[(valve, tunnel_to)] = 1000
        for a, b, c in permutations(adjlist, 3):
            self.__distances[b, c] = min(
                self.__distances[b, c], self.__distances[b, a] + self.__distances[a, c]
            )

    def get_maxflow(self, maxtime: int, train_elephant: bool = False) -> int:
        if train_elephant:
            result = self.__checkroom(self.__start, maxtime, 0, 0, {})
            maxflow = max(
                [
                    flow1 + flow2
                    for mask1, flow1 in result.items()
                    for mask2, flow2 in result.items()
                    if not mask1 & mask2
                ]
            )
        else:
            maxflow = max(self.__checkroom(self.__start, maxtime, 0, 0, {}).values())
        return maxflow

    def __checkroom(
        self, valve: str, time: int, bitmask: int, released: int, flow: dict[int, int]
    ) -> dict[int, int]:
        flow[bitmask] = max(flow.get(bitmask, 0), released)
        for valve2, f in self.__valves.items():
            timeleft = time - self.__distances[valve, valve2] - 1
            if not (self.__valve_indicies[valve2] & bitmask) and timeleft > 0:
                _ = self.__checkroom(
                    valve2,
                    timeleft,
                    bitmask | self.__valve_indicies[valve2],
                    released + f * timeleft,
                    flow,
                )
        return flow


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_maxflow(30))
    if part in (None, 2):
        p2 = str(p.get_maxflow(26, True))

    return p1, p2
