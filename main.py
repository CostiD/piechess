import pygame
from typing import List

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

        image_filenames = [
            r"images\black_king.png",
            r"images\black_queen.png",
            r"images\black_bishop.png",
            r"images\black_knight.png",
            r"images\black_rook.png",
            r"images\black_pawn.png",
            r"images\white_king.png",
            r"images\white_queen.png",
            r"images\white_bishop.png",
            r"images\white_knight.png",
            r"images\white_rook.png",
            r"images\white_pawn.png",
        ]
        self.images = self._load_images(image_filenames)

        self.my_font = self.setup.game_font

        self.all_sprites = self._load_sprites()

    def _load_images(self, filenames: List[str]):
        self.filenames = filenames
        images = []
        for file in filenames:
            images.append(pygame.image.load(f"{file}"))
        return images

    def _load_sprites(self):
        all_sprites = []
        # the black pieces
        # -------------------------------
        black_rook_on_a8 = Rook(
            self.images[4],
            (
                self.chess_board.board_positions[0][0][0]
                + (self.setup.square_width - self.images[4].get_width()) / 2,
                self.chess_board.board_positions[0][0][1]
                + (self.setup.square_height - self.images[4].get_height()) / 2,
            ),
        )
        all_sprites.append(black_rook_on_a8)
        # -------------------------------
        black_bishop_on_b8 = Bishop(
            self.images[2],
            (
                self.chess_board.board_positions[1][0][0]
                + (self.setup.square_width - self.images[2].get_width()) / 2,
                self.chess_board.board_positions[1][0][1]
                + (self.setup.square_height - self.images[2].get_height()) / 2,
            ),
        )
        all_sprites.append(black_bishop_on_b8)
        # -------------------------------
        black_knight_on_c8 = Knight(
            self.images[3],
            (
                self.chess_board.board_positions[2][0][0]
                + (self.setup.square_width - self.images[3].get_width()) / 2,
                self.chess_board.board_positions[2][0][1]
                + (self.setup.square_height - self.images[3].get_height()) / 2,
            ),
        )
        all_sprites.append(black_knight_on_c8)
        # -------------------------------
        black_queen_on_d8 = Queen(
            self.images[1],
            (
                self.chess_board.board_positions[3][0][0]
                + (self.setup.square_width - self.images[1].get_width()) / 2,
                self.chess_board.board_positions[3][0][1]
                + (self.setup.square_height - self.images[1].get_height()) / 2,
            ),
        )
        all_sprites.append(black_queen_on_d8)
        # -------------------------------
        black_king_on_e8 = King(
            self.images[0],
            (
                self.chess_board.board_positions[4][0][0]
                + (self.setup.square_width - self.images[0].get_width()) / 2,
                self.chess_board.board_positions[4][0][1]
                + (self.setup.square_height - self.images[0].get_height()) / 2,
            ),
        )
        all_sprites.append(black_king_on_e8)
        # -------------------------------
        black_knight_on_f8 = Knight(
            self.images[3],
            (
                self.chess_board.board_positions[5][0][0]
                + (self.setup.square_width - self.images[3].get_width()) / 2,
                self.chess_board.board_positions[5][0][1]
                + (self.setup.square_height - self.images[3].get_height()) / 2,
            ),
        )
        all_sprites.append(black_knight_on_f8)
        # -------------------------------
        black_bishop_on_g8 = Bishop(
            self.images[2],
            (
                self.chess_board.board_positions[6][0][0]
                + (self.setup.square_width - self.images[2].get_width()) / 2,
                self.chess_board.board_positions[6][0][1]
                + (self.setup.square_height - self.images[2].get_height()) / 2,
            ),
        )
        all_sprites.append(black_bishop_on_g8)
        # -------------------------------
        black_rook_on_h8 = Rook(
            self.images[4],
            (
                self.chess_board.board_positions[7][0][0]
                + (self.setup.square_width - self.images[4].get_width()) / 2,
                self.chess_board.board_positions[7][0][1]
                + (self.setup.square_height - self.images[4].get_height()) / 2,
            ),
        )
        all_sprites.append(black_rook_on_h8)
        # --------------------------------
        for col in range(self.chess_board.num_cols):
            black_pawn = Pawn(
                self.images[5],
                (
                    self.chess_board.board_positions[col][1][0]
                    + (self.setup.square_width - self.images[5].get_width()) / 2,
                    self.chess_board.board_positions[col][1][1]
                    + (self.setup.square_height - self.images[5].get_height()) / 2,
                ),
            )
            all_sprites.append(black_pawn)

        # ======================================#
        # ======================================#
        # ======================================#
        # ======================================#
        # ======================================#
        # ======================================#
        # white pieces
        # -------------------------------
        black_rook_on_a8 = Rook(
            self.images[4 + 6],
            (
                self.chess_board.board_positions[0][7][0]
                + (self.setup.square_width - self.images[4 + 6].get_width()) / 2,
                self.chess_board.board_positions[0][7][1]
                + (self.setup.square_height - self.images[4 + 6].get_height()) / 2,
            ),
        )
        all_sprites.append(black_rook_on_a8)
        # -------------------------------
        black_bishop_on_b8 = Bishop(
            self.images[2 + 6],
            (
                self.chess_board.board_positions[1][7][0]
                + (self.setup.square_width - self.images[2 + 6].get_width()) / 2,
                self.chess_board.board_positions[1][7][1]
                + (self.setup.square_height - self.images[2 + 6].get_height()) / 2,
            ),
        )
        all_sprites.append(black_bishop_on_b8)
        # -------------------------------
        black_knight_on_c8 = Knight(
            self.images[3 + 6],
            (
                self.chess_board.board_positions[2][7][0]
                + (self.setup.square_width - self.images[3 + 6].get_width()) / 2,
                self.chess_board.board_positions[2][7][1]
                + (self.setup.square_height - self.images[3 + 6].get_height()) / 2,
            ),
        )
        all_sprites.append(black_knight_on_c8)
        # -------------------------------
        black_queen_on_d8 = Queen(
            self.images[1 + 6],
            (
                self.chess_board.board_positions[3][7][0]
                + (self.setup.square_width - self.images[1 + 6].get_width()) / 2,
                self.chess_board.board_positions[3][7][1]
                + (self.setup.square_height - self.images[1 + 6].get_height()) / 2,
            ),
        )
        all_sprites.append(black_queen_on_d8)
        # -------------------------------
        black_king_on_e8 = King(
            self.images[0 + 6],
            (
                self.chess_board.board_positions[4][7][0]
                + (self.setup.square_width - self.images[0 + 6].get_width()) / 2,
                self.chess_board.board_positions[4][7][1]
                + (self.setup.square_height - self.images[0 + 6].get_height()) / 2,
            ),
        )
        all_sprites.append(black_king_on_e8)
        # -------------------------------
        black_knight_on_f8 = Knight(
            self.images[3 + 6],
            (
                self.chess_board.board_positions[5][7][0]
                + (self.setup.square_width - self.images[3 + 6].get_width()) / 2,
                self.chess_board.board_positions[5][7][1]
                + (self.setup.square_height - self.images[3 + 6].get_height()) / 2,
            ),
        )
        all_sprites.append(black_knight_on_f8)
        # -------------------------------
        black_bishop_on_g8 = Bishop(
            self.images[2 + 6],
            (
                self.chess_board.board_positions[6][7][0]
                + (self.setup.square_width - self.images[2 + 6].get_width()) / 2,
                self.chess_board.board_positions[6][7][1]
                + (self.setup.square_height - self.images[2 + 6].get_height()) / 2,
            ),
        )
        all_sprites.append(black_bishop_on_g8)
        # -------------------------------
        black_rook_on_h8 = Rook(
            self.images[4 + 6],
            (
                self.chess_board.board_positions[7][7][0]
                + (self.setup.square_width - self.images[4 + 6].get_width()) / 2,
                self.chess_board.board_positions[7][7][1]
                + (self.setup.square_height - self.images[4 + 6].get_height()) / 2,
            ),
        )
        all_sprites.append(black_rook_on_h8)
        # --------------------------------
        for col in range(self.chess_board.num_cols):
            black_pawn = Pawn(
                self.images[5 + 6],
                (
                    self.chess_board.board_positions[col][6][0]
                    + (self.setup.square_width - self.images[5 + 6].get_width()) / 2,
                    self.chess_board.board_positions[col][6][1]
                    + (self.setup.square_height - self.images[5 + 6].get_height()) / 2,
                ),
            )
            all_sprites.append(black_pawn)
        return all_sprites

    # game loop
    def run_game(self):
        while True:
            # step 1: poll events and handle input
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break

            # step 2: update data structures/object - change color/position etc. of objects

            # step 3: draw everything from scratch on the hidden buffer
            self.main_window.fill((self.setup.bg_color))
            self.chess_board.draw_board(self.main_window)

            for sprite in self.all_sprites:
                sprite.draw_piece(self.main_window)

            # step 4: swap buffers to display what has been drawn at the previous step
            pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.run_game()
