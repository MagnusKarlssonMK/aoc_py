import argparse
from typing import cast

from aoc_py.runner import run


def main() -> None:
    """
    Entry point of CLI
    """
    parser = argparse.ArgumentParser(
        description="Advent of Code solver"
    )

    _ = parser.add_argument(
        "year",
        type=int,
        help="Year, 4 digits"
    )
    _ = parser.add_argument(
        "day",
        type=int,
        help="Day, 2 digits"
    )
    _ = parser.add_argument(
        "--part",
        type=int,
        choices=[1, 2],
        default=None,
        help="Run only part 1 or 2")

    args = parser.parse_args()
    year: int = cast(int, args.year)
    day: int = cast(int, args.day)
    part: int = cast(int, args.part)
    run(year, day, part)
