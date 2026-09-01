"""
2022 day 5 - Supply Stacks

Stores the input data in a crateship class, containing the crates and procedures. The answer is provided with a
method running the procedures. This is done on a local copy of the crate data to avoid having to create a copy
of the entire class for Part 2.
"""
from copy import deepcopy


class InputData:
    def __init__(self, rawstr: str):
        cratestr, procedurestr = rawstr.split("\n\n")
        self.__procedures: list[tuple[int, int, int]] = []
        for line in procedurestr.splitlines():
            tokens = line.split()
            self.__procedures.append((int(tokens[1]), int(tokens[3]), int(tokens[5])))
        self.__crates: dict[int, list[str]] = {}
        cratelines = cratestr.splitlines()
        crate_indices = [i for i, c in enumerate(cratelines[-1]) if c != " "]
        print(f"{crate_indices}")
        for row_idx, line in enumerate(reversed(cratelines)):
            if row_idx == 0:
                for i, _ in enumerate(crate_indices):
                    self.__crates[i + 1] = []
            else:
                for i, v in enumerate(crate_indices):
                    # Safety check for len(line), in case editor shaves trailing spaces from the input
                    if v < len(line) and (c := line[v]) != " ":
                        self.__crates[i + 1].append(c)

    def run_procedures(self, multicrates: bool = False) -> str:
        crates = deepcopy(self.__crates)
        for proc_nbr, proc_from, proc_to in self.__procedures:
            for idx in range(proc_nbr):
                if multicrates:
                    movecrate = crates[proc_from].pop(idx - proc_nbr)
                else:
                    movecrate = crates[proc_from].pop()
                crates[proc_to].append(movecrate)
        return ''.join([crates[key][-1] for key in list(crates.keys())])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = p.run_procedures()
        if part in (None, 2):
            p2 = p.run_procedures(True)

        return p1, p2
