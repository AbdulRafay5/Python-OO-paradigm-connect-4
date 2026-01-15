ROWS = 6
COLS = 7

board = [['.' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for i in range(ROWS - 1, -1, -1):
        for j in range(0, COLS):
            print(board[i][j], end=" ")
        print("")
    print("")

def main():
    print_board(board)

if __name__ == "__main__":
    main()