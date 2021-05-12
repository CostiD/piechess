"""
Class for maintaining sprites as piece objects
"""


class Piece:
    def __init__(self, image, target_position):
        """
        Create and initialize a piece for this target_position on the board
        """
        self.image = image
        self.target_position = target_position
        self.current_position = target_position

    def update(self):
        pass

    def draw_piece(self, target_surface):
        target_surface.blit(self.image, self.current_position)


class King(Piece):
    def __init__(self, image, target_position):
        super().__init__(image, target_position)

    def reset_position(self, target_position):
        self.target_position = target_position


class Queen(Piece):
    def __init__(self, image, target_position):
        super().__init__(image, target_position)

    def reset_position(self, target_position):
        self.target_position = target_position


class Bishop(Piece):
    def __init__(self, image, target_position):
        super().__init__(image, target_position)

    def reset_position(self, target_position):
        self.target_position = target_position


class Knight(Piece):
    def __init__(self, image, target_position):
        super().__init__(image, target_position)

    def reset_position(self, target_position):
        self.target_position = target_position


class Rook(Piece):
    def __init__(self, image, target_position):
        super().__init__(image, target_position)

    def reset_position(self, target_position):
        self.target_position = target_position


class Pawn(Piece):
    def __init__(self, image, target_position):
        super().__init__(image, target_position)

    def reset_position(self, target_position):
        self.target_position = target_position
