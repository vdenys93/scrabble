import pygame

# Colors by RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
TAN = (238, 232, 170)
MAGENTA = (255, 0, 255)
LT_MAGENTA = (221, 160, 221)
CYAN = (0, 255, 255)
LT_CYAN = (175, 238, 238)

# Display settings
DISPLAY_WIDTH, DISPLAY_HEIGHT = 600, 600

# Board constants
BOARD_WIDTH, BOARD_HEIGHT = DISPLAY_WIDTH * 0.75, DISPLAY_HEIGHT * 0.75
ROWS, COLS = 15, 15
SQUARE_SIZE = (BOARD_WIDTH//COLS)

BOARD_PATTERN =[['TW', '__', '__', 'DL', '__', '__', '__', 'TW', '__', '__', '__', 'DL', '__', '__', 'TW'],
                ['__', 'DW', '__', '__', '__', 'TL', '__', '__', '__', 'TL', '__', '__', '__', 'DW', '__'],
                ['__', '__', 'DW', '__', '__', '__', 'DL', '__', 'DL', '__', '__', '__', 'DW', '__', '__'],
                ['DL', '__', '__', 'DW', '__', '__', '__', 'DL', '__', '__', '__', 'DW', '__', '__', 'DL'],
                ['__', '__', '__', '__', 'DW', '__', '__', '__', '__', '__', 'DW', '__', '__', '__', '__'],
                ['__', 'TL', '__', '__', '__', 'TL', '__', '__', '__', 'TL', '__', '__', '__', 'TL', '__'],
                ['__', '__', 'DL', '__', '__', '__', 'DL', '__', 'DL', '__', '__', '__', 'DL', '__', '__'],
                ['TW', '__', '__', 'DL', '__', '__', '__', 'ST', '__', '__', '__', 'DL', '__', '__', 'TW'],
                ['__', '__', 'DL', '__', '__', '__', 'DL', '__', 'DL', '__', '__', '__', 'DL', '__', '__'],
                ['__', 'TL', '__', '__', '__', 'TL', '__', '__', '__', 'TL', '__', '__', '__', 'TL', '__'],
                ['__', '__', '__', '__', 'DW', '__', '__', '__', '__', '__', 'DW', '__', '__', '__', '__'],
                ['DL', '__', '__', 'DW', '__', '__', '__', 'DL', '__', '__', '__', 'DW', '__', '__', 'DL'],
                ['__', '__', 'DW', '__', '__', '__', 'DL', '__', 'DL', '__', '__', '__', 'DW', '__', '__'],
                ['__', 'DW', '__', '__', '__', 'TL', '__', '__', '__', 'TL', '__', '__', '__', 'DW', '__'],
                ['TW', '__', '__', 'DL', '__', '__', '__', 'TW', '__', '__', '__', 'DL', '__', '__', 'TW']]



# Tile constants
TILE_SIZE = SQUARE_SIZE-4

