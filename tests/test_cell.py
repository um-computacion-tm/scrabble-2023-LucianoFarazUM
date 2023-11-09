import unittest
from game.game_models import Tile
from game.cell import Cell  # Asegúrate de importar la clase Cell desde tu código

class TestCell(unittest.TestCase):
    def setUp(self):
        self.tile_A = Tile('A', 1)
        self.tile_B = Tile('B', 3)
        self.cell = Cell()

    def test_initial_cell_value(self):

        self.assertEqual(self.cell.calculate_value(), 0)

    def test_add_letter(self):

        self.cell.add_letter(self.tile_A)
        self.assertEqual(self.cell.calculate_value(), 1)

    def test_letter_multiplier_active(self):
        self.cell.multiplier_type = 'letter'
        self.cell.multiplier = 2
        self.cell.add_letter(self.tile_B) 
        self.assertEqual(self.cell.calculate_value(), 6)  

    def test_letter_multiplier_inactive(self):
        self.cell.multiplier_type = 'letter'
        self.cell.multiplier = 2
        self.cell.active = False
        self.cell.add_letter(self.tile_B)  
        self.assertEqual(self.cell.calculate_value(), 3)  


    def test_word_multiplier_inactive(self):
        self.cell.multiplier_type = 'word'
        self.cell.multiplier = 3
        self.cell.active = False
        self.cell.add_letter(self.tile_A)  
        self.assertEqual(self.cell.calculate_value(), 1)  

    def test_repr_with_letter(self):
        self.cell.add_letter(self.tile_A)
        self.assertEqual(repr(self.cell), repr(self.tile_A))

    def test_repr_with_word_multiplier(self):
        
        self.cell.multiplier_type = 'word'
        self.cell.multiplier = 3
        self.assertEqual(repr(self.cell), 'Wx3')

if __name__ == '__main__':
    unittest.main()
