import math
import random

class Connect4AI:
    def __init__(self, game):
        self.game = game

    def score_position(self, board, player):
        score = 0
        # Placeholder for heuristic implementation
        return score

    def minimax(self, board, depth, maximizingPlayer):
        valid_cols = [c for c in range(self.game.COLS) if self.game.is_valid_location(board, c)]

        for col in valid_cols:
            row = self.game.get_next_open_row(board, col)
            b, winner = self.game.win_condition(board, row, col)
            if b:
                if winner == 'A':
                    return col, 1000000
                elif winner == 'H':
                    return col, -1000000

        if depth == 0 or not valid_cols:
             # Basic score or 0
             return (valid_cols[0] if valid_cols else None), self.score_position(board, 'A')

        if maximizingPlayer:
            value = -float('inf')
            best_col = valid_cols[0]
            for col in valid_cols:
                row = self.game.get_next_open_row(board, col)
                self.game.drop_piece(board, row, col, 'A')
                _, new_score = self.minimax(board, depth-1, False)
                self.game.drop_piece(board, row, col, '.') # Backtrack
                if new_score > value:
                    value = new_score
                    best_col = col
            return best_col, value
        else:
            value = float('inf')
            best_col = valid_cols[0] 
            for col in valid_cols:
                row = self.game.get_next_open_row(board, col)
                self.game.drop_piece(board, row, col, 'H')
                _, new_score = self.minimax(board, depth-1, True)
                self.game.drop_piece(board, row, col, '.') # Backtrack
                if new_score < value:
                    value = new_score
                    best_col = col
            return best_col, value
