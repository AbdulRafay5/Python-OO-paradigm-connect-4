import pygame
import sys
import math
from game_OOP import Connect4Game
from game_AI import Connect4AI

class Connect4UI:
    # Constants
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    SQUARESIZE = 100

    def __init__(self):
        pygame.init()
        self.game = Connect4Game()
        self.ai = Connect4AI(self.game)
        self.width = self.game.COLS * self.SQUARESIZE
        self.height = (self.game.ROWS + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.radius = int(self.SQUARESIZE / 2 - 5)
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont("monospace", 75)
        self.game_over = False
        pygame.display.set_caption("Connect 4 OOP")

    def draw_board(self):
        board = self.game.board
        # Draw the blue grid background first
        for c in range(self.game.COLS):
            for r in range(self.game.ROWS):
                rect_x = c * self.SQUARESIZE
                rect_y = (r + 1) * self.SQUARESIZE
                pygame.draw.rect(self.screen, self.BLUE, (rect_x, rect_y, self.SQUARESIZE, self.SQUARESIZE))

        # Draw the pieces/holes on top
        for c in range(self.game.COLS):
            for r in range(self.game.ROWS):
                center_x = int(c * self.SQUARESIZE + self.SQUARESIZE / 2)
                # Using the exact same formula as before for Y:
                center_y = int((self.game.ROWS - r) * self.SQUARESIZE + self.SQUARESIZE / 2) 

                color = self.BLACK
                if board[r][c] == 'H':
                    color = self.RED
                elif board[r][c] == 'A':
                    color = self.YELLOW
                
                pygame.draw.circle(self.screen, color, (center_x, center_y), self.radius)
        
        pygame.display.update()

    def handle_human_move(self, posx):
        col = int(math.floor(posx / self.SQUARESIZE))

        if self.game.is_valid_location(self.game.board, col):
            row = self.game.get_next_open_row(self.game.board, col)
            self.game.drop_piece(self.game.board, row, col, 'H')

            b, w = self.game.win_condition(self.game.board, row, col)
            if b:
                label = self.font.render("Human Wins!!", 1, self.RED)
                self.screen.blit(label, (40, 10))
                self.game_over = True
            
            self.draw_board() # Show move
            self.game.turn = 'A' # Switch

    def process_ai_turn(self):
        col, minimax_score = self.ai.minimax(self.game.board, 3, True)

        # random move if minimax returns None (shouldn't happen unless full)
        if col is None:
             pass
        else:
            if self.game.is_valid_location(self.game.board, col):
                # pygame.time.wait(500) # Thinking time
                row = self.game.get_next_open_row(self.game.board, col)
                self.game.drop_piece(self.game.board, row, col, 'A')

                b, w = self.game.win_condition(self.game.board, row, col)
                if b:
                    label = self.font.render("AI Wins!!", 1, self.YELLOW)
                    self.screen.blit(label, (40, 10))
                    self.game_over = True

                self.draw_board()
                self.game.turn = 'H'

    def run(self):
        self.draw_board()
        
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    # Floating piece removed
                    pass

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Draw over the top area in case (not strictly needed with new flow but keeps it clean)
                    pygame.draw.rect(self.screen, self.BLACK, (0, 0, self.width, self.SQUARESIZE))
                    
                    if self.game.turn == 'H':
                        self.handle_human_move(event.pos[0])
                            
            # AI Turn Logic
            if self.game.turn == 'A' and not self.game_over:
                 self.process_ai_turn()

            if self.game_over:
                pygame.time.wait(3000)

if __name__ == "__main__":
    ui = Connect4UI()
    ui.run()
