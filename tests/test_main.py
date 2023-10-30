import unittest
from unittest.mock import patch
from game.main import Main
from game.board import Board
import io


class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=[2])
    def test_get_player_count_valid_input(self, mock_input):
        result = Main.get_player_count()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=[0, 4, 3])
    def test_get_player_count_invalid_then_valid_input(self, mock_input):
        result = Main.get_player_count()
        self.assertEqual(result, 4)

    @patch('builtins.input', side_effect=['foo', '1,1', 'H'])
    def test_get_inputs(self, mock_input):
        word, coords, orientation = Main.get_inputs()
        self.assertEqual(word, 'foo')
        self.assertEqual(coords, (1, 1))
        self.assertEqual(orientation, 'H')

    @patch('builtins.input', side_effect=['bar', '1,2', 'V'])
    def test_get_inputs_valid_input(self, mock_input):
        word, coords, orientation = Main.get_inputs()
        self.assertEqual(word, 'bar')
        self.assertEqual(coords, (1, 2))
        self.assertEqual(orientation, 'V')

    @patch('builtins.input', side_effect=['foo', '1,1', 'X', 'H'])
    def test_get_inputs_invalid_orientation_then_valid_input(self, mock_input):
        word, coords, orientation = Main.get_inputs()
        self.assertEqual(word, 'foo')
        self.assertEqual(coords, (1, 1))
        self.assertEqual(orientation, 'H')

    @patch('builtins.input', side_effect=['foo', '1,1', 'H'])
    def test_show_board(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            board = Board()
            Main.show_board(board)
            expected_output = "\n  |  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14 \n" \
                              " 0|                          \n" \
                              " 1|                          \n" \
                              " 2|                          \n" \
                              " 3|                          \n" \
                              " 4|                          \n" \
                              " 5|                          \n" \
                              " 6|                          \n" \
                              " 7|                          \n" \
                              " 8|                          \n" \
                              " 9|                          \n" \
                              "10|                          \n" \
                              "11|                          \n" \
                              "12|                          \n" \
                              "13|                          \n" \
                              "14|                          \n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()




