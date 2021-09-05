import csv


# Load the Sudoku puzzle from the given filename
def load_sudoku(filename):
    """
    Reads the Sudoku grid from a CSV file.
    The file must contain a 9x9 grid of integers,
    with 0s indicating empty squares.
    """
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            # Convert each row to a list of integers
            grid = [list(map(int, row)) for row in reader]
            return grid
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found.")
    except csv.Error:
        raise Exception("CSV Error encountered while reading the file.")


# Create a Sudoku board from the given grid
def create_board(grid):
    """
    Creates a Sudoku board from the given grid.
    The board is a dictionary,
    mapping (row, column) to a set of possible values.
    """
    # Create a list of digits and a list of all squares
    digits = list(range(9))  # values 0 to 8
    squares = [(i, j) for i in digits for j in digits]

    # Create the unitlist. Each unit is a group of squares that must contain all digits 1-9.
    # There are three types of units: rows, columns, and boxes.
    unitlist = ([[(i, j) for j in digits] for i in digits] +  # rows
                [[(i, j) for i in digits] for j in digits] +  # columns
                [[(i, j) for i in range(3*r, 3*r+3) for j in range(3*c, 3*c+3)] for r in range(3) for c in range(3)])  # boxes

    # Create a dictionary that maps each square to the units it belongs to
    units = {s: [u for u in unitlist if s in u] for s in squares}

    # Assign initial values to the squares based on the input grid
    values = assign_values_to_squares(grid, units)

    if not values:
        print("Invalid Sudoku grid.")

    return values, units


# Print the Sudoku board to the console
def print_grid(values):
    """
    Prints the Sudoku grid state, separating the box regions with lines.
    """
    for r in range(9):
        # Each cell contains a set of possible values. If a cell is solved, it contains only one value.
        # We print the first (and only) value of each cell, separated by spaces and vertical bars.
        row_output = ''.join(str(list(values[r, c])[0]).ljust(2) + ('|' if c in [2,5] else '') for c in range(9))
        print(row_output)
        if r in [2,5]:  # print horizontal line to separate boxes
            print('-' * 21)
    print()


# Assign the given values to the squares of the Sudoku board
def assign_values_to_squares(grid, units):
    """
    Assigns initial values to the squares based on the input grid.
    Each cell starts with a set of all possible values (1-9).
    If a cell is filled in the input grid, start with only that value.
    """
    digits = list(range(9))  # values 0 to 8
    squares = [(i, j) for i in digits for j in digits]
    # Start by assigning all digits to every square
    values = {s: set(range(1, 10)) for s in squares}

    # For each square, assign its value from the input grid
    for s, d in {s: grid[s[0]][s[1]] for s in squares}.items():
        if d != 0 and not assign(values, s, d, units):  # Call assign only for filled squares
            return False
    return values


# Assign a value to a square and eliminate it from its peers
def assign(values, s, d, units):
    """
    Assigns a value to a square,
    then eliminates the value as a possibility from its peers.
    """
    # Copy the other values to avoid changing the original set
    other_values = values[s].copy()
    # Remove the assigned value from the other values
    other_values.remove(d)
    # If the value can be eliminated from the other values, assign the value to the square
    if all(eliminate(values, s, d2, units) for d2 in other_values):
        return values
    return False


# Eliminate a value from a square
def eliminate(values, s, d, units):
    """
    Eliminates a possible value from a square.
    If that square is reduced to one value,
    it eliminates that value from its "peers"s.
    """
    # If the value is not in the square, return the values as is
    if d not in values[s]:
        return values  # already eliminated
    # Otherwise, remove the value from the square
    values[s].remove(d)  # remove d from possible values

    # If a square is reduced to one value, then remove this value from its peers
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = next(iter(values[s]))  # get the first (and only) value
        if not all(eliminate(values, s2, d2, units) for u in units[s] for s2 in u if s2 != s):
            return False

    # If a unit is reduced to one place for a value, then put the value there
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d, units):
                return False

    return values


# Search for a solution using DFS
def search(values, units):
    """
    Uses depth-first search to find a solution.
    Chooses the square with the fewest possible values,
    and tries all of those potential values.
    """
    if values is False:
        return False  # Failed earlier
    if all(len(values[s]) == 1 for s in values.keys()):  # If all squares have one value, it's solved!
        return values

    # Choose the square with the fewest possibilities
    n, s = min((len(values[s]), s) for s in values.keys() if len(values[s]) > 1)
    for d in values[s]:
        # Try each possible value and search for a solution
        new_values = assign(values.copy(), s, d, units)
        if new_values:
            result = search(new_values, units)
            if result:
                return result
    return False


# Solve a Sudoku puzzle
def solve_sudoku(input_filename):
    """
    This function solves a Sudoku puzzle given in a file.
    """
    # Load the Sudoku puzzle from the file
    grid = load_sudoku(input_filename)
    if grid:
        # Create the Sudoku board from the grid
        values, units = create_board(grid)
        # Search for a solution
        solution = search(values, units)

        # Print the solution or a message if no solution exists
        if solution:
            print("Solution to the Sudoku puzzle:")
            print_grid(solution)
        else:
            print("No solution exists.")


# Specify the Sudoku puzzle file and solve the puzzle
sudoku_filename = "sudoku.csv"
solve_sudoku(sudoku_filename)