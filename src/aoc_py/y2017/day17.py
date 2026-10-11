"""
2017 day 17 - Spinlock

Part 1

Just build the buffer while keeping track of the current position.

Part 2

The value 0 never moves from index 0, so we only need to know which value ends up at index 1. A naive
loop over all 50M insertions is slow, so whole stretches are skipped at a time:

Between two wrap-arounds the position simply climbs. Each insertion moves the current position by `steps`
positions plus one extra step for the newly inserted value (steps + 1 in total), while the buffer only
grows by one. The gap between the current position and the end of the buffer therefore shrinks by exactly
`steps` every insertion, and no value can land at index 1 while the position is just climbing. So the climb
up to the next wrap-around can be jumped over in one go: the jump is `(gap - 1) // steps` rounds (a
ceil-div). At a wrap-around the position drops back below `steps`, so the number of wraps - and thus the
number of loop iterations - is tiny.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__steps = int(s)

    def get_p1(self) -> int:
        buffer = [0]
        current_pos = 0
        for nbr in range(1, 2018):
            current_pos = 1 + (current_pos + self.__steps) % nbr
            buffer.insert(current_pos, nbr)
        return buffer[current_pos + 1]

    def get_p2(self, target: int = 50_000_000) -> int:
        steps = self.__steps
        current_pos = 0
        pos_1 = -1
        nbr = 1
        while nbr <= target:
            gap = nbr - current_pos
            if gap > steps:
                # Climb: gap shrinks by `steps` per round, so the next wrap-around happens
                # `(gap - 1) // steps` rounds from here. No index-1 value can land in between.
                jump = (gap - 1) // steps
                if nbr + jump > target:
                    break
                nbr += jump
                current_pos += jump * (steps + 1)
            # Wrap-around: the only round that can drop a value at index 1.
            current_pos = 1 + (current_pos + steps) % nbr
            if current_pos == 1:
                pos_1 = nbr
            nbr += 1
        return pos_1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
