import unittest
from Game.calculator_values import CalculateValue
from Game.cell import Cell
from Game.game_models import Tile
from Game.game_models import Tile,LETTER_VALUES

class TestCalculateValue(unittest.TestCase):
    def test_simple(self):
        # Crea una lista de celdas utilizando la clase Cell y asigna las letras con sus valores
        word = [
            Cell(1, 'letter', Tile('C', LETTER_VALUES['C'])),
            Cell(1, 'letter', Tile('A', LETTER_VALUES['A'])),
            Cell(1, 'letter', Tile('S', LETTER_VALUES['S'])),
            Cell(1, 'letter', Tile('A', LETTER_VALUES['A'])),
        ]

        value = CalculateValue.calculate(word)
        self.assertEqual(value, 6)

if __name__ == '__main__':
     unittest.main()