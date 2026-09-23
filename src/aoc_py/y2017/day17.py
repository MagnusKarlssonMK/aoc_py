"""
2017 day 17 - Spinlock

Part 1

Just build the buffer while keeping track of the current position.

Part 2

No need to actually build the buffer now, since the value 0 will always be in index 0, i.e. we are only looking
for the number in index 1 after 50M iterations. So all we need to do is to keep track of the current position and
update the current value of index 1 whenever it ends up there.
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

    def get_p2(self) -> int:
        pos_1 = -1
        current_pos = 0
        for nbr in range(1, 50_000_001):
            current_pos = 1 + (current_pos + self.__steps) % nbr
            if current_pos == 1:
                pos_1 = nbr
        return pos_1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
