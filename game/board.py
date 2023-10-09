from game.game_models import Tile
from game.cell import Cell
# class Board:
#     SIZE=15
#     def __init__(self):
#         self.grid = [[None for _ in range(15)] for _ in range(15)]

#     def add_letter(self, x, y, letter, value):
#         if self.grid[x][y] is None:
#             self.grid[x][y] = Tile(letter, value)
#         else:
#             # Si la celda no está vacía, levanta un error o maneja la situación según tu lógica de negocio
#             pass

#     def clear_board(self):
#         self.grid = [[None for _ in range(15)] for _ in range(15)]

    # def validate_word_inside_board(self, word, location, orientation):
    #     x, y = location
    #     if x < 0 or y < 0 or x >= 15 or y >= 15:
    #         return False

    #     if orientation == "H":
    #         if y + len(word) > 15:
    #             return False
    #         for i in range(len(word)):
    #             if self.grid[x][y + i] is not None:
    #                 return False
    #     elif orientation == "V":
    #         if x + len(word) > 15:
    #             return False
    #         for i in range(len(word)):
    #             if self.grid[x + i][y] is not None:
    #                 return False
    #     else:
    #         return False

    #     return True

    # @property
    # def is_empty(self):
    #     for row in self.grid:
    #         for tile in row:
    #             if tile is not None:
    #                 return False
    #     return True

    # def validate_word_place_board(self, word: str, location: tuple, orientation: str) -> bool:
    #     x, y = location
    #     len_word = len(word)

    #     if orientation == "H":
    #         if x < 0 or x + len_word > len(self.grid) or y < 0 or y >= len(self.grid[0]):
    #             return False
    #     else:
    #         if x < 0 or x >= len(self.grid) or y < 0 or y + len_word > len(self.grid[0]):
    #             return False

    #     for i in range(len_word):
    #         if orientation == "H" and self.grid[x + i][y] is not None:
    #             return False
    #         elif orientation == "V" and self.grid[x][y + i] is not None:
    #             return False

    #     return True
    


from game.cell import Cell

class Board:
    SIZE = 15

    def __init__(self):
        self.grid = [[Cell() for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def clear_board(self):
        self.grid = [[Cell() for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def validate_word_inside_board(self, word, location, orientation):
        x, y = location
        len_word = len(word)
        max_x, max_y = self.SIZE, self.SIZE

        if orientation == "H":
            if x < 0 or x + len_word > max_x or y < 0 or y >= max_y:
                return False
        else:
            if x < 0 or x >= max_x or y < 0 or y + len_word > max_y:
                return False

        for i in range(len_word):
            cell = self.grid[x + i][y] if orientation == "H" else self.grid[x][y + i]
            if cell.letter and cell.letter != word[i]:
                return False

        return True

    def place_word_on_board(self, word, location, orientation):
        x, y = location
        for i, letter in enumerate(word):
            cell = self.grid[x + i][y] if orientation == "H" else self.grid[x][y + i]
            cell.letter = letter

    def validate_word_place_board(self, word, location, orientation):
        if not self.validate_word_inside_board(word, location, orientation):
            return False

        x, y = location
        for i, letter in enumerate(word):
            cell = self.grid[x + i][y] if orientation == "H" else self.grid[x][y + i]
            if cell.letter == letter:
                return False

        return True

    @property
    def is_empty(self):
        return all(not cell.letter for row in self.grid for cell in row)
    
    ###############################################



    

