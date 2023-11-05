from game.scrabble import ScrabbleGame
from game.player import Player
from game.game_models import BagTiles
import random



def main():
        bagtiles = BagTiles()
        
        print("Bienvenidos al scrabble de luciano!")
        while True:
            try:
                players_count = int(input("Ingrese cantidad de jugadores(de 1 a 4): "))
                if 1 <= players_count <= 4:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Error Ingrese de 1 a 4 jugadores")
        scrabbleGame = ScrabbleGame(players_count=players_count)
        
        print("Cantidad de jugadores: ", len(scrabbleGame.players))

        for i in range(len(scrabbleGame.players)):
            scrabbleGame.players[i].set_nickname()
            scrabbleGame.next_turn()
        print('Scrabble')

        while True:
            player=scrabbleGame.players[scrabbleGame.current_player]
            print(f"Turno del jugador {scrabbleGame.players[scrabbleGame.current_player].nickname} \n")
            print('_' * 15)
            print('--Menu--')
            print('1. Mostrar Tablero')
            print('2. Mostrar puntos')
            print('3. Mostrar mis fichas')
            print('4. Colocar palabra')
            print('5. Cambiar fichas')
            print('6. Pasar turno')
            print('7. Terminar juego')
            print('+' * 100)
            option = input("Ingrese una opción: ")


            if option == '1':
                print ('tablero:')
                scrabbleGame.show_board()
            elif option == '2':
                scrabbleGame.show_score()
            elif option == '3':
                player.display_rack()
            elif option == '4':
                scrabbleGame.play()
            elif option == '5':
                bagtiles.put(player.rack)
                random.shuffle(bagtiles.bag)
                player.rack = bagtiles.take(len(player.rack))
                rack_strings = [str(tile) for tile in player.rack]   
                print("Sus nuevas fichas son : " + ", ".join(rack_strings))
            elif option == '6':
                scrabbleGame.next_turn()
            elif option == '7':   
                scrabbleGame.end_game()


            else:
                print ('------------------------------------------------------------------------------------------------------\n'
            )
                print("Opción inválida")
                print ('------------------------------------------------------------------------------------------------------\n'
            )



if __name__ == '__main__':
        main()


