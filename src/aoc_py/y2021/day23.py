"""
2021 day 23 - Amphipod

Well then.
Started out trying to make a very tidy data structure and neighbor lists etc., stumbled on trying to make it hashable
for the Dijkstra search, and instead wound up with this absolute monstrosity. I should probably try to refactor it into
something readable, but right now I feel like leaving it like this for the comedy effect. Good luck to anyone trying
to decipher this in the future (myself included...).
"""

from heapq import heappop, heappush
from typing import Final


class InputData:
    __POD_COSTS: Final = {"A": 1, "B": 10, "C": 100, "D": 1000}
    __ROOM_INDEX: Final = {0: "A", 1: "B", 2: "C", 3: "D"}
    __INDEX_ROOM: Final = {"A": 0, "B": 1, "C": 2, "D": 3}

    def __init__(self, rawstr: str) -> None:
        rooms: dict[int, list[str]] = {}
        hallway: set[int] = set()
        for line in rawstr.splitlines():
            for x, c in enumerate(line):
                if c == ".":
                    hallway.add(x)
                elif c in InputData.__POD_COSTS:
                    if x not in rooms:
                        rooms[x] = []
                    rooms[x].append(c)
        hallstartidx = min(hallway)
        self.__room_hall_index: dict[int, int] = {
            i: r - hallstartidx for i, r in enumerate(rooms)
        }
        self.__rooms = ["".join(rooms[r]) for r in sorted(rooms)]
        self.__hallway = "".join(["." for _ in range(len(hallway))])

    def get_energycost(self, unfolded: bool = False) -> int:
        target_rooms = (
            ("AA", "BB", "CC", "DD")
            if not unfolded
            else ("AAAA", "BBBB", "CCCC", "DDDD")
        )
        starting_rooms = list(self.__rooms)
        if unfolded:
            starting_rooms[0] = starting_rooms[0][0] + "DD" + starting_rooms[0][1]
            starting_rooms[1] = starting_rooms[1][0] + "CB" + starting_rooms[1][1]
            starting_rooms[2] = starting_rooms[2][0] + "BA" + starting_rooms[2][1]
            starting_rooms[3] = starting_rooms[3][0] + "AC" + starting_rooms[3][1]
        visited = {}
        pqueue: list[tuple[int, str, tuple[str, ...]]] = []
        heappush(pqueue, (0, self.__hallway, tuple(starting_rooms)))
        while pqueue:
            energy, hallway, rooms = heappop(pqueue)
            if rooms == target_rooms:
                return energy
            if (rooms, hallway) in visited and visited[(rooms, hallway)] <= energy:
                continue
            visited[(rooms, hallway)] = energy
            # print(rooms, hallway, energy)
            for i, c in enumerate(hallway):
                if c != ".":
                    # Check if target room is open and the path clear
                    if len(set(rooms[InputData.__INDEX_ROOM[c]]) | {c, "."}) > 2:
                        continue
                    pathstart = sorted(
                        [self.__room_hall_index[InputData.__INDEX_ROOM[c]], i]
                    )
                    if len(set(hallway[pathstart[0] + 1 : pathstart[1]]) | {"."}) > 1:
                        continue
                    steps = pathstart[1] - pathstart[0]
                    newrooms = list(rooms)
                    j = len(newrooms[InputData.__INDEX_ROOM[c]]) - 1
                    while j >= 0:
                        if newrooms[InputData.__INDEX_ROOM[c]][j] == ".":
                            newrooms[InputData.__INDEX_ROOM[c]] = (
                                newrooms[InputData.__INDEX_ROOM[c]][0:j]
                                + c
                                + newrooms[InputData.__INDEX_ROOM[c]][j + 1 :]
                            )
                            steps = (steps + 1 + j) * InputData.__POD_COSTS[c]
                            break
                        j -= 1
                    newrooms = tuple(newrooms)
                    newhallway = hallway[0:i] + "." + hallway[i + 1 :]
                    heappush(pqueue, (energy + steps, newhallway, newrooms))
            for i, room in enumerate(rooms):
                if (
                    len(set(room) | set(target_rooms[i]) | {"."}) == 2
                ):  # Skip if it only contains empty or target pod
                    continue
                for j, c in enumerate(room):
                    if c != ".":
                        newrooms = list(rooms)
                        newrooms[i] = room[0:j] + "." + room[j + 1 :]
                        steps = j + 1  # Nbr of steps to get it to hall level
                        # First check if the target room is open and path clear, if so move directly bypassing hallway
                        pathstart = sorted(
                            [
                                self.__room_hall_index[InputData.__INDEX_ROOM[c]],
                                self.__room_hall_index[i],
                            ]
                        )
                        if (
                            len(set(rooms[InputData.__INDEX_ROOM[c]]) | {c, "."}) == 2
                        ) and (
                            len(set(hallway[pathstart[0] + 1 : pathstart[1]]) | {"."})
                            == 1
                        ):
                            steps += pathstart[1] - pathstart[0]
                            destinationroom = newrooms[InputData.__INDEX_ROOM[c]]
                            k = len(destinationroom) - 1
                            while k >= 0:
                                if destinationroom[k] == ".":
                                    newrooms[InputData.__INDEX_ROOM[c]] = (
                                        destinationroom[0:k]
                                        + c
                                        + destinationroom[k + 1 :]
                                    )
                                    steps = (steps + 1 + k) * InputData.__POD_COSTS[c]
                                    break
                                k -= 1
                            heappush(pqueue, (energy + steps, hallway, tuple(newrooms)))
                            break
                        newrooms = tuple(newrooms)
                        # left:
                        for hallpos in reversed(range(self.__room_hall_index[i])):
                            if hallpos in self.__room_hall_index.values():
                                continue
                            if hallway[hallpos] != ".":
                                break
                            newhallway = hallway[0:hallpos] + c + hallway[hallpos + 1 :]
                            newenergy = (
                                steps + self.__room_hall_index[i] - hallpos
                            ) * InputData.__POD_COSTS[c]
                            heappush(pqueue, (energy + newenergy, newhallway, newrooms))
                        # right:
                        for hallpos in range(
                            self.__room_hall_index[i] + 1, len(hallway)
                        ):
                            if hallpos in self.__room_hall_index.values():
                                continue
                            if hallway[hallpos] != ".":
                                break
                            newhallway = hallway[0:hallpos] + c + hallway[hallpos + 1 :]
                            newenergy = (
                                steps + hallpos - self.__room_hall_index[i]
                            ) * InputData.__POD_COSTS[c]
                            heappush(pqueue, (energy + newenergy, newhallway, newrooms))
                        break
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_energycost())
    if part in (None, 2):
        p2 = str(p.get_energycost(True))

    return p1, p2
