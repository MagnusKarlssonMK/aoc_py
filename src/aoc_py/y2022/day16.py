"""
2022 day 16 - Proboscidea Volcanium

Stores the parsed data in a graph and computes all-pairs shortest distances between the rooms with the
Floyd-Warshall algorithm.
Then finds the answer with a recursive search over the openable valves using bitmaps.
"""

from itertools import permutations


class InputData:
    def __init__(self, rawstr: str) -> None:
        adj_list: dict[str, list[str]] = {}
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
            adj_list[from_valve] = to_valves
            if flow_rate > 0:
                self.__valves[from_valve] = flow_rate
        self.__start = "AA"
        self.__valve_indices = {valve: 1 << i for i, valve in enumerate(self.__valves)}
        # All-pairs shortest distances between rooms; 1000 marks a pair with no route between them.
        self.__distances: dict[tuple[str, str], int] = {}
        for valve, lead_to in adj_list.items():
            for tunnel_to in adj_list:
                if tunnel_to in lead_to:
                    self.__distances[(valve, tunnel_to)] = 1
                else:
                    self.__distances[(valve, tunnel_to)] = 1000
        for a, b, c in permutations(adj_list, 3):
            self.__distances[b, c] = min(
                self.__distances[b, c], self.__distances[b, a] + self.__distances[a, c]
            )

    def get_maxflow(self, max_time: int, train_elephant: bool = False) -> int:
        if train_elephant:
            result = self.__checkroom(self.__start, max_time, 0, 0, {})
            maxflow = max(
                [
                    flow1 + flow2
                    for mask1, flow1 in result.items()
                    for mask2, flow2 in result.items()
                    if not mask1 & mask2
                ]
            )
        else:
            maxflow = max(self.__checkroom(self.__start, max_time, 0, 0, {}).values())
        return maxflow

    def __checkroom(
        self, valve: str, time: int, bitmask: int, released: int, flow: dict[int, int]
    ) -> dict[int, int]:
        flow[bitmask] = max(flow.get(bitmask, 0), released)
        for valve2, f in self.__valves.items():
            time_left = time - self.__distances[valve, valve2] - 1
            if not (self.__valve_indices[valve2] & bitmask) and time_left > 0:
                _ = self.__checkroom(
                    valve2,
                    time_left,
                    bitmask | self.__valve_indices[valve2],
                    released + f * time_left,
                    flow,
                )
        return flow


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_maxflow(30))
    if part in (None, 2):
        p2 = str(p.get_maxflow(26, True))

    return p1, p2
