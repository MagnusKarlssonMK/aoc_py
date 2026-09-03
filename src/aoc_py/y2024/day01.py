"""
2024 day 1 - Historian Hysteria

Part 1

Store the two lists in sorted vectors, then simply zip them together
and calculate the differences between each pair.

Part 2

Make use of the already sorted lists, and iterate over the left side.
Keep track of the index of the last element used on the right side
to minimize the amount of looping on the right side.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__left: list[int] = []
        self.__right: list[int] = []
        for line in rawstr.splitlines():
            left, right = line.split()
            self.__left.append(int(left))
            self.__right.append(int(right))
        self.__left.sort()
        self.__right.sort()

    def get_p1(self) -> int:
        return sum(abs(left - right) for left, right in zip(self.__left, self.__right))

    def get_p2(self) -> int:
        score = 0
        right_idx = 0
        for left in self.__left:
            delta = 0
            while right_idx + delta < len(self.__right):
                if self.__right[right_idx + delta] > left:
                    break
                if self.__right[right_idx + delta] == left:
                    score += left
                    delta += 1
                else:
                    right_idx += 1
        return score


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
