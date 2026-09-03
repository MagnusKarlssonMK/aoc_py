"""
2025 day 5 - Cafeteria

Part 1

Trivial - for every available ID, iterate over the ID ranges and if any range contains
the available ID, increment the total and skip to the next available ID.

## Part 2

First merge all the overlapping ranges:
1. Put all the input ranges on a queue, and create a list of processed ranges.
2. Pull a range from the queue and check if it overlaps with any of the already
   processed ranges. If it does, pull that processed range out of the list and push
   the combined range back to the queue.
3. Repeat 2 until the queue is empty.

Once the new list of combined ranges is completed, take the total sum of ID:s contained
by each range. Note that the ranges are inclusive, so the number of ID:s for a range
is 1 + upper_range - lower range.
"""


class InputData:
    def __init__(self, s: str) -> None:
        blocks = s.split("\n\n")
        self.__fresh_id_ranges = [
            (int(r[0]), int(r[1]))
            for r in [line.split("-") for line in blocks[0].splitlines()]
        ]
        self.__available_ids = [int(line) for line in blocks[1].splitlines()]

    def get_p1(self) -> int:
        total = 0
        for a in self.__available_ids:
            for r0, r1 in self.__fresh_id_ranges:
                if a in range(r0, r1 + 1):
                    total += 1
                    break
        return total

    def get_p2(self) -> int:
        processed: list[tuple[int, int]] = []
        queue = self.__fresh_id_ranges.copy()
        while queue:
            r0, r1 = queue.pop(0)
            for i, (p0, p1) in enumerate(processed):
                if (
                    r0 in range(p0, p1 + 1)
                    or r1 in range(p0, p1 + 1)
                    or p0 in range(r0, r1 + 1)
                ):
                    _ = processed.pop(i)
                    queue.append((min(p0, r0), max(p1, r1)))
                    break
            else:
                processed.append((r0, r1))
        return sum([1 + p1 - p0 for p0, p1 in processed])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
