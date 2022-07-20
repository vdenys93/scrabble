import Tile

class Board:
    #(top-down, left-right) access


    def __init__(self,  d=15):
        line_1 = ['TW', '', '', 'DL', '', '', '', 'TW', '', '', '', 'DL', '', '', 'TW']
        line_2 = ['', 'DW', '', '', '', 'TL', '', '', '', 'TL', '', '', '', 'DW', '']
        line_3 = ['', '', 'DW', '', '', '', 'DL', '', 'DL', '', '', '', 'DW', '', '']
        line_4 = ['DL', '', '', 'DW', '', '', '', 'DL', '', '', '', 'DW', '', '', 'DL']
        line_5 = ['', '', '', '', 'DW', '', '', '', '', '', 'DW', '', '', '', '']
        line_6 = ['', 'TL', '', '', '', 'TL', '', '', '', 'TL', '', '', '', 'TL', '']
        line_7 = ['', '', 'DL', '', '', '', 'DL', '', 'DL', '', '', '', 'DL', '', '']
        line_8 = ['TW', '', '', 'DL', '', '', '', '', '', '', '', 'DL', '', '', 'TW']
        line_9 = line_7
        line_10 = line_6
        line_11 = line_5
        line_12 = line_4
        line_13 = line_3
        line_14 = line_2
        line_15 = line_1

        self._board = [['' for x in range(d)] for _ in range(d)]

        self._multipliers = [[line_1], [line_2], [line_3], [line_4], [line_5]
                                    , [line_6], [line_7], [line_8], [line_9], [line_10]
                                            , [line_11], [line_12], [line_13], [line_14], [line_15]]

    def place_tile(self, tile_to_add: Tile, x_y: tuple):
        self.board[x_y[1],x_y[0]]=tile_to_add

    def get_board(self):
        return self._board
