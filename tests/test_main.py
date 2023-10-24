import unittest
from unittest.mock import patch
from game.main import Main  # Reemplaza 'your_module' con el nombre de tu archivo o módulo

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=[2])
    def test_get_player_count_valid_input(self, mock_input):
        result = Main.get_player_count()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=[0, 4, 3])
    def test_get_player_count_invalid_then_valid_input(self, mock_input):
        result = Main.get_player_count()
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['foo', '1,1', 'H'])
    def test_get_inputs(self, mock_input):
        word, coords, orientation = Main.get_inputs()
        self.assertEqual(word, 'foo')
        self.assertEqual(coords, (1, 1))
        self.assertEqual(orientation, 'H')

if __name__ == '__main__':
    unittest.main()








