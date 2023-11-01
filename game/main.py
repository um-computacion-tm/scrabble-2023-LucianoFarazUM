from game.scrabble import ScrabbleGame
from game.board import Board
from game.player import Player
from game.game_models import BagTiles
import random


def play_word():
        word = input("Ingrese la palabra:")
        location_x = input("Ingrese posicion X: ")
        location_y = input("Ingrese posicion Y: ")
        location = (location_x, location_y)
        orientation = input("Ingrese orientacion (V/H)")
        self.scrabbleGame.play(word, player, orientation, location)


def main():
        bagtiles = BagTiles()  # Crear una instancia de BagTiles
        player = Player()
        board = Board() 



        print("Bienvenido!")
        while True:
            try:
                players_count = int(input("Ingrese cantidad de jugadores: "))
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
        
        while True:
        

            
            print('Scrabble')
            
            print(f"Turno del jugardor {scrabbleGame.players[scrabbleGame.current_player].nickname} \n")
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
                play_word(scrabbleGame, scrabbleGame.players[scrabbleGame.current_player])
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


