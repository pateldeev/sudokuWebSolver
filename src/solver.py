# File to implement functions that solve a sudoku puzzle - by: Deev Patel


# computes list of options available for a given board
# board: 9x9 2D list representing board - unknown = 0
# returns 2D list containing the available options as sets
# returns empty list if it finds location with an invalid decision and there are no valid options
def compute_board_options(board):
    options = list()  # holds options

    for r, row in enumerate(board):
        options.append(list())

        for c, val in enumerate(row):
            used_values = set()  # set to hold value that cannot be used at a given position

            # add values in same row
            for c_temp, val_temp in enumerate(row):
                if c_temp != c and val_temp:
                    used_values.add(val_temp)

            # add values in same column
            for r_temp, row_temp in enumerate(board):
                if r_temp != r and row_temp[c]:
                    used_values.add(row_temp[c])

            # add values in same 3x3 grid cell
            r_start, c_start = int(r / 3) * 3, int(c / 3) * 3
            for r_temp in range(r_start, r_start + 3):
                for c_temp in range(c_start, c_start + 3):
                    if r_temp != r and c_temp != c and board[r_temp][c_temp]:
                        used_values.add(board[r_temp][c_temp])

            options[-1].append({1, 2, 3, 4, 5, 6, 7, 8, 9} - used_values)  # add possible values

            if (board[r][c] and board[r][c] not in options[-1][-1]) or (not board[r][c] and not len(options[-1][-1])):
                return list()  # found invalid choice or not valid options. indicate invalid board

    return options


# solves sudoku puzzle
# board: 9x9 2D list representing board - unknown = 0
# returns True if success or False if board is unsolvable
def solve(board):
    options = compute_board_options(board)  # compute options

    if not options:
        return False  # one of cells contains an invalid choice - unsolvable

    for r, row in enumerate(board):
        for c in range(len(row)):
            if not board[r][c]:  # no decision has been made
                while options[r][c]:  # try all possibilities
                    board[r][c] = options[r][c].pop()

                    if solve(board):
                        return True  # found correct decision. Board is solved
                    else:
                        board[r][c] = 0  # undo decision and move onto to next one

                return False  # no valid decision can be made - puzzle is unsolvable

    return True  # everything is solved and correct
