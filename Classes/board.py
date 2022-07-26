from tile import Tile
from constants import *
import pygame
import player

class Board:
    def __init__(self):

        self._board = [[Tile() for x in range(15)] for _ in range(15)]
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



    def draw_tile_holder(self, win, player: player.Player):
        pygame.draw.rect(win, TAN, (TILE_HOLDER_OFFSET_X, TILE_HOLDER_OFFSET_Y, HOLDER_SIZE_X, HOLDER_SIZE_Y))


        if player is not None and len(player.tile_array) > 0:
            for idx, tile in enumerate(player.tile_array):
                if tile.is_tile():
                    tile.draw(win, (idx * SQUARE_SIZE) + TILE_HOLDER_OFFSET_X, TILE_HOLDER_OFFSET_Y)
                    #pygame.draw.rect(win, WHITE, (TILE_HOLDER_OFFSET_X + (idx * SQUARE_SIZE), TILE_HOLDER_OFFSET_Y, TILE_SIZE, TILE_SIZE))
                    #font = pygame.font.Font('freesansbold.ttf', 25)
                    #TW_tiles = font.render(tile.get_letter(), True, BLACK)
                    #win.blit(TW_tiles, (TILE_HOLDER_OFFSET_X + (idx * SQUARE_SIZE), TILE_HOLDER_OFFSET_Y, TILE_SIZE, TILE_SIZE))


    def draw(self, win, player):
        pygame.draw.rect(win, BLACK, (0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT))

        for idx, row in enumerate(self._board):
            for idy, column in enumerate(row):
                if BOARD_PATTERN[idx][idy] == 'TW':
                    pygame.draw.rect(win, BLACK, (BOARD_OFFSET_X + (idx * SQUARE_SIZE), BOARD_OFFSET_Y + (idy * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, MAGENTA, (BOARD_OFFSET_X + 2 + (idx * SQUARE_SIZE), (BOARD_OFFSET_Y + 2) + (idy * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                    font = pygame.font.Font('freesansbold.ttf', 16)
                    TW_tiles = font.render("TW", True, BLACK)
                    win.blit(TW_tiles, (BOARD_OFFSET_X + 8 + (idx * SQUARE_SIZE), BOARD_OFFSET_Y + 14 + (idy * SQUARE_SIZE)))
                elif BOARD_PATTERN[idx][idy] == 'DW':
                    pygame.draw.rect(win, BLACK, (BOARD_OFFSET_X + (idx * SQUARE_SIZE), BOARD_OFFSET_Y + (idy * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_MAGENTA, (BOARD_OFFSET_X + 2  + (idx * SQUARE_SIZE), (BOARD_OFFSET_Y + 2) + (idy * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                    font = pygame.font.Font('freesansbold.ttf', 16)
                    DW_tiles = font.render("DW", True, BLACK)
                    win.blit(DW_tiles, (BOARD_OFFSET_X + 8+ (idx * SQUARE_SIZE), BOARD_OFFSET_Y + 14 + (idy * SQUARE_SIZE)))
                elif BOARD_PATTERN[idx][idy] == 'TL':
                    pygame.draw.rect(win, BLACK, (BOARD_OFFSET_X + (idx * SQUARE_SIZE), BOARD_OFFSET_Y + (idy * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, CYAN, (BOARD_OFFSET_X + 2  + (idx * SQUARE_SIZE), (BOARD_OFFSET_Y + 2) + (idy * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                    font = pygame.font.Font('freesansbold.ttf', 16)
                    TL_tiles = font.render("TL", True, BLACK)
                    win.blit(TL_tiles, (BOARD_OFFSET_X + 8+ (idx * SQUARE_SIZE), BOARD_OFFSET_Y + 14 + (idy * SQUARE_SIZE)))
                elif BOARD_PATTERN[idx][idy] == 'DL':
                    pygame.draw.rect(win, BLACK, (BOARD_OFFSET_X + (idx * SQUARE_SIZE), BOARD_OFFSET_Y + (idy * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_CYAN, (BOARD_OFFSET_X + 2  + (idx * SQUARE_SIZE), (BOARD_OFFSET_Y + 2) + (idy * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                    font = pygame.font.Font('freesansbold.ttf', 16)
                    DL_tiles = font.render("DL", True, BLACK)
                    win.blit(DL_tiles, (BOARD_OFFSET_X + 8+ (idx * SQUARE_SIZE), BOARD_OFFSET_Y + 14 + (idy * SQUARE_SIZE)))
                elif BOARD_PATTERN[idx][idy] == 'ST':
                    pygame.draw.rect(win, BLACK, (BOARD_OFFSET_X + (idx * SQUARE_SIZE), BOARD_OFFSET_Y + (idy * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, LT_MAGENTA, (BOARD_OFFSET_X + 2  + (idx * SQUARE_SIZE), (BOARD_OFFSET_Y + 2) + (idy * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
                    font = pygame.font.Font('freesansbold.ttf', 16)
                    ST_tiles = font.render("ST", True, BLACK)
                    win.blit(ST_tiles, (BOARD_OFFSET_X + 8+ (idx * SQUARE_SIZE), BOARD_OFFSET_Y + 14 + (idy * SQUARE_SIZE)))
                    font = pygame.font.Font('freesansbold.ttf', 6)
                    E_tiles = font.render("1", True, BLACK)
                    win.blit(E_tiles, (123 + (idx * SQUARE_SIZE), 174 + (idy * SQUARE_SIZE)))
                elif BOARD_PATTERN[idx][idy] == "__":
                    pygame.draw.rect(win, BLACK, (BOARD_OFFSET_X + (idx * SQUARE_SIZE), BOARD_OFFSET_Y + (idy * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(win, TAN, (BOARD_OFFSET_X + 2  + (idx * SQUARE_SIZE), (BOARD_OFFSET_Y + 2) + (idy * SQUARE_SIZE), SQUARE_SIZE-4, SQUARE_SIZE-4))
        self.draw_tile_holder(win, player)

        for idx, row in enumerate(self._board):
            for idy, tile in enumerate(row):
                if tile.is_tile():
                    tile.draw(win, (idx*SQUARE_SIZE) + BOARD_OFFSET_X, idy*SQUARE_SIZE + BOARD_OFFSET_Y)
                    #font = pygame.font.Font('freesansbold.ttf', 25)
                    #TW_tiles = font.render(col.get_letter(), True, BLACK)
                    #win.blit(TW_tiles, (BOARD_OFFSET_X + (idx * SQUARE_SIZE), BOARD_OFFSET_Y + (idy * SQUARE_SIZE), TILE_SIZE, TILE_SIZE))

