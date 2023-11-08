from game.game_models import Tile

class Cell:
    def __init__(self, multiplier=1, multiplier_type="", letter=None, active=True):

        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter' and self.active:
            self.active =  False 
            return self.letter.value * self.multiplier
        elif self.multiplier_type == 'letter' and not self.active:
            return self.letter.value * 1
        else:
            return self.letter.value

    def add_letter(self, letter:Tile):
        self.letter = letter

    
    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '
        