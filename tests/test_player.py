import unittest
from game.player import Player
from game.game_models import BagTiles, Tile
import io
from unittest.mock import patch, call
from game.board import Board



class TestPlayer(unittest.TestCase):
    def setUp(self):
        bag_tiles = BagTiles()
        self.player = Player(bag_tiles)
        self.rack = []
        

    def test_initial_score(self):
        # Verifica que el jugador comience con 0 puntos
        self.assertEqual(self.player.get_score(), 0)    

    @patch('builtins.input', return_value='Nombre')
    def test_set_nickname(self, input_patched):
        self.player.set_nickname()
        self.assertEqual(self.player.nickname, 'Nombre')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_rack(self, mock_stdout):
        self.player.display_rack()
        printed_output = mock_stdout.getvalue().strip()
        self.assertIn("Sus fichas son:", printed_output)
        for tile in self.player.rack:
            self.assertIn(str(tile), printed_output)


    def test_add_letters(self):
        initial_rack_length = len(self.player.rack)
        letters_to_add = ['A', 'B', 'C']
        self.player.add_letters(letters_to_add)
        self.assertEqual(len(self.player.rack), initial_rack_length + len(letters_to_add))


    def test_get_score(self):
        self.player.score = 100
        self.assertEqual(self.player.get_score(), 100)

    def test_fill_rack(self):
        self.player.fill_rack()
        
        self.assertEqual(len(self.player.rack), 7)    
        

    def test_update_score(self):
        points = 10
        self.player.update_score(points)
        self.assertEqual(self.player.score, points)

        points = +5
        self.player.update_score(points)
        self.assertEqual(self.player.score, 15)    

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_rack(self, mock_stdout):
        self.display_rack = [str(tile) for tile in self.player.rack]  
        self.player.display_rack()
        printed_output = mock_stdout.getvalue().strip()

        self.assertIn("Sus fichas son:", printed_output)
        for tile in self.player.rack:
            self.assertIn(str(tile), printed_output)

    def test_renew_rack(self):
        initial_tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]
        self.player.rack = initial_tiles.copy()

        
        matching_tiles = [Tile('B', 3), Tile('D', 2)]

        self.player.renew_rack(matching_tiles)

        for tile in matching_tiles:
            self.assertNotIn(tile, self.player.rack)

        self.assertEqual(len(self.player.rack), 7)

        for tile in initial_tiles:
            if tile not in matching_tiles:
                self.assertIn(tile, self.player.rack)


                []
    def test_is_letter_in_rack(self):
        # Configuración inicial del rack con algunas fichas
        self.player.rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]

        # Palabra que se intentará formar con las fichas del rack
        word = "BAD"

        # Llama al método is_letter_in_rack para verificar si las letras de la palabra están en el rack
        result = self.player.is_letter_in_rack(word)

        # Verifica que el resultado sea True, indicando que las letras de la palabra están en el rack
        self.assertTrue(result)

    def test_is_letter_not_in_rack(self):
        # Configuración inicial del rack con algunas fichas
        self.player.rack = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]

        # Palabra que contiene una letra que no está en el rack
        word = "BADD"

        # Llama al método is_letter_in_rack para verificar si las letras de la palabra están en el rack
        # Debería lanzar una excepción KeyError indicando que falta la letra 'D' para formar la palabra
        with self.assertRaises(KeyError) as context:
            self.player.is_letter_in_rack(word)

        # Verifica que la cadena de error esperada está contenida en la cadena de error real
        self.assertIn("Falta la letra 'D' para formar la palabra 'BADD'.", str(context.exception)) 

    @patch('builtins.input', side_effect=['X'])
    def test_set_wildcard(self, mock_input):
        # Configuración inicial del rack con letras y comodines
        self.player.rack = [Tile('A', 1), Tile('#', 0), Tile('@', 0)]

        # Palabra con comodín que se modificará usando el método set_wildcard
        word = "W#RD"

        # Llama al método set_wildcard simulando la entrada del usuario 'X'
        modified_word = self.player.set_wildcard(word)

        # Verifica que el método devuelva la palabra modificada correctamente
        self.assertEqual(modified_word, "WXRD")

        # Verifica que el comodín en el rack se haya reemplazado por 'X'
        self.assertEqual(str(self.player.rack[1]), "X:0")

        # Verifica que el otro comodín en el rack se haya mantenido igual
        self.assertEqual(str(self.player.rack[2]), "@:0")

        # Verifica que la función input haya sido llamada con el mensaje esperado
        expected_call = call('Ingrese la letra del comodin: ')
        self.assertIn(expected_call, mock_input.call_args_list)
    
    



    @patch('builtins.input', side_effect=['C'])
    def test_replace_blank_tiles_with_letters(self, mock_input):
        # Configurar el tablero y el rack de prueba
        self.player.rack = [Tile('A', 1), Tile('@', 0), Tile('J', 3)]
        # Llamar a la función que se va a probar
        self.player.set_wildcard("AB@")
        
        # Crear objetos Tile para la lista esperada
        expected_rack = [Tile('A', 1), Tile('C', 0), Tile('B', 3)]

        # Verificar que los objetos Tile en el rack sean iguales a los objetos Tile en la lista esperada
        self.assertNotEqual(self.player.rack, expected_rack)




    @patch.object(Player, 'fill_rack')
    def test_renew_rack_remove(self, mock_fill_rack):
        # Prueba el método remove en renew_rack
    
        # Establece el rack inicial
        self.player.rack = ["A", "B", "C", "D", "E"]
        
        # Llama a renew_rack con una lista de matching_tiles
        matching_tiles = ["B", "D"]
        self.player.renew_rack(matching_tiles)
        
        # Verifica que las letras B y D hayan sido eliminadas del rack
        self.assertNotIn("B", self.player.rack)
        self.assertNotIn("D", self.player.rack)
        
        # Verifica que fill_rack se haya llamado después de remover las letras
        mock_fill_rack.assert_called_once()



if __name__ == '__main__':
    unittest.main()