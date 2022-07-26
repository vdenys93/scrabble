from board import Board
from Classes.player import Player
from Classes.tile import Tile
from Classes.tileBag import TileBag
import pygame
from constants import *
import sys


class Controller:
    def __init__(self, win):
        self._board = Board()
        self._players = [Player("testone", 1), Player("testtwo", 2)]
        self._tile_bag = TileBag()
        self._placed_tiles = {}
        self.win = win

        self.current_players_turn = 0 #by index


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

    #def player_turn(self):

    #def self._tile_move()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def next_turn(self):
        if self.current_players_turn == len(self._players) - 1:
            self.current_players_turn = 0
        else:
            self.current_players_turn += 1


    def player_turn_display(self):
        button_rect = Rect(SQUARE_SIZE * 3, SQUARE_SIZE * 18, TILE_SIZE * 3, TILE_SIZE)
        pygame.draw.rect(self.win, WHITE, button_rect)
        font = pygame.font.Font('freesansbold.ttf', 25)
        submit_button = font.render("Player: " + str(self.current_players_turn), True, BLACK)
        self.win.blit(submit_button, button_rect)

    #def clicked_tile(self):
    def pass_button(self, win, event) -> bool:
        button_rect = Rect(SQUARE_SIZE * 15, SQUARE_SIZE * 18, TILE_SIZE * 3, TILE_SIZE)
        pygame.draw.rect(self.win, WHITE, button_rect)
        font = pygame.font.Font('freesansbold.ttf', 25)
        submit_button = font.render('Pass', True, BLACK)
        self.win.blit(submit_button, button_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mpos[0], mpos[1]):
                self._players[self.current_players_turn].turn_since_last_placement += 1
                print("COLLISION")
                return False

        return True

    #def submit_word

    def tile_holder_clicks(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mgrid = self.get_row_col_from_mouse(pygame.mouse.get_pos())
            print(TILE_HOLDER_OFFSET_Y // SQUARE_SIZE)
            print(mgrid[0])

            # print(mgrid[0])
            # print(TILE_HOLDER_OFFSET_Y // SQUARE_SIZE)

            if TILE_HOLDER_OFFSET_X // SQUARE_SIZE <= mgrid[1] < TILE_HOLDER_OFFSET_X // SQUARE_SIZE + 7 and mgrid[
                0] == TILE_HOLDER_OFFSET_Y // SQUARE_SIZE:
                tile_index = int(mgrid[1] - (TILE_HOLDER_OFFSET_X // SQUARE_SIZE))
                # print(tile_index)
                player_tiles = self._players[self.current_players_turn].tile_array
                if player_tiles[tile_index] and player_tiles[tile_index].is_tile():

                    # print("TILE: " + str(mgrid[1] - TILE_HOLDER_OFFSET_X // SQUARE_SIZE))
                    # TODO convert to mouse sticky then place on next click or return to tray
                    placed = False
                    while placed is not True:
                        for idx, row in enumerate(self._board._board):
                            for idy, col in enumerate(row):
                                if col.is_tile() is not True and placed == False:
                                    print("runs")
                                    self._board._board[idx][idy] = player_tiles.pop(tile_index)
                                    if self._tile_bag.get_tile_count() > 1:
                                        player_tiles += self._tile_bag.get_tiles(1)

                                    placed = True
                                    # TODO submit tiles ended turn

    def update(self):
        turn = True
        while turn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                turn = self.pass_button(self.win, event)
                self.tile_holder_clicks(event)
                self.player_turn_display()


        #draw on mouse()#TODO waiting for tiles to draw themselves
            self._board.draw(self.win, self._players[self.current_players_turn])
            #TODO add buttons to submit word, pass
            #self.curr

            pygame.display.flip()

        self.next_turn()

    # Draw(): TODO add all draw methods
