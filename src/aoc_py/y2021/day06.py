"""
2021 day 6 - Lanternfish

Count the fish at each timer value into one bucket per timer, so that the work per
day is independent of how fast the population grows. The buckets are not rebuilt each
day; the array is instead read as a fixed window that rotates one slot per day, so
bucket i holds the fish whose timer is (i - day) mod 9. A fish at timer 0 both resets
to 6 and spawns a newborn at 8, and a single add into bucket (day + 7) mod 9 covers
both halves at once, since 7 is the newborn's slot 8 pulled back by the one slot that
the window slides today.
Part 1 reports the population after 80 days; Part 2 continues the same run to 256 days.
"""

from typing import Final

NBR_TIMERS: Final = 9
P1_NBR_DAYS: Final = 80
P2_NBR_DAYS: Final = 256


class InputData:
    def __init__(self, s: str) -> None:
        self.__states = [0] * NBR_TIMERS
        for nbr in list(map(int, s.split(","))):
            self.__states[nbr] += 1

    def get_answers(self) -> tuple[int, int]:
        """Returns the population for Part 1 and Part 2. Assumes that the number of days
        for Part 2 is larger than for Part 1."""
        states = self.__states.copy()
        p1 = 0
        for day in range(P2_NBR_DAYS):
            states[(day + 7) % NBR_TIMERS] += states[day % NBR_TIMERS]
            if day == P1_NBR_DAYS - 1:
                p1 = sum(states)
        return p1, sum(states)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_answers()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
