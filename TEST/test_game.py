import unittest
from Game.game_models import (
    
    Tile,BagTiles,
)
from unittest.mock import patch
import random


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.bag),
            102,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.bag,
        )


    def test_take(self):
          bag = BagTiles()
          tiles = bag.take(2)
          self.assertEqual(
             len(bag.bag),
             100,
         )
          self.assertEqual(
             len(tiles),
             2,   )

    def test_put(self):
         bag = BagTiles()
         put_tiles = [Tile('Z', 1), Tile('Y', 1)]
         bag.put(put_tiles)
         self.assertEqual(
             len(bag.bag),
             104,
         )



if __name__ == '__main__':
    unittest.main()