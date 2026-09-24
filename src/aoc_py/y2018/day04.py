"""
2018 day 4 - Repose Record

Parsing, parsing, parsing... and then some sorting.
Not much else to say, just some dict trickery to extract the corresponding values / keys from the records.
"""

from enum import Enum


class Event(Enum):
    BEGIN_SHIFT = "Guard"
    FALLS_ASLEEP = "falls"
    WAKES_UP = "wakes"


class Timestamp:
    year: int
    month: int
    day: int
    hour: int
    minute: int

    def __init__(self, s: str) -> None:
        d, t = s.split()
        h, m = t.split(":")
        y, mo, day = d.split("-")
        self.year = int(y)
        self.month = int(mo)
        self.day = int(day)
        self.hour = int(h)
        self.minute = int(m)

    def __lt__(self, other: Timestamp) -> bool:
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        if self.day != other.day:
            return self.day < other.day
        if self.hour != other.hour:
            return self.hour < other.hour
        return self.minute < other.minute


class InputData:
    def __init__(self, s: str) -> None:
        self.__records: list[tuple[Timestamp, int, Event]] = []
        for line in s.splitlines():
            left, right = line.lstrip("[").split("] ")
            right = right.split()
            event = Event(right[0])
            guard = int(right[1].strip("#")) if event == Event.BEGIN_SHIFT else -1
            self.__records.append((Timestamp(left), guard, event))
        self.__records.sort(key=lambda x: x[0])

    def get_guard_id(self) -> tuple[int, int]:
        guards: dict[int, dict[int, int]] = {
            g: {} for _, g, e in self.__records if e == Event.BEGIN_SHIFT
        }  # guardid: (asleepminutes: count))
        asleepminute = -1
        guard = -1
        for timestamp, g, event in self.__records:
            match event:
                case Event.BEGIN_SHIFT:
                    guard = g
                case Event.FALLS_ASLEEP:
                    asleepminute = timestamp.minute
                case Event.WAKES_UP:
                    for t in range(asleepminute, timestamp.minute):
                        if t not in guards[guard]:
                            guards[guard][t] = 1
                        else:
                            guards[guard][t] += 1

        maxasleep = 0, 0, 0
        maxminute = 0, 0, 0
        for g, value in guards.items():
            if (m := sum(value.values())) > maxasleep[1]:
                maxasleep = g, m, max(value, key=lambda k: value[k])
            if value and (n := max(value.values())) > maxminute[1]:
                maxminute = g, n, max(value, key=lambda k: value[k])
        return maxasleep[0] * maxasleep[2], maxminute[0] * maxminute[2]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_guard_id()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
