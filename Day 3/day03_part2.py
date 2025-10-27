# day03_part2.py
import re

# Tokenize only the valid constructs, in order
TOKENS = re.compile(
    r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)"
)

def sum_enabled_multiplies(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        s = f.read()

    # mul is enabled at the beginning
    enabled = True   
    total = 0

    for match in TOKENS.finditer(s):
        # Check which token was matched
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        else:
            # It's a mul(a,b)
            if enabled:
                a = int(match.group(1))
                b = int(match.group(2))
                total += a * b
    return total

if __name__ == "__main__":
    # Test
    print(f"Test = {sum_enabled_multiplies('test_3_2.txt')}")
    # Input
    print(f"Output = {sum_enabled_multiplies('input_3.txt')}")
