## Question 1: Number Spiral Matrix

Write a program that generates a square matrix of numbers in a spiral pattern. The matrix should be filled with consecutive integers starting from 1, spiraling inwards in a clockwise direction from the top-left corner.

For n = 4:

1   2   3   4

12  13  14   5

11  16  15   6

10   9   8   7

Hints:

Use a 2D list to keep track of the grid.
Use four directions (right, down, left, up) in a repeating sequence, changing direction when you hit the edge of the grid or an already-filled cell.
Update the current position based on the direction.

<br>

## Question 2: Conway's Game of Life

Simulate the next generation of Conway's Game of Life, a cellular automaton with the following rules:

Any live cell with 2 or 3 live neighbors survives.
Any dead cell with exactly 3 live neighbors becomes a live cell.
All other cells die or remain dead.

Write a program to print the board state after one generation. Use nested for loops to iterate over the grid and calculate the number of neighbors for each cell.

Input:
An integer n (size of the grid).
A n x n grid of 0s and 1s, where 1 represents a live cell and 0 a dead cell.

Output:
Print the grid state after applying the rules of the game for one generation.

For n = 4 and initial grid:

0 1 0 0

0 0 1 0

1 1 1 0

0 0 0 0

The output after one generation should be:

0 0 0 0

1 0 1 0

0 1 1 0

0 1 0 0



