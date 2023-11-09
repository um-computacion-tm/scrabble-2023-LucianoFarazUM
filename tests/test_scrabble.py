import unittest
from game.scrabble import ScrabbleGame
from game.game_models import Tile
from unittest.mock import patch, PropertyMock
from game.board import Board
from game.player import Player
from game.game_models import BagTiles
import io
import sys
class TestNextTurn(unittest.TestCase):

    def setUp(self):
        # Configurar el juego con dos jugadores y sus propias instancias de BagTiles
        bag_tiles = BagTiles()
        self.player1 = Player(bag_tiles)  # Crea una instancia de BagTiles para el primer jugador
        self.player2 = Player(bag_tiles)  # Crea otra instancia de BagTiles para el segundo jugador
        self.scrabble_game = ScrabbleGame(players_count=2)
    
        self.scrabble_game = ScrabbleGame(2)  # Reemplaza '2' con el número adecuado de jugadores

    @patch('tu_modulo.ScrabbleGame.current_player', new_callable=PropertyMock)
    @patch('tu_modulo.ScrabbleGame.players', new_callable=PropertyMock)
    def test_next_turn_single_player(self, mock_players, mock_current_player):
        # Simula los valores iniciales de current_player y players
        mock_players.return_value = [mock.Mock(), mock.Mock()]
        mock_current_player.return_value = 0
        
        # Comprobar que el primer turno es para el primer jugador
        self.assertEqual(self.scrabble_game.current_player, 0)
        self.assertEqual(self.scrabble_game.player, self.scrabble_game.players[0])

        # Cambiar al siguiente turno
        self.scrabble_game.next_turn()

        # Comprobar que el turno ha cambiado al segundo jugador
        self.assertEqual(self.scrabble_game.current_player, 1)
        self.assertEqual(self.scrabble_game.player, self.scrabble_game.players[1])

        # Cambiar al siguiente turno
        self.scrabble_game.next_turn()

        # Comprobar que el turno ha vuelto al primer jugador (ciclo)
        self.assertEqual(self.scrabble_game.current_player, 0)
        self.assertEqual(self.scrabble_game.player, self.scrabble_game.players[0])


        []



    
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
        self.game = ScrabbleGame(2)  # Reemplaza el número de jugadores según tu caso
    def test_can_form_word_valid_word_horizontal(self):
        word = "HELLO"
        location = (7, 7)
        orientation = "H"
        result= self.game.can_form_word(word, location, orientation)
        self.assertFalse(result)
        self.assertEqual(self.game.matching_tiles, [])

    def test_can_form_word_valid_word_vertical(self):
        word = "HELLO"
        location = (7, 7)
        orientation = "V"
        result = self.game.can_form_word(word, location, orientation)
        self.assertFalse(result)
        self.assertEqual(self.game.matching_tiles, [])

    def test_can_form_word_invalid_word(self):
        word = "INVALID"
        location = (7, 7)
        orientation = "H"

        result = self.game.can_form_word(word, location, orientation)
        

        self.assertFalse(result)
        self.assertEqual(self.game.matching_tiles, [])

    def test_can_form_word_invalid_word_with_wildcards(self):
        word = "HEL#O"
        location = (7, 7)
        orientation = "H"
        result = self.game.can_form_word(word, location, orientation)
        self.assertFalse(result)
        self.assertEqual(self.game.matching_tiles, [])

    def test_can_form_word_not_enough_tiles(self):
        word = "EXAMPLE"
        location = (7, 7)
        orientation = "H"
        self.game.players[0].rack.clear()  # Simula que el jugador no tiene letras suficientes
        result = self.game.can_form_word(word, location, orientation)
        self.assertFalse(result)
        self.assertEqual(self.game.matching_tiles, [])



        []






        
     
if __name__ == "__main__":
    unittest.main()