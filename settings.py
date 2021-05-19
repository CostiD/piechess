import pygame
import pygame.freetype

pygame.init()


class Settings:
    def __init__(self):
        """
        Initialize dimensions, colors and text options
        """
        # dimensions
        self.square_width, self.square_height = 100, 100
        self.board_width, self.board_height = (
            self.square_width * 8,
            self.square_height * 8,
        )
        self.left_margin, self.top_margin = 50, 50
        self.right_margin, self.bottom_margin = 550, 50
        self.screen_width = self.left_margin + self.board_width + self.right_margin
        self.screen_height = self.top_margin + self.board_height + self.bottom_margin

        # colors
        self.dark_squares_color = (87, 58, 46)
        self.white_squares_color = (252, 204, 116)
        self.bg_color = (207, 138, 74)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        # text
        self.game_font = pygame.freetype.SysFont("courier", 16)
        self.ASCII_a = 97
        self.ASCII_A = 65

        # centering offsets
        self.x_offset = None
        self.y_offset = None
