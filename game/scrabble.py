from game.board import Board
from game.player import Player
from game.game_models import BagTiles
from game.dictionary import Dictionary, DictionaryConnectionError
import sys
 
class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.dict = Dictionary()
        self.players = [Player(self.bag_tiles) for _ in range(players_count)]
        
        self.current_player = 0
        self.player=self.players[self.current_player]
    
    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)
        self.player = self.players[self.current_player]


    def can_form_word(self, word, location,orientation) -> bool:
        player_tiles=[]
        hand_letters=[]
        player_tiles = self.player.rack.copy()  
        hand_letters = [tile.letter for tile in player_tiles]
        if self.board.validate_word_connections(word, location, orientation, hand_letters, player_tiles):
            player_tiles, hand_letters=self.board.verify_tiles()
            self.player.rack=player_tiles.copy()
            if len(self.player.rack) > 7:
                num_elements_to_remove = len(self.player.rack) - 7
                for _ in range(num_elements_to_remove):
                    self.player.rack.pop()
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
        else:
            return False



    def show_board(self):
        print('\n  +' + '-' * 89 + '+')
        print('  |' + ''.join([f' {str(col_index).rjust(2)}  |' for col_index in range(15)]))
        print('+' + '-' * 92 + '+')
        for row_index, row in enumerate(self.board.grid):
            print(str(row_index).rjust(2) + '| ' + ' | '.join([repr(cell) for cell in row]) + ' |')
            print('+' + '-' * 92 + '+')


    def show_score(self):
        print("Su puntaje es :",self.player.score)



    def end_game(self):
        if len(self.player.rack)==0:
            for player in self.players:
                sys.exit()
        else:
            while True:
                choice = input("¿Quieres terminar el juego? (Sí/No): ").strip().lower()
                if choice == "si":
                    for player in self.players:
                        print(f"el jugador:{player.nickname} obtuvo {player.score} puntos")
                    sys.exit()
                elif choice == "no":
                    return False
                else:
                    print("Por favor, ingresa 'Sí' o 'No'.")
                
        
    def validate_word(self, word, location, orientation):
        if not self.can_form_word(word,location,orientation):
            
            return False
        if not self.board.validate_word_place_board(word, location, orientation):
            print("La palabra no puede ser colocada en esa posición(si es la primer palabra a ingresar va en la posicion 7,7).")
            return False
        try:
            if not self.dict.validate_dict(word):
                print("La palabra no se encuentra en el diccionario.")
                return False
        except DictionaryConnectionError as e:
            print(str(e)) 
            return False
        return True   
        
    


    def obtener_posicion(self):
        while True:
            try:
                y= int(input("Ingrese posicion X: "))
                x = int(input("Ingrese posicion Y: "))
                if 0 <= x <= 14 and 0 <= y <= 14:
                    return x,y 
                else:
                    print("Posición incorrecta. Solo se permiten números del 0 al 14.")
            except ValueError:
                print("Posición incorrecta. Solo se permiten números del 0 al 14.")

    def play(self):
        while True:
            word = input("Ingrese la palabra:")

            
            if word.isalpha() or "#" or "@" in word:
                if "#" in word:
                    modified_word = self.player.set_wildcard(word)
                    word= modified_word.upper()
                    str(word)
                if "@" in word:
                    modified_word = self.player.set_wildcard(word)
                    word= modified_word.upper()
                    str(word)    
                break  
            else:
                print("Palabra inválida. Por favor, ingrese solo letras o palabras que contengan '#' o '@'.")

            modified_word = word.upper()
            word= modified_word
            
        
        location_x, location_y = self.obtener_posicion()
        location = (location_x, location_y)
        
        orientation = input("Ingrese orientacion (V/H)").upper()
        
        while orientation not in ['V', 'H']:
            print("Posicion incorrecta. Ingrese V o H.")
            orientation = input("Ingrese orientacion (V/H)").upper()
        
        player=self.player
        if self.validate_word(word, location, orientation):
            word = self.matching_tiles
            self.board.put_word(word, location, orientation,player)
            word = self.board.occupied_cells
            total_points = self.board.calculate_word_value(word)
            self.player.update_score(total_points)
            self.player.renew_rack(self.matching_tiles)
            self.next_turn()  