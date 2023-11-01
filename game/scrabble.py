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


    def can_form_word(self, word: str, player: Player) -> bool:
        player_letters = player.rack
        hand_letters = list(player_letters)
        for letter in word:
            if letter in hand_letters:
                hand_letters.remove(letter)  
            else:
                return False
        return True

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

    def display_tiles(self, player):
        print
        for tile in player.rack:
            print(f"[{tile.letter}, {tile.value}]", end=' ')
        print()


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

    
    def validate_word(self, word, player, location, orientation):
        if not self.can_form_word(word, player):
            return False
        if not self.board.validate_word_place_board(word, location, orientation):
            return False
        if not self.dict.validate_dict(word):
            return False
        

    
    def play(self, word, player, location, orientation):
        if self.validate_word(word, player, location, orientation):
            word = self.board.put_word(word, location, orientation)
            total_points = self.board.calculate_word_value(word)
            current_player_instance = self.players[self.current_player]
            current_player_instance.update_score(total_points)
            self.next_turn()