from tile import Tile
import random

class TileBag:


    def __init__(self):
        self.default_tileset = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1,
                           'L': 4
            , 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2,
                           'Z': 1, '': 0}
        self._tiles_in_bag = self._fill_bag()

    def get_tile_count(self) -> int:
        return len(self._tiles_in_bag)

    def _fill_bag(self) -> [Tile]:
        tiles = []
        for letter in self.default_tileset:
            for _ in range(self.default_tileset[letter]):
                tiles.append(Tile(letter))
        return tiles

    def get_tiles(self, count) -> [Tile]:
        if len(self._tiles_in_bag):
            starting_tiles_in_bag = len(self._tiles_in_bag)
            print(len(self._tiles_in_bag))
            tiles = [self._tiles_in_bag.pop(random.randrange(0, len(self._tiles_in_bag))) for _ in range(min(count, len(self._tiles_in_bag)))]

            if count > starting_tiles_in_bag:
                need = count - starting_tiles_in_bag
                tiles.extend([Tile() for _ in range(need)])

            return tiles
        else:
            return [Tile() for _ in range(count)]


