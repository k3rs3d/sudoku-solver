# Sudoku Solver

This is a Python-based solution to solving Sudoku puzzles by reading them from a CSV file. It utilizes constraint propagation and depth-first search to efficiently find the solution.

Part of my tutorial here: https://kersed.net/posts/sudoku-solver/

"Constraint propagation" is a technique that reduces the domain of possible solutions by continually applying constraints. In the context of Sudoku, the constraints come from the rules of the game. Constraint propagation is used to iteratively refine the possibilities for each square, leading to a more efficient search. For example, if a square is assigned the digit 3, all its peers must eliminate 3 as a possibility.

Then, DFS explores the possibilities in depth. If a contradiction is found (a square with no possible values), it backtracks to the previous possibilities, effectively navigating the solution space to find a valid configuration.

Basic elimination methods might solve easy puzzles, but often take a relatively long time, or sometimes even get stuck on more complex puzzles. Combining DFS with constraint propagation allows the code to handle a wider variety of puzzles, exploring the solution space very efficiently.

## How it Works

- Load the Sudoku Puzzle: Reads a 9x9 Sudoku grid from a CSV file (0s represent empty squares).
- Create Board: It constructs a Sudoku board; each square on the board maps to a set of possible values (1-9).
- Solve the Puzzle: The solution is found through a combination of constraint propagation and depth-first search, reducing the possibilities for each square until the solution is found.

## Usage 

Specify the Sudoku puzzle file (e.g., "sudoku.csv") and run the code. If the Sudoku puzzle is valid, it will print the solution to the console.

```
sudoku_filename = "sudoku.csv"
solve_sudoku(sudoku_filename)
```

## Requirements 

- Python 3.x
- CSV file containing a valid initial Sudoku state