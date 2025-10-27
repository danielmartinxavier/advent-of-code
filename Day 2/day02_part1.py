# day01_part1.py

def is_safe(levels):
    # Adjacent diffs
    diffs = [b - a for a, b in zip(levels, levels[1:])]

    # No equal adjacent levels
    if any(d == 0 for d in diffs):          
        return False
    
    # Direction must be consistent
    all_inc = all(d > 0 for d in diffs)
    all_dec = all(d < 0 for d in diffs)
    if not (all_inc or all_dec):
        return False
    
    # Step sizes must be [1,3]
    return all(1 <= abs(d) <= 3 for d in diffs)

def count_safe(filename: str) -> int:
    
    safe = 0
    # Opens the .txt file so the program can read it line by line
    with open(filename) as f:
        for line in f:
            if not line.strip(): # Skip empty lines
                continue

            # Convert line to list of integers
            levels = list(map(int, line.split()))

            # Check if the levels are safe
            if is_safe(levels):
                safe += 1
    return safe

if __name__ == "__main__":
    # Test
    result = count_safe("test_2.txt")
    print(f"Test = {result}")
    # Input
    output = count_safe("input_2.txt")
    print(f"Output = {output}")