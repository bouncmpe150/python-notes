# Number Spiral Matrix
def generate_spiral_matrix(n):
    # Create an n x n matrix initialized with zeros
    matrix = [[0] * n for _ in range(n)]

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0  # Start by moving right
    x, y = 0, 0  # Starting position

    for num in range(1, n * n + 1):
        matrix[x][y] = num
        # Calculate the next position
        next_x = x + directions[direction_index][0]
        next_y = y + directions[direction_index][1]

        # Check if the next position is out of bounds or already filled
        if (0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] == 0):
            x, y = next_x, next_y
        else:
            # Change direction
            direction_index = (direction_index + 1) % 4
            x += directions[direction_index][0]
            y += directions[direction_index][1]

    # Print the matrix in the specified format
    for row in matrix:
        print(' '.join(str(num) for num in row))

# Example
generate_spiral_matrix(4)



# Conway's Game of Life
def next_generation(grid):
    n = len(grid)
    new_grid = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # Count live neighbors
            live_neighbors = 0
            for x in range(max(0, i - 1), min(n, i + 2)):
                for y in range(max(0, j - 1), min(n, j + 2)):
                    if (x, y) != (i, j):
                        live_neighbors += grid[x][y]

            # Apply the rules of the Game of Life
            if grid[i][j] == 1:
                new_grid[i][j] = 1 if live_neighbors in (2, 3) else 0
            else:
                new_grid[i][j] = 1 if live_neighbors == 3 else 0

    return new_grid


def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

# Example
n = 4
initial_grid = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0]
]

print("Initial Grid:")
print_grid(initial_grid)
new_grid = next_generation(initial_grid)
print("Next Generation:")
print_grid(new_grid)
