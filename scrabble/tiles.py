import pygame
from .constants import SQUARE_SIZE, GREY, TILE_SCORES


class Tile:
    PADDING = 2

    def __init__(self, row, col, tile: tuple):
        self.row = row
        self.col = col
        self.score, self.letter = tile
        self.x = 0
        self.y = 0
        self.calc_position()


    def calc_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2  # puts the tile in the center of the tile so it lines up right
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw_tile(self, win):
        # pygame.draw.square()
        pass

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()

