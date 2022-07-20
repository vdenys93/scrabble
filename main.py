import pygame
import sys
from scrabble.constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, TAN
from scrabble.board import Board

FPS = 60
WIN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT),
                                 pygame.RESIZABLE)
pygame.display.set_caption("Scrabble")

pygame.init()

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # On click event to see if the mouse clicks on a square
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # draw a blank screen
        # WIN.fill(TAN)

        # Redraw the screen
        board.draw_squares(WIN)
        pygame.display.update()

        # Make the most recently drawn screen visible
        # pygame.display.flip()

    pygame.quit()
    sys.exit()


main()
