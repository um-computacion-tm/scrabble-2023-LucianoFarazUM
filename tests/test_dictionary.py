import unittest
from unittest.mock import patch
from game.dictionary import (Dictionary,  DictionaryConnectionError
) 

class TestDiccionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary()

    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='1. interj. U. como salutación familiar.'
        )
    )
    def test_valid(self, search_by_word_patched):
        self.assertTrue(self.dictionary.validate_dict('hola'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        )
    )
    def test_invalid(self, search_by_word_patched):
        with self.assertRaises(DictionaryConnectionError):
            self.dictionary.validate_dict('asd')
    @patch(
        'pyrae.dle.search_by_word',
        return_value=None
    )
    def test_connection_error(self, search_by_word_patched):
        with self.assertRaises(DictionaryConnectionError):
            self.dictionary.validate_dict('hola')

if __name__ == '__main__':
    unittest.main()