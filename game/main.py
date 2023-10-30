from game.scrabble import ScrabbleGame
from game.board import Board


class Main:
    @staticmethod
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([str(cell) for cell in row])
            )

    @staticmethod
    def get_player_count():
        while True:
            try:
                player_count = int(input('Cantidad de jugadores (1-4): '))
                if 1 <= player_count <= 4:
                    break
                else:
                    print('Número de jugadores no válido. Intente de nuevo.')
            except ValueError:
                print('Ingrese un número válido por favor.')
        return player_count

    @staticmethod
    def get_inputs():
        word = input('Palabra: ')
        coords_str = input('Coordenadas (fila, columna): ')
        coords_str = coords_str.replace('(', '').replace(')', '')  # Eliminar paréntesis
        coords_str = coords_str.strip()  # Eliminar espacios en blanco adicionales
        coords = tuple(map(int, coords_str.split(',')))
        orientation = input('Orientación (H/V): ')

        while orientation not in ['H', 'V']:
            print('Orientación no válida. Intente de nuevo.')
            orientation = input('Orientación (H/V): ')

        return word, coords, orientation


if __name__ == "__main__":
    board = Board()
    Main.show_board(board)