"""
2025 day 11 - Reactor

Input lines list connections between named nodes ("from: to1 to2 ...").

Part 1

Simple recursive DFS with memoization to count the number of paths from "you" to "out".

Part 2

Similar to part 1, but the memoization key also carries whether or not "fft" and "dac"
have been visited, and only paths that reach "out" after visiting both count.
"""


class InputData:
    __tree: dict[str, list[str]]

    def __init__(self, rawstr: str) -> None:
        self.__tree = {
            left: right.split()
            for left, right in [line.split(": ", 1) for line in rawstr.splitlines()]
        }

    def __find_nbr_paths_straight(self, key: str, seen: dict[str, int]) -> int:
        if key == "out":
            return 1
        total = 0
        if (connections := self.__tree.get(key)) is not None:
            for connection in connections:
                if (v := seen.get(connection)) is not None:
                    total += v
                else:
                    v = self.__find_nbr_paths_straight(connection, seen)
                    seen[connection] = v
                    total += v
        return total

    def __find_nbr_paths_fft_dac(
        self, key: str, fft: bool, dac: bool, seen: dict[tuple[str, bool, bool], int]
    ) -> int:
        if key == "out":
            return 1 if fft and dac else 0
        fft = fft or key == "fft"
        dac = dac or key == "dac"
        total = 0
        if (connections := self.__tree.get(key)) is not None:
            for connection in connections:
                new_key = (connection, fft, dac)
                if (v := seen.get(new_key)) is not None:
                    total += v
                else:
                    v = self.__find_nbr_paths_fft_dac(*new_key, seen)
                    seen[new_key] = v
                    total += v
        return total

    def get_p1(self) -> int:
        return self.__find_nbr_paths_straight("you", {})

    def get_p2(self) -> int:
        return self.__find_nbr_paths_fft_dac("svr", False, False, {})


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
