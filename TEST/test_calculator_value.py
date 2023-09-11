import unittest
from Game.calculator_value import CalculateValue
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

    def test_with_letter_multiplier(self):

         word = [
             Cell(3, 'letter'),  # Letra 'C' con multiplicador de 3
             Cell(1, 'letter'),  # Letra 'A' con multiplicador de 1
             Cell(2, 'letter'),    # Letra 'S' con multiplicador de palabra de 2
             Cell(1, 'letter'),  # Letra 'A' con multiplicador de 1
         ]

         # Agregar letras a las celdas
         word[0].add_letter(Tile('C', LETTER_VALUES['C']))
         word[1].add_letter(Tile('A', LETTER_VALUES['A']))
         word[2].add_letter(Tile('S', LETTER_VALUES['S']))
         word[3].add_letter(Tile('A', LETTER_VALUES['A']))

         value = CalculateValue.calculate_Word_Value(word)
         self.assertEqual(value, 13)  # El valor correcto es 13 para este caso


    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 3)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 1),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value =CalculateValue.calculate_Word_Value(word)
        self.assertEqual(value, 7)
    

if __name__ == '__main__':
     unittest.main()