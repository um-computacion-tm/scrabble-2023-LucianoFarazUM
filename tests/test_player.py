import unittest
from game.player import Player
import io
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Configuración común para los tests
        self.player = Player()

    def test_initialization(self):
        self.assertEqual(self.player.score, 0)
        self.assertEqual(len(self.player.rack), 7)

    @patch('builtins.input', return_value='NuevoNombre')
    def test_set_nickname(self, mock_input):
        self.player.set_nickname()
        # Verifica que el atributo nickname de la instancia Player se haya actualizado correctamente
        self.assertEqual(self.player.nickname, 'NuevoNombre')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_rack(self, mock_stdout):
        self.player.display_rack()
        printed_output = mock_stdout.getvalue().strip()
        # Aquí puedes agregar aserciones para verificar el contenido impreso
        # Por ejemplo, puedes verificar si ciertos valores esperados están en la salida
        self.assertIn("Sus fichas son:", printed_output)
        for tile in self.player.rack:
            self.assertIn(str(tile), printed_output)


    def test_add_letters(self):
        initial_rack_length = len(self.player.rack)
        letters_to_add = ['A', 'B', 'C']
        self.player.add_letters(letters_to_add)
        self.assertEqual(len(self.player.rack), initial_rack_length + len(letters_to_add))

    def test_get_letters(self):
        letters_to_add = ['A', 'B', 'C']
        initial_rack_letters = set(str(tile) for tile in self.player.get_letters())  # Convertir las letras iniciales a un conjunto
        self.player.add_letters(letters_to_add)
        updated_rack_letters = set(str(tile) for tile in self.player.get_letters())  # Convertir las letras después de la adición a un conjunto
        added_letters_set = set(letters_to_add)  # Convertir las letras que se van a agregar a un conjunto
        self.assertSetEqual(updated_rack_letters, initial_rack_letters.union(added_letters_set),
                            "Las letras en el rack no coinciden con las letras agregadas.")
    def test_get_score(self):
        # Asigna un valor a la puntuación y verifica que se devuelva correctamente
        self.player.score = 100
        self.assertEqual(self.player.get_score(), 100)

if __name__ == '__main__':
    unittest.main()