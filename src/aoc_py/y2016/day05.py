"""
2016 day 5 - How About a Nice Game of Chess?

Iterate with an increasing index value and use hashlib to calculate the md5 checksums to generate the passwords.
Takes a lot of iterations, i.e. doorbreaking is NOT fast.
"""

import hashlib


class InputData:
    __PASSWORD_LEN = 8

    def __init__(self, rawstr: str) -> None:
        self.__door_id = rawstr

    def get_p1(self) -> str:
        pwd = ""
        index = 0
        while len(pwd) < InputData.__PASSWORD_LEN:
            hashed = hashlib.md5((self.__door_id + str(index)).encode()).hexdigest()
            if hashed.startswith("00000"):
                pwd += hashed[5]
            index += 1
        return pwd

    def get_p2(self) -> str:
        pwd = ["_" for _ in range(InputData.__PASSWORD_LEN)]
        index = 0
        while "_" in pwd:
            hashed = hashlib.md5((self.__door_id + str(index)).encode()).hexdigest()
            if hashed.startswith("00000") and hashed[5].isdigit():
                pos = int(hashed[5])
                if pos < InputData.__PASSWORD_LEN and pwd[int(pos)] == "_":
                    pwd[int(pos)] = hashed[6]
            index += 1
        return "".join(pwd)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = p.get_p1()
    if part in (None, 2):
        p2 = p.get_p2()

    return p1, p2
