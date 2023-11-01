
import unittest
from game.game_models import (
    Tile, BagTiles, Exception100, Exception0,
)
from unittest.mock import patch


class TestTile(unittest.TestCase):
    def test_tile_initialization(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tile_repr(self):
        tile = Tile('A', 1)
        expected_repr = "A:1"
        self.assertEqual(repr(tile), expected_repr)


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.bag), 100)
        self.assertEqual(patch_shuffle.call_count, 1)
        self.assertEqual(patch_shuffle.call_args[0][0], bag.bag)

    def test_take(self):
           bag = BagTiles()
           tiles = bag.take(2)
           self.assertEqual(
              len(bag.bag),
              98,
          )
           self.assertEqual(
              len(tiles),
              2,   )
           
    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.bag), 102)
    
    def test_exception0(self):
        bag = BagTiles()
        with self.assertRaises(Exception0):
            bag.add_to_bag(Tile('A', 1), 10)  # Agregar 10 fichas cuando ya hay 100 fichas en la bolsa

    def test_exception100(self):
        bag = BagTiles()
        with self.assertRaises(Exception100):
            bag.take(101)  # Intentar tomar 101 fichas cuando solo hay 100 disponibles
        self.assertEqual(len(bag.bag), 100)  # Asegurarse de que la bolsa no cambió después de la excepción

if __name__ == '__main__':
    unittest.main()
    