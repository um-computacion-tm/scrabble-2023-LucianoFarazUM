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
            self.players.append(Player(bag_tiles=self.bag_tiles))
        
        self.current_player = None
    
    def get_current_player(self):
            return self.players[self.current_player]
    

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            index = (self.players.index(self.current_player) + 1) % len(self.players)
            self.current_player = self.players[index]

    def valid_word(self, word: str, player: Player) -> bool:
        player_letters = player.tiles
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
    def word_exists(self, word: str) -> bool:
        user_input = input(f"¿Es '{word}' una palabra válida? (Sí/No): ").strip().lower()
        return user_input == "si"

    def put_word(self, word: str, location: tuple, orientation: str) -> bool:
        if self.can_place_word(word, location, orientation):
            self.board.place_word_on_board(word, location, orientation)
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
