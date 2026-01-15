import math
import random

class Connect4Game:
    ROWS = 6
    COLS = 7

    def __init__(self):
        self.board = [['.' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.turn = 'H'  # Start with human

    def print_board(self, board=None):
        if board is None:
            board = self.board
        for i in range(self.ROWS - 1, -1, -1):
            for j in range(self.COLS):    
                print(board[i][j], end=" ")
            print("")
        print("")

    def is_valid_location(self, board, col):
        return board[self.ROWS-1][col] == '.'

    def get_next_open_row(self, board, col):
        for r in range(self.ROWS):
            if board[r][col] == '.':
                return r
        return None

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def win_condition(self, board, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        players = ["H", "A"]

        for player in players:
            # Check if we can check for this player:
            # 1. If tile is empty ('.'), we are checking hypothetically for Minimax
            # 2. If tile is occupied, it must match the player we are checking
            if board[row][col] != '.' and board[row][col] != player:
                continue

            for dr, dc in directions:
                count = 1  # include current piece

                # Check positive direction
                r, c = row + dr, col + dc
                while 0 <= r < self.ROWS and 0 <= c < self.COLS and board[r][c] == player:
                    count += 1
                    r += dr
                    c += dc

                # Check negative direction
                r, c = row - dr, col - dc
                while 0 <= r < self.ROWS and 0 <= c < self.COLS and board[r][c] == player:
                    count += 1
                    r -= dr
                    c -= dc

                if count >= 4:
                    return True, player

        return False, None

    def play(self):
        # Local import to avoid circular dependency if game_AI imports game_OOP (it doesn't, but safer)
        from game_AI import Connect4AI
        ai = Connect4AI(self)
        
        print("Starting Connect 4 Game (OOP)")
        
        while True:
            self.print_board()

            if self.turn == 'H':
                try:
                    col_input = input("Enter column number (0-6): ")
                    col = int(col_input)
                    if not (0 <= col < self.COLS):
                        print("Invalid column range.")
                        continue
                    if not self.is_valid_location(self.board, col):
                        print("Column full.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                
                row = self.get_next_open_row(self.board, col)
                self.drop_piece(self.board, row, col, 'H')
            else:
                print("AI is thinking...")
                col, _ = ai.minimax(self.board, depth=3, maximizingPlayer=True)
                
                if col is None: 
                    print("Game Over. Draw!")
                    break
                    
                row = self.get_next_open_row(self.board, col)
                self.drop_piece(self.board, row, col, 'A')
                print(f"AI plays column {col}")

            # Check win
            b, w = self.win_condition(self.board, row, col)
            if b:
                self.print_board()
                print(w, "wins!")
                break
            
            # Check draw
            if all(not self.is_valid_location(self.board, c) for c in range(self.COLS)):
                 self.print_board()
                 print("Game Over. Draw!")
                 break

            # Switch turn
            self.turn = 'A' if self.turn == 'H' else 'H'

if __name__ == "__main__":
    game = Connect4Game()
    game.play()
