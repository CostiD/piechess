"""
Class for maintaining sprites as piece objects
"""
import pygame
from settings import Settings


class Piece:
    def __init__(self, color, target_position, image=None):
        """
        Create and initialize a piece for this target_position on the board
        """
        self.image = image

        self.color = color
        self.target_position = target_position
        self.current_position = target_position

        self.setup = Settings()

    def update(self):
        pass

    def draw_piece(self, target_surface):
        target_surface.blit(self.image, self.current_position)

    def center_piece(self, image):
        self.setup.x_offset = (self.setup.square_width - image.get_width()) / 2
        self.setup.y_offset = (self.setup.square_height - image.get_height()) / 2
        (x, y) = self.current_position
        new_x = x + self.setup.x_offset
        new_y = y + self.setup.y_offset
        self.current_position = (new_x, new_y)

    def contains_point(self, point, image):
        """
        Returns True if the sprie rectangle contains point `point`
        """
        (current_x, current_y) = self.current_position
        image_width = image.get_width()
        image_height = image.get_height()
        (point_x, point_y) = point
        return (
            point_x >= current_x
            and point_x < current_x + image_width
            and point_y >= current_y
            and point_y < current_y + image_height
        )

    def handle_click(self, image):
        print("I got clicked!!!!!!!!!!!")


class King(Piece):
    def __init__(self, color, target_position, image=None):
        super().__init__(color, target_position, image=None)
        if self.color == "black":
            if image is None:
                self.image = pygame.image.load(r"images\black_king.png")
            else:
                self.image = image
        elif self.color == "white":
            if image is None:
                self.image = pygame.image.load(r"images\white_king.png")
            else:
                self.image = image
        else:
            print(f"{color} is invalid; color can be either black or white")

        self.center_piece(self.image)

    def center_piece(self, image):
        return super().center_piece(image)

    def contains_point(self, point, image):
        return super().contains_point(point, image)

    def handle_click(self, image):
        return super().handle_click(image)

    def reset_position(self):
        pass


class Queen(Piece):
    def __init__(self, color, target_position, image=None):
        super().__init__(color, target_position, image=None)
        if self.color == "black":
            if image is None:
                self.image = pygame.image.load(r"images\black_queen.png")
            else:
                self.image = image
        elif self.color == "white":
            if image is None:
                self.image = pygame.image.load(r"images\white_queen.png")
            else:
                self.image = image
        else:
            print(f"{color} is invalid; color can be either black or white")
        self.center_piece(self.image)

    def center_piece(self, image):
        return super().center_piece(image)

    def reset_position(self):
        pass


class Bishop(Piece):
    def __init__(self, color, target_position, image=None):
        super().__init__(color, target_position, image=None)
        if self.color == "black":
            if image is None:
                self.image = pygame.image.load(r"images\black_bishop.png")
            else:
                self.image = image
        elif self.color == "white":
            if image is None:
                self.image = pygame.image.load(r"images\white_bishop.png")
            else:
                self.image = image
        else:
            print(f"{color} is invalid; color can be either black or white")
        self.center_piece(self.image)

    def center_piece(self, image):
        return super().center_piece(image)

    def reset_position(self):
        pass


class Knight(Piece):
    def __init__(self, color, target_position, image=None):
        super().__init__(color, target_position, image=None)
        if self.color == "black":
            if image is None:
                self.image = pygame.image.load(r"images\black_knight.png")
            else:
                self.image = image
        elif self.color == "white":
            if image is None:
                self.image = pygame.image.load(r"images\white_knight.png")
            else:
                self.image = image
        else:
            print(f"{color} is invalid; color can be either black or white")
        self.center_piece(self.image)

    def center_piece(self, image):
        return super().center_piece(image)

    def reset_position(self):
        pass


class Rook(Piece):
    def __init__(self, color, target_position, image=None):
        super().__init__(color, target_position, image=None)
        if self.color == "black":
            if image is None:
                self.image = pygame.image.load(r"images\black_rook.png")
            else:
                self.image = image
        elif self.color == "white":
            if image is None:
                self.image = pygame.image.load(r"images\white_rook.png")
            else:
                self.image = image
        else:
            print(f"{color} is invalid; color can be either black or white")
        self.center_piece(self.image)

    def center_piece(self, image):
        return super().center_piece(image)

    def reset_position(self):
        pass


class Pawn(Piece):
    def __init__(self, color, target_position, image=None):
        super().__init__(color, target_position, image=None)
        if self.color == "black":
            if image is None:
                self.image = pygame.image.load(r"images\black_pawn.png")
            else:
                self.image = image
        elif self.color == "white":
            if image is None:
                self.image = pygame.image.load(r"images\white_pawn.png")
            else:
                self.image = image
        else:
            print(f"{color} is invalid; color can be either black or white")
        self.center_piece(self.image)

    def center_piece(self, image):
        return super().center_piece(image)

    def reset_position(self):
        pass
