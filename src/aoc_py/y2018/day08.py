"""
2018 day 8 - Memory Maneuver

Recursive solution for both parts.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbrs = list(map(int, s.split()))

    def __decode_node(self, idx: int) -> tuple[int, int]:
        child_count, meta_count = self.__nbrs[idx], self.__nbrs[idx + 1]
        next_idx = idx + 2
        meta_sum = 0
        for _ in range(child_count):
            next_idx, child_meta = self.__decode_node(next_idx)
            meta_sum += child_meta
        meta_sum += sum(self.__nbrs[next_idx : next_idx + meta_count])
        return next_idx + meta_count, meta_sum

    def __get_node_value(self, idx: int) -> tuple[int, int]:
        child_count, meta_count = self.__nbrs[idx], self.__nbrs[idx + 1]
        next_idx = idx + 2
        child_metas: list[int] = []
        for _ in range(child_count):
            next_idx, child_meta = self.__get_node_value(next_idx)
            child_metas.append(child_meta)
        meta_values = self.__nbrs[next_idx : next_idx + meta_count]
        if child_count == 0:
            return next_idx + meta_count, sum(meta_values)
        # Note: the meta values as child references are 1-indexed; our local list is not.
        meta_sum = sum(
            [child_metas[mv - 1] for mv in meta_values if 1 <= mv <= len(child_metas)]
        )
        return next_idx + meta_count, meta_sum

    def get_p1(self) -> int:
        return self.__decode_node(0)[1]

    def get_p2(self) -> int:
        return self.__get_node_value(0)[1]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
