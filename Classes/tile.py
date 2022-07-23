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

    #def draw(self, mpos: tuple, win):
        # TODO