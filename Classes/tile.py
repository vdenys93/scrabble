

class Tile:


    def __init__(self, character=''):
        self.tile_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1
            , 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
                       'Z': 10, '': 0}
        self._letter = character
        self._points = self.tile_values[character]

    def get_points(self):
        return self._points

    def get_letter(self):
        return self._letter

    def set_letter(self, character):
        self._letter = character
        self._points = self.tile_values[character]
