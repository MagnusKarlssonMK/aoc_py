"""
2023 day 9 - Mirage Maintenance

Just a simple recursive function to generate the lines until a line of zeroes shows up.
Surprisingly simple part 2, basically just to reverse the input data and run the same function.
"""


def findnextnumber(nbrs: list[int]) -> int:
    if all(nbr == 0 for nbr in nbrs):
        return 0
    else:
        nextlevellist = [nbrs[i] - nbrs[i - 1] for i in range(1, len(nbrs))]
        return nbrs[-1] + findnextnumber(nextlevellist)


def get_numbers(s: str) -> tuple[int, int]:
    result_p1 = 0
    result_p2 = 0
    for line in s.splitlines():
        numbers = list(map(int, line.split()))
        result_p1 += findnextnumber(numbers)
        result_p2 += findnextnumber(list(reversed(numbers)))
    return result_p1, result_p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = get_numbers(inputdata)
    if part in (None, 1):
        p1 = str(p[0])
    if part in (None, 2):
        p2 = str(p[1])

    return p1, p2
