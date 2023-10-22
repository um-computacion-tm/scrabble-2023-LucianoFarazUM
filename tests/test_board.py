# import unittest
# from game.board import Board
# from game.game_models import Tile
# class TestBoard(unittest.TestCase):
#     def test_init(self):
#         board = Board()
#         self.assertEqual(
#             len(board.grid),
#             15,
#         )
#         self.assertEqual(
#             len(board.grid[0]),
#             15,
#         )
    
    # def test_word_inside_board(self):
    #     board = Board()
    #     word = "Facultad"
    #     location = (5, 4)
    #     orientation = "H"

    #     word_is_valid = board.validate_word_inside_board(word, location, orientation)

    #     assert word_is_valid == True

    # def test_word_out_of_board(self):
    #         board = Board()
    #         word = "Facultad"
    #         location = (14, 4)
    #         orientation = "H"   
    #         word_is_valid = board.validate_word_inside_board(word, location, orientation)
    
    #         assert word_is_valid == False

    # def test_board_is_empty(self):
    #         board = Board()
    #         assert board.is_empty == True
    
    # def test_board_is_not_empty(self):
    #         board = Board()
    #         board.grid[7][7].add_letter(Tile('C', 1))
    #         assert board.is_empty == False

    # def test_place_word_empty_board_horizontal_fine(self):
    #     board = Board()
    #     word = "Facultad"
    #     location = (7, 4)
    #     orientation = "H"
    #     word_is_valid = board.validate_word_place_board(word, location, orientation)
    #     assert word_is_valid == True

    # def test_place_word_empty_board_horizontal_wrong(self):
    #     board = Board()
    #     word = "Facultad"
    #     location = (2, 4)
    #     orientation = "H"
    #     word_is_valid = board.validate_word_place_board(word, location, orientation)
    #     assert word_is_valid == False

    # def test_place_word_empty_board_vertical_fine(self):
    #     board = Board()
    #     word = "Facultad"
    #     location = (4, 7)
    #     orientation = "V"
    #     word_is_valid = board.validate_word_place_board(word, location, orientation)
    #     assert word_is_valid == True

    # def test_place_word_empty_board_vertical_wrong(self):
    #     board = Board()
    #     word = "Facultad"
    #     location = (2, 4)
    #     orientation = "V"
    #     word_is_valid = board.validate_word_place_board(word, location, orientation)
    #     assert word_is_valid == False

    # def test_place_word_not_empty_board_horizontal_fine(self):
    #     board = Board()
    #     board.grid[7][7].add_letter(Tile('C', 1))
    #     board.grid[8][7].add_letter(Tile('A', 1)) 
    #     board.grid[9][7].add_letter(Tile('S', 1)) 
    #     board.grid[10][7].add_letter(Tile('A', 1)) 
    #     word = "Facultad"
    #     location = (8, 6)
    #     orientation = "H"
    #     word_is_valid = board.validate_word_place_board(word, location, orientation)
    #     assert word_is_valid == True



import unittest
from game.board import Board
from game.game_models import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    
    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.is_empty, True)

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        self.assertEqual(board.is_empty, False)

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (15, 15)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
    
    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)

    
    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (10, 10)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False    

    def test_clear_board(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        board.validate_word_place_board(word, location, orientation)
        board.clear_board()
        self.assertEqual(board.is_empty, True)

    # Prueba para validar cuando se coloca una palabra que se superpone verticalmente.
    def test_place_word_overlapping_vertical(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = "Facultad"
        location = (7, 7)  # Intenta superponer "Facultad" incorrectamente sobre "CASA"
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_display_board(self):
        self.board = Board
        # Redirigir la salida estándar para capturar la impresión en un string
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        # Llamar a la función display_board
        self.board.display_board()

        # Restaurar la salida estándar
        sys.stdout = saved_stdout

        # Obtener la salida de la función display_board
        displayed_board = sys.stdout.getvalue().strip()

        # Comparar la salida con el tablero esperado
        expected_board = (
            "Tablero de Scrabble:\n"
            "  0     1     2     3     4     5     6     7     8     9    10    11    12    13    14 "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  " 
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
            "   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .     .     .  "
        )

        self.assertEqual(displayed_board, expected_board)


if __name__ == '__main__':
    unittest.main()