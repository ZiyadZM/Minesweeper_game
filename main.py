import random


def initialize_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    for _ in range(num_mines):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while board[row][col] == 'X':
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        board[row][col] = 'X'

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == ' ':
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= row + dr < rows and 0 <= col + dc < cols and board[row + dr][col + dc] == 'X':
                            count += 1
                if count > 0:
                    board[row][col] = str(count)
    return board

####h
def play_minesweeper():
    rows, cols, num_mines = 8, 8, 10
    board = initialize_board(rows, cols, num_mines)

    for row in board:
        print(' '.join(row))


if __name__ == '__main__':
    play_minesweeper()
