# day03_part1.py
import re

# Tokenize only the valid mul constructs
PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def sum_valid_multiplies(filename: str) -> int:
    # Read the file
    with open(filename, "r", encoding="utf-8") as f:
        s = f.read()
    total = 0
    # Sum all valid mul(a,b)
    for a, b in PATTERN.findall(s):
        total += int(a) * int(b)
    return total

if __name__ == "__main__":
    # Test
    print(f"Test = {sum_valid_multiplies('test_3.txt')}")
    # Input
    print(f"Output = {sum_valid_multiplies('input_3.txt')}")