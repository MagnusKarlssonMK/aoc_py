"""
2020 day 13 - Shuttle Search

Part 1 finds the first bus departing at or after the estimate. Part 2 finds the earliest
timestamp satisfying every (bus id, offset) congruence by sieving: advance by the product of the
bus ids already fixed, which keeps all earlier congruences intact.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        estimate, buslist = rawstr.splitlines()
        self.__estimate = int(estimate)
        self.__buslist = [
            (int(v), i) for i, v in enumerate(buslist.split(",")) if v != "x"
        ]

    def get_p1(self) -> int:
        busid, wait = min(
            ((busid, busid - self.__estimate % busid) for busid, _ in self.__buslist),
            key=lambda x: x[1],
        )
        return busid * wait

    def get_p2(self) -> int:
        timestamp = 0
        step = 1
        for busid, idx in self.__buslist:
            while (timestamp + idx) % busid != 0:
                timestamp += step
            step *= busid
        return timestamp


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
