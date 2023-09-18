from game.cell import Cell
from game.game_models import Tile

class Board:
    def __init__(self):
        self.grid = [[Cell(1, "", "") for _ in range(15)] for _ in range(15)]

    @staticmethod
    def calculate_word_value(word: [Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value

    
    def validate_word_inside_board(self, word, location, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)

        # Primero, verifica si la palabra cabe en el tablero según la orientación.
        if orientation == "H":
            if position_x + len_word > 15:
                return False
        else:
            if position_y + len_word > 15:
                return False

        # Luego, verifica si hay letras en las celdas que intersectan con la palabra.
        for i in range(len(word)):
            if orientation == "H":
                if (
                    self.grid[position_x + i][position_y].letter != ""
                    and self.grid[position_x + i][position_y].letter != word[i]
                ):
                    return False
            else:
                if (
                    self.grid[position_x][position_y + i].letter != ""
                    and self.grid[position_x][position_y + i].letter != word[i]
                ):
                    return False

        return True
    def place_word_on_board(self, word, location, orientation):
        position_x = location[0]
        position_y = location[1]
        if orientation == "H":
            for i in range(len(word)):
                self.grid[position_x + i][position_y].add_letter(Tile(word[i], 1))
        else:
            for i in range(len(word)):
                self.grid[position_x][position_y + i].add_letter(Tile(word[i], 1))

    @property
    def is_empty(self):
        for row in self.grid:
            for cell in row:
                if cell.letter != "":
                    return False
        return True

    def clear_board(self):
        self.grid = [[Cell(1, "", "") for _ in range(15)] for _ in range(15)]
