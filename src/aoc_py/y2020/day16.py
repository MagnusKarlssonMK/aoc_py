"""
2020 day 16 - Ticket Translation
"""

import math


class Field:
    def __init__(self, s: str) -> None:
        name, nbrstring = s.split(": ")
        self.name: str = name
        n1, n2 = nbrstring.split(" or ")
        nbrs = list(map(int, n1.split("-") + n2.split("-")))
        # nbrs = list(map(int, re.findall(r'\d+', nbrstring)))
        self.__ranges: tuple[range, range] = (
            range(nbrs[0], nbrs[1] + 1),
            range(nbrs[2], nbrs[3] + 1),
        )

    def is_inrange(self, nbr: int) -> bool:
        return any(nbr in r for r in self.__ranges)


class Ticket:
    def __init__(self, nbrs: list[int]) -> None:
        self.nbrs: list[int] = list(nbrs)


class InputData:
    def __init__(self, rawstr: str) -> None:
        fields, your, nearby = rawstr.split("\n\n")
        your = list(map(int, your.splitlines()[1].split(",")))
        nearby = nearby.splitlines()
        self.__fields: list[Field] = [Field(line) for line in fields.splitlines()]
        self.__your: Ticket = Ticket(your)
        self.__nearby: list[Ticket] = [
            Ticket(list(map(int, nearby[i].split(",")))) for i in range(1, len(nearby))
        ]

    def get_p1(self) -> int:
        invalid_nbrs: list[int] = []
        validnearby: list[Ticket] = []
        for ticket in self.__nearby:
            for nbr in ticket.nbrs:
                if not any(f.is_inrange(nbr) for f in self.__fields):
                    invalid_nbrs.append(nbr)
                    break
            else:
                validnearby.append(ticket)
        self.__nearby = validnearby
        return sum(invalid_nbrs)

    def get_p2(self) -> int:
        nbrsets = [
            {nt.nbrs[i] for nt in self.__nearby}
            for i in range(len(self.__nearby[0].nbrs))
        ]
        possible = [
            [
                field.name
                for field in self.__fields
                if all(field.is_inrange(nbr) for nbr in nbrset)
            ]
            for nbrset in nbrsets
        ]
        possible = [(i, p) for i, p in enumerate(possible)]
        possible = sorted(possible, key=lambda x: len(x[1]))
        queue = [[p] for p in possible[0][1]]
        paths: list[list[str]] = []
        while queue:
            p = queue.pop(0)
            for nxt in possible[len(p)][1]:
                if nxt not in p:
                    n_p = list(p)
                    n_p.append(nxt)
                    if len(n_p) >= len(possible):
                        paths.append(n_p)
                    else:
                        queue.append(n_p)
        if len(paths) != 1:
            return -1
        path = sorted(zip([p[0] for p in possible], paths[0]), key=lambda x: x[0])
        return math.prod(
            [self.__your.nbrs[idx] for idx, name in path if "departure" in name]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
