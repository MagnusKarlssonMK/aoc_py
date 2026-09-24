"""
2018 day 7 - The Sum of Its Parts

Store the step rules in a dict, then keep track of which steps are done (and working for part 2) to figure out
which steps are available.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__steprules: dict[str, set[str]] = {}
        for line in s.splitlines():
            w = line.split()
            if w[1] not in self.__steprules:
                self.__steprules[w[1]] = set()
            if w[7] not in self.__steprules:
                self.__steprules[w[7]] = set()
            self.__steprules[w[7]].add(w[1])

    def get_p1(self) -> str:
        done: list[str] = []
        # Sorted list so that we choose alphabetically when multiple steps are available
        not_done = sorted(self.__steprules)
        while not_done:
            available = None
            for i, step in enumerate(not_done):
                for req in self.__steprules[step]:
                    if req not in done:
                        break
                else:
                    available = not_done.pop(i)
                if available:
                    done.append(available)
                    break
        return "".join(done)

    def get_p2(self, additional_workers: int = 4, flatcost: int = 60) -> int:
        done: list[str] = []
        not_done = sorted([step for step in self.__steprules])
        working: dict[str, int] = {}
        seconds = 0
        while not_done or working:
            isdone: list[str] = []
            for w, val in working.items():
                if val == 0:
                    isdone.append(w)
                else:
                    working[w] -= 1
            for d in isdone:
                done.append(d)
                working.pop(d)
            seconds += 1
            available: list[str] = []
            for step in not_done:
                for req in self.__steprules[step]:
                    if req not in done:
                        break
                else:
                    available.append(step)
            for a in available:
                if len(working) < 1 + additional_workers:
                    working[a] = flatcost + ord(a) - ord("A")
                    not_done.remove(a)
                else:
                    break
        return seconds - 1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
