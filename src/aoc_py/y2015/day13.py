"""
2015 day 13 - Knights of the Dinner Table

Similar to day 9.
Rather than going through all the permutations, try to reduce the space by using a BFS queue based on first and last
positions of the people seated so far, and only add an expansion of that combination to the queue if the score of the
people in the middle (who will not be affected by any further additions) yields a better result.

This works quite well and much faster than brute-forcing with permutations
"""

from collections import deque


class InputData:
    __MYSELF = "YOU"

    def __init__(self, rawstr: str) -> None:
        self.__people: set[str] = set()
        self.__happyness: dict[str, dict[str, int]] = {}
        for line in rawstr.splitlines():
            person1, _, lg, value, _, _, _, _, _, _, person2 = line.strip(".").split()
            self.__people.add(person1)
            if lg == "lose":
                value = -int(value)
            else:
                value = int(value)
            self.__happyness.setdefault(person1, {})[person2] = value
        # Add yourself for part 2
        self.__happyness[InputData.__MYSELF] = {}
        for neighbor in self.__people:
            self.__happyness[InputData.__MYSELF][neighbor] = 0
            self.__happyness[neighbor][InputData.__MYSELF] = 0

    def get_max_happiness(self, addself: bool = False) -> int:
        people = set(self.__people)
        if addself:
            people.add(InputData.__MYSELF)
        first = people.pop()
        best_seen: dict[
            tuple[str, str], list[tuple[set[str], int]]
        ] = {}  # (first, last): [(middle, value), ...]
        queue: deque[tuple[str, list[str], int]] = deque()
        for p in people:
            queue.append((p, [], self.__get_happiness([first, p])))
        while queue:
            last, middle, happy = queue.popleft()
            # Check if something better has been discovered since adding this entry to the queue
            if self.__dominated((first, last), set(middle), happy, best_seen):
                continue
            for new_last in people:
                if new_last != last and new_last not in middle:
                    new_middle: list[str] = [*middle, last]
                    new_happiness = self.__get_happiness([first, *new_middle, new_last])
                    if not self.__record(
                        (first, new_last), set(new_middle), new_happiness, best_seen
                    ):
                        continue
                    queue.append((new_last, new_middle, new_happiness))
        maxhappy = 0
        # Go through the 'seen' data and find the max happiness where everyone is seated
        for value in best_seen.values():
            for middle, happy in value:
                if len(middle) == len(people) - 1:
                    maxhappy = max(maxhappy, happy)
        return maxhappy

    @staticmethod
    def __dominated(
        key: tuple[str, str],
        middle: set[str],
        happiness: int,
        best_seen: dict[tuple[str, str], list[tuple[set[str], int]]],
    ) -> bool:
        """True if a strictly better version of this already-seen seating arrangement exists."""
        for old_middle, old_happiness in best_seen.get(key, ()):
            if old_middle == middle and old_happiness > happiness:
                return True
        return False

    @staticmethod
    def __record(
        key: tuple[str, str],
        middle: set[str],
        happiness: int,
        best_seen: dict[tuple[str, str], list[tuple[set[str], int]]],
    ) -> bool:
        """Record this seating arrangement, returning True if it is worth pursuing any further."""
        for i, (old_middle, old_happiness) in enumerate(best_seen.get(key, ())):
            if old_middle == middle:
                if old_happiness >= happiness:
                    return False  # No use continuing this branch
                best_seen[key][i] = (middle, happiness)
                return True
        if key in best_seen:
            best_seen[key].append((middle, happiness))
        else:
            best_seen[key] = [(middle, happiness)]
        return True

    def __get_happiness(self, seating: list[str]) -> int:
        length = len(seating)
        return sum(
            [
                self.__happyness[p][seating[(i + 1) % length]]
                + self.__happyness[p][seating[(i - 1) % length]]
                for i, p in enumerate(seating)
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_max_happiness())
    if part in (None, 2):
        p2 = str(p.get_max_happiness(True))

    return p1, p2
