from constants import *

class Tile:


    def __init__(self, character=''):
        self._letter = character
        self._points = TILE_SCORES[character]

    def get_points(self):
        return self._points

    def get_letter(self):
        return self._letter

    def set_letter(self, character):
        self._letter = character
        self._points = TILE_SCORES[character]


    def is_tile(self) -> bool:
        if self._letter == '':
            return False
        return True

    def draw(self, xy: tuple, win):
        x = SQUARE_SIZE * xy[0] + SQUARE_SIZE // 2
        y = SQUARE_SIZE * xy[1] + SQUARE_SIZE // 2
        pygame.draw.rect(win, BLACK, (100 + (x * SQUARE_SIZE), 150 + (y * SQUARE_SIZE), TILE_SIZE, TILE_SIZE))
        font = pygame.font.Font('freesansbold.ttf', 26)
        TW_tiles = font.render(self._letter, True, BLACK)
        win.blit(TW_tiles, (108 + (x * SQUARE_SIZE), 164 + (y * SQUARE_SIZE)))