import unittest
from Game.game_models import (
    
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile_A(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tile_B(self):
        tile = Tile('B', 3)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 3)    

    def test_tile_C(self):
        tile = Tile('C', 3)
        self.assertEqual(tile.letter, 'C')
        self.assertEqual(tile.value, 3)  

    def test_tile_D(self):
        tile = Tile('D', 2)
        self.assertEqual(tile.letter, 'D')
        self.assertEqual(tile.value, 2)  
# class TestBagTiles(unittest.TestCase):
#     @patch('random.shuffle')
#     def test_bag_tiles(self,
#         self.assertEqual(
#             len(bag.tiles), patch_shuffle):
#         bag = BagTiles()
#             5,
#         )
#         self.assertEqual(
#             patch_shuffle.call_count,
#             1,
#         )
#         self.assertEqual(
#             patch_shuffle.call_args[0][0],
#             bag.tiles,
#         )
#     def test_take(self):
#         bag = BagTiles()
#         tiles = bag.take(2)
#         self.assertEqual(
#             len(bag.tiles),
#             3,
#         )
#         self.assertEqual(
#             len(tiles),
#             2,
#         )
        
    # def test_put(self):
    #     bag = BagTiles()
    #     put_tiles = [Tile('Z', 1), Tile('Y', 1)]
    #     bag.put(put_tiles)
    #     self.assertEqual(
    #         len(bag.tiles),
    #         7,
    #     )
        #########################################################################33


if __name__ == '__main__':
    unittest.main()