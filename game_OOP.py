ROWS = 6
COLS = 7

board = [['.' for _ in range(COLS)] for _ in range(ROWS)]
def is_valid_location(board, col):
    return board[ROWS-1][col] == '.'

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == '.':
            return r
    return None

def update(board, col, player):
    for i in range(0, ROWS):
        if board[i][col] == ".":
            board[i][col] = player
            return i, col
    return None, col

def main():
    turn = 'H'
    
    while True:
        print_board(board)
        
        if turn == 'H':
            col = int(input("Enter column number: "))
            if is_valid_location(board, col):
                row, col = update(board, col, turn)
                turn = 'A'
        else:
            # AI will be added later
            turn = 'H'

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