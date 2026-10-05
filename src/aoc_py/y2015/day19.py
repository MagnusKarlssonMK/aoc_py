"""
2015 day 19 - Medicine for Rudolph

Part 1 applies every replacement rule once at every position it matches, and counts how many
distinct molecules come out. The results go into a set because the puzzle counts distinct
molecules rather than distinct applications, and two different rules can easily produce the same
one. match_indices scans every offset rather than using str.replace, so a rule whose right-hand
side overlaps its own left-hand side still matches at each position.

Part 2 is a closed form, not a search. Working backwards from the molecule to "e" is a shortest
path problem over an enormous graph, but it turns out not to need solving at all. Give a string s
the measure

    P(s) = uppercase letters - occurrences of Rn - occurrences of Ar - 2 * occurrences of Y

and then note what one reduction step does to it. In the real input every rule satisfies

    P(right) - P(left) == 1

with exactly three exceptions, the rules that reduce to "e", where the difference is 2 instead.
A reduction ends at "e", and P("e") is 0, so if the molecule takes n steps then one of them is
the "e" rule and the other n - 1 are ordinary:

    P(molecule) = (n - 1) * 1 + 1 * 2 = n + 1

which gives n = P(molecule) - 1, and that is what get_p2 computes. The trailing 1 in the code is
therefore the extra unit contributed by the "e" rule, and it is the only
reason the subtraction is there. Because each step removes a fixed amount, the total does not
depend on which reduction path is taken, so no search or tie-breaking is required.
"""


def match_indices(s: str, needle: str) -> list[int]:
    return [i for i in range(len(s) - len(needle) + 1) if s.startswith(needle, i)]


class InputData:
    __replacements: dict[str, list[str]]
    __molecule: str

    def __init__(self, s: str) -> None:
        r, self.__molecule = s.split("\n\n")
        self.__replacements = {}
        for line in r.splitlines():
            left, right = line.split(" => ")
            self.__replacements.setdefault(left, []).append(right)

    def get_p1(self) -> int:
        altered: set[str] = set()
        for replaced, v in self.__replacements.items():
            for replacement in v:
                for i in match_indices(self.__molecule, replaced):
                    j = i + len(replaced)
                    altered.add(self.__molecule[:i] + replacement + self.__molecule[j:])
        return len(altered)

    def get_p2(self) -> int:
        elements = len([c for c in self.__molecule if c.isupper()])
        rn = self.__molecule.count("Rn")
        ar = self.__molecule.count("Ar")
        y = self.__molecule.count("Y")
        return elements - ar - rn - (2 * y) - 1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
