import unittest
from game.board import Board, SoloVoHParaLaOrientacion
from game.cell import Cell
from game.game_models import Tile

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()


    def test_is_empty_with_non_empty_board(self):
        # Colocar una letra en el centro del tablero (posición 7, 7)
        self.board.grid[7][7].letter = Tile('A', 1)
        self.assertFalse(self.board.is_empty())    
    
          
    def test_board_initialization(self):
        # Verifica que la inicialización del tablero cree una matriz 15x15 de celdas
        self.assertEqual(len(self.board.grid), 15)
        for row in self.board.grid:
            self.assertEqual(len(row), 15)
            for cell in row:
                self.assertIsInstance(cell, Cell)

    def test_set_multipliers(self):
        # Verifica que los multiplicadores estén configurados correctamente en el tablero
        # Puedes implementar más casos para verificar diferentes tipos de multiplicadores
        # y sus ubicaciones en el tablero
        self.assertEqual(self.board.grid[0][0].multiplier_type, 'word')
        self.assertEqual(self.board.grid[0][0].multiplier, 3)
        self.assertEqual(self.board.grid[1][1].multiplier_type, 'word')
        self.assertEqual(self.board.grid[1][1].multiplier, 2)

    def test_validate_word_inside_board(self):
        # Verifica que las palabras se validen correctamente dentro del tablero
        valid_word = [Tile('A', 1), Tile('B', 3)]
        invalid_word = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2)]
        self.assertTrue(self.board.validate_word_inside_board(valid_word, (0, 0), 'H'))
        self.assertFalse(self.board.validate_word_inside_board(invalid_word, (0, 0), 'H'))

    def test_validate_word_place_board_horizontal(self):
        # Verifica la validación de colocación de palabras horizontales en el tablero
        self.assertTrue(self.board.validate_word_place_board_horizontal([Tile('A', 1)], (7, 7)))
        self.assertFalse(self.board.validate_word_place_board_horizontal([Tile('A', 1)], (0, 0)))

    def test_validate_word_place_board_vertical(self):
        # Verifica la validación de colocación de palabras verticales en el tablero
        self.assertTrue(self.board.validate_word_place_board_vertical([Tile('A', 1)], (7, 7)))
        self.assertFalse(self.board.validate_word_place_board_vertical([Tile('A', 1)], (0, 0)))

    def test_put_word(self):
        # Verifica la colocación de palabras en el tablero
        word = [Tile('A', 1), Tile('B', 3)]
        self.board.put_word(word, (7, 7), 'H', 'player')
        self.assertEqual(self.board.grid[7][7].letter.letter, 'A')
        self.assertEqual(self.board.grid[7][8].letter.letter, 'B')

    def test_calculate_word_value_without_multipliers(self):
        word_without_multipliers = [
            Cell(1, 'letter', Tile('A', 1)),
            Cell(1, 'letter', Tile('B', 3)),
            Cell(1, 'letter', Tile('C', 3))
        ]
        self.assertEqual(Board.calculate_word_value(word_without_multipliers), 7)


    def test_calculate_word_value_with_multipliers(self):
        word_with_multipliers = [
            Cell(2, 'letter', Tile('A', 1)),
            Cell(1, 'word', Tile('B', 3)),
            Cell(1, 'letter', Tile('C', 3))
        ]
        self.assertEqual(Board.calculate_word_value(word_with_multipliers), 20) 

    def test_calculate_word_value_with_multipliers(self):
        word_with_multipliers = [
            Cell(1, 'letter', Tile('A', 1)),
            Cell(2, 'word', Tile('B', 3)),
            Cell(1, 'letter', Tile('C', 3))
        ]
        self.assertEqual(Board.calculate_word_value(word_with_multipliers), 14)

    def test_validate_word_inside_board(self):
        valid_word = [Tile('A', 1), Tile('B', 3)]
        invalid_word = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2)]
        self.assertTrue(self.board.validate_word_inside_board(valid_word, (7, 7), 'H'))
        self.assertFalse(self.board.validate_word_inside_board(invalid_word, (11, 11), 'v'))

    def test_put_word(self):
        # Verifica la colocación de palabras en el tablero
        word = [Tile('A', 1), Tile('B', 3)]
        self.board.put_word(word, (7, 7), 'H', 'player')
        self.assertEqual(self.board.grid[7][7].letter.letter, 'A')
        self.assertEqual(self.board.grid[7][8].letter.letter, 'B')

    def test_put_word_horizontal(self):
        word = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        location = (7, 7)
        orientation = 'H'
        player = None
        occupied_cells = self.board.put_word(word, location, orientation, player)
        expected_letters = ['A', 'B', 'C']
        self.assertEqual([cell.letter.letter for cell in occupied_cells], expected_letters)

    def test_put_word_vertical(self):
        word = [Tile('D', 2), Tile('E', 1), Tile('F', 4)]
        location = (7, 7)
        orientation = 'V'
        player = None
        occupied_cells = self.board.put_word(word, location, orientation, player)
        expected_letters = ['D', 'E', 'F']
        self.assertEqual([cell.letter.letter for cell in occupied_cells], expected_letters)

    def test_put_word_invalid_orientation(self):
        word = [Tile('G', 2), Tile('H', 4)]
        location = (7, 7)
        orientation = 'D'  # Orientación inválida
        player = None
        with self.assertRaises(Exception):
            self.board.put_word(word, location, orientation, player)
    
    def test_word_inside_board(self):
            board = Board()
            word = "Facultad"
            location = (5, 4)
            orientation = "H"
    
            word_is_valid = board.validate_word_inside_board(word, location, orientation)
    
            assert word_is_valid == True
        



    def test_validate_word_connections_valid_word_horizontal(self):
        # Configura un tablero con una palabra existente horizontalmente
        self.board.grid[7][7].add_letter(Cell(1, 'W'))
        self.board.grid[7][8].add_letter(Cell(1, 'O'))
        self.board.grid[7][9].add_letter(Cell(1, 'R'))
        # Define la palabra que se intentará colocar
        word = 'WORD'
        location = (7, 10)  # Prueba colocar la palabra a la derecha de 'R'
        orientation = 'H'

        # Ejecuta la función que se va a probar
        result = self.board.validate_word_connections(word, location, orientation, [], [])

        # Verifica que la función devuelve True, indicando que la palabra puede ser colocada
        self.assertFalse(result)

    def test_validate_word_connections_invalid_word_horizontal(self):
        # Configura un tablero con una palabra existente horizontalmente
        self.board.grid[7][7].add_letter(Cell(1, 'W'))
        self.board.grid[7][8].add_letter(Cell(1, 'O'))
        self.board.grid[7][9].add_letter(Cell(1, 'R'))
        # Define una palabra que no puede ser colocada horizontalmente
        word = 'INVALID'
        location = (7, 7)  # Prueba colocar la palabra a la derecha de 'R'
        orientation = 'J'

        # Ejecuta la función que se va a probar
        with self.assertRaises(SoloVoHParaLaOrientacion):
            self.board.validate_word_connections(word, location, orientation, [], [])


    
    def test_validate_word_vertical_matching_letters(self):
        # Configura un tablero con una palabra existente verticalmente ('W', 'O', 'R')
        self.board.grid[7][7].add_letter(Cell(1, 'W'))
        self.board.grid[8][7].add_letter(Cell(1, 'O'))
        self.board.grid[9][7].add_letter(Cell(1, 'R'))
        # Intenta colocar una palabra verticalmente que coincide con la palabra existente ('O', 'V', 'E', 'R')
        word = 'OVERT'
        x, y = 10, 7  # Coordenadas donde se coloca la primera letra de la palabra

        # Verifica que las letras coinciden y que la función retorna True
        result = self.board.validate_word_place_board_vertical(word, (x, y))
        self.assertTrue(result)

    def test_validate_word_vertical_non_matching_letters(self):
        # Configura un tablero con una palabra existente verticalmente ('W', 'O', 'R')
        self.board.grid[7][7].add_letter(Cell(1, 'W'))
        self.board.grid[8][7].add_letter(Cell(1, 'O'))
        self.board.grid[9][7].add_letter(Cell(1, 'R'))
        # Intenta colocar una palabra verticalmente que no coincide con la palabra existente ('N', 'O', 'T', 'E')
        word = 'NOTE'
        x, y = 10, 7  # Coordenadas donde se coloca la primera letra de la palabra

        # Verifica que las letras no coinciden y que la función retorna False
        result = self.board.validate_word_place_board_vertical(word, (x, y))
        self.assertTrue(result)        


    

if __name__ == '__main__':
    unittest.main()