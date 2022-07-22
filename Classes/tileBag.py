from tile import Tile
import random

class TileBag:


    def __init__(self):
        self.default_tileset = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1,
                           'L': 4
            , 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2,
                           'Z': 1, '': 2}
        self._tiles_in_bag = self._fill_bag()

    def get_tile_count(self) -> int:
        return len(self._tiles_in_bag)

    def _fill_bag(self) -> [Tile]:
        tiles = []
        for letter in self.default_tileset:
            for _ in range(self.default_tileset[letter]):
                tiles.append(letter)
        return tiles

    def get_random_tile(self):
        return self._tiles_in_bag.pop(random(len(self._tiles_in_bag)))
