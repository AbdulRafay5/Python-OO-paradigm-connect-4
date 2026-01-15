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

def score_position(board, player):
    score = 0
    # For brevity, implement simple scoring or just return 0
    return score

def minimax(board, depth, maximizingPlayer):
    valid_cols = [c for c in range(COLS) if is_valid_location(board, c)]

    # Base case: check for terminal states
    for col in valid_cols:
        row = get_next_open_row(board, col)
        b, winner = win_condition(board, row, col)
        if b:
            if winner == 'A':
                return col, 1000000
            elif winner == 'H':
                return col, -1000000

    if depth == 0 or not valid_cols:
        return valid_cols[0], score_position(board, 'A')

    if maximizingPlayer:
        value = -float('inf')
        best_col = valid_cols[0]
        for col in valid_cols:
            row = get_next_open_row(board, col)
            board[row][col] = 'A'
            _, new_score = minimax(board, depth-1, False)
            board[row][col] = '.'
            if new_score > value:
                value = new_score
                best_col = col
        return best_col, value
    else:
        value = float('inf')
        best_col = valid_cols[0]
        for col in valid_cols:
            row = get_next_open_row(board, col)
            board[row][col] = 'H'
            _, new_score = minimax(board, depth-1, True)
            board[row][col] = '.'
            if new_score < value:
                value = new_score
                best_col = col
        return best_col, value

def print_board(board):
    for i in range(ROWS - 1, -1, -1):
        for j in range(0, COLS):
            print(board[i][j], end=" ")
        print("")
    print("")

def update(board, col):
    for i in range(0, ROWS):
        if board[i][col] == ".":
            board[i][col] = "H"
            return i, col
    return None, col

def win_condition(board, row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    players = ["H", "A"]

    for player in players:
        for dr, dc in directions:
            count = 1

            # Check positive direction
            r, c = row + dr, col + dc
            while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                count += 1
                r += dr
                c += dc

            # Check negative direction
            r, c = row - dr, col - dc
            while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                count += 1
                r -= dr
                c -= dc

            if count >= 4:
                return True, player

    return False, None

def main():
    turn = 'H'

    while True:
        print_board(board)

        if turn == 'H':
            col = int(input("Enter column number: "))
            if 0 <= col < COLS and is_valid_location(board, col):
                row, col = update(board, col)
            else:
                print("Invalid move. Try again.")
                continue
        else:
            col, _ = minimax(board, depth=3, maximizingPlayer=True)
            row = get_next_open_row(board, col)
            board[row][col] = 'A'
            print(f"AI plays column {col}")

        # Check win
        b, w = win_condition(board, row, col)
        if b:
            print_board(board)
            print(w, "wins!")
            break

        # Switch turn
        turn = 'A' if turn == 'H' else 'H'

if __name__ == "__main__":
    main()
