
# You can take any board from here https://sandiway.arizona.edu/sudoku/examples.html

# python Project.py < sudoku_puzzle.txt




import sys

board = []
for line in sys.stdin:
    if line.strip():
        ele = list(map(int, line.split()))
        board.append(ele)



def find_empty(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return (row, column)
    return None


def draw_board_on_console(board):
    print('-------------------')
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print()

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(' ', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')
    print('-------------------')


def valid(board, num, position):
    # Checking rows
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Checking Columns
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # Checking 3x3 squares

    square_x = position[1] // 3
    square_y = position[0] // 3

    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True


def backtrack(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if backtrack(board):
                return True
            board[row][column] = 0
    return False

if not backtrack(board):
    print("no solution")
else:
    draw_board_on_console(board)






backtrack(board)
draw_board_on_console(board)
