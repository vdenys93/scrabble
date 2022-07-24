from constants import *

class Tile:


    def __init__(self, character=''):
        self._letter = character
        self._points = TILE_SCORES[character]

    def get_points(self):
        return self._points

    def get_letter(self):
        return self._letter

    def set_letter(self, character):
        self._letter = character
        self._points = TILE_SCORES[character]

    def is_tile(self) -> bool:
        if self._letter == '':
            return False
        return True

    def draw(win, letter: str, points: str, xcor: int, ycor: int):
        # mpos: tuple, win
        # Will need to update coordinates with mouse position and move text rectangles
        # Text currently appearing in top left corner

        letter_font = pygame.font.Font('freesansbold.ttf', 16)
        letter_text = letter_font.render(letter, True, BLACK, None)
        letter_rect_obj = letter_text.get_rect()
        letter_rect_obj.center = (SQUARE_SIZE// 2, SQUARE_SIZE // 2)
        points_font = pygame.font.Font('freesansbold.ttf', 8)
        points_text = points_font.render(points, True, BLACK, None)
        points_rect_obj = points_text.get_rect()
        points_rect_obj.center = (SQUARE_SIZE - 8, SQUARE_SIZE - 8) #40 - 8
        tile_border_obj = pygame.Rect(xcor, ycor, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(win, WHITE, tile_border_obj)
        win.blit(letter_text, letter_rect_obj)
        win.blit(points_text, points_rect_obj)
