# import unittest
# from game.cell import Cell
# from game.game_models import Tile
# from game.game_models import Tile
# from game.game_models import Tile,LETTER_VALUES



# class TestCell(unittest.TestCase):
#     def test_init(self):
#         cell = Cell(multiplier=2, multiplier_type='letter')

#         self.assertEqual(
#             cell.multiplier,
#             2,
#         )
#         self.assertEqual(
#             cell.multiplier_type,
#             'letter',
#         )
#         self.assertIsNone(cell.letter)
#         self.assertEqual(
#             cell.calculate_value(),
#             0,
#         )

#     def test_add_letter(self):
#         cell = Cell(multiplier=1, multiplier_type='')
#         letter = Tile(letter='p', value=3)

#         cell.add_letter(letter=letter)

#         self.assertEqual(cell.letter, letter)

#     def test_cell_value(self):
#         cell = Cell(multiplier=2, multiplier_type='letter')
#         letter = Tile(letter='p', value=3)
#         cell.add_letter(letter=letter)

#         self.assertEqual(
#             cell.calculate_value(),
#             6,
#         )

#     def test_cell_multiplier_word(self):
#         cell = Cell(multiplier=2, multiplier_type='word')
#         letter = Tile(letter='p', value=3)
#         cell.add_letter(letter=letter)

#         self.assertEqual(
#             cell.calculate_value(),
#             3,
#         )

#     def test_repr_with_tile(self):
#         tile = Tile('A', 1)
#         cell = Cell(letter=tile, multiplier=2, multiplier_type='word')
#         expected_repr = 'A:1'
#         self.assertEqual(repr(cell), expected_repr)

#     def test_repr_with_word_multiplier(self):
#         cell = Cell(multiplier=3, multiplier_type='word')
#         expected_repr = 'Wx3'
#         self.assertEqual(repr(cell), expected_repr)

#     def test_repr_with_letter_multiplier(self):
#         cell = Cell(multiplier=2, multiplier_type='letter')
#         expected_repr = 'Lx2'
#         self.assertEqual(repr(cell), expected_repr)

#     def test_repr_with_no_multipliers(self):
#         cell = Cell(multiplier=1, multiplier_type='letter')
#         expected_repr = '   '
#         self.assertEqual(repr(cell), expected_repr)


#     def test_simple(self):
#         # Crea una lista de celdas utilizando la clase Cell y asigna las letras con sus valores
#         word = [
#             Cell(1, 'letter', Tile('C', LETTER_VALUES['C'])),
#             Cell(1, 'letter', Tile('A', LETTER_VALUES['A'])),
#             Cell(1, 'letter', Tile('S', LETTER_VALUES['S'])),
#             Cell(1, 'letter', Tile('A', LETTER_VALUES['A'])),
#         ]

#         value = Cell.calculate_value(word)
#         self.assertEqual(value, 6)

#     def test_with_letter_multiplier(self):

#          word = [
#              Cell(3, 'letter'),  # Letra 'C' con multiplicador de 3
#              Cell(1, 'letter'),  # Letra 'A' con multiplicador de 1
#              Cell(2, 'letter'),    # Letra 'S' con multiplicador de palabra de 2
#              Cell(1, 'letter'),  # Letra 'A' con multiplicador de 1
#          ]

#          # Agregar letras a las celdas
#          word[0].add_letter(Tile('C', LETTER_VALUES['C']))
#          word[1].add_letter(Tile('A', LETTER_VALUES['A']))
#          word[2].add_letter(Tile('S', LETTER_VALUES['S']))
#          word[3].add_letter(Tile('A', LETTER_VALUES['A']))

#          value = Cell.calculate_word_value(word)
#          self.assertEqual(value, 13)  # El valor correcto es 13 para este caso


#     def test_with_word_multiplier(self):
#         word = [
#             Cell(letter=Tile('C', 3)),
#             Cell(letter=Tile('A', 1)),
#             Cell(
#                 letter=Tile('S', 1),
#                 multiplier=2,
#                 multiplier_type='word',
#             ),
#             Cell(letter=Tile('A', 1)),
#         ]
#         value =Cell.calculate_word_value(word)
#         self.assertEqual(value, 7)


#     def test_with_letter_word_multiplier_active(self):
#         word = [
#             Cell(
#                 multiplier=3,
#                 multiplier_type='letter',
#                 letter=Tile('C', 3)
#             ),
#             Cell(letter=Tile('A', 1)),
#             Cell(
#                 letter=Tile('S', 1),
#                 multiplier=2,
#                 multiplier_type='word',
#             ),
#             Cell(letter=Tile('A', 1)),
#         ]
#         value = Cell.calculate_word_value(word)
#         self.assertEqual(value, 13)    
    

#     def test_with_letter_word_multiplier_no_active(self):
       
#         word = [
#             Cell(
#                 multiplier=3,
#                 multiplier_type='letter',
#                 letter=Tile('C', 3),
#                 active=False

#             ),
#             Cell(letter=Tile('A', 1)),
#             Cell(
#                 letter=Tile('S', 1),
#                 multiplier=2,
#                 multiplier_type='word',
#                 active= False
#             ),
#             Cell(letter=Tile('A', 1)),
#         ]
#         value = Cell.calculate_word_value(word)
#         self.assertEqual(value, 6)





# if __name__ == '__main__':
#      unittest.main()