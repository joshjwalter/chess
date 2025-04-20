import pytest
from bitboard import Bitboard





class TestBitboard:
    def test_clear_square(self):
        test_clear_board = Bitboard()
        test_clear_board.move_piece("white", "pawn", 0, 8)
        test_clear_board.clear_square(8)
        for x in test_clear_board.board_array:
            assert x == 0

    def test_move_piece(self):
        test_move_board = Bitboard()
        test_move_board.move_piece("white", "pawn", 0, 8)
        assert test_move_board.white_pawns == 256

    def test_moveback_piece(self):
        test_move_board = Bitboard()
        test_move_board.move_piece("white", "pawn", 0, 8)
        test_move_board.move_piece("white", "pawn", 8, 0)
        assert test_move_board.white_pawns == 1

    def test_output_index(self):
        test_output_board = Bitboard()
        test_output_board.move_piece("white", "pawn", 0, 8)
        test_output_board.move_piece("white", "pawn", 0, 9)
        assert test_output_board.output_index(test_output_board.white_pawns) == [8, 9]