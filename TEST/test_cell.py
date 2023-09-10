import unittest
from Game.cell import Cell
from Game.game_models import Tile



class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)


    def calculate_cell_value(self, multiplier, multiplier_type, letter, value):
        cell = Cell(multiplier=multiplier, multiplier_type=multiplier_type)
        tile = Tile(letter=letter, value=value)
        cell.add_letter(letter=tile)
        return cell.calculate_value()

    def test_cell_value(self):
        self.assertEqual(self.calculate_cell_value(3, 'letter', 'a', 1), 3)

    def test_cell_multiplier_word(self):
        self.assertEqual(self.calculate_cell_value(2, 'word', 'p', 3), 3)
        ###########################################################




if __name__ == '__main__':
    unittest.main()