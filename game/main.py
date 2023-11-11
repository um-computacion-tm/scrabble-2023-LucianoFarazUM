from game.scrabble import ScrabbleGame
import random


def get_players_count_main():
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores (de 1 a 4): "))
            if 1 <= players_count <= 4:
                return players_count
            else:
                raise ValueError
        except ValueError:
            print("Error: Ingrese de 1 a 4 jugadores")

def setup_players(game):
    print("Cantidad de jugadores: ", len(game.players))
    for player in game.players:
        player.set_nickname()
    game.next_turn()

def print_menu():
    print("Scrabble")
    print('--Menu--')
    print('1. Tablero')
    print('2. Puntos')
    print('3. Colocar palabra')
    print('4. Cambiar fichas')
    print('5. Pasar turno')
    print('6. Terminar juego')

def main():
    print("Bienvenidos al scrabble de Luciano!")
    
    players_count = get_players_count_main()
    scrabble_game = ScrabbleGame(players_count=players_count)
    bag_tiles = scrabble_game.bag_tiles

    setup_players(scrabble_game)

    while True:
        player = scrabble_game.players[scrabble_game.current_player]
        
        if len(player.rack) == 0:
            scrabble_game.end_game()

        print(f"Turno del jugador {player.nickname}\n")
        player.display_rack()
        print('_' * 15)
        
        print_menu()
        option = input("Ingrese una opción: ")

        if option == '1':
            scrabble_game.show_board()
        elif option == '2':
            scrabble_game.show_score()
        elif option == '3':
            scrabble_game.play()
        elif option == '4':
            bag_tiles.put(player.rack)
            random.shuffle(bag_tiles.bag)
            player.rack = bag_tiles.take(len(player.rack))
            rack_strings = [str(tile) for tile in player.rack]
            print("Sus nuevas fichas son: " + ", ".join(rack_strings))
        elif option == '5':
            scrabble_game.next_turn()
        elif option == '6':
            scrabble_game.end_game()
        else:
            print("Opción inválida\n")
if __name__ == '__main__':
        main()


