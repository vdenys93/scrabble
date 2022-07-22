from board import Board
from Classes.player import Player
from Classes.tile import Tile
from Classes.tileBag import TileBag
import pygame
from scrabble.constants import *
import sys

class Controller:
    def __init__(self, win):
        self._board = Board()
        self._players = [Player("testone", 1), Player("testtwo", 2)]
        self._tile_bag = TileBag()
        self._placed_tiles = {}
        self.win = win
        self.current_players_turn = 0


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

    def create_player(self, win, count):
        input_font = pygame.font.Font('freesansbold.ttf', 20)
        user_text= ''
        input_rect = pygame.Rect(300, 300, 300, 100)

        entered = False

        for player_number in range(count):
            while entered is False:
                message_font = pygame.font.Font('freesansbold.ttf', 16)
                display_message = message_font.render("Player " + str(player_number) + " NickName?", True, BLACK)
                win.blit(display_message, (200, 200, 200, 100))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        elif event.key == pygame.K_KP_ENTER:
                            entered = True
                        else:
                            user_text += event.unicode

                pygame.draw.rect(win, WHITE, input_rect)
                text_surface = input_font.render(user_text, True, BLACK)
                win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                input_rect.w = max(100, text_surface.get_width()+10)
                pygame.display.flip()

            self._players.append(Player(user_text, player_number))


    def get_player_count(self, win):
        input_font = pygame.font.Font('freesansbold.ttf', 20)
        user_text= ''
        input_rect = pygame.Rect(300, 300, 300, 100)

        entered = False

        while entered is False:
            message_font = pygame.font.Font('freesansbold.ttf', 16)
            display_message = message_font.render("How many players?", True, BLACK)
            win.blit(display_message, (200, 200, 200, 100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_KP_ENTER:
                        if user_text.isdigit():
                            if 0 < int(user_text) < 5:
                                entered = True
                else:
                    user_text += event.unicode

            pygame.draw.rect(win, WHITE, input_rect)
            text_surface = input_font.render(user_text, True, BLACK)
            win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.flip()

        self.create_player(int(user_text))

    def start_pass_out_tiles(self):
        for player in self._players:
            player.tile_array = self._tile_bag.get_tiles(7)

    def start(self, win):
        #get_player_count(win)
        self.start_pass_out_tiles()

    def player_turn(self):


    def update(self):

        self._board.draw(self.win, self._players[self.current_players_turn])


    # Draw(): TODO add all draw methods
    #   self._board.Draw(WIN)
    #
