import unittest
from Game.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles), 0)

    def test_get_score(self):
        player = Player()
        player.score = 10
        self.assertEqual(player.get_score(), 10)

if __name__ == '__main__':
    unittest.main()
    