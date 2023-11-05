from game.board import Board
from game.player import Player
from game.game_models import BagTiles
from game.dictionary import Dictionary
import sys

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.dict = Dictionary()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())
        
        self.current_player = 0
    
    
    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)


   
    def can_form_word(self, word, player: Player) -> bool:
        player = self.players[self.current_player]
        player_tiles = player.rack  
        hand_letters = [tile.letter for tile in player_tiles]  
        self.matching_tiles = []  
        for letter in word:
            if letter in hand_letters:
                matching_tile_index = hand_letters.index(letter)
                matching_tile = player_tiles.pop(matching_tile_index) 
                self.matching_tiles.append(matching_tile)  
                hand_letters.remove(letter)  
            else:
                return False
        return True, self.matching_tiles  




    def show_board(self):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(self.board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )

    def show_score(self):
        print("Su puntaje es :",self.players[self.current_player].score)



    def end_game(self):
        if len(self.bag_tiles.bag) == 0:
            sys.exit()
        else:
            while True:
                choice = input("¿Quieres terminar el juego? (Sí/No): ").strip().lower()
                if choice == "si":
                    sys.exit()
                elif choice == "no":
                    return False
                else:
                    print("Por favor, ingresa 'Sí' o 'No'.")

    
    def validate_word(self,word,location,orientation,player):
        if not self.can_form_word(word, player):
            return False
        if not self.board.validate_word_place_board(word, location, orientation):
            return False
        if not self.dict.validate_dict(word):
            return False
        return True

        
    def play(self): 
        word = input("Ingrese la palabra:")
        location_x = int(input("Ingrese posicion X: "))  # Convertir la entrada a un entero
        location_y = int(input("Ingrese posicion Y: "))  # Conviertir la entrada a un entero
        location = (location_x, location_y)
        print(location)
        orientation = input("Ingrese orientacion (V/H)")
        player = self.players[self.current_player]
        if self.validate_word(word,location,orientation,player):
            word = self.matching_tiles
            self.board.put_word(word, location, orientation)
            word= self.board.occupied_cells
            total_points = self.board.calculate_word_value(word)
            player.update_score(total_points)  # Debes pasar total_points como argumento a update_score
            self.next_turn()