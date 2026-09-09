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
                return int(v) in range(1920, 2003) if v.isdigit() else False
            case self.IYR:
                return int(v) in range(2010, 2021) if v.isdigit() else False
            case self.EYR:
                return int(v) in range(2020, 2031) if v.isdigit() else False
            case self.HGT:
                if v.endswith("cm"):
                    return int(v[:-2]) in range(150, 194) if v[:-2].isdigit() else False
                elif v.endswith("in"):
                    return int(v[:-2]) in range(59, 77) if v[:-2].isdigit() else False
                else:
                    return False
            case self.HCL:
                if v.startswith("#"):
                    return all(c in "abcdef0123456789" for c in v[1:])
                else:
                    return False
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
    def __init__(self, s: str) -> None:
        self.__fields: dict[Field, str] = {
            Field(f): v for f, v in [fs.split(":") for fs in s.split()]
        }

    def get_validity(self) -> Validity:
        if len(self.__fields) == 8 or (
            len(self.__fields) == 7 and not Field.CID in self.__fields
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
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_valid_passports_count()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
