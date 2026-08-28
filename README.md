# --- NOTICE ---
This project is currently being restructured to use UV for managing it, and porting the old standalone solvers
into the new structure is work-in-progress. This notice will be removed when everything has been migrated.

# Introduction
This is a collection of my Python solutions with varying degrees of quality to [Advent of Code](http://adventofcode.com) challenges, which 
I have been going through retroactively to blow the dust off my coding skills. Advent of Code is an annual event, with 
a daily coding puzzle between December 1 - 25, usually of gradually increasing complexity. I highly recommend these 
challenges to anyone looking to improve their coding skills or learn a new language.

Note - If you don't know how to find the past years challenges, you can get there by clicking the 'Events' link on the
AoC page.

# Input files
It is assumed that the input data for each problem is stored in a file with a file structure like 
`/AdventOfCode-Input/<year>/day<xx>.txt`, where that parent folder is placed in the root folder of this repo.
If your naming, file structure or location is different, the paths in the "load_input" function in src/runner.py
needs to be modified accordingly.

# Running the solver
This package is managed using UV, which needs to be installed locally. Once installed, the solver can be run with the CLI tool.
To run the solver for a certain day, for example 2024 day 12:

bash
uv run aoc-py 2024 12

To run only either part 1 or part 2:

bash
uv run aoc-py 2024 12 --part 2

## Running tests
To run all unit tests:

bash
uv run pytest

To specify and run tests only for a certain year, for example 2024:

bash
uv run pytest tests/y2024
