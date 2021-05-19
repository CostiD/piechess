import pygame
from typing import List

import time

from settings import Settings
from board import Board
from pieces import *


class ChessGame:
    def __init__(self):
        pygame.init()

        # setup stage
        self.setup = Settings()
        self.main_window = pygame.display.set_mode(
            (self.setup.screen_width, self.setup.screen_height)
        )
        self.chess_board = Board(self)

        self.my_font = self.setup.game_font

        self.all_pieces = []

        # add kings: black king on e8, white king on e1
        # ---> ranks: 8, 1; files: e
        self.all_pieces += [
            King(
                color,
                tuple(
                    self.chess_board.board_positions.sel(rank=rank).sel(file="e").values
                ),
            )
            for color, rank in zip(["black", "white"], [8, 1])
        ]

        # add Queens
        self.all_pieces += [
            Queen(
                color,
                tuple(
                    self.chess_board.board_positions.sel(rank=rank).sel(file="d").values
                ),
            )
            for color, rank in zip(["black", "white"], [8, 1])
        ]

        # add Bishops
        self.all_pieces += [
            Bishop(
                color,
                tuple(
                    self.chess_board.board_positions.sel(rank=rank)
                    .sel(file=file)
                    .values
                ),
            )
            for color, rank, file in zip(
                ["black", "white"] * 2, [8, 1] * 2, ["f", "f", "c", "c"]
            )
        ]

        # add Knights
        self.all_pieces += [
            Knight(
                color,
                tuple(
                    self.chess_board.board_positions.sel(rank=rank)
                    .sel(file=file)
                    .values
                ),
            )
            for color, rank, file in zip(
                ["black", "white"] * 2, [8, 1] * 2, ["g", "g", "b", "b"]
            )
        ]

        # add Rooks
        self.all_pieces += [
            Rook(
                color,
                tuple(
                    self.chess_board.board_positions.sel(rank=rank)
                    .sel(file=file)
                    .values
                ),
            )
            for color, rank, file in zip(
                ["black", "white"] * 2, [8, 1] * 2, ["h", "h", "a", "a"]
            )
        ]

        # add Pawns; NOTE: ASCII code for `a` is 97.
        self.all_pieces += [
            Pawn(
                color,
                tuple(
                    self.chess_board.board_positions.sel(rank=rank)
                    .sel(file=file)
                    .values
                ),
            )
            for color, rank, file in zip(
                ["black", "white"] * 8,
                [7, 2] * 8,
                [s for s in [chr(c) for c in range(97, 97 + 8)] for i in range(2)],
            )
        ]

    # game loop
    def run_game(self):
        t0 = time.perf_counter()
        frame_count = 0
        frame_rate = 0
        while True:
            # step 1: poll events and handle input
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                position_of_click = event.dict["pos"]
                for piece in self.all_pieces:
                    if piece.contains_point(position_of_click, piece.image):
                        piece.handle_click(piece.image)
                        break

            frame_count += 1
            if frame_count % 500 == 0:
                t1 = time.perf_counter()
                frame_rate = 500 / (t1 - t0)
                t0 = t1
            # step 2: update data structures/object - change color/position etc. of objects

            # step 3: draw everything from scratch on the hidden buffer
            self.main_window.fill((self.setup.bg_color))
            self.chess_board.draw_board(self.main_window)

            for piece in self.all_pieces:
                piece.draw_piece(self.main_window)

            self.my_font.render_to(
                self.main_window,
                (100, 500),
                f"Frame {frame_count}. {frame_rate:.2f} fps",
                fgcolor=(0, 0, 0),
            )
            # step 4: swap buffers to display what has been drawn at the previous step
            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.run_game()
