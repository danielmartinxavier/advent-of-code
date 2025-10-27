# advent-of-code
This repository contains Python implementations for the first four days of the [Advent of Code](https://adventofcode.com/) programming challenge. The code was originally prepared for the Wandercraft hiring challenge and focuses on clear logic, readability, and reproducibility.

## Requirements
- Python 3.10 or newer.
- No third-party dependencies are required. All solutions rely exclusively on the Python standard library.

## Repository Structure
Each puzzle day lives in its own directory with separate scripts for Part 1 and Part 2 alongside the corresponding input data. The table below summarises the available solutions.

| Day | Part | Script | Description |
| --- | --- | --- | --- |
| 1 | Part 1 | `Day 1/day01_part1.py` | Computes the sum of distances between two sorted lists extracted from the puzzle input. |
| 1 | Part 2 | `Day 1/day01_part2.py` | Uses frequency counting to evaluate the similarity score between the two columns of integers. |
| 2 | Part 1 | `Day 2/day02_part1.py` | Counts the number of “safe” level reports where the differences between adjacent levels are monotonic and stay within the allowed range. |
| 2 | Part 2 | `Day 2/day02_part2.py` | Extends the part 1 logic by allowing a single removal (problem dampener) to make a report safe. |
| 3 | Part 1 | `Day 3/day03_part1.py` | Parses `mul(a,b)` instructions and sums the products of every valid pair in the input stream. |
| 3 | Part 2 | `Day 3/day03_part2.py` | Processes the same instruction stream while toggling multiplication on and off with `do()`/`don't()` markers. |
| 4 | Part 1 | `Day 4/day04_part1.py` | Searches a character grid for the word `XMAS` in all eight directions. |
| 4 | Part 2 | `Day 4/day04_part2.py` | Counts occurrences of the word in an X-shaped pattern centred around `A` characters. |

Each folder also includes the original puzzle input (`input*.txt`) and example data (`test*.txt`) used to verify correctness.

## Running the Solutions

1. Move into the project directory:
   ```bash
   cd advent-of-code
   ```
2. Navigate to the desired puzzle day, for example day 3:
   ```bash
   cd "Day 3"
   ```
3. Run the part you want to evaluate with Python:
   ```bash
   python day03_part1.py
   ```

By default each script will print the result for the provided sample input followed by the answer for the full puzzle input. To reuse the solvers with different data, replace the content of the `input` files or modify the file paths in the `__main__` block at the bottom of each script.

## Results (8 integers)

**Day 1**
- Part 1: 1320851  
- Part 2: 26859182  

**Day 2**
- Part 1: 526
- Part 2: 566

**Day 3**
- Part 1: 159892596
- Part 2: 92626942

**Day 4**
- Part 1: 2633
- Part 2: 1936
