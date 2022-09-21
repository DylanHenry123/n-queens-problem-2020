# N queens problem
# for n x n

# imports
import copy

# getting dimensions
n = int(input('N: '))


def print_board(board):
    for i in range(len(board)):
        print(board[i])


def place_n(board, row, col):
    # Form for the diagonals are:
    # i, j in make_tuple(range(increment for i), range(increment for j)
    # With ranges being (start, stop, step)

    # Does the columns
    for i in range(len(board)):
        board[i][col] = '_'

    # Does the rows
    for j in range(len(board[row])):
        board[row][j] = '_'

    # top left diagonals
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        board[i][j] = '_'

    # bottom left diagonals
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        board[i][j] = '_'

    # top right diagonals
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        board[i][j] = '_'

    # bottom right diagonals
    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        board[i][j] = '_'

    # Place queen
    board[row][col] = 'Q'

    return board


def place_queens(board, col):

    # if column is greater than the possible number of columns then all queens have been placed
    if col >= n:
        print('')
        print_board(board)
        exit()

    # copying the board before doing operations on it
    board_copy = copy.deepcopy(board)

    # Searching the rows for a free space
    for row in range(n):
        if board[row][col] == '':
            place_n(board, row, col)

            # recursion
            if place_queens(board, col + 1):
                return True

            else:
                board = board_copy
                board[row][col] = '_'
                place_queens(board, col)

    return False


def main():

    # creating the board
    board = [['' for i in range(n)] for j in range(n)]

    place_queens(board, 0)


if __name__ == '__main__':
    main()
