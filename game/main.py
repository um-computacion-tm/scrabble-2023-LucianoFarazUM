from game.scrabble import ScrabbleGame
import random



def main():

        
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
        bag_tiles=scrabbleGame.bag_tiles
        
        print("Cantidad de jugadores: ", len(scrabbleGame.players))

        for i in range(len(scrabbleGame.players)):
            scrabbleGame.players[i].set_nickname()
            scrabbleGame.next_turn()
        print('Scrabble')

        while True:
            player=scrabbleGame.players[scrabbleGame.current_player]
            if len(player.rack)==0:
                scrabbleGame.end_game()
                
            print(f"Turno del jugador {scrabbleGame.players[scrabbleGame.current_player].nickname} \n")
            player.display_rack()
            print('_' * 15)
            print('--Menu--')
            print('1. Tablero')
            print('2. Puntos')
            print('3. Colocar palabra')
            print('4. Cambiar fichas')
            print('5. Pasar turno')
            print('6. Terminar juego')
            option = input("Ingrese una opción: ")


            if option == '1':
                scrabbleGame.show_board()
            elif option == '2':
                scrabbleGame.show_score()
            elif option == '3':
                scrabbleGame.play()
            elif option == '4':
                bag_tiles.put(player.rack)
                random.shuffle(bag_tiles.bag)
                player.rack = bag_tiles.take(len(player.rack))
                rack_strings = [str(tile) for tile in player.rack]   
                print("Sus nuevas fichas son : " + ", ".join(rack_strings))
            elif option == '5':
                scrabbleGame.next_turn()
            elif option == '6':   
                scrabbleGame.end_game()
            
            else:
                print ('------------------------------------------------------------------------------------------------------\n'
            )
                print("Opción inválida")
                print ('------------------------------------------------------------------------------------------------------\n'
            )



if __name__ == '__main__':
        main()


