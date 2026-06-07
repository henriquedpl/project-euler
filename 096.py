from itertools import product

def get_forbidden_numbers(s, i, j):
    """
    Get all invalid possibilities for a given cell of the board.
    It works by adding to a set all numbers in the cells's row, column
    and 3x3 square.

    Parameters
    ----------
    s: list[list[int]]
        9x9 Sudoku grid.
    i, j: coordinates of the cell
    Returns
    -------
    set
        Set with all numbers already used in the cell's row/column/3x3 grid
    """
    line_numbers = [s[i][y] for y in range(0, 9) if y != j]
    col_numbers = [s[x][j] for x in range(0, 9) if x != i]
    square_numbers = [
        s[x[0]][x[1]]
        for x in product(
            list(range(int(i / 3) * 3, int(i / 3) * 3 + 3)),
            list(range(int(j / 3) * 3, int(j / 3) * 3 + 3)),
        )
        if (x[0], x[1]) != (i, j)
    ]
    return set(line_numbers + col_numbers + square_numbers)


def get_next_square(i, j, fixed):
    """
    Get the coordinates of the next empty cell, always from left to right and
    top to bottom.

    Parameters
    ----------
    i, j : int
        coordinates of the current cell

    fixed : list[list[int]]
        list of fixed cells (the ones already filled in the starting board)

    Returns
    -------
    i, j: int
        coordinates of the next cell
    """
    j += 1
    if j == 9:
        j = 0
        i += 1
    if (i, j) in fixed:
        return get_next_square(i, j, fixed)
    return (i, j)


def solve(s):
    """
    Solve a Sudoku board.

    Parameters
    ----------
    board : list[list[int]]
        9x9 Sudoku grid. Empty cells are represented by 0.
        The algorithm assumes that the board is solvable.

    Returns
    -------
    list[list[int]]
        The solved board.
    """
    ...
    fixed = set()
    squares = []
    i, j = 0, 0
    while (i, j) != (9, 0):
        if s[i][j] in range(1, 10):
            fixed.add((i, j))
        elif not squares:
            squares.append({"pos": (i, j), "used": []})
        j += 1
        if j == 9:
            i += 1
            j = 0

    i, j = 0, 0
    while (i, j) != (9, 0):
        current_square = squares[-1]
        i, j = current_square["pos"]
        if len(current_square["used"]) >= 9:
            s[i][j] = 0
            squares = squares[:-1]
            continue
        s[i][j] = 1 + len(current_square["used"])
        current_square["used"].append(s[i][j])
        forbidden_numbers = get_forbidden_numbers(s, i, j)
        if s[i][j] not in forbidden_numbers:
            i, j = get_next_square(i, j, fixed)
            squares.append({"pos": (i, j), "used": []})
    return s

with open('input/096.txt') as f:
    text = f.read()

def solution096():
    _sum = 0
    for grid in text.split('Grid ')[1:]:
        grid = grid[3:]
        lines = grid.split('\n')[:-1]
        board = [[int(c) for c in list(x)] for x in lines]
        solved = solve(board)

        _sum += solved[0][0] * 100
        _sum += solved[0][1] * 10
        _sum += solved[0][2]

    return _sum
