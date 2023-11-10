import unittest
from game.scrabble import ScrabbleGame
from game.game_models import Tile
from unittest.mock import patch ,Mock
from game.board import Board


class TestEndGame(unittest.TestCase):



    def test_show_board(self):
        # Prueba la función show_board. Para este caso, solo se asegura de que no haya errores durante la ejecución.
        self.game.show_board()

    
    def setUp(self):
        # Inicializa tu clase o cualquier otro objeto necesario para las pruebas
        self.game = ScrabbleGame(2)  # Reemplaza '2' con el número adecuado de jugadores

    @patch('builtins.input', side_effect=["si"])
    def test_end_game_with_empty_rack(self, mock_input):
        # Simula que el rack del jugador está vacío
        self.game.player.rack = []

        # Asegúrate de que sys.exit() lance una excepción SystemExit
        with self.assertRaises(SystemExit):
            # Llama al método end_game
            self.game.end_game()

    @patch('builtins.input', side_effect=["no"])
    def test_end_game_with_non_empty_rack(self, mock_input):
        # Simula que el rack del jugador no está vacío
        self.game.player.rack = ['A', 'B', 'C']
        
        # Llama al método end_game y asegúrate de que no lance excepciones
        result = self.game.end_game()

        # Comprueba que el método devuelve False
        self.assertFalse(result)


class TestScrabbleGame(unittest.TestCase):



    @patch('builtins.input', side_effect=["WORD", "7", "7", "H"])
    def test_valid_word_placement(self, mock_input):
        game = ScrabbleGame(players_count=2)
        game.player.rack = self.game.bag_tiles.take(7)  # Configura el rack del jugador
        game.play()
        # Asegúrate de que el juego haya avanzado al siguiente turno correctamente y que el estado del juego sea el esperado
        self.assertEqual(game.current_player, 0)  # Cambiar a otro jugador después de un turno exitoso
        self.assertEqual(game.player.score, 0)  # Ajusta este valor según la puntuación esperada para la palabra "WORD"

    @patch('builtins.input', side_effect=["INVALIDWORD", "7", "7", "H", "WORD", "7", "7", "H"])
    def test_invalid_word_then_valid_word_placement(self, mock_input):
        game = ScrabbleGame(players_count=1)
        game.player.rack = self.game.bag_tiles.take(7)  # Configura el rack del jugador
        game.play()
        # Asegúrate de que el juego haya avanzado al siguiente turno correctamente y que el estado del juego sea el esperado
        self.assertEqual(game.current_player, 0)  # Cambiar a otro jugador después de un turno exitoso
        self.assertEqual(game.player.score, 0)  # Ajusta este valor según la puntuación esperada para la palabra "WORD"

    @patch('builtins.input', side_effect=["INVALIDWORD", "7", "7", "H", "NO", "INVALIDWORD", "7", "7", "H", "WORD", "7", "7", "H"])
    def test_invalid_word_then_continue_and_invalid_word_then_valid_word_placement(self, mock_input):
        game = ScrabbleGame(players_count=1)
        game.player.rack = self.game.bag_tiles.take(7)  # Configura el rack del jugador
        game.play()
        # Asegúrate de que el juego haya avanzado al siguiente turno correctamente y que el estado del juego sea el esperado
        self.assertEqual(game.current_player, 0)  # Cambiar a otro jugador después de un turno exitoso
        self.assertEqual(game.player.score, 0)  # Ajusta este valor según la puntuación esperada para la palabra "WORD"


    def setUp(self):
        self.game = ScrabbleGame(2)
        self.board = Board()
  # Reemplaza el número de jugadores según tu caso
    def test_can_form_word_valid_word_horizontal(self):
        self.game.player.rack = [Tile("H", 1), Tile("E", 1), Tile("L", 1), Tile("L", 1), Tile("O", 1)]
        word = "HELLO"
        location = (7, 7)
        orientation = "H"
        result, self.game.matching_tiles = self.game.can_form_word(word, location, orientation)
        self.assertTrue(result)
        
        # Extrae los valores de las letras de los objetos Tile en una lista
        matching_tile_values = [tile.value for tile in self.game.matching_tiles]
        
        # Compara los valores de las letras en lugar de los objetos Tile
        expected_values = [1, 1, 1, 1, 1]
        self.assertEqual(matching_tile_values, expected_values)

    def test_can_form_word_valid_word_vertical(self):
        self.game.player.rack = [Tile("H", 1), Tile("E", 1), Tile("L", 1), Tile("L", 1), Tile("O", 1)]
        word = "HELLO"
        location = (7, 7)
        orientation = "V"
        result, self.game.matching_tiles = self.game.can_form_word(word, location, orientation)
        self.assertTrue(result)
        
        # Extrae los valores de las letras de los objetos Tile en una lista
        matching_tile_values = [tile.value for tile in self.game.matching_tiles]
        
        # Compara los valores de las letras en lugar de los objetos Tile
        expected_values = [1, 1, 1, 1, 1]
        self.assertEqual(matching_tile_values, expected_values)
   
    def test_can_form_word_not_enough_tiles(self):
        word = "EXAMPLE"
        location = (7, 7)
        orientation = "H"
        self.game.players[0].rack.clear()  # Simula que el jugador no tiene letras suficientes
        result = self.game.can_form_word(word, location, orientation)
        self.assertFalse(result)
        self.assertEqual(self.game.matching_tiles, [])


    def test_validate_word_valid_word_placement(self):
        # Configura un tablero vacío
        # El jugador tiene las letras 'H', 'A', 'T' en su rack
        self.board.grid[7][7].add_letter(Mock(1, 'H'))
        self.board.grid[7][8].add_letter(Mock(1, 'A'))
        self.board.grid[7][9].add_letter(Mock(1, 'T'))
        word = 'HAT'
        location = (7, 10)  # Coloca la palabra 'HAT' horizontalmente después de 'T'
        orientation = 'H'

        # Simula que la función de validación del diccionario siempre devuelve True
        with patch.object(self.game.dict,'validate_dict', return_value=True):
            result = self.game.validate_word(word, location, orientation)
            self.assertFalse(result)

    def test_validate_word_invalid_word_format(self):
        # Configura un tablero vacío
        # El jugador tiene las letras 'H', 'A', 'T' en su rack
        word = 'INVALID123'  # La palabra contiene caracteres no permitidos
        location = (7, 7)  # Coloca la palabra 'INVALID123' horizontalmente en la posición (7, 7)
        orientation = 'H'

        # Simula que la función de validación del diccionario siempre devuelve True
        with patch.object(self.game.dict, 'validate_dict', return_value=True):
            result = self.game.validate_word(word, location, orientation)
            self.assertFalse(result)  # La palabra contiene caracteres no permitidos

   

    
    @patch('builtins.input', side_effect=['HELLO', '7', '7', 'H'])
    def test_play_valid_word_horizontal(self, mock_input):
        game = ScrabbleGame(players_count=2)
        initial_rack = game.player.rack.copy()

        game.board.grid[7][7].letter = None  # Simula que la celda está vacía
        game.play()
        game.player.rack=self.game.player.rack = [Tile("H", 1), Tile("E", 1), Tile("L", 1), Tile("L", 1), Tile("O", 1), Tile("U",1),Tile("D",1)]
        game.board.put_word('HELLO', (7, 7), 'H',game.player)

        self.assertNotEqual(initial_rack, game.player.rack)
        self.assertEqual(len(game.player.rack), 7)
        self.assertNotEqual(game.board.grid[7][7].letter, None)
        self.assertNotEqual(game.board.grid[7][8].letter, None)
        self.assertNotEqual(game.board.grid[7][9].letter, None)
        self.assertNotEqual(game.board.grid[7][10].letter, None)
        self.assertNotEqual(game.board.grid[7][11].letter, None)

    @patch('builtins.input', side_effect=['INVALID', '7', '7', 'H', 'No'])
    def test_play_invalid_word_horizontal(self, mock_input):
        game = ScrabbleGame(players_count=2)
        initial_rack = game.player.rack.copy()
        game.board.grid[7][7].letter = None  # Simula que la celda está vacía
        game.play()
        game.player.rack=self.game.player.rack = [Tile("H", 1), Tile("E", 1), Tile("L", 1), Tile("L", 1), Tile("O", 1), Tile("U",1),Tile("D",1)]
        self.assertNotEqual(initial_rack, game.player.rack)
        self.assertEqual(len(game.player.rack), 7)
        self.assertEqual(game.board.grid[7][7].letter, None)
        self.assertEqual(game.board.grid[8][7].letter, None)
        self.assertEqual(game.board.grid[9][7].letter, None)
        self.assertEqual(game.board.grid[10][7].letter, None)
        self.assertEqual(game.board.grid[11][7].letter, None)


    @patch('builtins.input', side_effect=['HELLO', '7', '7', 'V'])
    def test_play_valid_word_vertical(self, mock_input):
        game = ScrabbleGame(players_count=2)
        initial_rack = game.player.rack.copy()
        game.board.grid[7][7].letter = None  # Simula que la celda está vacía
        game.play()
        game.player.rack=self.game.player.rack = [Tile("H", 1), Tile("E", 1), Tile("L", 1), Tile("L", 1), Tile("O", 1), Tile("U",1),Tile("D",1)]
        game.board.put_word('HELLO', (7, 7), 'V',game.player)
        self.assertNotEqual(initial_rack, game.player.rack)
        self.assertEqual(len(game.player.rack), 7)
        self.assertNotEqual(game.board.grid[7][7].letter, None)
        self.assertNotEqual(game.board.grid[8][7].letter, None)
        self.assertNotEqual(game.board.grid[9][7].letter, None)
        self.assertNotEqual(game.board.grid[10][7].letter, None)
        self.assertNotEqual(game.board.grid[11][7].letter, None)


    @patch('builtins.input', side_effect=['INVALID', '7', '7', 'V', 'No'])
    def test_play_invalid_word_vertical(self, mock_input):
        game = ScrabbleGame(players_count=2)
        initial_rack = game.player.rack.copy()

        game.play()

        self.assertEqual(initial_rack, game.player.rack)
        self.assertEqual(game.board.grid[7][7].letter, None)
        self.assertEqual(game.board.grid[8][7].letter, None)
        self.assertEqual(game.board.grid[9][7].letter, None)
        self.assertEqual(game.board.grid[10][7].letter, None)
        self.assertEqual(game.board.grid[11][7].letter, None)


    def test_next_turn(self):
        # Configuración inicial
        game = ScrabbleGame(players_count=3)
        initial_current_player = game.current_player
        initial_player = game.player

        # Llamada al método que se va a probar
        game.next_turn()

        # Asegurar que el jugador actual se ha cambiado correctamente
        self.assertNotEqual(initial_current_player, game.current_player)

        # Asegurar que el objeto de jugador también ha cambiado correctamente
        self.assertNotEqual(initial_player, game.player)
        self.assertEqual(game.player, game.players[game.current_player])





    def test_validate_word_valid_word_placement(self):
        # Configura un escenario donde la palabra se puede colocar válidamente en el tablero
        word = "HAT"
        location = (7, 7)
        orientation = "H"
        self.game.player.rack = [Tile("H", 1), Tile("A", 1), Tile("T", 1)]  # Configura el rack del jugador
        self.game.board.grid[7][7].letter = None  # Configura la celda como vacía
        result = self.game.validate_word(word, location, orientation)
        self.assertFalse(result)


    def test_obtener_posicion_invalid_input_then_valid_input(self):
        # Prueba la función obtener_posicion con una entrada no válida seguida de una entrada válida
        with patch('builtins.input', side_effect=['invalid', '7', '7']):
            x, y = self.game.obtener_posicion()
            self.assertEqual(x, 7)
            self.assertEqual(y, 7)

    def test_end_game_no(self):
        with patch('builtins.input', return_value='no'):
            juego = ScrabbleGame(1)
            resultado = juego.end_game()
            # Verifica que el método devuelva False cuando el usuario ingresa 'no'
            self.assertFalse(resultado)

    def test_can_form_word_false(self):
        # Prueba cuando self.can_form_word devuelve False
        self.game.can_form_word = lambda word, location, orientation: False
        resultado = self.game.validate_word("palabra", (1, 1), "horizontal")
        self.assertFalse(resultado)
    
    def test_validate_word_place_board_false(self):
        # Prueba cuando self.board.validate_word_place_board devuelve False
        self.game.board.validate_word_place_board = lambda word, location, orientation: False
        resultado = self.game.validate_word("palabra", (1, 1), "horizontal")
        self.assertFalse(resultado)
    
    def test_validate_dict_false(self):
        # Prueba cuando self.dict.validate_dict lanza una excepción
        self.game.dict.validate_dict = lambda word: False
        resultado = self.game.validate_word("palabra", (1, 1), "horizontal")
        self.assertFalse(resultado)



if __name__ == '__main__':
    unittest.main()