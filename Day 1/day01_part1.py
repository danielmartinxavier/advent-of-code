# day01_part1.py
def total_distance(filename: str) -> int:
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
    # Sorts both lists in ascending order,
    left.sort()
    right.sort()

    # Compute the total distance
    return sum(abs(x - y) for x, y in zip(left, right))

if __name__ == "__main__":
    # Test
    result = total_distance("test.txt")
    print(f"Test = {result}")
    # Input
    output = total_distance("input.txt")
    print(f"Output = {output}")