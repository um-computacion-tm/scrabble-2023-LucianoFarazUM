from game.cell import Cell
from typing import List

TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2),
                    (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11),
                        (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

class SoloVoHParaLaOrientacion(Exception):
    pass

class WordOutOfBoard(Exception):
    pass

class NotEnoughLetters(Exception):
    pass

class NoValid(Exception):
    pass

class Board:
    def __init__(self):
        self.grid=[
            [Cell(1, '') for _ in range (15)]
            for _ in range (15)
        ]

        self.set_multipliers()

    
    def cell_multiplier(self, coordinate, multiplier_type, multiplier):
        cell = self.grid[coordinate[0]][coordinate[1]]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier
    
    def set_multipliers(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.cell_multiplier(coordinate, "word", 3)
        for coordinate in DOUBLE_WORD_SCORE:
            self.cell_multiplier(coordinate, "word", 2)
        for coordinate in TRIPLE_LETTER_SCORE:
            self.cell_multiplier(coordinate, "letter", 3)
        for coordinate in DOUBLE_LETTER_SCORE:
            self.cell_multiplier(coordinate, "letter", 2)
   
    @staticmethod
    def calculate_word_value(word: List[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value

    def validate_word_horizontal(self, word, location):
        x, y = location
        if x < 0 or x >= 15 or y < 0 or y + len(word) > 15:
            return False
        else:
            return True
        

    def validate_word_vertical(self, word, location):
        x, y = location
        if x < 0 or x + len(word) > 15 or y < 0 or y >= 15:
            return False
        else:
            return True
    
    def validate_word_inside_board(self, word, location, orientation):
        x, y = location

        if orientation not in ['H', 'V']:
            return False
        if orientation == 'H':
            return self.validate_word_horizontal(word, (x, y))
        elif orientation == 'V':
            return self.validate_word_vertical(word, (x, y))


    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
            
    def can_place_word_at_start(self, x, y, word):
            if y <= 7 < y + len(word) and x == 7:
                return True
            else:
                return False

    def validate_word_place_board_horizontal(self, word, location):
        x, y = location
        if not self.validate_word_inside_board(word, location, "H"):
            raise WordOutOfBoard(Exception)
        if self.is_empty():
            return self.can_place_word_at_start(x, y, word)
        else:
            for i in range(len(word)):
                if self.grid[x][y + i].letter is not None:
                    if self.grid[x][y + i].letter.letter != word[i]:
                        return False
            return True

    def validate_word_place_board_vertical(self, word, location):
        x, y = location
        if not self.validate_word_inside_board(word, location, "V"):
            raise WordOutOfBoard(Exception)
        if self.is_empty():
            return self.can_place_word_at_start(y, x, word)
        else:
            for i in range(len(word)):
                if self.grid[x + i][y].letter is not None:
                    if self.grid[x + i][y].letter.letter != word[i]:
                        return False
            return True


    def put_word(self, word, location, orientation):
        x, y = location
        self.occupied_cells = []  

        if orientation == 'H':
            for i, tile in enumerate(word):
                cell = self.grid[x][y + i]  
                cell.add_letter(tile)  
                self.occupied_cells.append(cell)  
        elif orientation == 'V':
            for i, tile in enumerate(word):
                cell = self.grid[x + i][y]  
                cell.add_letter(tile)  
                self.occupied_cells.append(cell)  
        else:
            raise SoloVoHParaLaOrientacion(Exception)

        return self.occupied_cells  


    def validate_adjacent_placement(self, word, location, orientation):
        position_x, position_y = location
        if self.is_empty():
            return self.can_place_word_at_start(position_x, position_y, word)
        else: 
            if orientation == 'H':
                for i in range(len(word)):
                    if self.grid[position_x + i][position_y].letter is None:
                        
                        return False
            else:
                for i in range(len(word)):
                    if self.grid[position_x][position_y + i].letter is None:
                        return False
        
        return True
    
    def validate_word_place_board(self, word, location, orientation):
        if not self.validate_adjacent_placement(word, location, orientation):
            return False
        else:
            if orientation == "H":
                return self.validate_word_place_board_horizontal(word, location)
            elif orientation == "V":
                return self.validate_word_place_board_vertical(word, location)
            else:
                raise SoloVoHParaLaOrientacion(Exception)      