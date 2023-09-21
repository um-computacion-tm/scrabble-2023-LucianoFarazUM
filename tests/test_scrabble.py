import unittest
from game.scrabble import ScrabbleGame  # Corrección en la importación
from game.game_models import Tile


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    
    def test_next_turn_when_game_is_starting(self):
        # Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(players_count=3)

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

    # Nuevos tests para las funciones adicionales
    def test_is_valid_word(self):
        scrabble_game = ScrabbleGame(players_count=3)
        player = scrabble_game.players[0]
        player.tiles = ["a", "p", "p", "l", "e"]  # Asignar letras al jugador

        # Probar con una palabra que el jugador tiene
        result = scrabble_game.valid_word("apple", player)
        self.assertTrue(result)

        # Probar con una palabra que el jugador no tiene
        result = scrabble_game.valid_word("banana", player)
        self.assertFalse(result)


    def test_can_place_word(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.board.clear_board()  # Limpiar el tablero

        # Colocar una palabra en posición válida
        result = scrabble_game.can_place_word("hello", (7, 7), "H")
        self.assertTrue(result)

        # Colocar una palabra en posición no válida
        result = scrabble_game.can_place_word("world", (12, 12), "H")
        self.assertFalse(result)
    def test_can_place_word_edge_cases(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.board.clear_board()

        # Colocar una palabra en el borde izquierdo del tablero
        result = scrabble_game.can_place_word("hello", (7, 0), "H")
        self.assertTrue(result)

        # Colocar una palabra en el borde superior del tablero
        result = scrabble_game.can_place_word("world", (0, 7), "V")
        self.assertTrue(result)

        # Colocar una palabra que se extiende más allá del borde derecho del tablero
        result = scrabble_game.can_place_word("overflow", (8, 1), "H")
        self.assertFalse(result)


    
    def test_can_place_word_vertical_edge_cases(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.board.clear_board()

        # Colocar una palabra en el borde superior del tablero
        result = scrabble_game.can_place_word("hello", (0, 7), "V")
        self.assertTrue(result)

        # Colocar una palabra en el borde inferior del tablero
        result = scrabble_game.can_place_word("world", (14, 7), "V")
        self.assertTrue(result)

        # Colocar una palabra que se extiende más allá del borde inferior del tablero
        result = scrabble_game.can_place_word("overflow", (11, 8), "V")
        self.assertFalse(result)

    def test_can_place_word_overlap(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.board.clear_board()
        scrabble_game.board.grid[7][7].add_letter(Tile('H', 1))

        # Colocar una palabra que se superpone con otra
        result = scrabble_game.can_place_word("hello", (7, 6), "H")
        self.assertTrue(result)

        # Colocar una palabra que se superpone con otra pero es inválida
        result = scrabble_game.can_place_word("world", (12, 5), "H")
        self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()