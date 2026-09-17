"""
2015 day 14 - Reindeer Olympics

Pretty much just parse the reindeers into a class that gives a method to calculate distance based on time.

For part 2 we simply need to simulate the race second-for-second and award points along the way. The only minor thing
to keep in mind is that the time loop needs to start at 1 to avoid awarding points on the starting line, and to run
until 2503+1 to compensate for python's range not including the last value.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Reindeer:
    speed: int
    time: int
    rest: int

    def get_distance(self, time: int) -> int:
        cycle_time = self.time + self.rest
        cycles = time // cycle_time
        remainder = time % cycle_time
        total = self.speed * ((cycles * self.time) + min(remainder, self.time))
        return total


class InputData:
    __TIME_LIMIT = 2503

    def __init__(self, rawstr: str) -> None:
        self.__reindeers: dict[str, Reindeer] = {}
        for line in rawstr.splitlines():
            words = line.split()
            name = words[0]
            self.__reindeers[name] = Reindeer(
                int(words[3]), int(words[6]), int(words[13])
            )
        if len(self.__reindeers) < 3:
            # Assume test input for short inputs
            self.__TIME_LIMIT = 1000

    def get_p1(self) -> int:
        return max(
            [
                self.__reindeers[r].get_distance(self.__TIME_LIMIT)
                for r in self.__reindeers
            ]
        )

    def get_p2(self) -> int:
        scoretable: dict[str, int] = {r: 0 for r in self.__reindeers}
        # Start on 1, so we don't award points at the starting line!
        for seconds in range(1, self.__TIME_LIMIT + 1):
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
