import pygame
import board
import tile
import player
import tileBag
import controller
import sys


from constants import *

FPS = 60
win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Scrabble")
pygame.init()


def get_row_col_from_mouse(pos):
    x, y = pos
    x -= 100
    y -= 150

    row = (y + 0.5) // SQUARE_SIZE
    col = (x + 0.5) // SQUARE_SIZE
    return row, col


def main():
    print("anything")
    run = True
    clock = pygame.time.Clock()
    game_controller = controller.Controller(win)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # On click event to see if the mouse clicks on a square
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print(row,col)

        game_controller.update()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    pygame.quit()
    sys.exit()


main()

