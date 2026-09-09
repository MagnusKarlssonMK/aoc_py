"""
2020 day 7 - Handy Haversacks

Even more string parsing gymnastics. Extract the data into a dictionary, BFS to expand all reachable bags from the
starting bag until either the golden bag is found or list runs out, which gives the answer to Part 1.
For Part 2, make a recursive call on the dictionary to count the bags in the bag in the bag...
I added a memo cache for the recursion just in case, since I suspected that there would be a lot of repeated
calls for the same bag, but it doesn't seem to make much of a performance difference.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        lines: list[tuple[str, list[str]]] = [
            (i[0], i[1].split(", "))
            for i in [line.split(" bags contain ") for line in rawstr.splitlines()]
        ]
        self.__rules: dict[str, list[tuple[int, str]]] = {}
        for line in lines:
            self.__rules[line[0]] = []
            for content in line[1]:
                if "no other" in content:
                    break
                nbr, bag_p1, bag_p2, _ = content.split()
                self.__rules[line[0]].append((int(nbr), bag_p1 + " " + bag_p2))
        self.__bagcontent_cache: dict[str, int] = {}

    def get_p1(self, bag: str) -> int:
        count = 0
        for key in self.__rules:
            content: list[tuple[int, str]] = list(self.__rules[key])
            while content:
                _, color = content.pop(0)
                if color == bag:
                    count += 1
                    break
                for n, c in self.__rules[color]:
                    content.append((n, c))
        return count

    def get_p2(self, bag: str) -> int:
        return self.__count_content(bag) - 1  # -1 to not count the input bag itself

    def __count_content(self, bag: str) -> int:
        if bag in self.__bagcontent_cache:
            return self.__bagcontent_cache[bag]
        count = 1  # +1 to include the bag itself too, not just its content.
        for nbr, color in self.__rules[bag]:
            count += nbr * self.__count_content(color)
        self.__bagcontent_cache[bag] = count
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1("shiny gold"))
    if part in (None, 2):
        p2 = str(p.get_p2("shiny gold"))

    return p1, p2
