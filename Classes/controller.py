import time
from board import Board
from player import Player
from tile import Tile
from tileBag import TileBag
import pygame
from constants import *
import sys


class Controller:
    def __init__(self, win):
        self._board = Board()
        self._players = [Player("testone", 1), Player("testtwo", 2)]
        self._tile_bag = TileBag()
        self._placed_tiles = []
        self.win = win

        self.current_players_turn = 0 #by index

    def place_tile(self, xy: tuple):
        self._placed_tiles.append(xy)

    def remove_tile(self, xy: tuple):
        self._placed_tiles.remove(xy)

    def draw_text(self, text, x, y):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(text, True, BLACK, BLUE)
        text_rect = text.get_rect()
        text_rect.center = (x // 2, y // 2)

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

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = int(y // SQUARE_SIZE)
        col = int(x // SQUARE_SIZE)
        return col, row

    def next_turn(self):
        if self.current_players_turn == len(self._players) - 1:
            self.current_players_turn = 0
        else:
            self.current_players_turn += 1

    # Player turn display
    def player_turn_display(self):
        button_rect = Rect(4, SQUARE_SIZE * 6, TILE_SIZE * 3, SQUARE_SIZE)
        pygame.draw.rect(self.win, WHITE, button_rect)
        pygame.draw.rect(self.win, BLACK, button_rect, 1)
        font = pygame.font.Font('freesansbold.ttf', 24)
        submit_button = font.render("Player: " + str(self.current_players_turn), True, BLACK)
        submit_butto_rect = font.render("Player: " + str(self.current_players_turn), True, BLACK)
        submit_button_rect = submit_button.get_rect(center = (4 + (TILE_SIZE * 1.5), SQUARE_SIZE * 6.5))
        self.win.blit(submit_button, submit_button_rect)

    def challenge(self) -> bool:
        button_rect = Rect(SQUARE_SIZE * 2, SQUARE_SIZE * 18, SQUARE_SIZE * 5, SQUARE_SIZE)
        pygame.draw.rect(self.win, WHITE, button_rect)
        font = pygame.font.Font('freesansbold.ttf', 25)
        submit_button = font.render("Challenge Word!" + str(self.current_players_turn), True, BLACK)
        self.win.blit(submit_button, button_rect)

        decided = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
                print(mpos)
                if button_rect.collidepoint(mpos[0], mpos[1]):
                    while decided is not True:
                        self.draw()
                        valid_rect = Rect(SQUARE_SIZE * 1, SQUARE_SIZE * 1, TILE_SIZE * 7, TILE_SIZE)
                        pygame.draw.rect(self.win, WHITE, valid_rect)
                        font = pygame.font.Font('freesansbold.ttf', 25)
                        valid_button = font.render("Is the word valid?", True, BLACK)
                        self.win.blit(valid_button, valid_rect)

                        yes_rect = Rect(SQUARE_SIZE * 8, SQUARE_SIZE * 1, TILE_SIZE * 2, TILE_SIZE)
                        pygame.draw.rect(self.win, WHITE, yes_rect)
                        yes_button = font.render("Yes", True, BLACK)
                        self.win.blit(yes_button, yes_rect)

                        no_rect = Rect(SQUARE_SIZE * 11, SQUARE_SIZE * 1, TILE_SIZE * 2, TILE_SIZE)
                        pygame.draw.rect(self.win, WHITE, no_rect)
                        no_button = font.render("No", True, BLACK)
                        self.win.blit(no_button, no_rect)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                mpos = pygame.mouse.get_pos()

                                if yes_rect.collidepoint(mpos[0], mpos[1]):
                                    which_player_rect = Rect(SQUARE_SIZE * 3, SQUARE_SIZE * 19, TILE_SIZE * 5, TILE_SIZE)
                                    pygame.draw.rect(self.win, WHITE, which_player_rect)
                                    font = pygame.font.Font('freesansbold.ttf', 25)
                                    which_player_button = font.render("Which player number losses their turn?", True, BLACK)
                                    self.win.blit(which_player_button, which_player_rect)

                                    input_rect = Rect(SQUARE_SIZE * 3, SQUARE_SIZE * 19, TILE_SIZE * 5, TILE_SIZE)


                                    input_player_num = ''
                                    player = False
                                    while player is not True:
                                        input_player = font.render(str(input_player_num), True, BLACK)
                                        self.win.blit(input_player, input_rect)

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                            if event.type == pygame.KEYDOWN:

                                                if event.key == pygame.K_BACKSPACE:

                                                    input_player_num = input_player_num[:-1]

                                                elif event.key == pygame.K_RETURN:
                                                    if input_player_num.isdigit() and int(input_player_num) in range(len(self._players)):
                                                        self._players[int(input_player_num)].skip_next_turn = True
                                                        player = True
                                                        return True

                                                else:
                                                    input_player_num += event.unicode
                                            pygame.draw.rect(self.win, WHITE, input_rect)

                                            input_player = font.render(str(input_player_num), True, BLACK)
                                            self.win.blit(input_player, input_rect)
                                            pygame.display.flip()

                                    self.win.blit(no_button, no_rect)

                                if no_rect.collidepoint((mpos[0], mpos[1])):
                                    end_time = time.time() + 4
                                    while time.time() < end_time:
                                        lost_turn_rect = Rect(SQUARE_SIZE * 3, SQUARE_SIZE * 19, TILE_SIZE * 5, TILE_SIZE)
                                        pygame.draw.rect(self.win, WHITE, lost_turn_rect)
                                        font = pygame.font.Font('freesansbold.ttf', 25)

                                        lost_turn_button = font.render("Player " + str(self._players[self.current_players_turn].player_num) + " losses turn", True, BLACK)
                                        # TODO return new tiles to bag from player hand
                                        self.win.blit(lost_turn_button, lost_turn_rect)
                                        pygame.display.flip()
                                        decided = True
                                    return True

                        pygame.display.flip()






    #def clicked_tile(self):
    def pass_button(self, event) -> bool:
        #Draw Pass Button
        button_rect = Rect(BOARD_WIDTH, SQUARE_SIZE * 18, SQUARE_SIZE * 3, SQUARE_SIZE)
        pygame.draw.rect(self.win, LT_GREY, button_rect)
        pygame.draw.rect(self.win, GREY, button_rect, 1)
        font = pygame.font.Font('freesansbold.ttf', 24)
        pass_button = font.render('Pass', True, BLACK)
        pass_button_rect = pass_button.get_rect(center = (BOARD_WIDTH + (SQUARE_SIZE * 1.5), SQUARE_SIZE * 18 + (TILE_SIZE * .5)))
        self.win.blit(pass_button, pass_button_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mpos[0], mpos[1]):
                self._players[self.current_players_turn].turn_since_last_placement += 1
                print("COLLISION")
                return False
        #if self._tile_bag.get_tile_count() > 1:
            #player_tiles += self._tile_bag.get_tiles(1)
        return True

    def submit_word(self, event):
        #Draw Submit word button
        button_rect = Rect(SQUARE_SIZE, SQUARE_SIZE * 18, SQUARE_SIZE * 5, SQUARE_SIZE)
        pygame.draw.rect(self.win, LT_GREY, button_rect)
        pygame.draw.rect(self.win, GREY, button_rect, 1)
        font = pygame.font.Font('freesansbold.ttf', 24)
        submit_button = font.render('Submit Word', True, BLACK)
        submit_button_rect = submit_button.get_rect(center = (SQUARE_SIZE * 3.5, SQUARE_SIZE * 18 +(TILE_SIZE * .5)))
        self.win.blit(submit_button, submit_button_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mpos[0], mpos[1]):
                if len(self._placed_tiles) > 0:
                    self._players[self.current_players_turn].last_placed_word = self._placed_tiles
                    self._placed_tiles = []
                    delay = time.time() + 10

                    go = False
                    while time.time() < delay and go is not True:
                        self.draw()
                        go = self.challenge()
                        pygame.display.flip()

                    #self.next_turn()



    def tile_placement(self, tile):
        floating_tile = tile
        placed = False

        while placed is not True:
            mpos = (pygame.mouse.get_pos())

            self.draw()
            tile.draw(self.win, mpos[0], mpos[1])
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mpos = pygame.mouse.get_pos()

                    mgrid = self.get_row_col_from_mouse(pygame.mouse.get_pos())

                    # board placement
                    if  BOARD_OFFSET_X < mpos[0] < BOARD_OFFSET_X + BOARD_WIDTH and BOARD_OFFSET_Y < mpos[1] < BOARD_OFFSET_Y + BOARD_HEIGHT:
                        print("X grid " + str(BOARD_OFFSET_X),str(mpos[0]))
                        print("Y grid " + str(BOARD_OFFSET_Y),str(mpos[1]))
                        if self._board._board[int(mgrid[0] - (BOARD_OFFSET_X // SQUARE_SIZE))][int(mgrid[1] - (BOARD_OFFSET_Y // SQUARE_SIZE))].is_tile() is not True:
                            board_grid = (int(mgrid[0] - (BOARD_OFFSET_X // SQUARE_SIZE)), int(mgrid[1] - (BOARD_OFFSET_Y // SQUARE_SIZE)))
                            self._board.place_tile(tile, board_grid)
                            self._placed_tiles.append(board_grid)
                            placed = True

    def tile_holder_clicks(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mgrid = self.get_row_col_from_mouse(pygame.mouse.get_pos())
            #print(TILE_HOLDER_OFFSET_Y // SQUARE_SIZE)
            #print(mgrid[0])

            # print(mgrid[0])
            # print(TILE_HOLDER_OFFSET_Y // SQUARE_SIZE)

            if TILE_HOLDER_OFFSET_X // SQUARE_SIZE <= mgrid[0] < TILE_HOLDER_OFFSET_X // SQUARE_SIZE + 7 and mgrid[
                1] == TILE_HOLDER_OFFSET_Y // SQUARE_SIZE:
                tile_index = int(mgrid[0] - (TILE_HOLDER_OFFSET_X // SQUARE_SIZE))
                # print(tile_index)
                player_tiles = self._players[self.current_players_turn].tile_array
                print(player_tiles[tile_index].is_tile())
                if player_tiles[tile_index] and player_tiles[tile_index].is_tile():
                    self.tile_placement(player_tiles.pop(tile_index))
                    # print("TILE: " + str(mgrid[1] - TILE_HOLDER_OFFSET_X // SQUARE_SIZE))
                    # TODO convert to mouse sticky then place on next click or return to tray

    def draw(self):
        pygame.draw.rect(self.win, BLACK, (0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self._board.draw(self.win, self._players[self.current_players_turn])
        self.player_turn_display()

    def update(self):
        turn = True
        if self._players[self.current_players_turn].skip_next_turn is True:
            turn = False
            self._players[self.current_players_turn].skip_next_turn = False

        while turn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.tile_holder_clicks(event)
                self.draw()
                self.submit_word(event)
                turn = self.pass_button(event)
                pygame.display.flip()
        # draw on mouse()#TODO waiting for tiles to draw themselves
            # TODO add buttons to submit word, pass
        self.next_turn()
