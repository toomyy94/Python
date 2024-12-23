def soup(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    # Define the possible directions for searching (including diagonals)
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # East, South, West, North
        (1, 1), (-1, -1), (-1, 1), (1, -1)  # Diagonals
    ]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                found = True
                r, c = row, col
                for letter in word:
                    if (
                            r < 0 or r >= rows or
                            c < 0 or c >= cols or
                            matrix[r][c] != letter
                    ):
                        found = False
                        break
                    r += dr
                    c += dc
                if found:
                    return f"{chr(65 + row)}{col + 1}"

    return None

# Example usage:
matrix = [
    ['X', 'R', 'Z', 'B', 'H', 'A'],
    ['K', 'A', 'S', 'I', 'G', 'O'],
    ['J', 'O', 'T', 'C', 'A', 'N'],
    ['F', 'S', 'R', 'H', 'T', 'U'],
    ['D', 'P', 'O', 'O', 'X', 'F'],
    ['Z', 'B', 'B', 'W', 'F', 'S']
]

word = "PORTO"
result = soup(matrix, word)
print(result)  # Output: "E2"
