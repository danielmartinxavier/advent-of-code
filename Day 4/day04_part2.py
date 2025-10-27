# day04_part2.py

def count_x_mas(filename: str) -> int:
    # Read the grid from the file
    with open(filename, "r", encoding="utf-8") as f:
        grid = [line.strip() for line in f if line.strip()]

    # Dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    # Valid patterns for "XMAS" in an X shape
    valid = {("M", "A", "S"), ("S", "A", "M")}
    total = 0

    # Only positions that can be the center of an X (i.e., have neighbors diagonally)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # The center must be 'A'
            if grid[r][c] != "A":
                continue
            # Check the two diagonal patterns
            diag1 = (grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1])  # (down, right)
            diag2 = (grid[r - 1][c + 1], grid[r][c], grid[r + 1][c - 1])  # (down, left)
            # If either diagonal matches a valid pattern, count it
            if diag1 in valid and diag2 in valid:
                total += 1
    return total

if __name__ == "__main__":
    # Test
    print(f"Test = {count_x_mas('test_4.txt')}")
    # Input
    print(f"Input = {count_x_mas('input_4.txt')}")