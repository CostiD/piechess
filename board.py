"""
Define class for holding board objects
"""
import numpy as np
import xarray as xr


class Board:
    def __init__(self, chess_game, reversed=False):
        self.reversed = reversed
        self.num_rows = 8
        self.num_cols = 8
        self.chess_game = chess_game

        # create list of (x_topleft, y_topleft) coordinates for board squares
        self._board_positions_list = [
            [
                [
                    self.chess_game.setup.left_margin
                    + col * self.chess_game.setup.square_width,
                    self.chess_game.setup.top_margin
                    + row * self.chess_game.setup.square_height,
                ]
                for col in range(self.num_cols)
            ]
            for row in range(self.num_rows)
        ]

        # create an xarray.Dataset with :
        self._board_positions_arr = np.array(self._board_positions_list)
        self._ranks = [self.num_rows - i for i in range(self.num_rows)]
        self._files = [chr(c) for c in range(97, 97 + self.num_cols)]
        self._coords = ["x", "y"]

        self._board_positions_dataset = xr.Dataset(
            data_vars={
                "topleft": (["rank", "file", "coord"], self._board_positions_arr),
            },
            coords={
                "rank": (["rank"], self._ranks),
                "file": (["file"], self._files),
                "coord": (["coord"], self._coords),
            },
        )

        self.square_colors = [
            self.chess_game.setup.white_squares_color,
            self.chess_game.setup.dark_squares_color,
        ]

        # extract the data variable which holds the (x_topleft, y_topleft)
        # board coordinates as a function of rank and file
        self.board_positions = self._board_positions_dataset["topleft"]

    def draw_board(self, main_window):
        """
        Make the board draw itself on the main window
        """
        for irow, row in enumerate(self._ranks):
            color_index = irow % 2
            for col in self._files:
                main_window.fill(
                    self.square_colors[color_index],
                    (
                        self.board_positions.sel(rank=row)
                        .sel(file=col)
                        .sel(coord="x")
                        .values,
                        self.board_positions.sel(rank=row)
                        .sel(file=col)
                        .sel(coord="y")
                        .values,
                        self.chess_game.setup.square_width,
                        self.chess_game.setup.square_height,
                    ),
                )
                color_index = (color_index + 1) % 2

    def annotate_board(self):
        pass

    def reverse_board(self):
        pass
