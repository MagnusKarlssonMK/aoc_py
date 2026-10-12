"""
2020 day 4 - Passport Processing
"""

from enum import Enum


class Field(Enum):
    BYR = "byr"
    IYR = "iyr"
    EYR = "eyr"
    HGT = "hgt"
    HCL = "hcl"
    ECL = "ecl"
    PID = "pid"
    CID = "cid"

    def is_valid(self, v: str) -> bool:
        match self:
            case self.BYR:
                return v.isdigit() and int(v) in range(1920, 2003)
            case self.IYR:
                return v.isdigit() and int(v) in range(2010, 2021)
            case self.EYR:
                return v.isdigit() and int(v) in range(2020, 2031)
            case self.HGT:
                if v.endswith("cm"):
                    return v[:-2].isdigit() and int(v[:-2]) in range(150, 194)
                if v.endswith("in"):
                    return v[:-2].isdigit() and int(v[:-2]) in range(59, 77)
                return False
            case self.HCL:
                return (
                    len(v) == 7
                    and v.startswith("#")
                    and all(c in "0123456789abcdef" for c in v[1:])
                )
            case self.ECL:
                return v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
            case self.PID:
                return len(v) == 9 and v.isdigit()
            case self.CID:
                return True


class Validity(Enum):
    RELAXED = 0
    STRICT = 1
    INVALID = 2


class Passport:
    def __init__(self, rawstr: str) -> None:
        self.__fields: dict[Field, str] = {
            Field(f): v for f, v in [fs.split(":") for fs in rawstr.split()]
        }

    def get_validity(self) -> Validity:
        if len(self.__fields) == 8 or (
            len(self.__fields) == 7 and Field.CID not in self.__fields
        ):
            for f, v in self.__fields.items():
                if not f.is_valid(v):
                    return Validity.RELAXED
            return Validity.STRICT
        return Validity.INVALID


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__passports = [Passport(p) for p in rawstr.split("\n\n")]

    def get_valid_passports_count(self) -> tuple[int, int]:
        p1 = p2 = 0
        for p in self.__passports:
            match p.get_validity():
                case Validity.RELAXED:
                    p1 += 1
                case Validity.STRICT:
                    p1 += 1
                    p2 += 1
                case Validity.INVALID:
                    pass
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_valid_passports_count()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
