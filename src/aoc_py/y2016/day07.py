"""
2016 day 7 - Internet Protocol Version 7

Use regex to split the IP addresses in segments based on the brackets; the first segment and every other segment after
that will be a supernet, while the second segment and every other after that will be a hypernet.
From there on it's mostly just string parsing, with a sliding window over the strings to scan them for the patterns.
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
    for i in range(len(word) - 2):
        if word[i] == word[i + 2] and word[i] != word[i + 1]:
            yield word[i + 1] + word[i] + word[i + 1]


class IpAddress:
    def __init__(self, ip: str) -> None:
        self.__supernets: list[str] = []
        self.__hypernets: list[str] = []
        parts = ip.replace("[", "]").split("]")
        self.__supernets = parts[0::2]
        self.__hypernets = parts[1::2]

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
