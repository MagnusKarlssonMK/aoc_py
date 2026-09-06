"""
2021 day 1 - Sonar Sweep

For part 2, we actually only need to compare the first element of the first window with the last element of the
second window, since all the elements in between are shared by both. So by making use of that logic, the answer
for both part 1 and 2 can be calculated with one function, taking the window length as an input.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbrs = list(map(int, s.splitlines()))

    def count_depth_increase(self, windowsize: int) -> int:
        return sum(
            [
                1
                for i in range(windowsize, len(self.__nbrs))
                if self.__nbrs[i] > self.__nbrs[i - windowsize]
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.count_depth_increase(1))
    if part in (None, 2):
        p2 = str(p.count_depth_increase(3))

    return p1, p2
