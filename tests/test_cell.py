import unittest
from game.cell import Cell
from game.game_models import Tile


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

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )

    def test_repr_with_tile(self):
        tile = Tile('A', 1)
        cell = Cell(letter=tile, multiplier=2, multiplier_type='word')
        expected_repr = 'A:1'
        self.assertEqual(repr(cell), expected_repr)

    def test_repr_with_word_multiplier(self):
        cell = Cell(multiplier=3, multiplier_type='word')
        expected_repr = 'Wx3'
        self.assertEqual(repr(cell), expected_repr)

    def test_repr_with_letter_multiplier(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        expected_repr = 'Lx2'
        self.assertEqual(repr(cell), expected_repr)

    def test_repr_with_no_multipliers(self):
        cell = Cell(multiplier=1, multiplier_type='letter')
        expected_repr = '   '
        self.assertEqual(repr(cell), expected_repr)

if __name__ == '__main__':
    unittest.main()