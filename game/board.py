from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)
        ]

    def validate_word_inside_board(self, word, location, orientation):
        row, col = location
        if orientation == "H":
            if col + len(word) > 15:
                return False
            for i, letter in enumerate(word):
                if self.grid[row][col + i].letter != '' and self.grid[row][col + i].letter != letter:
                    return False
            return True
        elif orientation == "V":
            if row + len(word) > 15:
                return False
            for i, letter in enumerate(word):
                if self.grid[row + i][col].letter != '' and self.grid[row + i][col].letter != letter:
                    return False
            return True
        return False
