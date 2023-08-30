# import unittest
# from Game.game_models import (
    
#     Tile,BagTiles,
# )
# from unittest.mock import patch
# import random


# class TestBagTiles(unittest.TestCase):
#     @patch('random.shuffle')
#     def test_bag_tiles(self, patch_shuffle):
#         bag = BagTiles()
#         self.assertEqual(
#             len(bag.bag),
#             100,
#         )
#         self.assertEqual(
#             patch_shuffle.call_count,
#             1,
#         )
#         self.assertEqual(
#             patch_shuffle.call_args[0][0],
#             bag.bag,
#         )


#     def test_take(self):
#           bag = BagTiles()
#           tiles = bag.take(2)
#           self.assertEqual(
#              len(bag.bag),
#              98,
#          )
#           self.assertEqual(
#              len(tiles),
#              2,   )

#     def test_put(self):
#          bag = BagTiles()
#          put_tiles = [Tile('Z', 1), Tile('Y', 1)]
#          bag.put(put_tiles)
#          self.assertEqual(
#              len(bag.bag),
#              102,
#          )



# if __name__ == '__main__':
#     unittest.main()
import unittest
from Game.game_models import (
    Tile, BagTiles, exception100, exception0,
)
from unittest.mock import patch


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.bag), 100)
        self.assertEqual(patch_shuffle.call_count, 1)
        self.assertEqual(patch_shuffle.call_args[0][0], bag.bag)

        def test_take(self):
            bag = BagTiles()
            initial_bag_size = len(bag.bag)
            bag.take_exception100(2)
            self.assertEqual(len(bag.bag), initial_bag_size - 2)

     
    def take_exception100(self, count):
        if len(self.bag) >= count:
            raise exception100("Trying to take more tiles than available")

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.bag), 102)

    def test_exception0(self):
        bag = BagTiles()
        with self.assertRaises(exception0):
            bag.add_to_bag(Tile('A', 1), 10)  # Adding 10 tiles when there are already 102 tiles 
     
if __name__ == '__main__':
    unittest.main()
