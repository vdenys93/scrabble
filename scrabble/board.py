import pygame
from .constants import ROWS, COLS, BLACK, TAN, MAGENTA, LT_MAGENTA, CYAN, LT_CYAN, SQUARE_SIZE, BOARD_PATTERN, VALID_MOVES
from .tiles import Tile


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.tiles_left = 100
        self.tiled_square = False
        self.turn = 1

    def draw_squares(self, win):
        win.fill(TAN)
        for row in range(7):
            pygame.draw.rect(win, BLACK, ((100 + (4 * SQUARE_SIZE) + (row * SQUARE_SIZE)), 25 + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(win, TAN, ((102 + (4 * SQUARE_SIZE) + (row * SQUARE_SIZE)), 27 + SQUARE_SIZE, SQUARE_SIZE-4, SQUARE_SIZE-4))
        for row in range(ROWS):
            for col in range(COLS):
                if BOARD_PATTERN[row][col] == 'TW':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 150 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, MAGENTA, (102 + (row * SQUARE_SIZE), 152 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                elif BOARD_PATTERN[row][col] == 'DW':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 150 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_MAGENTA, (102 + (row * SQUARE_SIZE), 152 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                elif BOARD_PATTERN[row][col] == 'TL':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 150 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, CYAN, (102 + (row * SQUARE_SIZE), 152 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                elif BOARD_PATTERN[row][col] == 'DL':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 150 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_CYAN, (102 + (row * SQUARE_SIZE), 152 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                elif BOARD_PATTERN[row][col] == 'ST':
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 150 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_MAGENTA, (102 + (row * SQUARE_SIZE), 152 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                else:
                    pygame.draw.rect(win, BLACK, (100 + (row * SQUARE_SIZE), 150 + (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, TAN, (102 + (row * SQUARE_SIZE), 152 + (col * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))

    # will recreate the board positions when tiles are laid.
    def get_tile(self, row, col):
        return self.board[row][col]

    def create_board(self, tile):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if self.tiled_square:
                    self.board[row].append(Tile(row, col, tile))
                else:
                    self.board[row].append(0)

    def move(self, tile, row, col):
        self.board[tile.row][tile.col], self.board[row][col] = self.board[row][col], self.board[tile.row][tile.col]
        tile.move(row, col)

    # redraw the board after the tile is laid.
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                tile = self.board[row][col]
                if tile != 0:
                    tile.draw(win)

'''
        def get_valid_moves(self, tile):
        if tile in VALID_MOVES:
            return True
        else:
            return False
'''
