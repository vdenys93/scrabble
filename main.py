import pygame
import sys
from scrabble.constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, SQUARE_SIZE
from scrabble.game import Game


FPS = 60
WIN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Scrabble")

pygame.init()


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    # tile = board.get_tile(row, col)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # On click event to see if the mouse clicks on a square
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)

        # Redraw the screen
        game.update()

        # Make the most recently drawn screen visible
        # pygame.display.flip()

    pygame.quit()
    sys.exit()


main()
