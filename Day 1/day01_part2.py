# day01_part2.py
from collections import Counter

def similarity_score(filename: str) -> int:
    # Declare empty lists
    left, right = [], []

    # Opens the .txt file so the program can read it line by line
    with open(filename) as f:
        for line in f:
            if not line.strip(): # Skip empty lines
                continue
            a, b = map(int, line.split()) # Divides the line into two pieces and converts them from text to integers

            # Appends the integers to their respective lists
            left.append(a)               
            right.append(b)
            
    # Count frequencies of elements in right list
    freq = Counter(right)
    return sum(x * freq[x] for x in left)

if __name__ == "__main__":
    # Test
    result = similarity_score("test.txt")
    print(f"Test = {result}")
    # Input
    output = similarity_score("input.txt")
    print(f"Output = {output}")