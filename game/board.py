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
        value: int = sum(cell.calculate_value() for cell in word)
        
        multiplier_word = next((cell.multiplier for cell in word if cell.multiplier_type == "word" and cell.active), None)
        
        if multiplier_word:
            value *= multiplier_word
        
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

        for i, cell in enumerate(self.grid[x][y:y+len(word)]):
            if cell.letter is not None and cell.letter.letter != word[i]:
                return False
        return True
        
    def validate_word_place_board_vertical(self, word, location):
        x, y = location

        if not self.validate_word_inside_board(word, location, "V"):
            raise WordOutOfBoard(Exception)

        if self.is_empty():
            return self.can_place_word_at_start(y, x, word)

        for i, letter in enumerate(word):
            cell = self.grid[x + i][y]
            if cell.letter is not None and cell.letter.letter != letter:
                return False

        return True


    def put_word(self, word, location, orientation, player):
        x, y = location
        self.occupied_cells = [] 
        if orientation not in ['H', 'V']:
            raise SoloVoHParaLaOrientacion(Exception)
        for i, tile in enumerate(word):
            if orientation == 'H':
                cell = self.grid[x][y + i]
            elif orientation == 'V':
                cell = self.grid[x + i][y]
            cell.add_letter(tile)
            self.occupied_cells.append(cell)
        return self.occupied_cells
    
    def validate_word_connections(self, word, location, orientation, hand_letters, player_tiles):
        position_x, position_y = location
        self.player_tiles = player_tiles
        self.hand_letters = hand_letters

        if self.is_empty():
            return self.can_place_word_at_start(position_x, position_y, word)
        else:
            return self.check_word_connections(word, position_x, position_y, orientation)

    def check_word_connections(self, word, position_x, position_y, orientation):
        letters_exist = self.get_letters_exist(position_x, position_y, word, orientation)

        if self.is_all_empty(letters_exist):
            return False
        else:
            return self.check_letters_match(word, position_x, position_y, orientation, letters_exist)

    def is_all_empty(self, letters_exist):
        return all(self.grid[x][y].letter is None for x, y in letters_exist)

    def check_letters_match(self, word, position_x, position_y, orientation, letters_exist):
        for letter_pos in letters_exist:
            letter_x, letter_y = letter_pos
            cell = self.grid[letter_x][letter_y]
            tile_object = cell.letter
            if tile_object is not None and not self.match_tile_letter(tile_object, word, position_x, position_y, orientation, letter_x, letter_y):
                return False, self.player_tiles, self.hand_letters
        return True, self.player_tiles, self.hand_letters

    def match_tile_letter(self, tile_object, word, position_x, position_y, orientation, letter_x, letter_y):
        tile_letter_value = tile_object.letter
        self.player_tiles.append(tile_object)
        self.hand_letters.append(tile_letter_value)
        matching_letter = word[letter_y - position_y] if orientation == 'H' else word[letter_x - position_x]
        return tile_letter_value == matching_letter
    
    def get_letters_exist(self, position_x, position_y, word, orientation):
        letters_exist = []
        if orientation not in ['H', 'V']:
            raise SoloVoHParaLaOrientacion("Orientación inválida. Solo se permite 'H' o 'V'.")
        elif orientation == 'H':
                letters_exist = [(position_x, i) for i in range(position_y, position_y + len(word))]
        elif orientation == 'V':
                letters_exist = [(i, position_y) for i in range(position_x, position_x + len(word))]
        return letters_exist
        
    def verify_tiles(self):
        player_tiles= self.player_tiles
        hand_letters=self.hand_letters
        return player_tiles, hand_letters
    
    def validate_word_place_board(self, word, location, orientation):
            if orientation == "H":
                return self.validate_word_place_board_horizontal(word, location)
            elif orientation == "V":
                return self.validate_word_place_board_vertical(word, location)
            else:
                raise SoloVoHParaLaOrientacion(Exception)      