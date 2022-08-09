# import pygame
import sys

import time
from .board import Board
from .player import Player
from .tile import Tile
from .tileBag import TileBag
from .constants import *


class Controller:
    def __init__(self, win):
        self._board = Board()
        self._players = [Player("John", 1), Player("George", 2)]
        self._tile_bag = TileBag()
        self._placed_tiles = []
        self.win = win
        self.current_players_turn = 0  # by index

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
        user_text = ''
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
        user_text = ''
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

    def pass_out_tiles(self):
        for player in self._players:
            if len(player.tile_array) == 0:
                player.tile_array = self._tile_bag.get_tiles(7)
            elif len(player.tile_array) < 7:
                count = 7 - len(player.tile_array)
                player.tile_array = player.tile_array + (self._tile_bag.get_tiles(count))

    def start(self, win):
        # get_player_count(win)
        self.pass_out_tiles()

    def adjacent_word_points(self):
        score_total = 0
        for xy in self._placed_tiles:
            adjacent_letters = [(xy[0], xy[1]-1),

            (xy[0]-1, xy[1]),                    (xy[0]+1, xy[1]),

                                 (xy[0], xy[1]+1)
                                ]
            for idx, a in enumerate(adjacent_letters):
                if a not in self._placed_tiles \
                        and 0 < a[0] < 15 \
                        and 0 < a[1] < 15 \
                        and self._board._board[a[0]][a[1]].is_tile():
                    # north
                    direction = [0, 0]
                    if idx == 0:
                        direction = [0, -1]
                    # east
                    if idx == 1:
                        direction = [-1, 0]
                    # west
                    if idx == 2:
                        direction = [1, 0]
                    # south
                    if idx == 3:
                        direction = [0, 1]

                    xy = list(a)

                    while self._board._board[xy[0]][xy[1]].is_tile():
                        score_total += self._board._board[xy[0]][xy[1]].get_points()
                        xy[0] += direction[0]
                        xy[1] += direction[1]
        return score_total

    def calculate_points(self, game_board: Board):
        word_score, double_word_bonus, triple_word_bonus = 0, 0, 0
        adjacent_words = self.adjacent_word_points()
        # adjacent_words = 0
        for i in self._placed_tiles:
            letter_bonus = 0
            if BOARD_PATTERN[i[0]][i[1]] == 'TW':
                triple_word_bonus += 1
            elif BOARD_PATTERN[i[0]][i[1]] == 'DW':
                double_word_bonus += 1
            if BOARD_PATTERN[i[0]][i[1]] == 'TL':
                letter_bonus = 3
            elif BOARD_PATTERN[i[0]][i[1]] == 'DL':
                letter_bonus = 2
            if letter_bonus > 0:
                word_score += game_board._board[i[0]][i[1]].get_points() * letter_bonus
            else:
                word_score += game_board._board[i[0]][i[1]].get_points()
        if double_word_bonus > 0:
            for n in range(double_word_bonus):
                word_score += game_board._board[i[0]][i[1]].get_points() * 2
        if triple_word_bonus > 0:
            for n in range(triple_word_bonus):
                word_score += game_board._board[i[0]][i[1]].get_points() * 3
        return word_score + adjacent_words

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
        if self._players[self.current_players_turn].skip_next_turn == True:
            self.next_turn()
        self._placed_tiles = []
        self.pass_out_tiles()
        pygame.display.flip()

    # Player turn display
    def player_turn_display(self):
        button_rect = pygame.Rect(4, SQUARE_SIZE * 6, TILE_SIZE * 3, SQUARE_SIZE)
        pygame.draw.rect(self.win, WHITE, button_rect)
        pygame.draw.rect(self.win, BLACK, button_rect, 1)
        font = pygame.font.Font('freesansbold.ttf', 24)
        submit_button = font.render("Player: " + str(self.current_players_turn), True, BLACK)
        submit_button_rect = font.render("Player: " + str(self.current_players_turn), True, BLACK)
        submit_button_rect = submit_button.get_rect(center=(4 + (TILE_SIZE * 1.5), SQUARE_SIZE * 6.5))
        self.win.blit(submit_button, submit_button_rect)

    def challenge(self) -> bool:
        button_rect = pygame.Rect(SQUARE_SIZE * 1, SQUARE_SIZE * 18, SQUARE_SIZE * 5.5, SQUARE_SIZE)
        pygame.draw.rect(self.win, WHITE, button_rect)
        font = pygame.font.Font('freesansbold.ttf', 25)
        submit_button = font.render("Challenge Word!", True, BLACK)
        self.win.blit(submit_button, button_rect)

        decided = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mpos[0], mpos[1]):
                    while decided is not True:
                        self.draw()
                        valid_rect = pygame.Rect(SQUARE_SIZE * 1, SQUARE_SIZE * 17, TILE_SIZE * 7, TILE_SIZE)
                        pygame.draw.rect(self.win, WHITE, valid_rect)
                        font = pygame.font.Font('freesansbold.ttf', 25)
                        valid_button = font.render("Is the word valid?", True, BLACK)
                        self.win.blit(valid_button, valid_rect)

                        yes_rect = pygame.Rect(SQUARE_SIZE * 8, SQUARE_SIZE * 17, TILE_SIZE * 2, TILE_SIZE)
                        pygame.draw.rect(self.win, WHITE, yes_rect)
                        yes_button = font.render("Yes", True, BLACK)
                        self.win.blit(yes_button, yes_rect)

                        no_rect = pygame.Rect(SQUARE_SIZE * 11, SQUARE_SIZE * 17, TILE_SIZE * 2, TILE_SIZE)
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
                                    which_player_rect = pygame.Rect(SQUARE_SIZE * 3, SQUARE_SIZE * 19, TILE_SIZE * 15, TILE_SIZE)
                                    pygame.draw.rect(self.win, WHITE, which_player_rect)
                                    font = pygame.font.Font('freesansbold.ttf', 25)
                                    which_player_button = font.render("Which player number losses their turn?", True, BLACK)
                                    self.win.blit(which_player_button, which_player_rect)

                                    input_rect = pygame.Rect(SQUARE_SIZE * 17, SQUARE_SIZE * 19, TILE_SIZE * 1, TILE_SIZE)

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
                                                        end_time = time.time() + 4
                                                        while time.time() < end_time:
                                                            self.draw()
                                                            lost_turn_rect = pygame.Rect(SQUARE_SIZE * 3,
                                                                                         SQUARE_SIZE * 19,
                                                                                         TILE_SIZE * 7, TILE_SIZE)
                                                            pygame.draw.rect(self.win, WHITE, lost_turn_rect)
                                                            font = pygame.font.Font('freesansbold.ttf', 25)

                                                            lost_turn_button = font.render("Player " + str(
                                                                input_player_num) + " losses turn", True, BLACK)

                                                            self.win.blit(lost_turn_button, lost_turn_rect)
                                                            pygame.display.flip()
                                                        player = True
                                                        return True
                                                else:
                                                    input_player_num += event.unicode
                                            pygame.draw.rect(self.win, WHITE, input_rect)

                                            input_player = font.render(str(input_player_num), True, BLACK)
                                            self.win.blit(input_player, input_rect)
                                            pygame.display.flip()

                                    self.win.blit(no_button, no_rect)
                                    return True

                                if no_rect.collidepoint((mpos[0], mpos[1])):
                                    for xy in self._placed_tiles:
                                        self._board._board[xy[0]][xy[1]] = Tile()
                                    end_time = time.time() + 4
                                    while time.time() < end_time:
                                        lost_turn_rect = pygame.Rect(SQUARE_SIZE * 3, SQUARE_SIZE * 19, TILE_SIZE * 8, TILE_SIZE)
                                        pygame.draw.rect(self.win, WHITE, lost_turn_rect)
                                        font = pygame.font.Font('freesansbold.ttf', 25)

                                        lost_turn_button = font.render("Player " + str(self._players[self.current_players_turn].player_num) + " losses turn", True, BLACK)
                                        # TODO return new tiles to bag from player hand
                                        self.win.blit(lost_turn_button, lost_turn_rect)
                                        pygame.display.flip()
                                        decided = True
                                    return False

                        pygame.display.flip()

    # def clicked_tile(self):
    def pass_button(self, event) -> bool:
        # Draw Pass Button
        button_rect = pygame.Rect(BOARD_WIDTH, SQUARE_SIZE * 18, SQUARE_SIZE * 3, SQUARE_SIZE)
        pygame.draw.rect(self.win, LT_GREY, button_rect)
        pygame.draw.rect(self.win, GREY, button_rect, 1)
        font = pygame.font.Font('freesansbold.ttf', 24)
        pass_button = font.render('Pass', True, BLACK)
        pass_button_rect = pass_button.get_rect(center=(BOARD_WIDTH + (SQUARE_SIZE * 1.5), SQUARE_SIZE * 18 + (TILE_SIZE * .5)))
        self.win.blit(pass_button, pass_button_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mpos[0], mpos[1]):
                self._players[self.current_players_turn].turn_since_last_placement += 1
                return False
        # if self._tile_bag.get_tile_count() > 1:
            # player_tiles += self._tile_bag.get_tiles(1)
        return True
    def discard_button(self, event) -> bool:
        button_rect = pygame.Rect(4, SQUARE_SIZE * 9, TILE_SIZE * 3, SQUARE_SIZE)
        pygame.draw.rect(self.win, WHITE, button_rect)
        pygame.draw.rect(self.win, BLACK, button_rect, 1)
        font = pygame.font.Font('freesansbold.ttf', 24)
        discard_button = font.render("Discard", True, BLACK)
        discard_button_rect = font.render("Discard", True, BLACK)
        discard_button_rect = discard_button.get_rect(center = (4 + (TILE_SIZE * 1.5), SQUARE_SIZE * 9.5))
        self.win.blit(discard_button, discard_button_rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mpos[0], mpos[1]):
                self._players[self.current_players_turn].tile_array.pop(0)
                self.pass_out_tiles()
                return False
        # if self._tile_bag.get_tile_count() > 1:
            # player_tiles += self._tile_bag.get_tiles(1)
        return True

    def end_game(self, event):
        button_rect = pygame.Rect(4, SQUARE_SIZE * 2, TILE_SIZE * 3, SQUARE_SIZE)
        pygame.draw.rect(self.win, LT_GREY, button_rect)
        pygame.draw.rect(self.win, GREY, button_rect, 1)
        font = pygame.font.Font('freesansbold.ttf', 20)
        end_game_button = font.render('End Game', True, BLACK)
        end_game_button_rect = end_game_button.get_rect(center=(4 + (TILE_SIZE * 1.5), SQUARE_SIZE * 2.5))
        self.win.blit(end_game_button, end_game_button_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mpos[0], mpos[1]):
                pygame.quit()
                sys.exit()

    def submit_word(self, event) -> bool:
        # Draw Submit word button
        button_rect = pygame.Rect(SQUARE_SIZE, SQUARE_SIZE * 18, SQUARE_SIZE * 5, SQUARE_SIZE)
        pygame.draw.rect(self.win, LT_GREY, button_rect)
        pygame.draw.rect(self.win, GREY, button_rect, 1)
        font = pygame.font.Font('freesansbold.ttf', 24)
        submit_button = font.render('Submit Word', True, BLACK)
        submit_button_rect = submit_button.get_rect(center=(SQUARE_SIZE * 3.5, SQUARE_SIZE * 18 +(TILE_SIZE * .5)))
        self.win.blit(submit_button, submit_button_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mpos[0], mpos[1]):
                if len(self._placed_tiles) > 0:
                    self._players[self.current_players_turn].last_placed_word = self._placed_tiles
                    delay = time.time() + 5

                    good_word = None
                    while time.time() < delay and good_word is None:
                        self.draw()
                        good_word = self.challenge()
                        pygame.display.flip()
                    if good_word is None or good_word is True:
                        self._players[self.current_players_turn].score += self.calculate_points(self._board)
                    self._board.draw_scoreboard(self.win, self._players[self.current_players_turn])
                    turn_active = False
                    return turn_active

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
                    if BOARD_OFFSET_X < mpos[0] < BOARD_OFFSET_X + BOARD_WIDTH and BOARD_OFFSET_Y < mpos[1] < BOARD_OFFSET_Y + BOARD_HEIGHT:
                        if self._board._board[int(mgrid[0] - (BOARD_OFFSET_X // SQUARE_SIZE))][int(mgrid[1] - (BOARD_OFFSET_Y // SQUARE_SIZE))].is_tile() is not True:
                            board_grid = (int(mgrid[0] - (BOARD_OFFSET_X // SQUARE_SIZE)), int(mgrid[1] - (BOARD_OFFSET_Y // SQUARE_SIZE)))
                            self._board.place_tile(tile, board_grid)
                            print(board_grid)
                            self._placed_tiles.append(board_grid)
                            placed = True

    def tile_holder_clicks(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mgrid = self.get_row_col_from_mouse(pygame.mouse.get_pos())

            if TILE_HOLDER_OFFSET_X // SQUARE_SIZE <= mgrid[0] < TILE_HOLDER_OFFSET_X // SQUARE_SIZE + 7 and mgrid[
                1] == TILE_HOLDER_OFFSET_Y // SQUARE_SIZE:
                tile_index = int(mgrid[0] - (TILE_HOLDER_OFFSET_X // SQUARE_SIZE))
                player_tiles = self._players[self.current_players_turn].tile_array
                if player_tiles[tile_index] and player_tiles[tile_index].is_tile():
                    self.tile_placement(player_tiles.pop(tile_index))

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
            pygame.event.post(pygame.event.Event(pygame.USEREVENT+1))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.tile_holder_clicks(event)
                self.draw()
                self.end_game(event)
                self.discard_button(event)
                turn = self.submit_word(event)
                if turn is not False:
                    turn = self.pass_button(event)

                pygame.display.flip()

        # draw on mouse()#TODO waiting for tiles to draw themselves
            # TODO add buttons to submit word, pass
        self.next_turn()


