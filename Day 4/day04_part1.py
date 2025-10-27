# day04_part1.py

def count_xmas(filename: str) -> int:
    # Read the grid from the file
    with open(filename, "r", encoding="utf-8") as f:
        grid = [line.strip() for line in f if line.strip()]

    # Dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # Valid pattern
    word = "XMAS"

    # All 8 possible directions (vertical, horizontal, diagonal)
    directions = [
        (1, 0), (-1, 0),   # vertical
        (0, 1), (0, -1),   # horizontal
        (1, 1), (-1, -1),  # diagonal (down, right) and (up, left))
        (1, -1), (-1, 1)   # diagonal (down,left)) and (up, right)
    ]

    def in_bounds(r, c):
        # Check if (r, c) is within grid bounds
        return 0 <= r < rows and 0 <= c < cols

    total = 0
    # Check each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "X":
                continue
            # Check all directions from the current 'X'
            for dr, dc in directions:
                match = True
                for k in range(1, len(word)):
                    nr, nc = r + dr * k, c + dc * k
                    # Check bounds and character match
                    if not in_bounds(nr, nc) or grid[nr][nc] != word[k]:
                        match = False
                        break
                if match:
                    # If a match is found in this direction, count it
                    total += 1
    return total


if __name__ == "__main__":
    # Test
    print(f"Test = {count_xmas('test_4.txt')}")
    # Input
    print(f"Input = {count_xmas('input_4.txt')}")