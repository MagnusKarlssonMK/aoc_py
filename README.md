# Introduction

This is a collection of my Python solutions with varying degrees of quality to [Advent of Code](http://adventofcode.com) challenges, which 
I have been going through retroactively to blow the dust off my coding skills. Advent of Code is an annual event, with 
daily coding puzzles starting December 1, usually of gradually increasing complexity. I highly recommend these 
puzzles to anyone looking to improve their coding skills or learn a new language.

Note - The puzzles for past years can be found by clicking the 'Events' link on the top of the AoC page.

# Input files

It is assumed that the input data for each problem is stored in a file with a file structure like 
`/AdventOfCode-Input/<year>/day<xx>.txt`, where that parent folder is placed in the root folder of this repo.
If your naming, file structure or location is different, the paths in the "load_input" function in `src/runner.py`
needs to be modified accordingly.

# Running the solver

This package is managed using UV, which needs to be installed locally. Once installed, the solver can be run with the CLI tool.
To run the solver for a certain day, for example 2024 day 12:

```sh
uv run aoc-py 2024 12
```

To run only either part 1 or part 2:

```sh
uv run aoc-py 2024 12 --part 2
```

# Running tests

To run all unit tests:

```sh
uv run pytest
```

To specify and run tests only for a certain year, for example 2024:

```sh
uv run pytest tests/y2024
```
