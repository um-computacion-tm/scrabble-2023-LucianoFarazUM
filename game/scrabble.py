from game.board import Board
from game.player import Player
from game.game_models import BagTiles
from game.calculator_value import CalculateValue

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.calculatorValue = CalculateValue()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())
        
        self.current_player = 0
    
    def get_current_player(self):
        return self.players[self.current_player]
    
    
    def playing(self):
        return True
    
    
    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)


    def valid_word(self, word: str, player: Player) -> bool:
        player_letters = player.rack
        hand_letters = list(player_letters)
        for letter in word:
            if letter in hand_letters:
                hand_letters.remove(letter)  
            else:
                return False
        return True
    def can_place_word(self, word: str, location: tuple, orientation: str) -> bool:
            x, y = location
            len_word = len(word)
            board = self.board.grid

            if orientation == "H":
                if x < 0 or x + len_word > len(board) or y < 0 or y >= len(board[0]):
                    return False
            else:
                if x < 0 or x >= len(board) or y < 0 or y + len_word > len(board[0]):
                    return False

            for i in range(len_word):
                cell = board[x + i][y] if orientation == "H" else board[x][y + i]
                if cell.letter and cell.letter != word[i]:
                    return False

            return True
    

    def put_word(self, word: str, location: tuple, orientation: str) -> bool:
        if self.can_place_word(word, location, orientation):
            self.board.place_word_on_board(word, location, orientation)
            self.next_turn()  # Cambiar al siguiente turno después de colocar la palabra.
            return True
        else:
            return False

    

    def play(self, word: str, location: tuple, orientation: str) -> bool:
        if self.put_word(word, location, orientation):
            total = self.calculatorValue.calculate_Word_Value(word)  # Calcular el valor de la palabra
            self.players[self.current_player].score += total
            self.next_turn()
            return True
        else:
            print(f"La palabra '{word}' no es válida en la ubicación especificada.")
            return False

    
    

    def create_tile_list(self, word, bag_tiles):
        tile_list = []
        for letter in word:
            tile = bag_tiles.get_tile(letter)
            tile_list.append(tile)
        return tile_list
    

    def show_score(self):
        print("Su puntaje es :",self.players[self.current_player].score)

    def display_tiles(self, player):
        print
        for tile in player.rack:
            print(f"[{tile.letter}, {tile.value}]", end=' ')
        print()


    def end_game(self):
        if len(self.bag_tiles.bag) == 0:
            return True
        else:
            while True:
                choice = input("¿Quieres terminar el juego? (Sí/No): ").strip().lower()
                if choice == "si":
                    return True
                elif choice == "no":
                    return False
                else:
                    print("Por favor, ingresa 'Sí' o 'No'.")

    