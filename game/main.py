from game.scrabble import ScrabbleGame

import random

def get_players_count_main():
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores (de 1 a 4): "))
            if 1 <= players_count <= 4:
                return players_count
        except ValueError:
            pass
        print("Error: Ingrese un número válido de jugadores (de 1 a 4)")

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
def print_welcome_message():
    print("Bienvenidos al Scrabble de Luciano!")

def display_player_turn(player):
    print(f"Turno del jugador {player.nickname}\n")
    player.display_rack()
    print('_' * 15)

def print_menu():
    print("1. Mostrar tablero")
    print("2. Mostrar puntajes")
    print("3. poner palabra")
    print("4. Cambiar fichas")
    print("5. Siguiente turno")
    print("6. Finalizar juego")

def handle_menu_option(option, scrabble_game, bag_tiles):
    player = scrabble_game.players[scrabble_game.current_player]

    option_handlers = {
        '1': scrabble_game.show_board,
        '2': scrabble_game.show_score,
        '3': scrabble_game.play,
        '4': lambda: exchange_tiles_menu(player, bag_tiles),
        '5': scrabble_game.next_turn,
        '6': scrabble_game.end_game,
    }

    handler = option_handlers.get(option, lambda: print("Opción inválida\n"))
    handler()

def exchange_tiles_menu(player, bag_tiles):
    bag_tiles.put(player.rack)
    random.shuffle(bag_tiles.bag)
    player.rack = bag_tiles.take(len(player.rack))
    rack_strings = [str(tile) for tile in player.rack]
    print("Sus nuevas fichas son: " + ", ".join(rack_strings))

def exchange_tiles(player, bag_tiles):
    bag_tiles.put(player.rack)
    random.shuffle(bag_tiles.bag)
    player.rack = bag_tiles.take(len(player.rack))
    rack_strings = [str(tile) for tile in player.rack]
    print("Sus nuevas fichas son: " + ", ".join(rack_strings))

def main():
    print_welcome_message()

    players_count = get_players_count_main()
    scrabble_game = ScrabbleGame(players_count=players_count)
    bag_tiles = scrabble_game.bag_tiles

    setup_players(scrabble_game)

    while True:
        player = scrabble_game.players[scrabble_game.current_player]

        if len(player.rack) == 0:
            scrabble_game.end_game()

        display_player_turn(player)
        print_menu()
        option = input("Ingrese una opción: ")

        handle_menu_option(option, scrabble_game, bag_tiles)

if __name__ == '__main__':
        main()


