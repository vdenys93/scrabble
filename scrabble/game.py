import pygame
from .board import Board
from .constants import MAX_PLAYERS, MAX_TILES_PLAYABLE


class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.turn = 1               # player number whose turn it is.

    def update(self):
        self.board.draw_squares(self.win)
        pygame.display.update()

    def _init(self):
        self.selected_tile = None
        self.board = Board()
        self.valid_move = False
        self.finished_move = False
        self.tiles_played = 0

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected_tile:
            result = self._move(row, col)
            if not result:
                self.selected_tile = None
                self.select(row, col)
        else:
            tile = self.board.get_tile(row, col)
            if tile != 0 and tile.player == self.turn:
                self.selected_tile = tile
                self.valid_move = self.board.get_valid_moves(tile)
                return True
        return False

    def _move(self, row, col):
        tile = self.board.get_tile(row, col)
        if self.selected_tile and tile == 0 and self.valid_move:
            self.board.move(self.selected_tile, row, col)
            if self.finished_move:
                self.change_turn()
            else:
                self.tiles_played += 1
                if self.tiles_played == MAX_TILES_PLAYABLE:
                    self.finished_move = True
                    self.tiles_played = 0
                    self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        if self.turn == MAX_PLAYERS:
            self.turn = 1
        else:
            self.turn += 1


