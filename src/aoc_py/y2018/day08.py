"""
2018 day 8 - Memory Maneuver

Recursive solution for both parts, done in a single walk that returns the metadata sum and the node value.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbrs = list(map(int, s.split()))

    def __decode(self, idx: int) -> tuple[int, int, int]:
        child_count, meta_count = self.__nbrs[idx], self.__nbrs[idx + 1]
        next_idx = idx + 2
        meta_sum = 0
        child_values: list[int] = []
        for _ in range(child_count):
            next_idx, child_meta, child_value = self.__decode(next_idx)
            meta_sum += child_meta
            child_values.append(child_value)
        meta_values = self.__nbrs[next_idx : next_idx + meta_count]
        if child_count == 0:
            value = sum(meta_values)
        else:
            # The meta values as child references are 1-indexed; our local list is not.
            value = sum(
                child_values[mv - 1]
                for mv in meta_values
                if 1 <= mv <= len(child_values)
            )
        return next_idx + meta_count, meta_sum + sum(meta_values), value

    def get_p1(self) -> int:
        return self.__decode(0)[1]

    def get_p2(self) -> int:
        return self.__decode(0)[2]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
