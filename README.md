# Sudoku Solver

This is a Python-based solution to solving Sudoku puzzles by reading them from a CSV file. 
It utilizes constraint propagation and depth-first search to efficiently find the solution.
Part of my tutorial: https://kersed.net/posts/sudoku-solver/

## How it Works

- Load the Sudoku Puzzle: The code reads a 9x9 Sudoku grid from a given CSV file (with 0s representing empty squares).
- Create Board: It constructs a Sudoku board, where each square on the board maps to a set of possible values (1-9).
- Solve the Puzzle: The solution is found through a combination of constraint propagation and depth-first search, reducing the possibilities for each square until the solution is found.

## Usage 

Specify the Sudoku puzzle file (e.g., "sudoku.csv") and run the code. If the Sudoku puzzle is valid, it will print the solution to the console.

```
sudoku_filename = "sudoku.csv"
solve_sudoku(sudoku_filename)
```

## Requirements 

- Python 3.x
- CSV file containing an initial Sudoku state