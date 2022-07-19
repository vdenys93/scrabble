import pygame

class Scrabble:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Scrabble")

        # Set background color to gray
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen
            self.screen.fill(self.bg_color)



            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a instance of Scrabble and run the run_game
    scrabble = Scrabble()
    scrabble.run_game()
