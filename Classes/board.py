from tile import Tile
from constants import *
import pygame

class Board:
    def __init__(self):

        self._board = [[Tile() for x in range(15)] for _ in range(15)]
        print(self._board)
        self._multipliers = BOARD_PATTERN

    def place_tile(self, tile_to_add: Tile, xy: tuple):
        self._board[xy[0]][xy[1]] = tile_to_add

    def  get_tile_locations(self) -> [tuple]:
        tiles_on_board = [()]
        for idx, x in enumerate(self._board):
            for idy, y in enumerate(x):
                if y.is_tile():
                    tiles_on_board.append((y, (idx, idy)))
        return tiles_on_board



    def draw(self, win):
        for idx, row in enumerate(self._board):
            for idy, column in enumerate(row):
                pygame.draw.rect(win, BLACK,
                                 (100 + (idx * SQUARE_SIZE), 150 + ( idy * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(win, CYAN, (
                102 + (idx * SQUARE_SIZE), 152 + (idy * SQUARE_SIZE), SQUARE_SIZE - 4, SQUARE_SIZE - 4))
