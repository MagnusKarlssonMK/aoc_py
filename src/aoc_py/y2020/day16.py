"""
2020 day 16 - Ticket Translation

Part 1 sums every nearby value that fits none of the field ranges. Part 2 keeps only the fully
valid tickets, uses each column's candidate fields to deduce the field order (settling
single-candidate columns and removing that field from the rest) and multiplies the departure
fields of your own ticket.
"""

import math


class Field:
    def __init__(self, rawstr: str) -> None:
        name, nbrstring = rawstr.split(": ")
        self.name: str = name
        n1, n2 = nbrstring.split(" or ")
        nbrs = list(map(int, n1.split("-") + n2.split("-")))
        self.__ranges: tuple[range, range] = (
            range(nbrs[0], nbrs[1] + 1),
            range(nbrs[2], nbrs[3] + 1),
        )

    def is_inrange(self, nbr: int) -> bool:
        return any(nbr in r for r in self.__ranges)


class InputData:
    def __init__(self, rawstr: str) -> None:
        fields, your, nearby = rawstr.split("\n\n")
        self.__fields = [Field(line) for line in fields.splitlines()]
        self.__your = list(map(int, your.splitlines()[1].split(",")))
        self.__nearby = [
            list(map(int, line.split(","))) for line in nearby.splitlines()[1:]
        ]

    def __in_any_field(self, nbr: int) -> bool:
        return any(f.is_inrange(nbr) for f in self.__fields)

    def get_p1(self) -> int:
        return sum(
            nbr
            for ticket in self.__nearby
            for nbr in ticket
            if not self.__in_any_field(nbr)
        )

    def get_p2(self) -> int:
        valid = [
            ticket for ticket in self.__nearby if all(map(self.__in_any_field, ticket))
        ]
        candidates = [
            {
                field.name
                for field in self.__fields
                if all(field.is_inrange(ticket[i]) for ticket in valid)
            }
            for i in range(len(self.__your))
        ]
        resolved: dict[int, str] = {}
        while len(resolved) < len(candidates):
            single = next(
                (i for i, names in enumerate(candidates) if len(names) == 1), None
            )
            if single is None:
                return -1
            name = candidates[single].pop()
            resolved[single] = name
            for names in candidates:
                names.discard(name)
        return math.prod(
            self.__your[i] for i, name in resolved.items() if "departure" in name
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
