import sys
import pygame
import pygamepopup
from pygamepopup.menu_manager import MenuManager
from pygamepopup.components import Button, InfoBox, TextElement
from Classes.constants import *
from Classes.controller import Controller


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE * .75
    col = x // SQUARE_SIZE * .75
    return row, col



def main():

    run = True
    clock = pygame.time.Clock()
    win.fill(GREEN)
    game_controller = Controller(win)
    pygame.mixer.music.load("start_menu_music.mp3")
    game_sound=pygame.mixer.Sound("game_music.mp3")
    pygame.mixer.music.set_volume(0.4)
    game_volume =  0.3
    pygame.mixer.Sound.set_volume(game_sound, max(0,game_volume))
    pygame.mixer.music.play(-1)






    while run:


        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # On click event to see if the mouse clicks on a square
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)

        game_controller.get_player_count(win, event)
        player_selection_completed = game_controller.player_selection_is_complete
        game_controller.start(win)


        while player_selection_completed:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(game_sound,-1)
            game_controller.update()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    FPS = 60
    win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Scrabble")
    pygame.init()
    pygamepopup.init()
    main()

