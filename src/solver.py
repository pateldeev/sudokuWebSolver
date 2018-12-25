# File to implement functions that solve a sudoku puzzle - by: Deev Patel


# computes list of options available for a given board
# board: 9x9 2D list representing board - unknown = 0
# returns 2D list containing the available options as a set
# returns empty list if it finds location with an invalid decision
def compute_board_options(board):
    options = list()  # holds options

    for row in range(len(board)):
        options.append(list())

        for col in range(len(board[row])):
            used_values = set()  # set to hold value that cannot be used at a given position

            # add values in same row
            for c in range(len(board[row])):
                if c != col and board[row][c]:
                    used_values.add(board[row][c])

            # add values in same column
            for r in range(len(board)):
                if r != row and board[r][col]:
                    used_values.add(board[r][col])

            # add values in same 3x3 grid cell
            r_start, c_start = int(row / 3) * 3, int(col / 3) * 3
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    if r != row and c != col and board[r][c]:
                        used_values.add(board[r][c])

            if board[row][col] not in used_values:
                options[-1].append({1, 2, 3, 4, 5, 6, 7, 8, 9} - used_values)  # add only the possible values
            else:
                return list()  # indicated invalid board - value in cell is not valid

    return options


# solves sudoku puzzle
# board: 9x9 2D list representing board - unknown = 0
# returns solved board or empty list if there is no solution
def solve(board):
    board_solved = board.copy()
    options = compute_board_options(board_solved)  # compute options

    if not options:
        return list()  # one of cells contains an invalid choice

    for r in range(len(board_solved)):
        for c in range(len(board_solved)):
            if not board[r][c]:  # no decision has been made
                while options[r][c]:  # try all possibilities
                    board_solved[r][c] = options[r][c].pop()
                    temp_solution = solve(board_solved)

                    if temp_solution:  # found correct decision
                        return temp_solution
                    else:  # undo decision and move onto to next one
                        board_solved[r][c] = 0

                return list()  # no valid decision can be made - puzzle is unsolvable

    return board_solved  # everything is solved and correct
