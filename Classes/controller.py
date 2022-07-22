from board import Board
from Classes.player import Player
from Classes.tile import Tile
from Classes.tileBag import TileBag
import pygame
from scrabble.constants import *


class Controller:
    def __init__(self, win):
        self._board = Board()
        self._player = []
        self._tile_bag = TileBag()
        self._placed_tiles = {}
        self.win = win

    def place_Tile(self, xy: tuple, tile: Tile):
        self._placed_tiles[xy] = tile

    def remove_Tile(self, xy: tuple, tile: Tile):
        del self._placed_tiles[xy]

    def submit_word(self):
        for tile in self._placed_tiles:
            self._board.place_tile(tile, tile[tile])

    def draw_text(self, text, x, y):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(text, True, BLACK, BLUE)
        textRect = text.get_rect()
        textRect.center = (x // 2, y // 2)
        #self.

    def create_player(self):
        font = pygame.font.Font('freesansbold.ttf', 32)

        text = font.render('Nickname')

        #nick_name = #TODO insert gui input requests
        #player_num

    def get_player_count(self):

        print("How many players?") #TODO DRAW OUTPUT
        for p in range(int(input())):
            self._player.append()


    def update(self):
        self._board.draw(self.win)
    # Draw(): TODO add all draw methods
    #   self._board.Draw(WIN)
    #
