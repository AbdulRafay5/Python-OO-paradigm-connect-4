ROWS = 6
COLS = 7

board = [['.' for _ in range(COLS)] for _ in range(ROWS)]

def score_position(board, player):
    # Simple scoring for now
    score = 0
    # Basic center preference
    center_col = COLS // 2
    for r in range(ROWS):
        if board[r][center_col] == player:
            score += 3
    return score

def simple_ai_move(board):
    # Prefer center, then random valid column
    center_col = COLS // 2
    if is_valid_location(board, center_col):
        return center_col
    
    valid_cols = [c for c in range(COLS) if is_valid_location(board, c)]
    if valid_cols:
        return valid_cols[0]
    return 0


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
    turn = 'H'
    
    while True:
        print_board(board)
        
        if turn == 'H':
            col = int(input("Enter column number: "))
            if is_valid_location(board, col):
                row, col = update(board, col, turn)
                
                # Check win
                b, w = win_condition(board, row, col)
                if b:
                    print_board(board)
                    print(w, "wins!")
                    break
                
                turn = 'A'
        else:
            col = simple_ai_move(board)
            row = get_next_open_row(board, col)
            board[row][col] = 'A'
            print(f"AI plays column {col}")
            
            # Check win
            b, w = win_condition(board, row, col)
            if b:
                print_board(board)
                print(w, "wins!")
                break
            
            turn = 'H'



if __name__ == "__main__":

    main()

