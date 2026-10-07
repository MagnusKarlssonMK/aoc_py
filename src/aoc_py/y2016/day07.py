"""
2016 day 7 - Internet Protocol Version 7

Split each address on its brackets: replace "[" with "]", split on "]", the even segments are the supernets
(parts outside brackets) while the odd ones are the hypernets (inside brackets). Part 1 counts addresses with
an ABBA -- equal first and last of four characters, equal middle two, different first two -- in a supernet and
none in any hypernet; part 2 those with an ABA in a supernet whose mirrored BAB sits in a hypernet.
"""

from collections.abc import Generator


def contains_abba(word: str) -> bool:
    for i in range(len(word) - 3):
        if (
            word[i] == word[i + 3]
            and word[i] != word[i + 1]
            and word[i + 1] == word[i + 2]
        ):
            return True
    return False


def get_aba(word: str) -> Generator[str]:
    for i in range(len(word) - 2):
        if word[i] == word[i + 2] and word[i] != word[i + 1]:
            yield word[i : i + 3]


def get_bab(word: str) -> Generator[str]:
    for aba in get_aba(word):
        yield aba[1] + aba[0] + aba[1]


class IpAddress:
    def __init__(self, ip: str) -> None:
        parts = ip.replace("[", "]").split("]")
        self.__supernets: list[str] = parts[0::2]
        self.__hypernets: list[str] = parts[1::2]

    def supports_tls(self) -> bool:
        for word in self.__hypernets:
            if contains_abba(word):
                return False
        for word in self.__supernets:
            if contains_abba(word):
                return True
        return False

    def supports_ssl(self) -> bool:
        aba: set[str] = set()
        bab: set[str] = set()
        for word in self.__supernets:
            for a in get_aba(word):
                aba.add(a)
        for word in self.__hypernets:
            for a in get_bab(word):
                bab.add(a)
        return len(aba & bab) > 0


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__ipaddr = [IpAddress(line) for line in rawstr.splitlines()]

    def get_tls_support_count(self) -> int:
        return sum([1 if ip.supports_tls() else 0 for ip in self.__ipaddr])

    def get_ssl_support_count(self) -> int:
        return sum([1 if ip.supports_ssl() else 0 for ip in self.__ipaddr])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_tls_support_count())
    if part in (None, 2):
        p2 = str(p.get_ssl_support_count())

    return p1, p2
