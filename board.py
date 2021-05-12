"""
Define class for holding board objects
"""


class Board:
    def __init__(self, chess_game, reversed=False):
        self.reversed = reversed
        self.num_rows = 8
        self.num_cols = 8
        self.chess_game = chess_game

        self.board_positions = [[None] * self.num_cols for row in range(self.num_rows)]
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.board_positions[row][col] = [
                    self.chess_game.setup.left_margin
                    + row * self.chess_game.setup.square_width,
                    self.chess_game.setup.top_margin
                    + col * self.chess_game.setup.square_height,
                ]

        self.square_colors = [
            self.chess_game.setup.white_squares_color,
            self.chess_game.setup.dark_squares_color,
        ]

    def draw_board(self, main_window):
        """
        Make the board draw itself on the main window
        """
        for row in range(self.num_rows):
            color_index = row % 2
            for col in range(self.num_cols):
                main_window.fill(
                    self.square_colors[color_index],
                    (
                        self.board_positions[row][col][0],
                        self.board_positions[row][col][1],
                        self.chess_game.setup.square_width,
                        self.chess_game.setup.square_height,
                    ),
                )
                color_index = (color_index + 1) % 2

    # def annotate_board()
