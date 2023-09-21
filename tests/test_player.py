import unittest
from game.player import Player
from game.game_models import BagTiles


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(bag_tiles=BagTiles())
        self.assertEqual(len(player_1.tiles), 0)

    def test_get_score(self):
        player = Player(bag_tiles=BagTiles())
        player.score = 10
        self.assertEqual(player.get_score(), 10)

    def test_add_letter(self):
        bag_tiles = BagTiles()
        player = Player(bag_tiles)
        
        # Agregar una letra a la mano del jugador
        player.add_letter("A")
        self.assertEqual(player.get_letters(), ["A"])

        # Agregar más letras
        player.add_letter("B")
        player.add_letter("C")
        self.assertEqual(player.get_letters(), ["A", "B", "C"])

    def test_get_letters(self):
        bag_tiles = BagTiles()
        player = Player(bag_tiles)
        
        # Verificar que la mano del jugador esté vacía inicialmente
        self.assertEqual(player.get_letters(), [])

        # Agregar letras a la mano del jugador
        player.add_letter("X")
        player.add_letter("Y")
        player.add_letter("Z")
        self.assertEqual(player.get_letters(), ["X", "Y", "Z"])

if __name__ == '__main__':
    unittest.main()