def number_in_the_row(board, number, row):
    """Give False if the number is already in the row"""
    for column in range(length):
        if board[row][column] == number:
            return False
    return True


def number_in_the_column(board, number, column):
    """Give False if the number is already in the column"""
    for row in range(length):
        if board[row][column] == number:
            return False
    return True


def number_in_the_box(board, number, column, row):
    """Give False if the number is already in the box"""
    right_column = column - column % 3
    upper_row = row - row % 3
    for c in range(right_column, right_column + 3):
        for r in range(upper_row, upper_row + 3):
            if board[row][column] == number:
                return False
    return True


def valid_place(board, number, column, row):
    """Checks if I can place there the number"""
    if number_in_the_box(board, number, column, row) and number_in_the_column(board, number,
                                                                              column) and number_in_the_row(board,
                                                                                                            number,
                                                                                                            row):
        return True
    else:
        return False


def print_board(board):
    """Yeah, just prints the board <- you can do better"""
    for row in board:
        print(row)


def core_of_solver(board):
    """The main loop-solver"""
    for row in range(length):
        for column in range(length):
            if board[row][column] == 0:
                """checking for numbers 1 - length_number (not 9 if we ever want to make bigger sudoku)"""
                for number in range(1, length + 1):
                    if valid_place(board, number, column, row):
                        board[row][column] = number
                        """Now we are making a loop and starting over for a next number"""
                        if core_of_solver(board):
                            return True
                        else:
                            """If we get to point where our numbers didn't give use the solution we get back here and 
                            start over with a new number"""
                            board[row][column] = 0
                return False
    return True


def full_solver(board):
    """All functions together with a nice comments and printing the solved board"""
    if core_of_solver(board):
        print("Solved!")
        print_board(board)
    else:
        print("Unsolvable!")


length = 9
sudoku_board = [[0, 0, 0, 4, 0, 0, 0, 3, 0],
                [7, 0, 4, 8, 0, 0, 1, 0, 2],
                [0, 0, 0, 2, 3, 0, 4, 0, 9],
                [0, 4, 0, 5, 0, 9, 0, 8, 0],
                [5, 0, 0, 0, 0, 0, 9, 1, 3],
                [1, 0, 0, 0, 8, 0, 2, 0, 4],
                [0, 0, 0, 0, 0, 0, 3, 4, 5],
                [0, 5, 1, 9, 4, 0, 7, 2, 0],
                [4, 7, 3, 0, 5, 0, 0, 9, 1]]
full_solver(sudoku_board)
