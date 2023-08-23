import unittest
from Game.game_models import (
    
    Tile,BagTiles,
)
from unittest.mock import patch
import random

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

    def test_tile_E(self):
        tile = Tile('E', 2)
        self.assertEqual(tile.letter, 'E')
        self.assertEqual(tile.value, 2)  

    def test_tile_F(self):
        tile = Tile('F', 4)
        self.assertEqual(tile.letter, 'F')
        self.assertEqual(tile.value, 4)  
    
    def test_tile_G(self):
        tile = Tile('G', 2)
        self.assertEqual(tile.letter, 'G')
        self.assertEqual(tile.value, 2)  

    def test_tile_H(self):
        tile = Tile('H', 4)
        self.assertEqual(tile.letter, 'H')
        self.assertEqual(tile.value, 4)   
    
    def test_tile_I(self):
        tile = Tile('I', 1)
        self.assertEqual(tile.letter, 'I')
        self.assertEqual(tile.value, 1)  
   
    def test_tile_J(self):
        tile = Tile('J', 8)
        self.assertEqual(tile.letter, 'J')
        self.assertEqual(tile.value, 8) 

    def test_tile_L(self):
        tile = Tile('L', 1)
        self.assertEqual(tile.letter, 'L')
        self.assertEqual(tile.value, 1)
     
    def test_tile_M(self):
        tile = Tile('M', 3)
        self.assertEqual(tile.letter, 'M')
        self.assertEqual(tile.value, 3)     
    
    def test_tile_N(self):
        tile = Tile('N', 1)
        self.assertEqual(tile.letter, 'N')
        self.assertEqual(tile.value, 1)  
    
    def test_tile_Ñ(self):
        tile = Tile('Ñ', 8)
        self.assertEqual(tile.letter, 'Ñ')
        self.assertEqual(tile.value, 8)  

    def test_tile_O(self):
        tile = Tile('O', 1)
        self.assertEqual(tile.letter, 'O')
        self.assertEqual(tile.value, 1)

    def test_tile_P(self):
        tile = Tile('P', 3)
        self.assertEqual(tile.letter, 'P')
        self.assertEqual(tile.value, 3)    

    def test_tile_Q(self):
        tile = Tile('Q', 5)
        self.assertEqual(tile.letter, 'Q')
        self.assertEqual(tile.value, 5)
    
    def test_tile_R(self):
        tile = Tile('R', 1)
        self.assertEqual(tile.letter, 'R')
        self.assertEqual(tile.value, 1)  

    def test_tile_S(self):
        tile = Tile('S', 1)
        self.assertEqual(tile.letter, 'S')
        self.assertEqual(tile.value, 1)    

    def test_tile_T(self):
        tile = Tile('T', 1)
        self.assertEqual(tile.letter, 'T')
        self.assertEqual(tile.value, 1)
   
    def test_tile_U(self):
        tile = Tile('U', 1)
        self.assertEqual(tile.letter, 'U')
        self.assertEqual(tile.value, 1)

    def test_tile_V(self):
        tile = Tile('v', 4)
        self.assertEqual(tile.letter, 'v')
        self.assertEqual(tile.value, 4)  

    def test_tile_X(self):
        tile = Tile('x', 8)
        self.assertEqual(tile.letter, 'x')
        self.assertEqual(tile.value, 8)

    def test_tile_Y(self):
        tile = Tile('y', 4)
        self.assertEqual(tile.letter, 'y')
        self.assertEqual(tile.value, 4)    

    def test_tile_Z(self):
        tile = Tile('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)  
    

    def test_tile_LL(self):
        tile = Tile('LL', 8)
        self.assertEqual(tile.letter, 'LL')
        self.assertEqual(tile.value, 8)  

    def test_tile_RR(self):
        tile = Tile('RR', 8)
        self.assertEqual(tile.letter, 'RR')
        self.assertEqual(tile.value, 8)  

    def test_tile_CH(self):
        tile = Tile('CH', 5)
        self.assertEqual(tile.letter, 'CH')
        self.assertEqual(tile.value, 5)  

    def test_tile_comodin(self):
        tile = Tile('#', 0)
        self.assertEqual(tile.letter, '#')
        self.assertEqual(tile.value, 0)
   



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
             2,
         )

    def test_put(self):
         bag = BagTiles()
         put_tiles = [Tile('Z', 1), Tile('Y', 1)]
         bag.put(put_tiles)
         self.assertEqual(
             len(bag.bag),
             104,
         )








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