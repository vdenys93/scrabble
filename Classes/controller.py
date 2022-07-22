from board import Board
from Classes.player import Player
from Classes.tile import Tile
from Classes.tileBag import TileBag
import pygame
from scrabble.constants import *


class Controller:
    def __init__(self, win):
        self._board = Board()
        self._players = [Player("testone", 1), Player("testtwo", 2)]
        self._tile_bag = TileBag()
        self._placed_tiles = {}
        self.win = win
        self.current_player = 0

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
            self._players.append()

    def start_pass_out_tiles(self):
        for player in self._players:
            player.tile_array = self._tile_bag.get_tiles(7)



    def update(self):


        self._board.draw(self.win, self._players[self.current_player])


    # Draw(): TODO add all draw methods
    #   self._board.Draw(WIN)
    #
