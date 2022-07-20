import pygame
from .constants import BOARD_WIDTH, BOARD_HEIGHT, ROWS, COLS, BLACK, TAN, MAGENTA, LT_MAGENTA, CYAN, LT_CYAN, SQUARE_SIZE, BOARD_PATTERN


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.tiles_left = 100

    def draw_squares(self, win):
        win.fill(TAN)
        for row in range(ROWS):
            for col in range(COLS):
                if BOARD_PATTERN[row][col] == 'TW':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 100 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, MAGENTA, (102 + (row * SQUARE_SIZE), 102 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                elif BOARD_PATTERN[row][col] == 'DL':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 100 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_CYAN, (102 + (row * SQUARE_SIZE), 102 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                elif BOARD_PATTERN[row][col] == 'TL':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 100 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, CYAN, (102 + (row * SQUARE_SIZE), 102 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                elif BOARD_PATTERN[row][col] == 'DW':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 100 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_MAGENTA, (102 + (row * SQUARE_SIZE), 102 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                elif BOARD_PATTERN[row][col] == 'ST':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 100 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_MAGENTA, (102 + (row * SQUARE_SIZE), 102 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                else:
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 100 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, TAN, (102 + (row * SQUARE_SIZE), 102 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))

    def create_board(self):
        pass
