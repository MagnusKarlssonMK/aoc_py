"""
2021 day 23 - Amphipod

A state is the four rooms, each a string of amphipod letters with the topmost pod first, plus
the hallway as a string of dots and letters. A single successor function lists the legal
one-pod moves out of a state, and A* picks the cheapest sequence of them.

Two things keep the branching factor down. A pod may only come to rest on a hallway square
that is not a room entrance, and only the topmost pod of a room can leave it, since the ones
above have to move first. A pod already in the hallway is never slid along it to another
resting square: that is never cheaper than having gone to that square directly, so leaving
those moves out cannot change the cheapest answer.

The estimate steering the search has to stay a lower bound, or A* will happily return a
sequence that is not the cheapest. See InputData.__estimate for why it is one.
"""

from collections.abc import Generator
from heapq import heappop, heappush
from typing import Final

POD_COSTS: Final[dict[str, int]] = {"A": 1, "B": 10, "C": 100, "D": 1000}
ROOM_LETTERS: Final = ("A", "B", "C", "D")
POD_ROOM: Final[dict[str, int]] = {
    letter: i for i, letter in enumerate(ROOM_LETTERS)
}  # which room a pod belongs in
UNFOLD_ROWS: Final = ("DD", "CB", "BA", "AC")  # part 2's extra rows, from the puzzle


class InputData:
    def __init__(self, rawstr: str) -> None:
        rooms: dict[int, list[str]] = {}
        hallway: set[int] = set()
        for line in rawstr.splitlines():
            for x, c in enumerate(line):
                if c == ".":
                    hallway.add(x)
                elif c in POD_COSTS:
                    rooms.setdefault(x, []).append(c)
        first = min(hallway)
        self.__room_x: tuple[int, ...] = tuple(
            r - first for r in sorted(rooms)
        )  # hallway index of each room entrance
        self.__rooms: tuple[str, ...] = tuple("".join(rooms[r]) for r in sorted(rooms))
        self.__hall_len: int = len(hallway)
        # Every hallway square is fair game except the four room entrances.
        self.__hall_spots: tuple[int, ...] = tuple(
            x for x in range(self.__hall_len) if x not in self.__room_x
        )

    @staticmethod
    def __is_clear(hallway: str, lo: int, hi: int) -> bool:
        """True when the stretch of hallway strictly between lo and hi is all dots. The ends
        are left out, so this also holds for adjacent squares, where the stretch is empty."""
        return hallway[lo + 1 : hi] == "." * (hi - lo - 1)

    @staticmethod
    def __deepest_free(room: str) -> int:
        """Index of the lowest empty square of a room, or -1 when the room is full."""
        for k in range(len(room) - 1, -1, -1):
            if room[k] == ".":
                return k
        return -1

    def __successors(
        self, rooms: tuple[str, ...], hallway: str
    ) -> Generator[tuple[tuple[str, ...], str, int]]:
        """Yields every legal single-pod move out of a state, as the new rooms, the new
        hallway and the energy it adds.

        A pod in a room either walks straight into its own room, when the way there is clear
        and that room holds nothing but pods of its own kind, or steps out to any hallway
        square it can reach. A pod in the hallway can only go into its own room. Only the
        topmost pod of a room is considered, as the ones above it would have to move first.
        """
        for i, room in enumerate(rooms):
            if set(room) <= {ROOM_LETTERS[i], "."}:
                continue  # settled: nothing left in here needs to move
            here = self.__room_x[i]
            for j, pod in enumerate(room):
                if pod == ".":
                    continue
                target = POD_ROOM[pod]
                # rooms with the topmost pod lifted out
                rest = rooms[:i] + (room[:j] + "." + room[j + 1 :],) + rooms[i + 1 :]
                up = j + 1  # steps to climb to hallway level
                to = self.__room_x[target]
                lo, hi = (here, to) if here < to else (to, here)
                home = set(rooms[target]) <= {pod, "."}
                if home and self.__is_clear(hallway, lo, hi):
                    k = self.__deepest_free(rooms[target])
                    if k >= 0:
                        filled = rest[target][:k] + pod + rest[target][k + 1 :]
                        yield (
                            rest[:target] + (filled,) + rest[target + 1 :],
                            hallway,
                            (up + (hi - lo) + 1 + k) * POD_COSTS[pod],
                        )
                        break
                for spot in self.__hall_spots:
                    if spot == here or hallway[spot] != ".":
                        continue
                    lo, hi = (here, spot) if here < spot else (spot, here)
                    if self.__is_clear(hallway, lo, hi):
                        yield (
                            rest,
                            hallway[:spot] + pod + hallway[spot + 1 :],
                            (up + abs(spot - here)) * POD_COSTS[pod],
                        )
                break
        for x, pod in enumerate(hallway):
            if pod == ".":
                continue
            target = POD_ROOM[pod]
            if not set(rooms[target]) <= {pod, "."}:
                continue
            to = self.__room_x[target]
            lo, hi = (x, to) if x < to else (to, x)
            if not self.__is_clear(hallway, lo, hi):
                continue
            k = self.__deepest_free(rooms[target])
            if k < 0:
                continue  # own room is full, so this pod can never get home
            filled = rooms[target][:k] + pod + rooms[target][k + 1 :]
            yield (
                rooms[:target] + (filled,) + rooms[target + 1 :],
                hallway[:x] + "." + hallway[x + 1 :],
                (hi - lo + 1 + k) * POD_COSTS[pod],
            )

    def __estimate(self, rooms: tuple[str, ...], hallway: str) -> int:
        """A lower bound on the energy still to be spent, used to steer the search towards
        the states that look closest to done.

        Every pod has to reach the entrance of its own room, so it must cover at least that
        much horizontal distance. A pod that is not in its own room must climb out of the one
        it is in and then descend into the other, and a pod out in the hallway still has to
        descend at least one step. Pods are moved independently of each other, so adding up
        those per-pod bounds bounds the state as a whole. Overestimating here instead would
        make the search discard the cheapest sequence and report a larger answer.
        """
        total = 0
        for i, room in enumerate(rooms):
            for j, pod in enumerate(room):
                if pod == ".":
                    continue
                target = POD_ROOM[pod]
                across = abs(self.__room_x[i] - self.__room_x[target])
                out_and_in = 0 if target == i else j + 2
                total += (across + out_and_in) * POD_COSTS[pod]
        for x, pod in enumerate(hallway):
            if pod != ".":
                target = POD_ROOM[pod]
                total += (abs(x - self.__room_x[target]) + 1) * POD_COSTS[pod]
        return total

    def __search(self, rooms: tuple[str, ...], hallway: str) -> int:
        """The least energy that sorts the rooms out, or -1 if no sequence of moves gets
        there. States are held in a dict of the cheapest energy found for each so far, and
        the queue holds (energy spent plus estimate, energy spent, hallway, rooms), so the
        most promising state comes off first and ties fall back on energy actually spent."""
        goal = tuple(letter * len(rooms[0]) for letter in ROOM_LETTERS)
        best: dict[tuple[tuple[str, ...], str], int] = {(rooms, hallway): 0}
        queue: list[tuple[int, int, str, tuple[str, ...]]] = [
            (self.__estimate(rooms, hallway), 0, hallway, rooms)
        ]
        while queue:
            _, energy, hallway, rooms = heappop(queue)
            state = (rooms, hallway)
            if energy > best[state]:
                continue  # a cheaper way into this state turned up after it was queued
            if rooms == goal:
                return energy
            for newrooms, newhallway, added in self.__successors(rooms, hallway):
                newstate = (newrooms, newhallway)
                newenergy = energy + added
                known = best.get(newstate)
                if known is None or newenergy < known:
                    best[newstate] = newenergy
                    heappush(
                        queue,
                        (
                            newenergy + self.__estimate(newrooms, newhallway),
                            newenergy,
                            newhallway,
                            newrooms,
                        ),
                    )
        return -1

    def get_answers(self) -> tuple[int, int]:
        """Reports the least energy for Part 1 and for Part 2, which is the same puzzle with
        the puzzle's own extra row wedged into each room. The two searches are independent, so
        they simply run one after the other."""
        blank = "." * self.__hall_len
        part1 = self.__search(self.__rooms, blank)
        unfolded = tuple(
            room[0] + extra + room[1:]
            for room, extra in zip(self.__rooms, UNFOLD_ROWS, strict=True)
        )
        return (part1, self.__search(unfolded, blank))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).get_answers()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
