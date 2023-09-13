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

if __name__ == '__main__':
    unittest.main()
    