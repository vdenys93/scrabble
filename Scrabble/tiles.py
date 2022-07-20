import pygame
from .constants import SQUARE_SIZE, GREY

class Tile:
    PADDING = 2

    def __init__(self, row, col, tile: tuple):
        self.row = row
        self.col = col
        self.score, self.letter = tile
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2  # puts the tile in the center of the tile so it lines up right
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        pygame.draw.square()
