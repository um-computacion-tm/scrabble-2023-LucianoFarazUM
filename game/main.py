from game.scrabble import ScrabbleGame
class Main:
    @staticmethod
    def get_player_count():
        while True:
            try:
                player_count = int(input('Cantidad de jugadores (1-3): '))
                if 1 <= player_count <= 3:
                    break
                else:
                    print('Número de jugadores no válido. Intente de nuevo.')
            except ValueError:
                print('Ingrese un número válido por favor.')
        return player_count

    @staticmethod
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )

    def show_player(self):
        return ScrabbleGame.get_current_player()

    @staticmethod
    def get_inputs():
        word = input('Palabra: ')
        coords_str = input('Coordenadas (fila, columna): ')
        coords_str = coords_str.replace('(', '').replace(')', '')  # Eliminar paréntesis
        coords_str = coords_str.strip()  # Eliminar espacios en blanco adicionales
        coords = tuple(map(int, coords_str.split(',')))
        orientation = input('Orientación (H/V): ')
        return word, coords, orientation

    # def main():
    #         player_count = get_player_count()
    #         game = ScrabbleGame(player_count)
    #         while game.is_playing():
    #             show_board(game.get_board())
    #             show_player(*game.get_current_player())
    #             word, coords, orientation =get_inputs()
    #             try:
    #                 game.play(word, coords, orientation)
    #             except Exception as e:
    #                 print(e)


if __name__=="__main__":
    main = Main()
