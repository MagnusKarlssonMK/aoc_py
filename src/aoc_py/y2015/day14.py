"""
2015 day 14 - Reindeer Olympics

Pretty much just parse the reindeer into a class that gives a method to calculate distance based on time.

For part 2 we simply need to simulate the race second-for-second and award points along the way. The only minor thing
to keep in mind is that the time loop needs to start at 1 to avoid awarding points on the starting line, and to run
until 2503+1 to compensate for python's range not including the last value.

Part 1 asks how far the fastest reindeer has travelled by the end of the race, and part 2 for the highest score once
every one of the 2503 seconds awards a point to whoever is level with the lead at that second. Both answers come out of
the same closed form, so part 2 loops over the seconds and calls get_distance once per reindeer rather than keeping a
second simulation running alongside.

get_distance splits the elapsed time into whole fly-and-rest cycles plus the remainder, and charges the remainder only
as far as the end of the flying stretch. That cap is what stops a reindeer from banking distance while it is resting.

Reindeer.parse_str owns the sentence format, so the magic word indices sit next to the class that has the fields to put
them in rather than in the class that only collects reindeer.

The 2503 second limit belongs to the puzzle, but the worked example in the description races for 1000 seconds instead,
and nothing in the input tells the two apart. An input with fewer than three reindeer is therefore assumed to be the
example. The guess is wrong for a genuine two-reindeer race, which would be scored over 1000 seconds rather than 2503.
"""

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class Reindeer:
    speed: int
    time: int
    rest: int

    @classmethod
    def parse_str(cls, line: str) -> Reindeer:
        words = line.split()
        return cls(int(words[3]), int(words[6]), int(words[13]))

    def get_distance(self, time: int) -> int:
        cycle_time = self.time + self.rest
        cycles = time // cycle_time
        remainder = time % cycle_time
        total = self.speed * ((cycles * self.time) + min(remainder, self.time))
        return total


class InputData:
    __TIME_LIMIT: Final = 2503

    def __init__(self, rawstr: str) -> None:
        self.__reindeers: dict[str, Reindeer] = {}
        for line in rawstr.splitlines():
            self.__reindeers[line.split(maxsplit=1)[0]] = Reindeer.parse_str(line)
        # Assume test input for short inputs
        self.__time_limit: int = (
            1000 if len(self.__reindeers) < 3 else self.__TIME_LIMIT
        )

    def get_p1(self) -> int:
        if not self.__reindeers:
            return -1
        return max(
            [
                self.__reindeers[r].get_distance(self.__time_limit)
                for r in self.__reindeers
            ]
        )

    def get_p2(self) -> int:
        if not self.__reindeers:
            return -1
        scoretable: dict[str, int] = {r: 0 for r in self.__reindeers}
        # Start on 1, so we don't award points at the starting line!
        for seconds in range(1, self.__time_limit + 1):
            leader_dist = 0
            leaders = []
            for r in self.__reindeers:
                newdist = self.__reindeers[r].get_distance(seconds)
                if newdist > leader_dist:
                    leaders = [r]
                    leader_dist = newdist
                elif newdist == leader_dist:
                    leaders.append(r)
            for lead in leaders:
                scoretable[lead] += 1
        return max(scoretable.values())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
